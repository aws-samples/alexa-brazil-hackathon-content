from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk.standard import StandardSkillBuilder
from ask_sdk_core.utils import is_request_type, is_intent_name
from ask_sdk_model.dialog.delegate_directive import DelegateDirective
import random
import re
import os
#################
# Set Up Logger #
#################
import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

###########
# Globals #
###########
DB = os.environ.get('DDB_NAME', None)
if DB:
    sb = StandardSkillBuilder(
        table_name=DB, auto_create_table=True)
else:
    logger.info("DB Name not set")
    sb = SkillBuilder()

###########
# Outputs #
###########
SKILL_NAME = "Ice Cream Parlor"
#Randomize speechcons
SPEECHCONS = {
    'excited': [
        "high five",
        "hurray",
        "kaboom",
        "kerching",
        "magnificent",
        "okey dokey",
        "splendid",
        "way to go",
        "wahoo",
        "well done",
        "yahoo",
        "yippee"
    ],
    'apology': [
        "aw man",
        "aww applesauce",
        "d'oh",
        "fiddlesticks",
        "good grief",
        "gracious me",
        "my bad",
        "my goodness",
        "oof",
        "oops",
        "ruh roh",
        "shucks",
        "uh oh",
        "whoops"
    ]
}
logger.info("Outputs are set")
#############
# Utilities #
#############
def get_speechcon(emotion):
    speech_con_number = random.randint(0,(int(len(SPEECHCONS[emotion])-1)))
    return '<say-as interpret-as="interjection">%s</say-as>.' % SPEECHCONS[emotion][speech_con_number]
def prepare_card(text):
    return re.sub('<[^<]+?>', '', text)
def set_session_attr(handler_input, key, value):
    handler_input.attributes_manager.session_attributes[key]=value
    return handler_input
def append_session_attr(handler_input, key, value):
    if value != None:
        if key in handler_input.attributes_manager.session_attributes:
                handler_input.attributes_manager.session_attributes[key].append(value)
        else:
                handler_input.attributes_manager.session_attributes[key] = []
                handler_input.attributes_manager.session_attributes[key].append(value)
    return handler_input
def get_session_attr(handler_input, key):
    try:
        return handler_input.attributes_manager.session_attributes.get(key, None)
    except:
        return None
def get_slot(handler_input, slot):
    try:
        return handler_input.request_envelope.request.intent.slots.get(slot, None)
    except:
        return None
def del_session_attr(handler_input, key):
    try:
        del handler_input.attributes_manager.session_attributes[key]
        return
    except:
        return
def save_data(handler_input):
    try:
        handler_input.attributes_manager.persistent_attributes = handler_input.attributes_manager.session_attributes
        handler_input.attributes_manager.save_persistent_attributes()
        return True
    except:
        return False
def get_data_from_database(handler_input):
    try:
        handler_input.attributes_manager.persistent_attributes = handler_input.attributes_manager.session_attributes = handler_input.attributes_manager.persistent_attributes
    except:
        return None


SPEECH = {
    'End': "Goodbye!",
    'Exception': "Sorry, there was some problem. Please try again!",
    'LaunchRequest': "Welcome to %s! To begin making ice cream just say, Lets start." % SKILL_NAME,
    'CancelIntent': "Okay. To start over you can say, Lets start. If you would like to exit the %s, just say, stop." % SKILL_NAME,
    'StopIntent': "Thank you for making ice cream together! Come back soon!",
    'HelpIntent': "If you would like to start making Ice Cream, just say, lets start. To add a topping, just say, I want sprinkles",
    'addTopping': "%s If you would like to add more toppings just tell me what you would like. To start over, just say, lets start." % get_speechcon('excited'),
    'addToppingNoIceCream': "That sounded like a topping, but I did not get your ice cream flavor yet. Just tell me flavor of ice cream you would like.",
    'Start': "Now, every good ice cream starts with a base, so tell me what flavor of ice cream do you want?",
    'StartReplay': "What flavor of ice cream do you want?",
    'IceCreamBuilder': "%s Now, what are some toppings you would like to add?" % get_speechcon('excited'),
    'IceCreamBuilderWithTopping': "%s If you would like to add toppings just tell me what you would like. When you are done adding toppings, just say, all done." % get_speechcon('excited'),
    'Finish': "Alright! What a wonderful %s ice cream with %s! To make a new ice cream just say, lets start!",
    'FinishNoState': "%s It does not appear that you have created an ice cream yet. To start, just say, Lets start. To exit, just say, close" % get_speechcon('apology'),
    'FinishNoTopping': "Alright! What a wonderful %s ice cream. Next time, add some toppings by saying, Add fudge. To make a new ice cream just say, lets start!",
    'FinishNoFlavor': "%s It does not appear that you have created an ice cream yet. To start, just say, Lets start. To exit, just say, close" % get_speechcon('apology'),
    'Fallback': "%s I cannot help you with that. To start making ice cream, just say, lets start. For help, you can say, help" % get_speechcon('apology')
}

REPROMPT = {
    'addTopping': "To add a topping just tell me what you want to add. To start over, just say, lets start.",
    'IceCreamBuilder': "To add a topping just tell me what you want to add. To start over, just say, lets start.",
    'IceCreamBuilderWithTopping': "To add a topping just tell me what you want to add. To start over, just say, all done.",
    'Fallback': "To start making ice cream, just say, lets start. For help, you can say, help"
}
logger.info("Utilities are set")

############
# Handlers #
############
## Custom Intents ##
@sb.request_handler(can_handle_func=is_intent_name("IceCreamBuilderIntent"))
def ice_cream_builder_intent_handler(handler_input):
    """Handler for Ice Cream Builder Intent."""
    # type: (HandlerInput) -> Response
    logger.info("Entering IceCreamBuilderIntent")
    flavor = get_slot(handler_input, slot='flavor')
    topping = get_slot(handler_input, slot='topping')
    if flavor.value:
        handler_input = set_session_attr(handler_input, key='FLAVOR', value=flavor.value)
        logger.info("Set flavor to %s" % flavor.value)
        if topping.value:
            logger.info("Set topping to %s" % topping.value) 
            handler_input = append_session_attr(handler_input, key='TOPPING', value=topping.value)
            speech_text = SPEECH['IceCreamBuilderWithTopping']
            reprompt = REPROMPT['IceCreamBuilderWithTopping']
            handler_input = set_session_attr(handler_input, key='STATE', value='TOPPING')
        else:
            speech_text = SPEECH['IceCreamBuilder']
            reprompt = REPROMPT['IceCreamBuilder']
            handler_input = set_session_attr(handler_input, key='STATE', value='FLAVOR')
        return handler_input.response_builder.speak(speech_text).ask(reprompt).set_should_end_session(
            False).response
    else:
        
        handler_input.response_builder.add_directive(DelegateDirective())
        return handler_input.response_builder.response

@sb.request_handler(can_handle_func=is_intent_name("StartIntent"))
def start_intent_handler(handler_input):
    """Handler for Start Intent."""
    # type: (HandlerInput) -> Response
    logger.info("Entering StartIntent")
    if get_session_attr(handler_input, key='STATE'):
        speech_text = SPEECH['StartReplay']
        del_session_attr(handler_input, 'TOPPING')
        del_session_attr(handler_input, 'FLAVOR')
    else:
        speech_text = SPEECH['Start']
    handler_input = set_session_attr(handler_input, key='STATE', value='START')
    return handler_input.response_builder.speak(speech_text).set_should_end_session(
        False).response

@sb.request_handler(can_handle_func=is_intent_name("FinishIntent"))
def finish_intent_handler(handler_input):
    """Handler for Finish Intent."""
    # type: (HandlerInput) -> Response
    logger.info("Entering FinishIntent")
    if get_session_attr(handler_input, key='STATE'):
        flavor = get_session_attr(handler_input, key='FLAVOR')
        topping = get_session_attr(handler_input, key='TOPPING')
        toppingList = ""
        if topping:
            if len(topping) > 1:
                topping[-1]= 'and ' + topping[-1]
                for t in topping:
                    toppingList += "%s, " % t
                #remove last comma and space
                toppingList = toppingList[:-2]
            else:
                toppingList = topping[0]
        if not flavor:
            speech_text = SPEECH['FinishNoFlavor']
        elif not toppingList:
            speech_text = SPEECH['FinishNoTopping'] % flavor
            handler_input = set_session_attr(handler_input, key='STATE', value='Finish')
        else:
            speech_text = SPEECH['Finish'] % (flavor, toppingList)
            handler_input = set_session_attr(handler_input, key='STATE', value='Finish')
    else:
        speech_text = SPEECH['FinishNoState']
    return handler_input.response_builder.speak(speech_text).set_should_end_session(
        False).response

@sb.request_handler(can_handle_func=is_intent_name("addToppingIntent"))
def add_topping_intent_handler(handler_input):
    """Handler for Add Topping Intent."""
    # type: (HandlerInput) -> Response
    logger.info("Entering addToppingIntent")
    topping = get_slot(handler_input, slot='topping')
    if topping:
        handler_input = append_session_attr(handler_input, key='TOPPING', value=topping.value)
        speech_text = SPEECH['addTopping']
        reprompt = REPROMPT['addTopping']
        handler_input = set_session_attr(handler_input, key='STATE', value='Topping')
        return handler_input.response_builder.speak(speech_text).ask(reprompt).set_should_end_session(
            False).response
    else:
        handler_input.response_builder.add_directive(DelegateDirective())
        return handler_input.response_builder.response

## Built-in Intents ##
@sb.request_handler(can_handle_func=is_request_type("LaunchRequest"))
def launch_request_handler(handler_input):
    """Handler for Skill Launch."""
    # type: (HandlerInput) -> Response
    logger.info("Entering LaunchRequest")
    get_data_from_database(handler_input)
    speech_text = SPEECH['LaunchRequest']

    return handler_input.response_builder.speak(speech_text).set_should_end_session(
        False).response

@sb.request_handler(can_handle_func=is_intent_name("AMAZON.HelpIntent"))
def help_intent_handler(handler_input):
    """Handler for Help Intent."""
    # type: (HandlerInput) -> Response
    logger.info("Entering HelpIntent")
    speech_text = SPEECH['HelpIntent']

    return handler_input.response_builder.speak(speech_text).ask(
        speech_text).response

@sb.request_handler(can_handle_func=is_intent_name("AMAZON.StopIntent"))
def stop_intent_handler(handler_input):
    """Handler for Stop Intent."""
    # type: (HandlerInput) -> Response
    logger.info("Entering AMAZON.StopIntent")
    speech_text = SPEECH['StopIntent']

    return handler_input.response_builder.speak(speech_text).set_should_end_session(
        True).response

@sb.request_handler(can_handle_func=is_intent_name("AMAZON.CancelIntent"))
def cancel_intent_handler(handler_input):
    """Handler for Cancel Intent."""
    # type: (HandlerInput) -> Response
    logger.info("Entering AMAZON.CancelIntent")
    speech_text = SPEECH['CancelIntent']

    return handler_input.response_builder.speak(speech_text).set_should_end_session(
        False).response

@sb.request_handler(can_handle_func=is_intent_name("AMAZON.FallbackIntent"))
def fallback_handler(handler_input):
    """AMAZON.FallbackIntent is only available in en-US locale.
    This handler will not be triggered except in that locale,
    so it is safe to deploy on any locale.
    """
    # type: (HandlerInput) -> Response
    logger.info("Entering AMAZON.FallbackIntent")
    speech = SPEECH['Fallback']
    reprompt = REPROMPT['Fallback']
    handler_input.response_builder.speak(speech).ask(reprompt)
    return handler_input.response_builder.response

@sb.request_handler(can_handle_func=is_request_type("SessionEndedRequest"))
def session_ended_request_handler(handler_input):
    """Handler for Session End."""
    # type: (HandlerInput) -> Response
    logger.info("Entering AMAZON.SessionEndedRequest")
    save_data(handler_input)
    return handler_input.response_builder.response
logger.info("Handlers are set")
handler = sb.lambda_handler()