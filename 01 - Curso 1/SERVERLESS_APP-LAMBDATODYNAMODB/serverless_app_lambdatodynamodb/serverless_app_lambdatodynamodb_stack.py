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
from aws_solutions_constructs.aws_lambda_dynamodb import LambdaToDynamoDB

class ServerlessAppLambdatodynamodbStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        products_backend = LambdaToDynamoDB(self, 'ProductBackend',
                                            lambda_function_props = lambda_.FunctionProps(
                                                code = lambda_.Code.from_asset('lambda_src'),
                                                handler = 'product_list_function.lambda_handler',
                                                runtime = lambda_.Runtime.PYTHON_3_10,
                                            ),
                                            table_environment_variable_name='TABLE_NAME',
                                            table_permissions='Read') # Garante permissões ao DynamoDB

        products_table = products_backend.dynamo_table

        product_list_function = products_backend.lambda_function

        # Deleta a tabela na pilha de exclusão
        products_table.apply_removal_policy(RemovalPolicy.DESTROY)

        # Adicionando uma URL Lambda pa a Função Lambda para executa via internet
        product_list_url = product_list_function.add_function_url(
            auth_type = lambda_.FunctionUrlAuthType.NONE)
        
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