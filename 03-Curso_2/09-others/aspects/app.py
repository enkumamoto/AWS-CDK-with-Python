#!/usr/bin/env python3
# Importação das bibliotecas necessárias para o funcionamento do script
import os

# Importação do módulo aws_cdk, que é essencial para a criação de infraestrutura na AWS usando CDK
import aws_cdk as cdk

# Importação específica de componentes do projeto, como AspectsStack e PolicyChecker
from aspects.aspects_stack import AspectsStack
from aspects.policychecker import PolicyChecker

# Inicialização da aplicação CDK
app = cdk.App()

# Criação de uma instância da stack AspectsStack, passando a aplicação e um identificador único
others_stack = AspectsStack(app, "AspectsStack")

# Adição do aspecto PolicyChecker à aplicação, para realizar verificações de políticas durante a construção
cdk.Aspects.of(app).add(PolicyChecker())

# Chamada para sintetizar a aplicação, gerando os recursos na AWS conforme definido nas stacks
app.synth()