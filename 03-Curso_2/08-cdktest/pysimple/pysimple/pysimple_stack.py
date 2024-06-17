# Importação das classes e funções necessárias do AWS CDK para a criação da stack
from aws_cdk import (
    Stack,
    aws_s3 as s3,
    aws_lambda as _lambda
)
from constructs import Construct

# Definição da classe PysimpleStack, que herda da classe Stack do AWS CDK
class PysimpleStack(Stack):

    # Método de inicialização da stack, onde são configurados seus componentes
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        # Chamada ao método de inicialização da classe base (Stack), passando o escopo e o ID do construct
        super().__init__(scope, construct_id, **kwargs)

        # Criação de uma função Lambda simples, que imprime uma mensagem no console
        # Especificação do ambiente de execução (Python 3.11), do manipulador e do código inline
        cool_lambda = _lambda.Function(self, "SimpleLambda",
            runtime = _lambda.Runtime.PYTHON_3_11,
            handler = "index.handler",
            code = _lambda.Code.from_inline("print()")
        )

        # Criação de um bucket S3 com suporte a versões
        # Atribuição de permissões de leitura ao bucket para a função Lambda criada anteriormente
        bucket = s3.Bucket(self, "SimpleBucket", versioned=True)
        bucket.grant_read(cool_lambda)