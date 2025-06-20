#!/usr/bin/env python3
import aws_cdk as cdk
from stacks.networking_stack import NetworkingStack
from stacks.services_stack import ServicesStack

app = cdk.App()

network_stack = NetworkingStack(app, "NetworkingStack",
    env=cdk.Environment(account="123456789012", region="us-east-1")
)

# Importar VPC da stack anterior (via .vpc export, se necessário em projeto real)
services_stack = ServicesStack(app, "ServicesStack",
    vpc=network_stack.node.try_find_child("MainVPC"),
    env=cdk.Environment(account="123456789012", region="us-east-1")
)

app.synth()
