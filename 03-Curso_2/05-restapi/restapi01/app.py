#!/usr/bin/env python3
import os

import aws_cdk as cdk

from restapi01.restapi01_stack import Restapi01Stack

app = cdk.App()

Restapi01Stack(app, "Restapi01Stack")

app.synth()