from aws_cdk import (
    # Importando classes necessárias da AWS CDK para criar uma pilha, um bucket S3 e uma função Lambda
    Stack,
    aws_s3 as s3,
    aws_lambda as _lambda
)
from constructs import Construct

class AspectsStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        # Chamando o construtor da classe pai para inicializar a pilha
        super().__init__(scope, construct_id, **kwargs)

        # Definindo uma função Lambda simples que imprime uma mensagem quando invocada
        cool_lambda = _lambda.Function(self, "SimpleLambda",
            runtime = _lambda.Runtime.PYTHON_3_11,  # Especificando a versão do Python para a função Lambda
            handler = "index.handler",  # O ponto de entrada da função Lambda
            code = _lambda.Code.from_inline("print()")  # Código inline que será executado pela função Lambda
        )

        # Criando um bucket S3 com controle de versões habilitado
        bucket = s3.Bucket(self, "SimpleBucket",
        versioned = True  # Ativando o controle de versões para o bucket
        )
        # Concedendo à função Lambda a permissão de ler objetos deste bucket
        bucket.grant_read(cool_lambda)