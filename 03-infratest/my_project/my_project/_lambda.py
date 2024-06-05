from aws_cdk import (
    aws_lambda as _lambda,
    aws_ecr as ecr,
    aws_iam as iam,
    Stack
)
from constructs import Construct

class LambdaStack(Stack):

    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        repository = ecr.Repository.from_repository_name(self, "MyRepo", "my-lambda-repo")

        role = iam.Role(self, "LambdaExecutionRole",
            assumed_by=iam.ServicePrincipal("lambda.amazonaws.com"),
            managed_policies=[
                iam.ManagedPolicy.from_aws_managed_policy_name("service-role/AWSLambdaBasicExecutionRole")
            ]
        )

        self.lambda_function = _lambda.DockerImageFunction(self, "MyFunction",
            code=_lambda.DockerImageCode.from_ecr(repository),
            role=role,
            environment={
                'KEY': 'VALUE'
            }
        )
