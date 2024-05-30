from aws_cdk import (
    Stack,
    aws_ec2 as ec2,
)
from constructs import Construct

class MySampleAppStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Cria uma VPC mas deixando como Restrito
        # my_vpc = ec2.Vpc(self, "MyVPC",
        #                 nat_gateways = 0)

        # Cria uma VPC
        my_vpc = ec2.CfnVPC(self, "MyVpc",
                            cidr_block = '10.0.0.0/16',
                            enable_dns_support = True,
                            enable_dns_hostnames = True)

        internet_gateway = ec2.CfnInternetGateway(self, "MyVpcIGTW")

        ec2.CfnVPCGatewayAttachment(self, "IgwAttachment",
                                        vpc_id = my_vpc.attr_vpc_id,
                                        internet_gateway_id = internet_gateway.attr_internet_gateway_id)
        
        # Dicionário para subnets. Ele pode ser usado em outras partes do código
        my_subnets = [
            {'cidr_block' : '10.0.1.0/24', 'public' : True},
            {'cidr_block' : '10.0.2.0/24', 'public' : True},
            {'cidr_block' : '10.0.3.0/24', 'public' : False},
            {'cidr_block' : '10.0.4.0/24', 'public' : False},
        ]

        # Cria as subnets
        for i,subnet in enumerate(my_subnets):
            subnet_resource = ec2.CfnSubnet(self, f"Subnet{i + 1}",
                                            vpc_id = my_vpc.attr_vpc_id,
                                            cidr_block = subnet['cidr_block'],
                                            map_public_ip_on_launch = subnet['public'],
                                            availability_zone = Stack.availability_zones.fget(self)[i % 2])
            
            route_table = ec2.CfnRouteTable(self, f"Subnet{i + 1}RouteTable",
                                            vpc_id = my_vpc.attr_vpc_id)
            
            # Associando a Route Table as Subnets
            ec2.CfnSubnetRouteTableAssociation(self, f"Subnet{i + 1}RouteTableAssociation",
                                                route_table_id = route_table.attr_route_table_id,
                                                subnet_id = subnet_resource.attr_subnet_id)
            
            if subnet ["public"]:
                ec2.CfnRoute(self, f"Subnet{i + 1}InternetRoute",
                                route_table_id = route_table.attr_route_table_id,
                                destination_cidr_block = "0.0.0.0/0",
                                gateway_id = internet_gateway.attr_internet_gateway_id)