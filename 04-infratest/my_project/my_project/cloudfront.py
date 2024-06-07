from aws_cdk import (
    aws_cloudfront as cloudfront,
    aws_s3 as s3,
    Stack
)
from constructs import Construct

class CloudFrontStack(Stack):

    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        bucket = s3.Bucket(self, "MyBucket")

        distribution = cloudfront.CloudFrontWebDistribution(self, "MyDistribution",
            origin_configs = [cloudfront.SourceConfiguration(
                s3_origin_source = cloudfront.S3OriginConfig(
                    s3_bucket_source = bucket
                ),
                behaviors = [cloudfront.Behavior(is_default_behavior = True)]
            )]
        )
