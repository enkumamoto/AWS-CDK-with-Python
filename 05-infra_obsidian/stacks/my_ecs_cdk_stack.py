from aws_cdk import (
    Stack,
    aws_ecs as ecs,
    aws_ec2 as ec2,
    CfnOutput,
    Tags,
)
from constructs import Construct

class MyEcsCdkStack(Stack):
    def __init__(self, scope: Construct, construct_id: str,
                 environment: str,
                 vpc_id: str,
                 tags_to_append: dict = None,
                 **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Variáveis e Locals
        base_tags = tags_to_append if tags_to_append is not None else {}
        base_tags["Environment"] = environment
        
        # Aplicar tags padrão
        for k, v in base_tags.items():
            Tags.of(self).add(k, v)

        # Referência à VPC existente (usada pelo Security Group)
        # Assumimos que a VPC já foi criada e seu ID é passado como variável
        vpc = ec2.Vpc.from_lookup(self, "VpcLookup", vpc_id=vpc_id)

        # ECS Cluster
        ecs_cluster = ecs.Cluster(
            self, "EcsCluster",
            cluster_name=f"obsidian-{environment}-Cluster",
            vpc=vpc, # O cluster ECS precisa de uma VPC, mesmo que o Terraform não a especifique diretamente.
                     # No Terraform, a dependência implícita é na VPC dos subnets onde as tasks rodam.
            container_insights=True # Habilita o Container Insights
        )
        # No CDK, 'depends_on' é geralmente inferido.
        # A dependência de 'db_host' é uma dependência lógica para o Terraform,
        # mas não afeta a criação do cluster ECS em si no CloudFormation.
        # Portanto, não há um equivalente direto no CDK para esta dependência para o cluster.
        Tags.of(ecs_cluster).add("Name", f"obsidian-{environment}-Cluster")


        # ECS Cluster Capacity Providers
        # O CDK permite configurar provedores de capacidade diretamente no Cluster.
        # Se você está usando Fargate, o cluster já gerencia a capacidade Fargate por padrão.
        # Para adicionar um CapacityProviderStrategy padrão:
        ecs_cluster.add_capacity("FargateSpotCapacity",
            capacity_provider_name="FARGATE_SPOT", # Nome do provedor de capacidade (FARGATE_SPOT já existe na AWS)
            default_capacity_provider_strategy=[
                ecs.CfnCluster.CapacityProviderStrategyProperty(
                    capacity_provider="FARGATE_SPOT",
                    base=1,
                    weight=100
                )
            ]
        )


        # Security Group para TLS
        allow_tls_sg = ec2.SecurityGroup(
            self, "AllowTlsSg",
            vpc=vpc,
            security_group_name=f"allow_tls_{environment}",
            description="Allow TLS inbound traffic",
            allow_all_outbound=True # Permite todo o tráfego de saída
        )

        allow_tls_sg.add_ingress_rule(
            peer=ec2.Peer.any_ipv4(),
            connection=ec2.Port.tcp(443),
            description="Allow HTTPS inbound from anywhere (IPv4)"
        )
        allow_tls_sg.add_ingress_rule(
            peer=ec2.Peer.any_ipv6(),
            connection=ec2.Port.tcp(443),
            description="Allow HTTPS inbound from anywhere (IPv6)"
        )
        Tags.of(allow_tls_sg).add("Name", f"allow_tls_{environment}")

        # Output: ecs_cluster_id
        CfnOutput(self, "EcsClusterIdOutput", value=ecs_cluster.cluster_arn, export_name=f"EcsClusterId-{environment}")