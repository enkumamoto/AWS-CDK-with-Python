from aws_cdk import (
    Stack,
    aws_s3 as s3,
    aws_lambda as _lambda
)
from constructs import Construct

class AspectsStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        cool_lambda = _lambda.Function(self, "SimpleLambda",
            runtime = _lambda.Runtime.PYTHON_3_11,
            handler = "index.handler",
            code = _lambda.Code.from_inline("print()")
        )

        bucket = s3.Bucket(self, "SimpleBucket",
        versioned = True
        )
        bucket.grant_read(cool_lambda)