from aws_cdk import (
    aws_ec2 as ec2,
    Stack,
    aws_s3 as s3,
    Duration,
    CfnOutput,
)

from constructs import Construct

class ConstructionsIdsStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        bucket = s3.Bucket(self, "TestBucket",
            bucket_name = "eijibucket",
            lifecycle_rules = [
            s3.LifecycleRule(
                expiration = Duration.days(3)
            )
            ]
        )
        CfnOutput(self, "BucketName", 
                  value = bucket.bucket_name)