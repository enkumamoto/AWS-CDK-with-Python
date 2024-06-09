#!/usr/bin/env python3
import os

import aws_cdk as cdk

from myrestapi.myrestapi_stack import MyRestapiStack
# from myrestapi.lambda_stack import PyHandlerStack

app = cdk.App()

starter_stack = MyRestapiStack(app, "MyRestapiStack")
# PyHandlerStack(app, "PyHandlerStack", bucket = starter_stack.cool_bucket)

app.synth()
