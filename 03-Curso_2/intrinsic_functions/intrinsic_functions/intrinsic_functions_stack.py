# Importa módulos necessários do pacote aws_cdk
from aws_cdk import (
    aws_ec2 as ec2,  # Módulo para recursos relacionados à EC2
    Stack,           # Classe base para todas as stacks no AWS CDK
    aws_s3 as s3,    # Módulo para recursos relacionados ao S3
    Duration,        # Classe para especificar durações
    CfnOutput,       # Classe para definir saídas de dados personalizadas
    Fn               # Classe para funções intrínsecas
)

# Importa a classe Construct do pacote constructs
from constructs import Construct

# Define a classe IntrinsicFunctionsStack que herda de Stack
class IntrinsicFunctionsStack(Stack):

    # Método construtor da stack
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        # Chama o construtor da classe base Stack
        super().__init__(scope, construct_id, **kwargs)

        # Inicializa o sufixo com base no ID da stack
        suffix = self.__initialize_suffix()

        # Cria um novo bucket S3 com o ID "TestBucket"
        bucket = s3.Bucket(self, "TestBucket",
            # Define o nome do bucket como "eijibucket" seguido pelo sufixo
            bucket_name=f"eijibucket-{suffix}",
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

    # Método privado para inicializar o sufixo com base no ID da stack
    def __initialize_suffix(self):
        # Extrai o terceiro elemento da lista dividida pelo '/' no ID da stack
        short_stack_id = Fn.select(2, Fn.split('/', self.stack_id))
        # Extrai o quarto elemento da lista dividida pelo '-' no ID curto da stack
        suffix = Fn.select(4, Fn.split('-', short_stack_id))
        return suffix