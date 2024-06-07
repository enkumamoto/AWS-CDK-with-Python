#!/usr/bin/env python3
import os

import aws_cdk as cdk

from infratest.network_stack import NetworkStack
from infratest.infratest_stack import InfratestStack

app = cdk.App()

network_stack = NetworkStack(app, 'NetworkStack')

InfratestStack(app, "InfratestStack", 
               project_vpc = network_stack.vpc)

app.synth()