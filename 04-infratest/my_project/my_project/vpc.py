from aws_cdk import (
    aws_ec2 as ec2,
    Stack
)
from constructs import Construct

class VPCStack(Stack):

    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        self.vpc = ec2.Vpc(self, "MyVpc",
            max_azs = 3,
            subnet_configuration = [
                ec2.SubnetConfiguration(
                    name = "PublicSubnet",
                    subnet_type = ec2.SubnetType.PUBLIC,
                    cidr_mask = 24
                ),
                ec2.SubnetConfiguration(
                    name = "PrivateSubnet",
                    subnet_type = ec2.SubnetType.PRIVATE,
                    cidr_mask = 24
                ),
                ec2.SubnetConfiguration(
                    name = "DatabaseSubnet",
                    subnet_type = ec2.SubnetType.PRIVATE_ISOLATED,
                    cidr_mask = 24
                )
            ]
        )
