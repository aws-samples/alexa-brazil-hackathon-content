# Alexathon

Workshop, material de apoio e regras da Hackaton de Alexathon.

## Agenda:

    9:00 - 9:30 Recepção e check-in.
    9:30 - 9:45 Boas-Vindas.
    9:45 - 11:00 Workshops de Design de Voz e Criação de Skills.
    11:00 - 11:30 O Mercado de Educação e o SAS.
    11:30 - 12:00 Formação dos times.
    12:00 - 16:00 Criação das Skills.
    16:00 - 16:30 Chill Break.
    16:30 - 20:00 Criação das Skills.
    20:00 - 21:00 Apresentações
    21:00 - 22:30 Premiação, Happy Hour e Networking.


Obs: Os momentos de lanches e coffe não impediremos a continuidade das atividades então as equipes podem se organizar/revezar entre quem lancha e desenvolve da forma que acharem mais interessante.

## Regras:

  - Seu time tem 8 horas para desenvolver uma Skill baseada em algum dos temas propostos na apresentação do evento.
  - A Skill desenvolvida pelo seu time deve estar em Português (Brasil).
  - O pitch da sua Skill deve ter no máximo 5 minutos e deve incluir uma demonstração.
  - Sua Skill deve ser original.
  - Sua equipe pode usar qualquer recurso fora do Alexa Hosted-Skill.

## Materiais de apoio:

Nesse repositório você pode encontrar os exemplos que demonstramos no workshop na pasta **examples**. Cada exemplo está divido em etapas, e você pode verificar cada etapa de construção modificando o branch do repositório. Por exemplo: 
```
  git checkout v1 #versão inicial da skill
  git checkout v2 #implementação de features como ssml e interação com o S3
  git checkout master #versão final da demonstração
```


Além disso, você pode utilizar a documentação da Alexa e da AWS:

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
