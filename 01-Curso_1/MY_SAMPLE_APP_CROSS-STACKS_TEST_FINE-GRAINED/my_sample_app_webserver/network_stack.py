from aws_cdk import (
    NestedStack,
    aws_ec2 as ec2,
)
from constructs import Construct

class NetworkStack(NestedStack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self.vpc = ec2.Vpc(self, 'MyVpc',
                         nat_gateways=0)
        