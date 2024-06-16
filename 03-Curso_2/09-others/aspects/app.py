#!/usr/bin/env python3
import os

import aws_cdk as cdk

from aspects.aspects_stack import AspectsStack
from aspects.policychecker import PolicyChecker


app = cdk.App()
others_stack = AspectsStack(app, "AspectsStack")

cdk.Aspects.of(app).add(PolicyChecker())

app.synth()