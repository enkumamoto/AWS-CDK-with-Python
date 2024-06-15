from aws_cdk import (
    Stack,  # Importando a classe Stack do AWS CDK
    aws_s3 as s3,  # Alias para simplificar a referência à biblioteca aws_s3
    aws_cloudfront as cloudfront,  # Alias para simplificar a referência à biblioteca aws_cloudfront
    aws_cloudfront_origins as origins,  # Alias para simplificar a referência à biblioteca aws_cloudfront_origins
    aws_s3_deployment as s3_deployment,  # Alias para simplificar a referência à biblioteca aws_s3_deployment
    CfnOutput  # Importando a classe CfnOutput do AWS CDK para saída de informações
)

from constructs import Construct  # Importando a classe Construct do pacote constructs
import os  # Importando o módulo os para manipulação de caminhos de arquivos

class Cfs3Stack(Stack):  # Definindo a classe Cfs3Stack que herda de Stack do AWS CDK

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:  # Método inicializador da classe
        super().__init__(scope, construct_id, **kwargs)  # Chamada ao construtor da classe base

        # Criando um bucket S3 para armazenamento temporário dos arquivos da aplicação
        deployment_bucket = s3.Bucket(self, 'WebDeplBucket')

        # Construindo o caminho para o diretório que contém os arquivos compilados da aplicação web
        # Usando variáveis de ambiente para maior flexibilidade
        UI_DIR_ENV_VAR = 'WEB_DIST_PATH'
        ui_dir = os.getenv(UI_DIR_ENV_VAR, os.path.join(os.path.dirname(__file__), '..', 'default/path/to/web/dist'))

        # Verificando se o diretório existe para evitar erros de execução
        if not os.path.exists(ui_dir):
            raise FileNotFoundError(f'O diretório {ui_dir} não foi encontrado.')

        # Configurando a identidade de acesso para o CloudFront
        origin_identity = cloudfront.OriginAccessIdentity(
            self, 'Cfs3StackAccessIdentity'
        )

        # Concedendo permissão de leitura ao bucket para a identidade de acesso do CloudFront
        deployment_bucket.grant_read(origin_identity)

        # Configurando a distribuição do CloudFront
        distribution = cloudfront.Distribution(
            self, 'Cfs3StackDistribution',
            default_root_object='index.html',  # Definindo o objeto padrão a ser retornado pela distribuição
            default_behavior=cloudfront.BehaviorOptions(  # Configurando o comportamento padrão da distribuição
                origin=origins.S3Origin(  # Especificando o bucket S3 como origem
                    deployment_bucket,
                    origin_access_identity=origin_identity  # Associando a identidade de acesso
                )
            ),
        )

        # Realizando o deploy dos arquivos da aplicação para o bucket S3
        s3_deployment.BucketDeployment(
            self, 'Cfs3StackDeployment',
            sources=[s3_deployment.Source.asset(ui_dir)],  # Especificando os arquivos a serem implantados
            destination_bucket=deployment_bucket,  # Bucket destino para o deploy
            distribution=distribution,  # Referenciando a distribuição do CloudFront
        )

        # Exibindo o URL público da distribuição do CloudFront como saída do stack
        CfnOutput(
            self, 'Cfs3StackUrl',
            value=distribution.distribution_domain_name  # Exibindo o domínio da distribuição
        )