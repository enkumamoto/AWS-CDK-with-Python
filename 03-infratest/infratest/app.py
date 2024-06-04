#!/usr/bin/env python3
import os

import aws_cdk as cdk

from infratest.infratest_stack import InfratestStack

app = cdk.App()

InfratestStack(app, "InfratestStack")

app.synth()
