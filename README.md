# Alexathon

Este repositório contém o material de apoio e regras do Hackaton de Alexa.

</br>
<p align="center"><img src="images/alexa.png" height="250" weight="250"/></p>
</br>

* *Governo*
    * Consultas de serviços ao cidadão
    * Consultas de pendências institucionais
    * Consulta de situação orçamentária para tomada de decisão
    * Consultas jurídicas
    * Agendamento de serviço ao cidadão


* *Educação*
    * Consulta de boletim
    * Consulta de grade escolar e sala
    * Comunicação pais e mestres
    * Comunicação mestres e alunos
    * Notificação de ausência escolar
* *Saúde*
    * Comunicação médicos e pacientes
    * Consulta de dados do pacientes pelo médicos
    * Agendamento de Consulta
    * Notificação de alterações nos sinais vitais do paciente
    * Lembretes de medicação
    
    
## Agenda:

    9:00 – 9:15 Boas-Vindas.
    9:15 – 10:00 Workshops de Design de Voz e Criação de Skills.
    10:00 – 18:30 Criação de skills.
    18:30 – 19:00 Apresentação.
    19:00 – 19:30 Premiação e Agradecimentos.



Obs: Os momentos de lanches e coffe não impediremos a continuidade das atividades então as equipes podem se organizar/revezar entre quem lancha e desenvolve da forma que acharem mais interessante.

## Regras:

  - Seu time tem 8 horas para desenvolver uma Skill baseada em algum dos temas propostos na apresentação do evento.
  - A Skill desenvolvida pelo seu time deve estar em Português (Brasil).
  - O pitch da sua Skill deve ter no máximo 5 minutos e deve incluir uma demonstração.
  - Sua Skill deve ser original.
  - Sua equipe pode usar qualquer recurso fora do Alexa Hosted-Skill.

## Materiais de apoio:

Nesse repositório você pode encontrar os exemplos que demonstramos no workshop na pasta **examples**.

Além disso, você pode utilizar a documentação da Alexa e da AWS:

* Exemplos do uso de API Alexa: https://github.com/alexa/alexa-cookbook
* Alexa SDK (Python, Node.js e Java): https://developer.amazon.com/docs/alexa-skills-kit-sdk-for-python/overview.html
* Alexa Skills Kit : https://developer.amazon.com/en-US/alexa/alexa-skills-kit
* Cake Walk (Skill criada do 0 com memória persistente): https://developer.amazon.com/pt-BR/alexa/alexa-skills-kit/courses/cake-walk-1
* Speech Synthesis Markup Language (SSML) Reference: https://developer.amazon.com/docs/custom-skills/speech-synthesis-markup-language-ssml-reference.html
* Alexa Skills Kit Sound Library: https://developer.amazon.com/docs/custom-skills/ask-soundlibrary.html
* Skillinator: https://skillinator.io/ / Alternativa (caso skillinator esteja fora do ar) : https://s3.amazonaws.com/webappvui/skillcode/v2/index.html
* Configurando o back-end de uma skill: https://www.youtube.com/watch?v=Vi3oGj1k0W0&t=169s
* Converter audio para formatos aceitos pela Alexa: https://www.jovo.tech/audio-converter
* Bibliotecas SDK (AWS):
  * JS: https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/index.html
  * Python: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/index.html
  * Java: https://sdk.amazonaws.com/java/api/latest/
  * Usando S3 pelo Python: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html

Caso queira se aprofundar um pouco mais no desenvolvimento de aplicações serverless, você pode consultar esses materiais:

* O que é Serverless: https://aws.amazon.com/serverless/?nc1=h_ls
* AWS Serverless Framework: https://aws.amazon.com/serverless/sam/

## Design de voz, checklist:

1. Idealize
2. Identifique seus usuários
3. Faça o script!
4. Anote sinônimos de fala
5. Encontre "slots" na lógica contextual
6. Reduza o desgaste das conversas


## Melhores práticas ao desenvolver uma skill:

1. Faça só uma coisa, mas faça muito bem
2. Use um nome de invocação memorável e fácil de falar
3. Simplifique escolhas
4. Inclua uma variedade de respostas
5. Provenha ajuda contextual
6. Faça testes beta


## License summary
This sample code is made available under the MIT-0 license. See the LICENSE file.
