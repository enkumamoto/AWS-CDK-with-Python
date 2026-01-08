from aws_cdk import (
    Stack,
    aws_ec2 as ec2,
    CfnOutput,
    Tags,
)
from constructs import Construct

class NetworkingStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, environment: str, tags_to_append: dict = None, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Variáveis e Locals
        vpc_network = "10.0.0.0/16"
        
        base_tags = tags_to_append if tags_to_append is not None else {}
        base_tags["Environment"] = environment
        
        az_subnets = {
            f"{self.region}a": {"public": "10.0.0.0/20", "private_app": "10.0.16.0/20"},
            f"{self.region}b": {"public": "10.0.64.0/20", "private_app": "10.0.80.0/20"},
            f"{self.region}c": {"public": "10.0.128.0/20", "private_app": "10.0.144.0/20"},
        }

        for k, v in base_tags.items():
            Tags.of(self).add(k, v)

        # VPC
        vpc = ec2.Vpc(
            self, "MainVpc",
            cidr=vpc_network,
            enable_dns_support=True,
            enable_dns_hostnames=True,
            max_azs=3,
            # Configuração de sub-rede padrão (serão sobrescritas pela criação manual)
            subnet_configuration=[
                ec2.SubnetConfiguration(name="Public", subnet_type=ec2.SubnetType.PUBLIC, cidr_mask=20),
                ec2.SubnetConfiguration(name="PrivateApp", subnet_type=ec2.SubnetType.PRIVATE_WITH_EGRESS, cidr_mask=20)
            ]
        )
        Tags.of(vpc).add("Name", f"obsidian_vpc_{environment}")
        CfnOutput(self, "VpcIdOutput", value=vpc.vpc_id, export_name=f"VpcId-{environment}")

        # Sub-redes, EIPs e NAT Gateways
        public_subnets = []
        private_app_subnets = []
        nat_gateways = {}
        external_ips = {}

        for i, (az_id, subnets_data) in enumerate(az_subnets.items()):
            az_letter = chr(ord('a') + i)
            
            eip = ec2.CfnEIP(
                self, f"Eip{az_letter.upper()}",
                domain="vpc",
                tags=[{"key": "Name", "value": f"eip_{az_letter.upper()}_{environment}"}]
            )
            external_ips[f"az_{az_letter}"] = eip.ref

            public_subnet = ec2.CfnSubnet(
                self, f"SubnetAz{az_letter.upper()}Public",
                vpc_id=vpc.vpc_id,
                cidr_block=subnets_data["public"],
                availability_zone=az_id,
                map_public_ip_on_launch=True,
                tags=[{"key": "Name", "value": f"subnet_az{az_letter}_public_{environment}"}]
            )
            public_subnets.append(public_subnet.ref)

            nat_gateway = ec2.CfnNatGateway(
                self, f"NatGateway{az_letter.upper()}",
                allocation_id=eip.attr_allocation_id,
                subnet_id=public_subnet.ref,
                tags=[{"key": "Name", "value": f"nat_gw_{az_letter.upper()}_{environment}"}],
            )
            nat_gateways[az_id] = nat_gateway.ref

            private_app_subnet = ec2.CfnSubnet(
                self, f"SubnetAz{az_letter.upper()}PrivateApp",
                vpc_id=vpc.vpc_id,
                cidr_block=subnets_data["private_app"],
                availability_zone=az_id,
                map_public_ip_on_launch=False,
                tags=[{"key": "Name", "value": f"subnet_az{az_letter}_private_app_{environment}"}]
            )
            private_app_subnets.append(private_app_subnet.ref)
        
        CfnOutput(self, "ExternalIpOutput", value=external_ips, export_name=f"ExternalIp-{environment}")

        # Internet Gateway
        igw = ec2.CfnInternetGateway(
            self, "InternetGateway",
            tags=[{"key": "Name", "value": f"igw_{environment}"}]
        )
        ec2.CfnVPCGatewayAttachment(
            self, "IgwAttachment",
            vpc_id=vpc.vpc_id,
            internet_gateway_id=igw.ref
        )

        # Tabelas de Rota e Associações
        public_route_table = ec2.CfnRouteTable(
            self, "PublicRouteTable",
            vpc_id=vpc.vpc_id,
            tags=[{"key": "Name", "value": f"rt_public_{environment}"}]
        )
        
        ec2.CfnRoute(
            self, "PublicRouteToIgw",
            route_table_id=public_route_table.ref,
            destination_cidr_block="0.0.0.0/0",
            gateway_id=igw.ref
        )

        for i, subnet_id_ref in enumerate(public_subnets):
            az_letter = chr(ord('a') + i)
            ec2.CfnSubnetRouteTableAssociation(
                self, f"PublicRouteTableAssociationAz{az_letter.upper()}",
                subnet_id=subnet_id_ref,
                route_table_id=public_route_table.ref
            )

        private_route_table = ec2.CfnRouteTable(
            self, "PrivateRouteTable",
            vpc_id=vpc.vpc_id,
            tags=[{"key": "Name", "value": f"rt_private_{environment}"}]
        )

        for i, (az_id, nat_gw_ref) in enumerate(nat_gateways.items()):
            az_letter = chr(ord('a') + i)
            ec2.CfnRoute(
                self, f"PrivateRouteToNatGw{az_letter.upper()}",
                route_table_id=private_route_table.ref,
                destination_cidr_block="0.0.0.0/0",
                nat_gateway_id=nat_gw_ref
            )

        for i, subnet_id_ref in enumerate(private_app_subnets):
            az_letter = chr(ord('a') + i)
            ec2.CfnSubnetRouteTableAssociation(
                self, f"PrivateRouteTableAssociationAz{az_letter.upper()}",
                subnet_id=subnet_id_ref,
                route_table_id=private_route_table.ref
            )

        CfnOutput(self, "PublicRouteTableIdsOutput", value=[public_route_table.ref], export_name=f"PublicRouteTableIds-{environment}")
        CfnOutput(self, "IntraRouteTableIdsOutput", value=[private_route_table.ref], export_name=f"IntraRouteTableIds-{environment}")

        # Security Group
        security_group = ec2.SecurityGroup(
            self, "ObsidianSG",
            vpc=vpc,
            description="Security Group for Obsidian application",
            allow_all_outbound=True,
        )
        security_group.add_ingress_rule(
            peer=ec2.Peer.any_ipv4(),
            connection=ec2.Port.all_traffic(),
            description="Allow all inbound traffic"
        )
        Tags.of(security_group).add("Name", f"sg_{environment}")
        CfnOutput(self, "SecurityGroupIdOutput", value=security_group.security_group_id, export_name=f"SecurityGroupId-{environment}")

        # VPC Endpoint para ECR
        ecr_endpoint = ec2.InterfaceVpcEndpoint(
            self, "EcrEndpoint",
            vpc=vpc,
            service=ec2.InterfaceVpcEndpointAwsService.ECR_DOCKER,
            security_groups=[security_group],
            subnets=list(map(lambda ref: ec2.Subnet.from_subnet_id(self, f"ImportedPrivateSubnet-{ref}", ref), private_app_subnets))
        )

        # Outputs adicionais
        CfnOutput(self, "PublicSubnetIdsOutput", value=public_subnets, export_name=f"PublicSubnetIds-{environment}")
        CfnOutput(self, "PrivateAppSubnetIdsOutput", value=private_app_subnets, export_name=f"PrivateAppSubnetIds-{environment}")