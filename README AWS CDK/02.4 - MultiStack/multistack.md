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