from aws_cdk import (
    # Importando as classes necessárias da AWS CDK para construir a infraestrutura
    Stack,
    aws_apigateway as apigw,
    aws_lambda as _lambda,
    aws_dynamodb as dynamodb
)

from constructs import Construct

class MyRestapiStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        # Chamando o construtor da classe base para inicializar este stack
        super().__init__(scope, construct_id, **kwargs)

        # Definindo uma tabela no DynamoDB para armazenar informações de empregados
        empl_table = dynamodb.TableV2(
            self,  # Referenciando o próprio stack
            "EmplTable",  # ID da tabela
            partition_key=dynamodb.Attribute(  # Definindo a chave de partição
                name="id",  # Nome da chave
                type=dynamodb.AttributeType.STRING  # Tipo da chave
            ),
            billing=dynamodb.Billing.on_demand(),  # Configuração de cobrança
        )

        # Criando uma função Lambda para processar requisições relacionadas a empregados
        empl_lambda = _lambda.Function(
            self,  # Referenciando o próprio stack
            "EmplLambda",  # ID da função Lambda
            runtime=_lambda.Runtime.PYTHON_3_10,  # Especificando a versão do Python
            code=_lambda.Code.from_asset("services"),  # Caminho para o código da função
            handler="index.handler",  # Função dentro do arquivo index.py que será chamada
            environment={  # Variáveis de ambiente passadas para a função Lambda
                "TABLE_NAME": empl_table.table_name  # Nome da tabela do DynamoDB
            },
        )

        # Concedendo permissões à função Lambda para acessar a tabela do DynamoDB
        empl_table.grant_read_write_data(empl_lambda)

        # Criando uma API Gateway REST
        api = apigw.RestApi(self, "Empl-Api")

        # Adicionando um recurso à raiz da API para representar empregados
        empl_resource = api.root.add_resource("empl")

        # Configurando a integração entre o recurso da API e a função Lambda
        empl_lambda_integration = apigw.LambdaIntegration(empl_lambda)

        # Associando métodos HTTP GET e POST ao recurso da API com a função Lambda
        empl_resource.add_method("GET", empl_lambda_integration)
        empl_resource.add_method("POST", empl_lambda_integration)