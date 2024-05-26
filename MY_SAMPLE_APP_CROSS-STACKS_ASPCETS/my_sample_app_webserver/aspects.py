import jsii
from aws_cdk import (
    IAspect,
)

@jsii.implements(IAspect)
class MyFirstAspect:

    def visit(self, construct_visited):

        print(f"{construct_visited.node.path} - {construct_visited.__class__.__name__}")