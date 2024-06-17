#!/usr/bin/env python3
import os

import aws_cdk as cdk

from tags.tags_stack import TagsStack

# Inicializa o aplicativo AWS CDK
app = cdk.App()

# Cria uma instância da pilha TagsStack, passando o aplicativo e um identificador único
others_stack = TagsStack(app, "TagsStack")

# Adiciona uma tag 'env' com valor 'sandbox' a todos os recursos dentro da pilha
cdk.Tags.of(others_stack).add('env', 'sandbox')

# Adiciona uma tag 'storage' com valor 'sandbox' especificamente aos buckets S3 dentro da pilha
# Isso é feito usando o método add com parâmetros adicionais para filtrar os tipos de recursos
cdk.Tags.of(others_stack).add('storage', 'sandbox',
                              include_resource_types=["AWS::S3::Bucket"],  # Filtra apenas os buckets S3
                              priority=150  # Define a prioridade da tag
                             )

# Gera a sintaxe do AWS CDK para deployment
app.synth()