#!/usr/bin/env python3
import os

import aws_cdk as cdk

from my_sample_app_nested_stack.my_sample_app_nested_stack_stack import MySampleAppNestedStackStack
from my_sample_app_nested_stack.network_stack import NetworkStack


app = cdk.App()

root_stack = cdk.Stack(app, "RootStack")

network_stack = NetworkStack(root_stack, "NetworkStack")

MySampleAppNestedStackStack(root_stack, "MySampleAppNestedStackStack", 
                            my_vpc=network_stack.vpc)

app.synth()