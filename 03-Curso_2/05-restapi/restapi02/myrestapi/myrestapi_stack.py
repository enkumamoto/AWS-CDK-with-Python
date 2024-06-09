from aws_cdk import (
    Stack,
    aws_apigateway as apigw,
    aws_lambda as _lambda,
    aws_dynamodb as dynamodb
)

from constructs import Construct

class MyRestapiStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        empl_table = dynamodb.TableV2(
            self,
            "EmplTable",
            partition_key = dynamodb.Attribute(
                name = "id",
                type = dynamodb.AttributeType.STRING
            ),
            billing = dynamodb.BillingMode.on_demand(),
        )

        empl_lambda = _lambda.Function (
            self,
            "EmplLambda",
            runtime = _lambda.Runtime.PYTHON_3_10,
            code = _lambda.Code.from_asset("services"),
            handler = "index.handler",
            environment = {
                "TABLE_NAME": empl_table.table_name
            }
        )

        api = apigw.RestApi(self, "Empl-Api")
        empl_resource = api.root.add_resource("empl")

        empl_lambda_integration = apigw.LambdaIntegration(empl_lambda)
        empl_resource.add_method("GET", empl_lambda_integration)
        empl_resource.add_method("POST", empl_lambda_integration)