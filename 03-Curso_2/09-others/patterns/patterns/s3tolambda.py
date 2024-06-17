# Importação do construct S3ToLambda da biblioteca aws_solutions_constructs, que facilita a integração entre S3 e Lambda
from aws_solutions_constructs.aws_s3_lambda import S3ToLambda
# Importação de componentes essenciais do AWS CDK para a criação da stack
from aws_cdk import (
    aws_lambda as _lambda,
    Stack
)
# Importação do pacote constructs para uso genérico na criação de estruturas de software
from constructs import Construct

# Definição da classe S3tolambdaStack, que estende a classe Stack do AWS CDK
class S3tolambdaStack(Stack):

    # Método de inicialização da stack, onde são configurados seus componentes
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        # Chamada ao método de inicialização da classe base (Stack), passando o escopo e o ID do construct
        super().__init__(scope, construct_id, **kwargs)

        # Instanciação do construct S3ToLambda, passando o contexto atual ('self') e um ID único ('test_s3_lambda')
        # Também são passadas propriedades específicas para a função Lambda, como o código inline, o ambiente de execução e o manipulador
        S3ToLambda(self, 'test_s3_lambda',
                lambda_function_props=_lambda.FunctionProps(
                    code=_lambda.Code.from_inline('print()'),  # Código inline simples para testes
                    runtime=_lambda.Runtime.PYTHON_3_9,  # Ambiente de execução especificado
                    handler='index.handler'  # Manipulador especificado
                )
                )