from aws_cdk import (
    aws_s3 as s3,
    Stack
)
from constructs import Construct

class S3Stack(Stack):

    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        self.bucket = s3.Bucket(self, "MyBucket")
