from aws_cdk import (
    RemovalPolicy,
    Stack,
    aws_dynamodb as dynamodb,
    aws_lambda as lambda_
)
from constructs import Construct

class ServerlessAppStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        products_table = dynamodb.Table (self, "ProductsTable",
                                        partition_key = dynamodb.Attribute(
                                            name = "id",
                                            type = dynamodb.AttributeType.STRING
                                        ),
                                        billing_mode = dynamodb.BillingMode.PAY_PER_REQUEST,
                                        removal_policy = RemovalPolicy.DESTROY)

        product_list_function = lambda_.Function(self, "ProductListFunction",
                                                code = lambda_.Code.from_asset("lambda_src"),
                                                handler = "product_list_function.lambda_handler",
                                                runtime = lambda_.Runtime.PYTHON_3_10,
                                                environment = {
                                                    "TABLE_NAME": products_table.table_name
                                                })
        
        # Adicionando uma URL Lambda pa a Função Lambda para executa via internet
        product_list_url = product_list_function.add_function_url(
            auth_type=lambda_.FunctionUrlAuthType.NONE
            )