#!/usr/bin/env python3
import os

import aws_cdk as cdk

from my_sample_app_webserver.my_sample_app_webserver_stack import MySampleAppWebserverStack
from my_sample_app_webserver.network_stack import NetworkStack

from my_sample_app_webserver.aspects import MyFirstAspect
from my_sample_app_webserver.second_aspects import EC2InstanceTypeChecker

app = cdk.App()

root_stack = cdk.Stack(app, "RootStack")

network_stack = NetworkStack(root_stack, 'NetworkStack')

# Para Adicionar tags para a stack da aplicação, crie uma variável
application_stack = MySampleAppWebserverStack(root_stack, "MySampleAppWebserverStack",
                                              my_vpc = network_stack.vpc)

# Anexando aspects ao stack
cdk.Aspects.of(root_stack).add(MyFirstAspect())

# Anexando validação de aspects ao stack da aplicação
cdk.Aspects.of(application_stack).add(EC2InstanceTypeChecker())

# Adicionando tags para a stacks 
cdk.Tags.of(network_stack).add("category", "networking")

# Adicionando prioridade as tags
cdk.Tags.of(application_stack).add("category", "application",
                                    priority = 200)

app.synth()
