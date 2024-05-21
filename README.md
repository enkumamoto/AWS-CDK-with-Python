# AWS-CDK-with-Python
Files from AWS CDK with Python class

## About
Here you may find something you need for your infrastructure. But remember, this repository contains files that were used to understand the concepts and perform additional exercises for the classes on AWS CDK.

More details in Portuguese

---

## Sobre 
Aqui você talvez encontre alguma coisa que você precise para sua infraestrutura. Mas lembre-se, neste repositório há arquivos que foram usados para entender os conceitos e executar exercícios complementares as aulas sobre AWS CDK.

## Como Instalar AWS CDK no Ubuntu
Como instalar o AWS Cloud Development Kit (CDK) e suas dependências no Ubuntu 22.04.

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

---

# Multiplos Stacks

No AWS CDK (Cloud Development Kit), você pode organizar sua infraestrutura em múltiplas stacks para melhorar a modularidade, a manutenção e a escalabilidade do seu projeto. Cada stack representa uma coleção de recursos AWS que são implantados juntos. Usar múltiplas stacks permite isolar diferentes partes da sua aplicação, facilitando a implantação, a atualização e o gerenciamento de recursos.

### Vantagens de Usar Múltiplas Stacks

1. **Modularidade**: Separar diferentes partes da infraestrutura em stacks distintas torna o código mais organizado e fácil de entender.
2. **Isolamento**: Isolar recursos relacionados em stacks específicas ajuda a evitar conflitos e facilita a gestão de dependências.
3. **Desempenho**: Ao dividir a infraestrutura em várias stacks, você pode implantar ou atualizar apenas a stack que sofreu mudanças, reduzindo o tempo de implantação.
4. **Escalabilidade**: Facilita o gerenciamento de infraestruturas grandes e complexas, distribuindo a carga entre várias stacks.

### Estrutura de Múltiplas Stacks

Vamos ver um exemplo de como criar um projeto AWS CDK com múltiplas stacks em Python. Suponha que queremos criar um projeto com duas stacks: uma para recursos de rede (como VPCs e sub-redes) e outra para uma aplicação (como buckets S3 e funções Lambda).

#### Estrutura de Diretórios

```
my-multi-stack-app/
├── app.py
├── cdk.json
├── requirements.txt
├── network_stack/
│   ├── __init__.py
│   └── network_stack.py
├── application_stack/
│   ├── __init__.py
│   └── application_stack.py
└── .gitignore
```

#### Arquivo `app.py`

Este é o ponto de entrada da aplicação CDK, onde as stacks são instanciadas e adicionadas ao aplicativo.

```python
from aws_cdk import core
from network_stack.network_stack import NetworkStack
from application_stack.application_stack import ApplicationStack

app = core.App()

# Instanciando a stack de rede
network_stack = NetworkStack(app, "NetworkStack")

# Instanciando a stack da aplicação, que pode depender da stack de rede
application_stack = ApplicationStack(app, "ApplicationStack", vpc=network_stack.vpc)

app.synth()
```

#### Arquivo `network_stack/network_stack.py`

Define a stack de recursos de rede.

```python
from aws_cdk import core
from aws_cdk import aws_ec2 as ec2

class NetworkStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Definição de uma VPC
        self.vpc = ec2.Vpc(self, "MyVpc",
            max_azs=3  # Número de zonas de disponibilidade
        )
```

#### Arquivo `application_stack/application_stack.py`

Define a stack de recursos da aplicação, que utiliza a VPC criada na stack de rede.

```python
from aws_cdk import core
from aws_cdk import aws_s3 as s3
from aws_cdk import aws_lambda as _lambda

class ApplicationStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, vpc, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Exemplo de bucket S3
        bucket = s3.Bucket(self, "MyBucket")

        # Exemplo de função Lambda dentro da VPC
        lambda_function = _lambda.Function(self, "MyFunction",
            runtime=_lambda.Runtime.PYTHON_3_8,
            handler="index.handler",
            code=_lambda.Code.from_asset("lambda"),
            vpc=vpc  # Referência à VPC criada na NetworkStack
        )
```

### Implementando e Gerenciando Dependências entre Stacks

No exemplo acima, a `ApplicationStack` depende da `NetworkStack`, pois a função Lambda na `ApplicationStack` precisa da VPC criada na `NetworkStack`. Passamos a VPC como um parâmetro para a `ApplicationStack` durante sua instânciação em `app.py`.

### Implantação de Múltiplas Stacks

Para implantar o projeto com múltiplas stacks, você pode usar o comando `cdk deploy` especificando as stacks que deseja implantar. Por exemplo:

```sh
cdk deploy NetworkStack
cdk deploy ApplicationStack
```

Ou para implantar todas as stacks:

```sh
cdk deploy --all
```

### Resumo

- **Múltiplas Stacks**: Permitem modularizar e organizar a infraestrutura em coleções distintas de recursos.
- **Vantagens**: Melhor modularidade, isolamento, desempenho e escalabilidade.
- **Implementação**: Criação de várias classes de stack, cada uma representando uma parte da infraestrutura.
- **Gerenciamento de Dependências**: Passagem de recursos entre stacks através de parâmetros no momento da instânciação.

Usar múltiplas stacks no AWS CDK é uma prática recomendada para projetos de infraestrutura grandes e complexos, facilitando a manutenção e a evolução contínua da infraestrutura.

---

# Cross-Stacks References
No AWS CDK (Cloud Development Kit), **cross-stack references** (referências entre stacks) são usadas quando você precisa compartilhar recursos entre diferentes stacks. Isso é útil para modularizar sua infraestrutura e ainda assim permitir que diferentes componentes compartilhem e utilizem recursos comuns.

### Conceito de Cross-Stack References

**Cross-stack references** permitem que uma stack se refira a recursos definidos em outra stack. Isso é alcançado exportando os atributos dos recursos de uma stack e importando-os na outra. O AWS CDK facilita esse processo e garante que as permissões necessárias sejam configuradas corretamente.

### Vantagens das Cross-Stack References

1. **Modularidade**: Permite dividir a infraestrutura em componentes menores e reutilizáveis.
2. **Separação de Responsabilidades**: Facilita a separação de responsabilidades entre diferentes equipes ou áreas do projeto.
3. **Reutilização de Recursos**: Recursos comuns, como VPCs ou buckets S3, podem ser definidos uma vez e reutilizados em várias stacks.

### Exemplo de Uso de Cross-Stack References

Um exemplo onde uma stack define uma VPC e outra stack cria uma função Lambda que usa essa VPC.

#### Estrutura de Diretórios

```
my-cross-stack-app/
├── app.py
├── cdk.json
├── requirements.txt
├── network_stack/
│   ├── __init__.py
│   └── network_stack.py
├── application_stack/
│   ├── __init__.py
│   └── application_stack.py
└── .gitignore
```

#### Arquivo `app.py`

Este arquivo é o ponto de entrada da aplicação CDK, onde as stacks são instanciadas e adicionadas ao aplicativo.

```python
from aws_cdk import core
from network_stack.network_stack import NetworkStack
from application_stack.application_stack import ApplicationStack

app = core.App()

# Instanciando a stack de rede
network_stack = NetworkStack(app, "NetworkStack")

# Instanciando a stack da aplicação, que depende da stack de rede
application_stack = ApplicationStack(app, "ApplicationStack", vpc=network_stack.vpc)

app.synth()
```

#### Arquivo `network_stack/network_stack.py`

Define a stack de rede que cria uma VPC e exporta uma referência a ela.

```python
from aws_cdk import core
from aws_cdk import aws_ec2 as ec2

class NetworkStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Definição de uma VPC
        self.vpc = ec2.Vpc(self, "MyVpc",
            max_azs=3  # Número de zonas de disponibilidade
        )
```

#### Arquivo `application_stack/application_stack.py`

Define a stack de aplicação que importa a VPC da stack de rede e cria uma função Lambda dentro dessa VPC.

```python
from aws_cdk import core
from aws_cdk import aws_lambda as _lambda
from aws_cdk import aws_ec2 as ec2

class ApplicationStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, vpc: ec2.IVpc, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Exemplo de função Lambda dentro da VPC
        lambda_function = _lambda.Function(self, "MyFunction",
            runtime=_lambda.Runtime.PYTHON_3_8,
            handler="index.handler",
            code=_lambda.Code.from_asset("lambda"),
            vpc=vpc  # Referência à VPC criada na NetworkStack
        )
```

### Como Funciona

1. **Exportação**: A stack `NetworkStack` cria uma VPC e a expõe como um atributo.
2. **Importação**: A stack `ApplicationStack` recebe a VPC como parâmetro no seu construtor, permitindo que os recursos definidos na `ApplicationStack` utilizem a VPC da `NetworkStack`.

### Considerações

- **Dependências**: Ao definir dependências entre stacks, o CDK garante que as stacks sejam implantadas na ordem correta.
- **Permissões**: O CDK automaticamente gerencia as permissões necessárias para que os recursos em diferentes stacks possam interagir.

### Implantação

Para implantar as stacks com referências entre elas, você pode usar o comando `cdk deploy --all` para garantir que todas as stacks sejam implantadas na ordem correta:

```sh
cdk deploy --all
```

Ou você pode implantar cada stack individualmente, respeitando a ordem de dependência:

```sh
cdk deploy NetworkStack
cdk deploy ApplicationStack
```

### Resumo

- **Cross-Stack References**: Permitem compartilhar recursos entre diferentes stacks.
- **Modularidade e Reutilização**: Facilitam a modularização e reutilização de recursos comuns.
- **Gerenciamento Automático**: O AWS CDK cuida das dependências e permissões necessárias.
- **Exemplo Prático**: Criação de uma VPC em uma stack e uso dessa VPC em outra stack que define uma função Lambda.

Usar referências entre stacks no AWS CDK é uma prática eficaz para gerenciar infraestruturas complexas de forma modular e escalável.

---
# Nested Stack
No AWS CDK (Cloud Development Kit), uma **nested stack** é uma stack que é definida dentro de outra stack, permitindo uma maior modularização e organização da infraestrutura. Isso facilita a reutilização de componentes e a manutenção de grandes projetos de infraestrutura.

### Conceito de Nested Stack

**Nested stacks** são usadas para criar hierarquias de stacks, onde uma stack principal (parent stack) contém outras stacks (child stacks). As nested stacks são ideais para agrupar logicamente recursos que devem ser gerenciados e implantados juntos, mas que fazem parte de um componente maior.

### Vantagens de Nested Stacks

1. **Modularidade**: Facilita a divisão da infraestrutura em componentes menores e reutilizáveis.
2. **Manutenção**: Simplifica a atualização e o gerenciamento de diferentes partes da infraestrutura.
3. **Escalabilidade**: Permite gerenciar infraestruturas complexas de maneira mais organizada.
4. **Reutilização**: Componentes definidos em nested stacks podem ser reutilizados em diferentes partes da aplicação.

### Exemplo de Uso de Nested Stacks

Um exemplo onde uma stack principal define duas nested stacks: uma para recursos de rede e outra para uma aplicação.

#### Estrutura de Diretórios

```
my-nested-stack-app/
├── app.py
├── cdk.json
├── requirements.txt
├── network/
│   ├── __init__.py
│   └── network_stack.py
├── application/
│   ├── __init__.py
│   └── application_stack.py
├── parent/
│   ├── __init__.py
│   └── parent_stack.py
└── .gitignore
```

#### Arquivo `app.py`

Este arquivo é o ponto de entrada da aplicação CDK, onde a stack principal é instanciada.

```python
from aws_cdk import core
from parent.parent_stack import ParentStack

app = core.App()
ParentStack(app, "ParentStack")
app.synth()
```

#### Arquivo `network/network_stack.py`

Define a stack de rede que cria uma VPC.

```python
from aws_cdk import core
from aws_cdk import aws_ec2 as ec2

class NetworkStack(core.NestedStack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Definição de uma VPC
        self.vpc = ec2.Vpc(self, "MyVpc",
            max_azs=3  # Número de zonas de disponibilidade
        )
```

#### Arquivo `application/application_stack.py`

Define a stack de aplicação que usa a VPC criada na stack de rede.

```python
from aws_cdk import core
from aws_cdk import aws_lambda as _lambda

class ApplicationStack(core.NestedStack):

    def __init__(self, scope: core.Construct, id: str, vpc, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Exemplo de função Lambda dentro da VPC
        lambda_function = _lambda.Function(self, "MyFunction",
            runtime=_lambda.Runtime.PYTHON_3_8,
            handler="index.handler",
            code=_lambda.Code.from_asset("lambda"),
            vpc=vpc  # Referência à VPC criada na NetworkStack
        )
```

#### Arquivo `parent/parent_stack.py`

Define a stack principal que contém as nested stacks de rede e aplicação.

```python
from aws_cdk import core
from network.network_stack import NetworkStack
from application.application_stack import ApplicationStack

class ParentStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Instanciando a stack de rede
        network_stack = NetworkStack(self, "NetworkStack")

        # Instanciando a stack da aplicação, que depende da stack de rede
        application_stack = ApplicationStack(self, "ApplicationStack", vpc=network_stack.vpc)
```

### Como Funciona

1. **Stack Principal**: A `ParentStack` é a stack principal que contém as nested stacks.
2. **Nested Stacks**: `NetworkStack` e `ApplicationStack` são definidas como nested stacks dentro da `ParentStack`.
3. **Referências Entre Stacks**: A `ApplicationStack` recebe a VPC criada na `NetworkStack` como parâmetro, permitindo que os recursos definidos na `ApplicationStack` utilizem a VPC.

### Benefícios

- **Organização**: Nested stacks ajudam a organizar a infraestrutura em componentes menores e mais gerenciáveis.
- **Reutilização**: Componentes definidos em nested stacks podem ser reutilizados em diferentes partes do projeto ou em diferentes projetos.
- **Isolamento**: Recursos em nested stacks são isolados, facilitando a depuração e a manutenção.

### Implantação

Para implantar a stack principal que contém as nested stacks, use o comando `cdk deploy`:

```sh
cdk deploy
```

### Resumo

- **Nested Stacks**: Permitem criar hierarquias de stacks, facilitando a modularização e organização da infraestrutura.
- **Vantagens**: Modularidade, manutenção simplificada, escalabilidade e reutilização de componentes.
- **Exemplo Prático**: Criação de uma stack principal contendo nested stacks para recursos de rede e aplicação.
- **Implantação**: Uso do comando `cdk deploy` para implantar a stack principal e suas nested stacks.

As nested stacks no AWS CDK são uma ferramenta poderosa para gerenciar infraestruturas complexas, promovendo uma abordagem modular e organizada para definir e implantar recursos.