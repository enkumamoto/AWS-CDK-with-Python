from aws_cdk import (
    aws_ec2 as ec2,
    Stack,
    aws_s3 as s3,
    Duration,
)

from constructs import Construct

class PyStarterStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        s3.Bucket(self, "TestBucket",
                  lifecycle_rules = [
                    s3.LifecycleRule(
                        expiration = Duration.days(3)
                    )
                  ])