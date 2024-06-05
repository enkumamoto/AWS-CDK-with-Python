from aws_cdk import (
    aws_cloudwatch as cloudwatch,
    Stack
)
from constructs import Construct

class CloudWatchStack(Stack):

    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        self.dashboard = cloudwatch.Dashboard(self, "MyDashboard")
