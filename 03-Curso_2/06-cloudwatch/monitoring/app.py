#!/usr/bin/env python3
import os

import aws_cdk as cdk

from monitoring.monitoring_stack import MonitoringStack


app = cdk.App()
MonitoringStack(app, "MonitoringStack")

app.synth()
