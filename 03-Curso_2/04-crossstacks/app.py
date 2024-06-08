#!/usr/bin/env python3
import os

import aws_cdk as cdk

from crossstacks.crossstacks_stack import CrossstacksStack
from crossstacks.lambda_stack import PyHandlerStack

app = cdk.App()

starter_stack = CrossstacksStack(app, "CrossstacksStack")
PyHandlerStack(app, "PyHandlerStack", bucket = starter_stack.cool_bucket)

app.synth()
