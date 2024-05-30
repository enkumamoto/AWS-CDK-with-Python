#!/usr/bin/env python3
import os

import aws_cdk as cdk

from my_sample_app.my_sample_app_stack import MySampleAppStack


app = cdk.App()
MySampleAppStack(app, "MySampleAppStack")

app.synth()
