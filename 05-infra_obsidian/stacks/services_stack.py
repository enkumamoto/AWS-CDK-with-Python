from aws_cdk import (
    Stack,
    aws_lambda as _lambda,
    aws_iam as iam,
    aws_ecs as ecs,
    aws_elasticloadbalancingv2 as elbv2,
    aws_secretsmanager as secretsmanager,
    aws_logs as logs,
    aws_ec2 as ec2,
    Tags
)
from constructs import Construct

class ServicesStack(Stack):

    def __init__(self, scope: Construct, id: str, vpc: ec2.Vpc, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Exemplo de função Lambda
        lambda_fn = _lambda.Function(self, "ExampleLambda",
            runtime=_lambda.Runtime.PYTHON_3_9,
            handler="index.handler",
            code=_lambda.Code.from_inline("def handler(event, context): return 'Hello from Lambda'")
        )

        # Exemplo de role IAM
        role = iam.Role(self, "LambdaExecutionRole",
            assumed_by=iam.ServicePrincipal("lambda.amazonaws.com"),
            managed_policies=[
                iam.ManagedPolicy.from_aws_managed_policy_name("service-role/AWSLambdaBasicExecutionRole")
            ]
        )

        # Associar role à Lambda (opcionalmente)
        lambda_fn.role = role

        Tags.of(lambda_fn).add("Name", "ExampleLambdaFunction")
