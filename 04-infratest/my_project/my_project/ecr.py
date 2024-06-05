from aws_cdk import (
    aws_ecr as ecr,
    Stack
)
from constructs import Construct

class ECRStack(Stack):

    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        self.repository = ecr.Repository(self, "MyRepository")
