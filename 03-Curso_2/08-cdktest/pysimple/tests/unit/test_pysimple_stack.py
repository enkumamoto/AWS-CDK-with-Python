# Importa as bibliotecas necessárias para os testes
import aws_cdk as core
import aws_cdk.assertions as assertions
import pytest
from aws_cdk.assertions import Match

# Importa a classe que será testada
from pysimple.pysimple_stack import PysimpleStack

# Configuração de fixture para reutilização em múltiplos testes
@pytest.fixture(scope="session")
def simple_template():
    # Cria uma instância do App do AWS CDK
    app = core.App()
    # Cria uma instância da stack que será testada
    stack = PysimpleStack(app, "pysimple")
    # Extrai o template CloudFormation da stack criada
    template = assertions.Template.from_stack(stack)
    return template

# Teste básico de propriedades de uma Lambda Function
def test_lambda_props(simple_template):
    # Comentado pois está sendo utilizado o fixture 'simple_template'
    # simple_template.has_resource_properties("AWS::Lambda::Function", {
    #     "Runtime": "python3.11",
    # })

    # Verifica se a quantidade de recursos Lambda na stack é exatamente 1
    simple_template.resource_count_is("AWS::Lambda::Function", 1)

# Teste utilizando matchers para verificar a propriedade Runtime da Lambda
def test_lambda_runtime_matchers(simple_template):
    # Verifica se a propriedade Runtime da Lambda é compatível com qualquer versão de Python
    simple_template.has_resource_properties("AWS::Lambda::Function", {
        "Runtime": Match.string_like_regexp("python"),
    })

# Teste utilizando matchers para verificar uma política IAM relacionada a um bucket S3
def test_lambda_bucket_matchers(simple_template):
    # Verifica se existe uma política IAM com uma estrutura específica,
    # incluindo referências a um recurso chamado "SimpleBucket"
    simple_template.has_resource_properties(
        "AWS::IAM::Policy",
        Match.object_like( # é um objeto matcher que permite especificar um padrão ou estrutura esperada para um objeto JSON.
            {
                "PolicyDocument": {
                    "Statement": [
                        {
                            "Resource": [
                                {
                                    "Fn::GetAtt": [
                                        Match.string_like_regexp("SimpleBucket"),  # Referência ao nome do bucket S3
                                        "Arn",  # Propriedade Arn do bucket
                                    ]
                                },
                                Match.any_value(),  # Aceita qualquer outro valor como segundo elemento do array
                            ]
                        }
                    ]
                }
            }
        )
    )