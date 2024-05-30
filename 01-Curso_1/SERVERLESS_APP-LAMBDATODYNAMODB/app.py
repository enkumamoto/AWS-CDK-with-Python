#!/usr/bin/env python3
import os

import aws_cdk as cdk
from serverless_app_lambdatodynamodb.serverless_app_lambdatodynamodb_stack import ServerlessAppLambdatodynamodbStack


app = cdk.App()
ServerlessAppLambdatodynamodbStack(app, "ServerlessAppLambdatodynamodbStack",)

app.synth()
