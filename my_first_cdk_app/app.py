#!/usr/bin/env python3

import aws_cdk as cdk

from my_first_cdk_app.my_first_cdk_app_stack import MyFirstCdkAppStack


app = cdk.App()
MyFirstCdkAppStack(app, "my-first-cdk-app")

app.synth()
