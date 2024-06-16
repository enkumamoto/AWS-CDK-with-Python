from aws_cdk import (
    Stack,
    aws_s3 as s3,
    aws_cloudfront as cloudfront,
    aws_cloudfront_origins as origins,
    aws_s3_deployment as s3_deployment,
    CfnOutput
)

from constructs import Construct
import os

class Cfs3Stack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Criando um bucket S3 para armazenar os arquivos estáticos
        deployment_bucket = s3.Bucket(self, 'WebDeplBucket')

        # Definindo o diretório onde os arquivos estáticos estão localizados
        ui_dir = os.path.join(os.path.dirname(__file__), "..", "..", 'web', 'dist')
        # Verificando se o diretório existe e retornando se não existir
        if not os.path.exists(ui_dir):
            print("Ui directory is not found: " + ui_dir)
            return
        
        # Configurando uma identidade de acesso para o CloudFront
        origin_identity = cloudfront.OriginAccessIdentity(
            self, 'Cfs3StackAccessIdentity'
        )
        # Concedendo permissão ao CloudFront para ler os arquivos do bucket S3
        deployment_bucket.grant_read(origin_identity)

        # Criando uma distribuição do CloudFront
        distribution = cloudfront.Distribution(
            self, 'Cfs3StackDistribution',
            default_root_object = 'index.html',  # Definindo o arquivo padrão a ser servido
            default_behavior = cloudfront.BehaviorOptions(
                origin = origins.S3Origin(  # Configurando o comportamento padrão para usar o bucket S3 como origem
                    deployment_bucket,
                    origin_access_identity = origin_identity  # Usando a identidade de acesso configurada anteriormente
                )
            ),
        )

        # Deployando os arquivos estáticos para o bucket S3
        s3_deployment.BucketDeployment(
            self, 'Cfs3StackDeployment',
            sources = [s3_deployment.Source.asset(ui_dir)],  # Especificando o diretório dos arquivos estáticos
            destination_bucket = deployment_bucket,  # Bucket destino para o deploy
            distribution = distribution,  # Associando a distribuição do CloudFront criada anteriormente
        )

        # Exibindo o URL da distribuição do CloudFront após o deploy
        CfnOutput(
            self, 'Cfs3StackUrl',
            value = distribution.distribution_domain_name  # Mostrando o nome de domínio público da distribuição
        )