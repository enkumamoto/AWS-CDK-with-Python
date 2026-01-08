#!/usr/bin/env python3
import os
import aws_cdk as cdk
from networking_stack import MyVpcCdkStack  # Ajuste o caminho conforme a estrutura do seu projeto
from my_ecs_cdk_stack import MyEcsCdkStack  # Certifique-se de que este caminho está correto
from database_stack import DatabaseStack    # Nova importação adicionada

app = cdk.App()

aws_region = os.environ.get("AWS_REGION", os.environ.get("AWS_DEFAULT_REGION", "us-east-1"))
environment_name = app.node.try_get_context("environment") or "sandbox"
tags_to_append_from_context = app.node.try_get_context("tags_to_append") or {}
vpc_id_from_context = app.node.try_get_context("vpc_id") 
db_host_from_context = app.node.try_get_context("db_host") # Passar o db_host se for usado por outras partes da stack

if not vpc_id_from_context:
    raise Exception("VPC ID must be provided via context, e.g., -c vpc_id=vpc-12345")

if not db_host_from_context:
    print("Warning: db_host not provided. If this is used for other resources, they might fail.")
    # Ou levante uma exceção se for um requisito estrito:
    # raise Exception("DB Host must be provided via context, e.g., -c db_host=your-db-endpoint")


MyEcsCdkStack(
    scope=app,
    construct_id="MyEcsStack",
    environment=environment_name,
    vpc_id=vpc_id_from_context,
    db_host=db_host_from_context,
    tags_to_append=tags_to_append_from_context,
    env=cdk.Environment(region=aws_region),
)

MyVpcCdkStack(
    scope=app,
    construct_id="MyVpcStack",
    environment=environment_name,
    tags_to_append=tags_to_append_from_context,
    env=cdk.Environment(region=aws_region),
)

DatabaseStack(
    scope=app,
    construct_id="DatabaseStack",
    environment=environment_name,
    vpc_id=vpc_id_from_context,
    private_app_subnet_ids=app.node.try_get_context("private_app_subnet_ids") or [],
    initial_db_name=app.node.try_get_context("initial_db_name"),
    master_username=app.node.try_get_context("master_username"),
    master_password=app.node.try_get_context("master_password"),
    tags_to_append=tags_to_append_from_context,
    env=cdk.Environment(region=aws_region),
)

app.synth()