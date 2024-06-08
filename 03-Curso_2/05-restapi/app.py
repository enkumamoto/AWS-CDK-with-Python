#!/usr/bin/env python3
import os

import aws_cdk as cdk

from myrestapi.myrestapi_stack import MyRestapiStack


app = cdk.App()
MyRestapiStack(app, "MyRestapiStack")

app.synth()
