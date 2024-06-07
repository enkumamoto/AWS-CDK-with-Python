#!/usr/bin/env python3
import os

import aws_cdk as cdk

from my_project.my_project_stack import MyProjectStack
from my_project.vpc import VPCStack
from my_project._lambda import LambdaStack
from my_project.api_gateway import ApiGatewayStack
from my_project.dynamodb import DynamoDBStack
from my_project.cloudfront import CloudFrontStack
from my_project.sns import SNSStack
from my_project.cloudwatch import CloudWatchStack
from my_project.ecr import ECRStack
from my_project.s3 import S3Stack


app = cdk.App()
MyProjectStack(app, "MyProjectStack")

vpc_stack = VPCStack(app, "VPCStack")
lambda_stack = LambdaStack(app, "LambdaStack")
api_gateway_stack = ApiGatewayStack(app, "ApiGatewayStack", lambda_function = _lambda_stack.lambda_function)
dynamodb_stack = DynamoDBStack(app, "DynamoDBStack")
cloudfront_stack = CloudFrontStack(app, "CloudFrontStack")
sns_stack = SNSStack(app, "SNSStack")
cloudwatch_stack = CloudWatchStack(app, "CloudWatchStack")
ecr_stack = ECRStack(app, "ECRStack")
s3_stack = S3Stack(app, "S3Stack")

app.synth()
