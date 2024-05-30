#!/usr/bin/env python3

import aws_cdk as cdk

from mysampleappnested.mysampleappnested_stack import MysampleappnestedStack
from mysampleappnested.network_stack import NetworkStack


app = cdk.App()

root_stack = cdk.Stack(app, "RootStack")

network_stack = NetworkStack(root_stack, "NetworkStack")

MysampleappnestedStack(root_stack, "MysampleappnestedStack",
                       my_vpc=network_stack.vpc)

app.synth()