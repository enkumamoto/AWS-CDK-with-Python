from aws_cdk import (
    aws_dynamodb as dynamodb,
    Stack
)
from constructs import Construct

class DynamoDBStack(Stack):

    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        self.table = dynamodb.Table(self, "MyTable",
            partition_key = {'name': 'id', 'type': dynamodb.AttributeType.STRING}
        )
