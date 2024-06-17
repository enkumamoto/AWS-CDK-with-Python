#!/usr/bin/env python3
# Importação do módulo os para interagir com o sistema operacional
import os

# Importação do módulo aws_cdk, que permite criar infraestrutura na AWS usando o modelo de código CDK
import aws_cdk as cdk

# Importação de componentes específicos do projeto, como AspectsStack, PolicyChecker e S3tolambdaStack
from patterns.aspects_stack import AspectsStack
from patterns.policychecker import PolicyChecker
from patterns.s3tolambda import S3tolambdaStack

# Inicialização da aplicação CDK
app = cdk.App()

# Criação de uma instância da stack AspectsStack, passando a aplicação e um identificador único
others_stack = AspectsStack(app, "AspectsStack")

# Criação de uma instância da stack S3tolambdaStack, passando a aplicação e um identificador único
# Note que não há atribuição dessa instância a nenhuma variável, então ela será criada mas não utilizada diretamente aqui
S3tolambdaStack(app, "S3tolambdaStack")

# Adição de uma tag 'env' a todos os recursos da stack AspectsStack, com o valor 'sandbox'
cdk.Tags.of(others_stack).add('env', 'sandbox')

# Adição de uma tag 'storage' apenas aos buckets S3 da stack AspectsStack, com o valor 'sandbox'
# Isso é feito especificando o tipo de recurso e a prioridade da tag
cdk.Tags.of(others_stack).add('storage', 'sandbox',
                             include_resource_types=["AWS::S3::Bucket"],
                             priority=150)

# Adição do aspecto PolicyChecker à aplicação, para realizar verificações de políticas durante a construção
cdk.Aspects.of(app).add(PolicyChecker())

# Chamada para sintetizar a aplicação, gerando os recursos na AWS conforme definido nas stacks
app.synth()