from aws_cdk import (
    Stack,
    aws_ec2 as ec2,
    Tags
)
from constructs import Construct

class NetworkingStack(Stack):

    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Exemplo de criação de VPC com subnets públicas e privadas
        vpc = ec2.Vpc(self, "MainVPC",
            max_azs=2,
            subnet_configuration=[
                ec2.SubnetConfiguration(name="Public", subnet_type=ec2.SubnetType.PUBLIC, cidr_mask=24),
                ec2.SubnetConfiguration(name="Private", subnet_type=ec2.SubnetType.PRIVATE_WITH_EGRESS, cidr_mask=24)
            ]
        )

        Tags.of(vpc).add("Name", "MainVPC")
