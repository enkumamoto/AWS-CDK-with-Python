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

O AWS CDK é baseado no Node.js. Você precisa instalá-lo junto com o npm (gerenciador de pacotes do Node.js). No Ubuntu, você pode usar o NodeSource para instalar a versão mais recente do Node.js.
Execute os seguintes comandos:

```
curl -fsSL https://deb.nodesource.com/setup_16.x | sudo -E bash -
sudo apt-get install -y nodejs

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

Inicialize um novo projeto CDK:

```
cdk init app --language python
```

## Passo 6: Configurar ambiente python
É recomendável usar um ambiente virtual para gerenciar suas dependências Python. Crie e ative um ambiente:

```
# Crie um ambiente virtual
python3 -m venv .venv

# Ative o ambiente virtual
source .venv/bin/activate

```

Agora, com o ambiente virtual ativado, você pode instalar o AWS CDK para Python:

```
pip install aws-cdk-lib
pip install constructs
```


## Passo 7: Instalar Dependências Adicionais

Durante a inicialização do projeto, o CDK criará um arquivo requirements.txt. Para instalar as dependências listadas, execute:

```
pip install -r requirements.txt
```

## Passo 8: Sintetizar e Implantar a Pilha

Depois de configurar tudo, você pode sintetizar (gerar) o CloudFormation template e implantar a pilha:

```
# Sintetizar a pilha
cdk synth

# Implantar a pilha
cdk deploy
```

## Passo 9: Limpar Recursos

Para excluir os recursos criados, você pode usar o comando:

```
cdk destroy
```

---
# Conceitos de Contruções e Stacks

No AWS CDK (Cloud Development Kit), os conceitos de **construções** (constructs) e **stacks** são fundamentais para a organização e gerenciamento de recursos da infraestrutura como código. Vou explicar cada um deles:

### Construções (Constructs)

**Construções** são os blocos de construção básicos do AWS CDK. Elas representam componentes ou padrões reutilizáveis da infraestrutura. Podem ser desde recursos individuais da AWS (como uma instância EC2 ou um bucket S3) até conjuntos mais complexos de recursos que trabalham juntos para cumprir um propósito específico (como uma aplicação web completa).

Existem três níveis de construções no AWS CDK:

1. **Nível 1 (L1) - Constructs de Nível Baixo**:
   - Representam diretamente os recursos da AWS.
   - São gerados a partir dos arquivos CloudFormation.
   - Exemplo: `s3.CfnBucket` representa um bucket S3 no nível CloudFormation.

2. **Nível 2 (L2) - Constructs de Nível Médio**:
   - São abstrações opinativas dos recursos de nível 1, oferecendo interfaces mais amigáveis e funcionalidades integradas.
   - Exemplo: `s3.Bucket` é uma construção L2 que facilita a criação e configuração de um bucket S3.

3. **Nível 3 (L3) - Constructs de Nível Alto**:
   - São padrões completos que combinam múltiplos recursos para resolver casos de uso específicos.
   - Exemplo: `aws_solutions_constructs.aws_s3_lambda` que configura um bucket S3 junto com uma função Lambda que responde a eventos desse bucket.

### Stacks

**Stacks** são as unidades de implantação no AWS CDK. Elas representam a coleção de construções que formam a sua aplicação ou uma parte dela. Cada stack é convertida em um modelo do CloudFormation quando você implanta a aplicação CDK.

- **Stack** é uma coleção de recursos que você quer implantar juntos. 
- Cada stack é implementada como uma classe que herda de `cdk.Stack`.
- Você pode definir múltiplas stacks dentro de uma aplicação CDK para separar diferentes partes da sua infraestrutura.

#### Exemplo de uma Stack com Construções

Aqui está um exemplo básico em Python, onde criamos uma stack com um bucket S3 usando uma construção de nível 2:

```python
from aws_cdk import (
    core,
    aws_s3 as s3
)

class MyFirstStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Construção de nível 2 para criar um bucket S3
        my_bucket = s3.Bucket(self, 
                              "MyFirstBucket", 
                              versioned=True,
                              removal_policy=core.RemovalPolicy.DESTROY)

app = core.App()
MyFirstStack(app, "MyFirstStack")
app.synth()
```

Neste exemplo:
- Definimos uma classe `MyFirstStack` que herda de `core.Stack`.
- Dentro do construtor da stack, criamos um bucket S3 usando a construção de nível 2 `s3.Bucket`.
- A stack `MyFirstStack` é então instanciada e adicionada ao aplicativo CDK (`app`), e o método `synth()` é chamado para sintetizar o modelo CloudFormation.

### Resumo

- **Construções** são blocos de construção reutilizáveis que representam componentes da infraestrutura.
- **Stacks** são coleções de construções que formam uma unidade de implantação.

Esses conceitos permitem a você estruturar, organizar e gerenciar a infraestrutura de forma eficiente e modular no AWS CDK.