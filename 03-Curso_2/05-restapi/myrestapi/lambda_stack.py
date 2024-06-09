# Importa classes e módulos específicos do pacote aws_cdk
from aws_cdk import (
    Stack,          # Classe base para todas as stacks no AWS CDK
    aws_s3 as s3,   # Alias para módulos relacionados ao Amazon Simple Storage Service (S3)
    aws_lambda,     # Alias para módulos relacionados à AWS Lambda
)

# Importa a classe Construct do pacote constructs
from constructs import Construct

# Define a classe PyHandlerStack que herda de Stack
class PyHandlerStack(Stack):

    # Método construtor da classe PyHandlerStack
    def __init__(self, scope: Construct, construct_id: str, bucket : s3.Bucket, **kwargs) -> None:
        # Chama o método construtor da classe base Stack
        super().__init__(scope, construct_id, **kwargs)