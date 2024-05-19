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

No AWS CDK (Cloud Development Kit), os conceitos de **construções** (constructs) e **stacks** são fundamentais para a organização e gerenciamento de recursos da infraestrutura como código.

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
---

# Estrutura de diretórios

Quando você executa o comando `cdk init app --language python` para iniciar um novo projeto AWS CDK em Python, o AWS CDK cria uma estrutura de diretórios padrão que serve como ponto de partida para o desenvolvimento da infraestrutura como código. Aqui está uma descrição detalhada da estrutura de diretórios e dos arquivos gerados:

```
my-cdk-app/
├── README.md
├── app.py
├── cdk.json
├── requirements.txt
├── source.bat
├── source.ps1
├── my_cdk_app/
│   ├── __init__.py
│   ├── my_cdk_app_stack.py
├── tests/
│   ├── __init__.py
│   └── unit/
│       ├── __init__.py
│       └── test_my_cdk_app_stack.py
├── .gitignore
└── .venv/
```

### Detalhamento dos Arquivos e Diretórios

#### Arquivos na Raiz

- **`README.md`**: Arquivo de documentação que descreve o seu projeto e fornece informações básicas sobre como configurá-lo e usá-lo.

- **`app.py`**: Arquivo principal do aplicativo CDK. É aqui que a aplicação CDK é instanciada e as stacks são definidas e adicionadas ao aplicativo. Exemplo de conteúdo:
  ```python
  # app.py
  from aws_cdk import core
  from my_cdk_app.my_cdk_app_stack import MyCdkAppStack

  app = core.App()
  MyCdkAppStack(app, "my-cdk-app")

  app.synth()
  ```

- **`cdk.json`**: Arquivo de configuração do CDK, que define como o CDK deve ser executado. Exemplo de conteúdo:
  ```json
  {
    "app": "python3 app.py"
  }
  ```

- **`requirements.txt`**: Arquivo que lista as dependências Python necessárias para o projeto. Inclui o `aws-cdk.core` e outras bibliotecas CDK que você venha a utilizar. Exemplo de conteúdo:
  ```plaintext
  aws-cdk.core
  ```

- **`source.bat` e `source.ps1`**: Scripts para ativar o ambiente virtual do Python no Windows (Batch e PowerShell, respectivamente).

- **`.gitignore`**: Arquivo de configuração que especifica quais arquivos e diretórios devem ser ignorados pelo Git. Inclui diretórios como `.venv` e arquivos gerados pelo CDK.

- **`.venv/`**: Diretório onde o ambiente virtual do Python será configurado (este diretório pode não existir imediatamente após a inicialização, mas será criado quando você configurar o ambiente virtual).

#### Diretório `my_cdk_app/`

- **`__init__.py`**: Arquivo que torna este diretório um pacote Python. Geralmente está vazio.

- **`my_cdk_app_stack.py`**: Arquivo onde você define a sua stack principal. Este arquivo contém a definição dos recursos AWS que compõem sua aplicação. Exemplo de conteúdo:
  ```python
  from aws_cdk import core
  from aws_cdk import aws_s3 as s3

  class MyCdkAppStack(core.Stack):

      def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
          super().__init__(scope, id, **kwargs)

          # Definição de um bucket S3
          s3.Bucket(self, 
                    "MyFirstBucket",
                    versioned=True,
                    removal_policy=core.RemovalPolicy.DESTROY)
  ```

#### Diretório `tests/`

- **`__init__.py`**: Arquivo que torna este diretório um pacote Python. Geralmente está vazio.

- **`unit/`**: Subdiretório para testes unitários.

  - **`__init__.py`**: Arquivo que torna este diretório um pacote Python. Geralmente está vazio.
  
  - **`test_my_cdk_app_stack.py`**: Arquivo onde você pode escrever testes unitários para a sua stack usando frameworks como `unittest` ou `pytest`. Exemplo de conteúdo:
    ```python
    import unittest
    from aws_cdk import core
    from my_cdk_app.my_cdk_app_stack import MyCdkAppStack

    class TestMyCdkAppStack(unittest.TestCase):

        def test_s3_bucket_created(self):
            app = core.App()
            stack = MyCdkAppStack(app, "test-stack")
            template = app.synth().get_stack_by_name("test-stack").template

            # Verificar se um bucket S3 foi criado
            self.assertIn("AWS::S3::Bucket", template["Resources"])
    ```

### Configuração do Ambiente Virtual

Para configurar o ambiente virtual Python e instalar as dependências, siga estes passos:

1. **Criar o ambiente virtual**:
   ```sh
   python3 -m venv .venv
   ```

2. **Ativar o ambiente virtual**:
   - No Linux/macOS:
     ```sh
     source .venv/bin/activate
     ```
   - No Windows (Cmd):
     ```cmd
     .venv\Scripts\activate.bat
     ```
   - No Windows (PowerShell):
     ```ps1
     .venv\Scripts\Activate.ps1
     ```

3. **Instalar as dependências**:
   ```sh
   pip install -r requirements.txt
   ```

Esta estrutura proporciona uma base organizada para desenvolver e gerenciar a infraestrutura com AWS CDK em Python, facilitando a manutenção, a escalabilidade e a colaboração no projeto.

---
# Conceito de Assets

No AWS CDK (Cloud Development Kit), **assets** são recursos que permitem incluir arquivos externos, como arquivos estáticos, imagens de contêiner, código-fonte de aplicações Lambda, entre outros, diretamente nas suas stacks. Eles são utilizados para empacotar e implantar esses arquivos juntamente com sua infraestrutura definida pelo CDK.

### Tipos de Assets

Existem dois tipos principais de assets no AWS CDK:

1. **Assets de Arquivo**: Permitem incluir arquivos ou diretórios do sistema de arquivos local no seu aplicativo CDK. Esses arquivos são carregados para o Amazon S3 e referenciados nas suas stacks.

2. **Assets de Imagem de Contêiner**: Permitem construir e carregar imagens de contêiner Docker para o Amazon Elastic Container Registry (ECR), facilitando a implantação de aplicações baseadas em contêiner.

### Uso de Assets de Arquivo

Um uso comum de assets de arquivo é empacotar o código-fonte para funções AWS Lambda. Aqui está um exemplo de como utilizar assets para uma função Lambda:

#### Exemplo de Uso de Assets para uma Função Lambda

1. **Estrutura de Diretórios**:
    ```
    my-cdk-app/
    ├── app.py
    ├── cdk.json
    ├── lambda/
    │   └── handler.py
    ├── my_cdk_app/
    │   ├── __init__.py
    │   └── my_cdk_app_stack.py
    └── requirements.txt
    ```

2. **Arquivo `lambda/handler.py`**:
    ```python
    def handler(event, context):
        return {
            'statusCode': 200,
            'body': 'Hello from Lambda!'
        }
    ```

3. **Definindo a Stack com Assets no `my_cdk_app/my_cdk_app_stack.py`**:
    ```python
    from aws_cdk import core
    from aws_cdk import aws_lambda as _lambda

    class MyCdkAppStack(core.Stack):

        def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
            super().__init__(scope, id, **kwargs)

            # Definição da função Lambda utilizando assets
            lambda_function = _lambda.Function(
                self, 'MyLambdaFunction',
                runtime=_lambda.Runtime.PYTHON_3_8,
                handler='handler.handler',
                code=_lambda.Code.from_asset('lambda')
            )
    ```

### Uso de Assets de Imagem de Contêiner

Para assets de imagem de contêiner, você pode usar o AWS CDK para construir e carregar imagens Docker para o ECR.

#### Exemplo de Uso de Assets para uma Imagem de Contêiner

1. **Estrutura de Diretórios**:
    ```
    my-cdk-app/
    ├── Dockerfile
    ├── app.py
    ├── cdk.json
    ├── my_cdk_app/
    │   ├── __init__.py
    │   └── my_cdk_app_stack.py
    └── requirements.txt
    ```

2. **Arquivo `Dockerfile`**:
    ```Dockerfile
    FROM public.ecr.aws/lambda/python:3.8
    COPY app.py ${LAMBDA_TASK_ROOT}
    CMD ["app.handler"]
    ```

3. **Definindo a Stack com Assets no `my_cdk_app/my_cdk_app_stack.py`**:
    ```python
    from aws_cdk import core
    from aws_cdk import aws_lambda as _lambda

    class MyCdkAppStack(core.Stack):

        def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
            super().__init__(scope, id, **kwargs)

            # Definição da função Lambda utilizando uma imagem Docker
            lambda_function = _lambda.DockerImageFunction(
                self, 'MyDockerLambdaFunction',
                code=_lambda.DockerImageCode.from_image_asset('.')
            )
    ```

### Funcionamento Interno dos Assets

Quando você usa assets no AWS CDK:

1. **Empacotamento**: Os arquivos especificados (ou a imagem Docker) são empacotados no seu diretório local.
2. **Carregamento**: Os assets são carregados para um bucket S3 (para arquivos) ou para o ECR (para imagens Docker) gerenciado pelo CDK.
3. **Referenciamento**: O CDK gera automaticamente as permissões necessárias e os metadados para que os recursos da AWS possam acessar esses assets.

### Resumo

- **Assets de Arquivo**: Empacotam e carregam arquivos ou diretórios locais para o S3.
- **Assets de Imagem de Contêiner**: Constroem e carregam imagens Docker para o ECR.
- **Utilização**: Facilitam a inclusão de arquivos externos, como código-fonte para Lambda ou imagens Docker, nas suas stacks CDK.
- **Automatização**: O CDK cuida de empacotar, carregar e gerenciar permissões para os assets, simplificando o processo de implantação.

Essa funcionalidade é poderosa para gerenciar e implantar componentes complexos da infraestrutura com facilidade e eficiência no AWS CDK.