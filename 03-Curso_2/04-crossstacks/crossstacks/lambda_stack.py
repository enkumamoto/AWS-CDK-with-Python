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
        
        # Cria uma função Lambda chamada "PyCoolLambda"
        aws_lambda.Function(self, "PyCoolLambda",
            # Especifica o código inline para a função Lambda
            code = aws_lambda.Code.from_inline (
                "import os\ndef handler(event, context):\n print(os.environ['COOL_BUCKET_ARN'])"),  # Código Python inline
            # Define o manipulador padrão da função Lambda
            handler = "index.handler",  # O ponto de entrada da função Lambda
            # Especifica a versão do runtime Python para a função Lambda
            runtime = aws_lambda.Runtime.PYTHON_3_10,  # Versão do Python usada pela função Lambda
            # Define variáveis de ambiente para a função Lambda
            environment = {
                "COOL_BUCKET_ARN": bucket.bucket_arn  # Passa o ARN do bucket S3 como variável de ambiente
            }
        )