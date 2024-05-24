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