#!/usr/bin/env python3

import aws_cdk as cdk

from my_sample_app_network_connections.my_sample_app_network_connections_stack import MySampleAppNetworkConnectionsStack


app = cdk.App()
MySampleAppNetworkConnectionsStack(app, "MySampleAppNetworkConnectionsStack")

app.synth()
