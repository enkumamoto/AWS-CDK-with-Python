from aws_cdk import (
    # Importando a classe Stack e os módulos para S3 e Lambda da AWS CDK
    Stack,
    aws_s3 as s3,
    aws_lambda as _lambda
)
from constructs import Construct

class TagsStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        # Chamada ao construtor da classe pai para inicializar a pilha
        super().__init__(scope, construct_id, **kwargs)

        # Criando uma função Lambda simples
        cool_lambda = _lambda.Function(self, "SimpleLambda",
            runtime = _lambda.Runtime.PYTHON_3_11,  # Especificando a versão do Python
            handler = "index.handler",  # O ponto de entrada da função Lambda
            code = _lambda.Code.from_inline("print()")  # Código inline para imprimir na execução
        )

        # Criando um bucket S3 com controle de versões habilitado
        bucket = s3.Bucket(self, "SimpleBucket",
        versioned = True  # Habilita o controle de versões no bucket
        )
        # Concedendo permissão de leitura ao bucket para a função Lambda criada anteriormente
        bucket.grant_read(cool_lambda)