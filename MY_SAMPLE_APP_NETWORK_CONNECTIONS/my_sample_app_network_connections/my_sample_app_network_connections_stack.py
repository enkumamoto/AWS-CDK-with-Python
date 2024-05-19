from aws_cdk import (
    Stack,
    aws_ec2 as ec2,
)
from constructs import Construct


class MySampleAppNetworkConnectionsStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Cria uma VPC mas deixando como Restrito
        my_vpc = ec2.Vpc(self, "MyVPC",
                        nat_gateways = 0)

        web_service = ec2.Instance(self, "WebServer",
                                   machine_image = ec2.MachineImage.latest_amazon_linux2(),
                                   instance_type = ec2.InstanceType.of(instance_class = ec2.InstanceClass.T2,
                                                                       instance_size = ec2.InstanceSize.NANO),
                                   vpc = my_vpc,
                                   vpc_subnets = ec2.SubnetSelection(subnet_type = ec2.SubnetType.PUBLIC),)