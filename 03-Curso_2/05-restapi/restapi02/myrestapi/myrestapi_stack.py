from aws_cdk import (
    Stack,  # Importação da classe Stack do pacote aws_cdk
    aws_apigateway as apigw,  # Alias para o módulo aws_apigateway
    aws_lambda as _lambda,  # Alias para o módulo aws_lambda
    aws_dynamodb as dynamodb  # Alias para o módulo aws_dynamodb
)

from constructs import Construct

class MyRestapiStack(Stack):  # Classe personalizada que estende a classe Stack do AWS CDK

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)  # Chamada ao construtor da classe pai

        # Criação de uma tabela no DynamoDB
        empl_table = dynamodb.TableV2(
            self,
            "EmplTable",  # ID da tabela
            partition_key=dynamodb.Attribute(  # Definição da chave primária
                name="id",
                type=dynamodb.AttributeType.STRING
            ),
            billing=dynamodb.Billing.on_demand(),  # Configuração de cobrança
        )

        # Criação de um Lambda Function
        empl_lambda = _lambda.Function(
            self,
            "EmplLambda",  # ID da função Lambda
            runtime=_lambda.Runtime.PYTHON_3_11,  # Runtime especificado
            code=_lambda.Code.from_asset("services"),  # Caminho para o código da função
            handler="index.handler",  # Função de entrada
            environment={  # Variáveis de ambiente
                "TABLE_NAME": empl_table.table_name
            },
        )

        # Concessão de permissões para a função Lambda acessar a tabela DynamoDB
        empl_table.grant_read_write_data(empl_lambda) 

        # Criação da API Gateway
        api = apigw.RestApi(self, "Empl-Api")

        # Adição de um recurso à raiz da API
        empl_resource = api.root.add_resource("empl")

        # Integração da função Lambda com o método GET e POST do recurso
        empl_lambda_integration = apigw.LambdaIntegration(empl_lambda)

        # Associação dos métodos GET e POST do recurso à integração Lambda
        empl_resource.add_method("GET", empl_lambda_integration)
        empl_resource.add_method("POST", empl_lambda_integration)