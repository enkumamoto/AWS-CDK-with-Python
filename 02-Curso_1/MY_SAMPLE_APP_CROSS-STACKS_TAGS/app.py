#!/usr/bin/env python3
import os

import aws_cdk as cdk

from my_sample_app_webserver.my_sample_app_webserver_stack import MySampleAppWebserverStack
from my_sample_app_webserver.network_stack import NetworkStack


app = cdk.App()

network_stack = NetworkStack(app, 'NetworkStack')

# Para Adicionar tags para a stack da aplicação, crie uma variável
application_stack = MySampleAppWebserverStack(app, "MySampleAppWebserverStack",
                          my_vpc=network_stack.vpc)

# Adicionando tags para a stacks 
cdk.Tags.of(network_stack).add("category", "networking")

# Adicionando prioridade as tags
cdk.Tags.of(application_stack).add("category", "application",
                                    priority = 200)

app.synth()
