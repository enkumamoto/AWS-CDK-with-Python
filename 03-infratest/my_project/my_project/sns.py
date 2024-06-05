from aws_cdk import (
    aws_sns as sns,
    Stack
)
from constructs import Construct

class SNSStack(Stack):

    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        self.topic = sns.Topic(self, "MyTopic")
