from aws_cdk import (
    Stack,
    CfnOutput,
    aws_ec2 as ec2,
)
from constructs import Construct


class InfratestStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, project_vpc: ec2.CfnVPC, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        
        web_server = ec2.Instance(self, 'WebServer',
                                  machine_image = ec2.MachineImage.latest_amazon_linux2(),
                                  instance_type = ec2.InstanceType.of(instance_class = ec2.InstanceClass.T2,
                                                                    instance_size = ec2.InstanceSize.MICRO),
                                  vpc = project_vpc,
                                  vpc_subnets=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PUBLIC),
                                  user_data_causes_replacement=True)

        # Anexar um Elastic IP para manter o nomes DNS atualizados
        ec2.CfnEIP(self, "ElasticIP",
                   instance_id = web_server.instance_id)
        
        # Instalação dos pacote durante lançamento
        web_server.add_user_data("yum update -y",
                                 "amazon-linux-extras install nginx1",
                                 "rm -rf /usr/share/nginx/html/*")
        
        CfnOutput(self, "WebServerDNS",
                  value = web_server.instance_public_dns_name)


        # Permissão para conectar ao WebServer
        web_server.connections.allow_from_any_ipv4(ec2.Port.tcp(80), "Allow HTTP access from the Internet")
        web_server.connections.allow_from_any_ipv4(ec2.Port.tcp(22), "Allow SSH access from the Internet")

        # # Deploy de web page no webserver
        # web_page_asset = s3_assets.Asset(self, "WebPageAsset",
        #                                  path = "web_pages/index.html")
        
        # web_server.user_data.add_s3_download_command(bucket = web_page_asset.bucket,
        #                                              bucket_key = web_page_asset.s3_object_key,
        #                                              local_file = '/usr/share/nginx/html/index.html')
        
        # web_page_asset.grant_read(web_server.role)


        # web_server.add_user_data('service start nginx')