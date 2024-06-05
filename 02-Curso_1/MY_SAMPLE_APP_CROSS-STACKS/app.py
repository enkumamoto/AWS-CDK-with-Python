#!/usr/bin/env python3
import os

import aws_cdk as cdk

from my_sample_app_webserver.my_sample_app_webserver_stack import MySampleAppWebserverStack
from my_sample_app_webserver.network_stack import NetworkStack


app = cdk.App()

network_stack = NetworkStack(app, 'NetworkStack')

MySampleAppWebserverStack(app, "MySampleAppWebserverStack",
                          my_vpc=network_stack.vpc)

app.synth()
