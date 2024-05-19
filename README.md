# AWS-CDK-with-Python
Files from AWS CDK with Python class

## About
Here you may find something you need for your infrastructure. But remember, this repository contains files that were used to understand the concepts and perform additional exercises for the classes on AWS CDK.

More details in Portuguese

---

## Sobre 
Aqui você talvez encontre alguma coisa que você precise para sua infraestrutura. Mas lembre-se, neste repositório há arquivos que foram usados para entender os conceitos e executar exercícios complementares as aulas sobre AWS CDK.

## Como Instalar AWS CDK no Ubuntu
Como instalar o AWS Cloud Development Kit (CDK) e suas dependências no Ubuntu 22.04. Vamos lá! 🚀

## Passo 1: Atualize seu sistema

Primeiro, certifique-se de que seu sistema está atualizado. Abra o terminal e execute:

```
sudo apt update
sudo apt upgrade -y
```

## Passo 2: Instale o Node.js e o npm

O AWS CDK é baseado no Node.js. Você precisa instalá-lo junto com o npm (gerenciador de pacotes do Node.js). Execute os seguintes comandos:

```
sudo apt install -y nodejs npm
```

Verifique a instalação do Node.js e npm:

```
node -v
npm -v
```
## Passo 3: Instale o AWS CDK
Agora que você tem o Node.js e o npm instalados, você pode instalar o AWS CDK. Execute o seguinte comando:

```
npm install -g aws-cdk
```

Verifique a instalação do AWS CDK

```
cdk --version
```

## Passo 4: Configure as credenciais da AWS

Para que o AWS CDK possa interagir com seus recursos na AWS, você precisa configurar suas credenciais da AWS. Se você ainda não tem o AWS CLI instalado, faça isso com o comando:

```
sudo apt install -y awscli
```

Depois, configure suas credenciais executando:

```
aws configure
```

## Passo 5: Inicialize um novo projeto AWS CDK

Crie um novo diretório para o seu projeto CDK e navegue até ele:

```
mkdir meu-projeto-cdk
cd meu-projeto-cdk
```

