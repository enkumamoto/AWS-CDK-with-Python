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

            if node.instance_type not in ['t2.nano', 't3.nano']:

                Annotations.of(node).add_warning(f"{node.instance_type} A instância declarada não é válida. A instância deve ser t2.nano ou t3.nano.")

                node.instance_type = 't2.nano'