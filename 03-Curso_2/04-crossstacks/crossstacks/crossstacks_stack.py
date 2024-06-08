# Importa módulos específicos do pacote aws_cdk
from aws_cdk import (
    aws_ec2 as ec2,  # Alias para módulos relacionados à Amazon EC2
    Stack,           # Classe base para todas as stacks no AWS Cloud Development Kit (CDK)
    aws_s3 as s3,    # Alias para módulos relacionados ao Amazon Simple Storage Service (S3)
    Duration,        # Classe para especificar durações de tempo
    CfnOutput,       # Classe para criar saídas de dados personalizadas
    Fn               # Classe para funções intrínsecas
)

# Importa a classe Construct do pacote constructs
from constructs import Construct

# Define a classe CrossstacksStack que herda de Stack
class CrossstacksStack(Stack):

    # Método construtor da classe CrossstacksStack
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        # Chama o método construtor da classe base Stack
        super().__init__(scope, construct_id, **kwargs)

        # Inicializa o sufixo com base no ID da stack
        suffix = self.__initialize_suffix()

        # Cria um novo bucket S3 com o ID "PyBucket"
        self.bucket = s3.Bucket(self, "PyBucket",
            # Define o nome do bucket como "cool-bucket-" seguido pelo sufixo
            bucket_name=f"cool-bucket-{suffix}",
            # Configura regras de ciclo de vida para o bucket
            lifecycle_rules=[
                # Define uma regra de ciclo de vida para expirar os objetos após 3 dias
                s3.LifecycleRule(
                    expiration=Duration.days(3)
                )
            ]
        )

        # Cria uma saída de dados personalizada para exibir o nome do bucket criado
        CfnOutput(self, "PyBucketName",
                  value=self.bucket.bucket_name)

    # Método privado para inicializar o sufixo com base no ID da stack
    def __initialize_suffix(self):
        # Extrai o terceiro elemento da lista dividida pelo '/' no ID da stack
        short_stack_id = Fn.select(2, Fn.split('/', self.stack_id))
        # Extrai o quarto elemento da lista dividida pelo '-' no ID curto da stack
        suffix = Fn.select(4, Fn.split('-', short_stack_id))
        return suffix
    
    # Propriedade para acessar o bucket criado
    @property
    def cool_bucket(self):
        return self.bucket