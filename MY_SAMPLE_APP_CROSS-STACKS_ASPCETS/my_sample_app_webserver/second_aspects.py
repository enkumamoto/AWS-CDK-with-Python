import jsii
from aws_cdk import (
    IAspect,
    Annotations,
    aws_ec2 as ec2
)

@jsii.implements(IAspect)
class EC2InstanceTypeChecker:

    def visit(self, node):

        if isinstance(node, ec2.CfnInstance):

            if node.instance_type not in ['t2.micro', 't3.micro']:

                Annotations.of(node).add_warning(f"{node.instance_type} instance type is NOT valid.")