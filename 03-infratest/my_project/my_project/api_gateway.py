from aws_cdk import (
    aws_apigateway as apigateway,
    Stack
)
from constructs import Construct

class ApiGatewayStack(Stack):

    def __init__(self, scope: Construct, id: str, lambda_function, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        api = apigateway.LambdaRestApi(self, "MyApi",
            handler=lambda_function
        )
