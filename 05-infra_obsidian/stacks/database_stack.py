# ...existing code...
from aws_cdk import (
    Stack,
    aws_ec2 as ec2,
    aws_rds as rds,
    CfnOutput,
    Tags,
)
from constructs import Construct

class PostgresAuroraStack(Stack):
    def __init__(
        self, scope: Construct, construct_id: str,
        environment: str,
        vpc_id: str,
        private_app_subnet_ids: list,
        initial_db_name: str,
        master_username: str,
        master_password: str,
        tags_to_append: dict = None,
        **kwargs
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Tags
        base_tags = tags_to_append if tags_to_append else {}
        base_tags["Environment"] = environment

        # VPC
        vpc = ec2.Vpc.from_lookup(self, "VpcLookup", vpc_id=vpc_id)

        # Subnets
        subnets = [ec2.Subnet.from_subnet_id(self, f"Subnet{i}", subnet_id)
                   for i, subnet_id in enumerate(private_app_subnet_ids)]

        # Security Group
        allow_postgres_sg = ec2.SecurityGroup(
            self, "AllowPostgresSg",
            vpc=vpc,
            security_group_name=f"allow_postgres_{environment}",
            description="Allow Postgres inbound traffic",
            allow_all_outbound=True
        )
        # Ingress/Egress for all traffic from subnet CIDRs
        for subnet in subnets:
            allow_postgres_sg.add_ingress_rule(
                peer=ec2.Peer.ipv4(subnet.ipv4_cidr_block),
                connection=ec2.Port.all_traffic(),
                description="Allow Postgres"
            )
            allow_postgres_sg.add_egress_rule(
                peer=ec2.Peer.ipv4(subnet.ipv4_cidr_block),
                connection=ec2.Port.all_traffic()
            )
        Tags.of(allow_postgres_sg).add("Name", f"allow_postgres_{environment}")
        for k, v in base_tags.items():
            Tags.of(allow_postgres_sg).add(k, v)

        # DB Subnet Group
        db_subnet_group = rds.SubnetGroup(
            self, "DbSubnetGroup",
            description="DB subnet group for Aurora Postgres",
            vpc_subnets=ec2.SubnetSelection(subnets=subnets),
            subnet_group_name=f"default_db_subnet_group_postgres_{environment}"
        )
        Tags.of(db_subnet_group).add("Name", f"default_db_subnet_group_postgres_{environment}")
        for k, v in base_tags.items():
            Tags.of(db_subnet_group).add(k, v)

        # Aurora PostgreSQL Cluster
        cluster = rds.DatabaseCluster(
            self, "AuroraCluster",
            engine=rds.DatabaseClusterEngine.aurora_postgres(version=rds.AuroraPostgresEngineVersion.VER_15_4),
            credentials=rds.Credentials.from_password(
                username=master_username,
                password=cdk.SecretValue.unsafe_plain_text(master_password)
            ),
            default_database_name=initial_db_name,
            instances=1,
            instance_props=rds.InstanceProps(
                instance_type=ec2.InstanceType.of(
                    ec2.InstanceClass.SERVERLESS, ec2.InstanceSize.SMALL
                ),
                vpc=vpc,
                vpc_subnets=ec2.SubnetSelection(subnets=subnets),
                security_groups=[allow_postgres_sg],
                publicly_accessible=False,
                auto_minor_version_upgrade=True
            ),
            subnet_group=db_subnet_group,
            backup=rds.BackupProps(
                retention=cdk.Duration.days(7),
                preferred_window="07:00-09:00"
            ),
            cluster_identifier="obsidian-datapolling",
            storage_encrypted=True,
            removal_policy=cdk.RemovalPolicy.DESTROY
        )
        Tags.of(cluster).add("Name", f"postgres_db_{environment}")
        for k, v in base_tags.items():
            Tags.of(cluster).add(k, v)

        # Outputs
        CfnOutput(self, "DbHost", value=cluster.cluster_endpoint.hostname)
        CfnOutput(self, "DbName", value=initial_db_name)
        CfnOutput(self, "AvaliabilityZones", value=",".join([subnet.availability_zone for subnet in subnets]))
# ...existing code...