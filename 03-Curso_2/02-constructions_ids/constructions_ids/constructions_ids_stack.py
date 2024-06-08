# Importa módulos necessários da biblioteca AWS CDK
from aws_cdk import (
    aws_ec2 as ec2,  # Módulo para recursos relacionados à EC2
    Stack,           # Classe base para todas as stacks no AWS CDK
    aws_s3 as s3,    # Módulo para recursos relacionados ao S3
    Duration,        # Classe para especificar durações
    CfnOutput       # Classe para definir saídas de dados personalizadas
)

# Importa a classe Construct do pacote constructs
from constructs import Construct

# Define uma nova stack chamada ConstructionsIdsStack que herda de Stack
class ConstructionsIdsStack(Stack):

    # Método construtor da stack
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        # Chama o construtor da classe base Stack
        super().__init__(scope, construct_id, **kwargs)

        # Cria um novo bucket S3 com o ID "TestBucket"
        bucket = s3.Bucket(self, "TestBucket",
            # Define o nome do bucket como "eijibucket"
            bucket_name="eijibucket",
            # Configura regras de ciclo de vida para o bucket
            lifecycle_rules=[
                # Define uma regra de ciclo de vida para expirar os objetos após 3 dias
                s3.LifecycleRule(
                    expiration=Duration.days(3)
                )
            ]
        )
        # Cria uma saída de dados personalizada para exibir o nome do bucket criado
        CfnOutput(self, "BucketName",
                  value=bucket.bucket_name)