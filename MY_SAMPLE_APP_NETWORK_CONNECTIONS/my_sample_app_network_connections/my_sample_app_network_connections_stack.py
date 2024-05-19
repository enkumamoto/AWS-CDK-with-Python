from aws_cdk import (
    Stack,
    CfnOutput,
    RemovalPolicy,
    aws_ec2 as ec2,
    aws_rds as rds
)
from constructs import Construct


class MySampleAppNetworkConnectionsStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Cria uma VPC mas deixando como Restrito
        my_vpc = ec2.Vpc(self, "MyVPC",
                        nat_gateways = 0)

        # Cria uma Instância para web server nginx, sem regras de saída para insternet
        web_server = ec2.Instance(self, "WebServer",
                                   machine_image = ec2.MachineImage.latest_amazon_linux2(),
                                   instance_type = ec2.InstanceType.of(instance_class = ec2.InstanceClass.T2,
                                                                       instance_size = ec2.InstanceSize.NANO),
                                   vpc = my_vpc,
                                   vpc_subnets = ec2.SubnetSelection(subnet_type = ec2.SubnetType.PUBLIC),
                                   user_data_causes_replacement = True)

        # Anexar um Elastic IP para manter o nomes DNS atualizados
        ec2.CfnEIP(self, "ElasticIP",
                   instance_id = web_server.instance_id)
        
        # Instalação dos pacote durante lançamento
        web_server.add_user_data("yum update -y",
                                 "amazon-linux-extras install nginx1",
                                 "service nginx start")
        
        CfnOutput(self, "WebServerDNS",
                  value = web_server.instance_public_dns_name)


        # Permissão para conectar ao WebServer
        web_server.connections.allow_from_any_ipv4(ec2.Port.tcp(80), "Allow HTTP access from the Internet")
        web_server.connections.allow_from_any_ipv4(ec2.Port.tcp(22), "Allow SSH access from the Internet")

        # Configuração de Instância para DB
        db_instance = rds.DatabaseInstance(self, "DbInstance",
                                       engine = rds.DatabaseInstanceEngine.MARIADB,
                                       vpc = my_vpc,
                                       vpc_subnets = ec2.SubnetSelection(subnet_type = ec2.SubnetType.PRIVATE_ISOLATED),
                                       instance_type = ec2.InstanceType.of(instance_class = ec2.InstanceClass.T3,
                                                                           instance_size = ec2.InstanceSize.MICRO),
                                       removal_policy = RemovalPolicy.DESTROY)
        # Permissão para conectar a instância de DB
        db_instance.connections.allow_default_port_from(web_server, "Allow MySQL access from the WebServer")
        web_server.connections.allow_to_default_port(db_instance)

        # Instalando o MySQL Client no servidor
        web_server.add_user_data('yum install -y mysql')

        CfnOutput(self, "DbEndpoint",
                  value = db_instance.db_instance_endpoint_address)