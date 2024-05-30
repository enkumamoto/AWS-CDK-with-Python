from aws_cdk import (
    aws_ec2 as ec2,
    Stack,
    aws_sns as sns,
    aws_lambda as lambda_,
    aws_apigateway as apigw,
    aws_cloudwatch as cloudwatch,
    aws_cloudfront as cloudfront,
    aws_dynamodb as dynamodb,
    aws_s3 as s3,
    aws_s3_assets as s3_assets,
    aws_route53 as route53,
    # aws_sqs as sqs,
)
from constructs import Construct

class PyStarterStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)