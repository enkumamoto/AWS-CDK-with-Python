# Importa a classe Stack do pacote aws_cdk para criar uma pilha CDK
from aws_cdk import (
    Stack, 
    aws_apigateway as apigw, 
    aws_lambda as _lambda, 
    aws_dynamodb as dynamodb
)

# Importa a classe Construct para ser usada como tipo genérico em parâmetros
from constructs import Construct

# Define a classe MyRestapiStack que herda de Stack, permitindo a criação de recursos AWS
class MyRestapiStack(Stack):

    # Método construtor da classe, inicializa a pilha com escopo e identificador
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Cria uma nova tabela no DynamoDB chamada "EmplTable"
        # Esta tabela usa uma chave de partição de tipo STRING chamada "id"
        # O custo da tabela é cobrado sob demanda
        empl_table = dynamodb.TableV2(
            self,
            "EmplTable",
            partition_key=dynamodb.Attribute(
                name="id",
                type=dynamodb.AttributeType.STRING
            ),
            billing=dynamodb.Billing.on_demand(),
        )

        # Cria uma função AWS Lambda chamada "EmplLambda"
        # A função usa a versão Python 3.11 e carrega seu código a partir de um diretório local chamado "services"
        # O ponto de entrada da função é definido como "index.handler"
        # Uma variável de ambiente "TABLE_NAME" é passada para a função, contendo o nome da tabela do DynamoDB
        empl_lambda = _lambda.Function(
            self,
            "EmplLambda",
            runtime=_lambda.Runtime.PYTHON_3_11,
            code=_lambda.Code.from_asset("services"),
            handler="index.handler",
            environment={
                "TABLE_NAME": empl_table.table_name
            },
        )

        # Concede aos usuários da função Lambda permissões para ler e escrever nos dados da tabela do DynamoDB
        empl_table.grant_read_write_data(empl_lambda) 

        # Cria uma API REST chamada "Empl-Api"
        api = apigw.RestApi(self, "Empl-Api")

        # Define as opções de CORS para a API, permitindo solicitações de qualquer origem e todos os métodos HTTP
        cors_options = apigw.CorsOptions(
            allow_origins = apigw.Cors.ALL_ORIGINS,
            allow_methods = apigw.Cors.ALL_METHODS,
        )

        # Adiciona um recurso "/empl" à raiz da API, aplicando as opções CORS definidas anteriormente
        empl_resource = api.root.add_resource(
            "empl",
            default_cors_preflight_options = cors_options
        )

        # Configura a integração da função Lambda com o recurso "/empl"
        empl_lambda_integration = apigw.LambdaIntegration(empl_lambda)

        # Mapeia os métodos GET e POST do recurso "/empl" para a função Lambda configurada
        empl_resource.add_method("GET", empl_lambda_integration)
        empl_resource.add_method("POST", empl_lambda_integration)