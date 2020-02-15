# Hello World Skill

Segunda Skill demonstrada no workshop.

## Como executar:

## Interface
Para essa skill temos temos dois arquivos. Na pasta **alexa_interface** podemos encontrar a interface da skill. Você pode copiar este JSON e colar no JSON Editor da skill que você está criando.

Serão necessárias algumas modificações no Endpoint do backend da Skill. Mas podemos fazer isso após criar o backend.

## Backend
Estamos utilizando o backend na AWS. Para isso executar é necessário uma conta na AWS com os seguintes acessos:
* AWS Lambda
* Amazon S3

### Criando nosso bucket S3
1) Vá para a console do S3: https://console.aws.amazon.com/s3/
2) Clique em **Create bucket**
3) As informações dos usuários serão armazenadas aqui

### Criando nossa função Lambda
1) Vá para a console do Lambda: https://console.aws.amazon.com/lambda/
2) Clique em criar **Create function**
3) Preencha o nome e selecione **Python3.7**
4) Copie o Skill Id da sua skill. Você pode encontrar na aba Endpoint no alexa developer console
4) Adicione um trigger de **Alexa Skills Kit** com o Skill id
5) Faça o upload do arquivo .zip da pasta **backend**
6) Modifique a duração da função para 10 segundos
7) Modifique sua Role para ter acesso ao S3

### Debugging
Além dos logs no CloudWatch, também podemos testar o backend de maneira local, utilizando o framework SAM: https://aws.amazon.com/serverless/sam/

### Lambda Deployment
* Arquivos compactados: https://docs.aws.amazon.com/pt_br/lambda/latest/dg/lambda-python-how-to-create-deployment-package.html
* SAM: https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-cli-command-reference-sam-deploy.html