#!/usr/bin/env python3
import os

import aws_cdk as cdk

from tags.tags_stack import TagsStack


app = cdk.App()
others_stack = TagsStack(app, "TagsStack")

cdk.Tags.of(others_stack).add('env', 'sandbox') # Esta linha coloca uma tags a todos os recursos

cdk.Tags.of(others_stack).add('storage', 'sandbox',
                              include_resource_types = ["AWS::S3::Bucket"],
                              priority = 150
                             ) # Esta linha coloca uma tags ao bucket




app.synth()
