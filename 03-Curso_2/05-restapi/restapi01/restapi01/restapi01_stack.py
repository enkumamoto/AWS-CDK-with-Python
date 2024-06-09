from aws_cdk import (
    # Importando classes necessárias da AWS CDK
    Stack,
    aws_apigateway as apigw,
    aws_lambda as _lambda
)

from constructs import Construct

class Restapi01Stack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        # Chamada ao construtor da classe base Stack
        super().__init__(scope, construct_id, **kwargs)

        # Criando uma função Lambda chamada EmplLambda
        empl_lambda = _lambda.Function(
            self,  # Referência ao próprio stack como contexto
            "EmplLambda",  # ID da função Lambda
            runtime=_lambda.Runtime.PYTHON_3_10,  # Versão do Python usada na função
            handler="index.handler",  # Arquivo e função dentro desse arquivo que serão executados
            code=_lambda.Code.from_asset("services")  # Caminho para o código da função Lambda
        )

        # Criando uma API Gateway REST
        api = apigw.RestApi(self, "Empl-Api")

        # Adicionando um recurso à raiz da API
        empl_resource = api.root.add_resource("empl")

        # Configurando a integração entre o recurso da API e a função Lambda
        empl_lambda_integration = apigw.LambdaIntegration(empl_lambda)

        # Associando métodos HTTP GET e POST ao recurso da API com a função Lambda
        empl_resource.add_method("GET", empl_lambda_integration)
        empl_resource.add_method("POST", empl_lambda_integration)