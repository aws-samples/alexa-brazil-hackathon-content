import logging
import ask_sdk_core.utils as ask_utils
import os
import requests
import calendar
from datetime import datetime
from pytz import timezone
from ask_sdk_s3.adapter import S3Adapter
s3_adapter = S3Adapter(bucket_name=os.environ["S3_PERSISTENCE_BUCKET"])

from ask_sdk_core.skill_builder import CustomSkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.dispatch_components import AbstractExceptionHandler
from ask_sdk_core.handler_input import HandlerInput
from ask_sdk_core.api_client import DefaultApiClient

from ask_sdk_model import Response

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class LaunchRequestHandler(AbstractRequestHandler):
    """Handler for Skill Launch."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        print('ta logando?')
        return ask_utils.is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Olá! Sou a skill do sas. Quando você nasceu?"
        reprompt_text = "Eu nasci dia 14 de agosto de 2000 e você?"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(reprompt_text)
                .response
        )

class HasBirthdayLaunchRequestHandler(AbstractRequestHandler):
    """Handler for launch after they have set their birthday"""

    def can_handle(self, handler_input):
        # extract persistent attributes and check if they are all present
        attr = handler_input.attributes_manager.persistent_attributes
        attributes_are_present = ("year" in attr and "month" in attr and "day" in attr)

        return attributes_are_present and ask_utils.is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        attr = handler_input.attributes_manager.persistent_attributes
        year = int(attr['year'])
        month = attr['month'] # month is a string, and we need to convert it to a month index later
        day = int(attr['day'])

        # get device id
        sys_object = handler_input.request_envelope.context.system
        device_id = sys_object.device.device_id

        # get Alexa Settings API information
        api_endpoint = sys_object.api_endpoint
        api_access_token = sys_object.api_access_token

        # construct systems api timezone url
        url = '{api_endpoint}/v2/devices/{device_id}/settings/System.timeZone'.format(api_endpoint=api_endpoint, device_id=device_id)
        headers = {'Authorization': 'Bearer ' + api_access_token}

        userTimeZone = ""
        try:
	        r = requests.get(url, headers=headers)
	        res = r.json()
	        logger.info("Device API result: {}".format(str(res)))
	        userTimeZone = res
        except Exception:
	        handler_input.response_builder.speak("Ocorreu um problema ao conectar ao serviço")
	        return handler_input.response_builder.response

        # getting the current date with the time
        now_time = datetime.now(timezone(userTimeZone))

        # Removing the time from the date because it affects our difference calculation
        now_date = datetime(now_time.year, now_time.month, now_time.day)
        current_year = now_time.year

        # getting the next birthday
        month_as_index = list(calendar.month_abbr).index(month[:3])
        next_birthday = datetime(current_year, month_as_index, day)

        # check if we need to adjust bday by one year
        if now_date > next_birthday:
            next_birthday = datetime(
                current_year + 1,
                month_as_index,
                day
            )
            current_year += 1
        # setting the default speak_output to Happy xth Birthday!!
        # alexa will automatically correct the ordinal for you.
        # no need to worry about when to use st, th, rd
        speak_output = "Feliz aniversário de {} anos".format(str(current_year - year))
        if now_date != next_birthday:
            diff_days = abs((now_date - next_birthday).days)
            speak_output = "Bem vindo de volta. Parece que faltam \
                            {days} dias até seu aniversário de  {birthday_num}\
                            anos".format(
                                days=diff_days,
                                birthday_num=(current_year-year)
                            )

        handler_input.response_builder.speak(speak_output)

        return handler_input.response_builder.response

class CaptureBirthdayIntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("CaptureBirthdayIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        slots = handler_input.request_envelope.request.intent.slots
        year = slots["year"].value
        month = slots["month"].value
        day = slots["day"].value

        attributes_manager = handler_input.attributes_manager

        birthday_attributes = {
            "year": year,
            "month": month,
            "day": day
        }

        attributes_manager.persistent_attributes = birthday_attributes
        attributes_manager.save_persistent_attributes()

        speak_output = 'Obrigado, vou lembrar que nasceu dia {day} de {month} de {year}.'.format(month=month, day=day, year=year)

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )


class HelpIntentHandler(AbstractRequestHandler):
    """Handler for Help Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AMAZON.HelpIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "You can say hello to me! How can I help?"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )


class CancelOrStopIntentHandler(AbstractRequestHandler):
    """Single handler for Cancel and Stop Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (ask_utils.is_intent_name("AMAZON.CancelIntent")(handler_input) or
                ask_utils.is_intent_name("AMAZON.StopIntent")(handler_input))

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Adeus!"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .response
        )


class SessionEndedRequestHandler(AbstractRequestHandler):
    """Handler for Session End."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("SessionEndedRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response

        # Any cleanup logic goes here.

        return handler_input.response_builder.response


class IntentReflectorHandler(AbstractRequestHandler):
    """The intent reflector is used for interaction model testing and debugging.
    It will simply repeat the intent the user said. You can create custom handlers
    for your intents by defining them above, then also adding them to the request
    handler chain below.
    """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("IntentRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        intent_name = ask_utils.get_intent_name(handler_input)
        speak_output = "You just triggered " + intent_name + "."

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )


class CatchAllExceptionHandler(AbstractExceptionHandler):
    """Generic error handling to capture any syntax or routing errors. If you receive an error
    stating the request handler chain is not found, you have not implemented a handler for
    the intent being invoked or included it in the skill builder below.
    """
    def can_handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> bool
        return True

    def handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> Response
        logger.error(exception, exc_info=True)

        speak_output = "Desculpe, não entendi, pode repetir?."

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

# The SkillBuilder object acts as the entry point for your skill, routing all request and response
# payloads to the handlers above. Make sure any new handlers or interceptors you've
# defined are included below. The order matters - they're processed top to bottom.


sb = CustomSkillBuilder(persistence_adapter=s3_adapter, api_client=DefaultApiClient())

sb.add_request_handler(HasBirthdayLaunchRequestHandler())
sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(CaptureBirthdayIntentHandler())
sb.add_request_handler(HelpIntentHandler())
sb.add_request_handler(CancelOrStopIntentHandler())
sb.add_request_handler(SessionEndedRequestHandler())
sb.add_request_handler(IntentReflectorHandler()) # make sure IntentReflectorHandler is last so it doesn't override your custom intent handlers

sb.add_exception_handler(CatchAllExceptionHandler())

lambda_handler = sb.lambda_handler()