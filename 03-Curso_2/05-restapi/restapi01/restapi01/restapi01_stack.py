from aws_cdk import (
    Stack,
    aws_apigateway as apigw,
    aws_lambda as _lambda
)

from constructs import Construct

class Restapi01Stack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        empl_lambda = _lambda.Function(
            self,
            "EmplLambda",
            runtime = _lambda.Runtime.PYTHON_3_10,
            handler = "index.handler",
            code = _lambda.Code.from_asset("services")
        )

        api = apigw.RestApi(self, "Empl-Api")
        empl_resource = api.root.add_resource("empl")

        empl_lambda_integration = apigw.LambdaIntegration(empl_lambda)
        empl_resource.add_method("GET", empl_lambda_integration)
        empl_resource.add_method("POST", empl_lambda_integration)