from aws_cdk import (
    RemovalPolicy,
    CfnOutput,
    Duration,
    Stack,
    aws_dynamodb as dynamodb,
    aws_lambda as lambda_,
    aws_cloudwatch as cloudwatch
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
        # Concedendo permissões para função Lambda para ler dados das tabelas do DynamoDB
        products_table.grant_read_data(product_list_function.role)

        # Adicionando uma URL Lambda pa a Função Lambda para executa via internet
        product_list_url = product_list_function.add_function_url(
            auth_type = lambda_.FunctionUrlAuthType.NONE
            )
        
        # Adicionando um output stack para acessar facilmente a função URL
        CfnOutput(self, "ProductUrl",
                  value = product_list_url.url)
        
        # Configuração de alarme para métricas de erros para Lambda Function
        errors_metric = product_list_function.metric_errors(
            label = "ProductListFunction Error",
            period = Duration.minutes(5),
            statistic = cloudwatch.Stats.SUM
        )

        errors_metric.create_alarm(self, "ProductListErrorAlarm",
                                   evaluation_periods = 1,
                                   threshold = 1,
                                   comparison_operator = cloudwatch.ComparisonOperator.GREATER_THAN_OR_EQUAL_TO_THRESHOLD,
                                   treat_missing_data = cloudwatch.TreatMissingData.IGNORE)