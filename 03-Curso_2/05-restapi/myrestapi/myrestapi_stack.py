# Importa módulos específicos do pacote aws_cdk
from aws_cdk import (
    Stack,           # Classe base para todas as stacks no AWS Cloud Development Kit (CDK)
    aws_apigateway as apigw,
    aws_lambda as _lambda,
    aws_s3 as s3,
)

# Importa a classe Construct do pacote constructs
from constructs import Construct

# Define a classe CrossstacksStack que herda de Stack
class MyRestapiStack(Stack):

    # Método construtor da classe CrossstacksStack
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        # Chama o método construtor da classe base Stack
        super().__init__(scope, construct_id, **kwargs)

        empl_lambda = _lambda.Function (
            self,
            "EmplLambda",
            runtime = _lambda.Runtime.PYTHON_3_10,
            code = _lambda.Code.from_asset("services"),
            handler = "index.handler"
        )

        api = apigw.RestApi(self, "Empl-Api")
        empl_resource = api.root.add_resource("empl")

        empl_lambda_integration = apigw.LambdaIntegration(empl_lambda)
        empl_resource.add_method("GET", empl_lambda_integration)
        empl_resource.add_method("POST", empl_lambda_integration)