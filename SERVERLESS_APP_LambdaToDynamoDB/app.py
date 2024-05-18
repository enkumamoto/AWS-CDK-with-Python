#!/usr/bin/env python3
import os

import aws_cdk as cdk

from serverless_app.serverless_app_stack import ServerlessAppStack


app = cdk.App()
ServerlessAppStack(app, "ServerlessAppStack",)

app.synth()
