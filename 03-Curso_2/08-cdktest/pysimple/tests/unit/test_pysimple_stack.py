import aws_cdk as core
import aws_cdk.assertions as assertions
import pytest

from pysimple.pysimple_stack import PysimpleStack

# Aqui otimiza-se o template para agilizar os testes
@pytest.fixture(scope = "session")
def simple_template():
    app = core.App()
    stack = PysimpleStack(app, "pysimple")
    template = assertions.Template.from_stack(stack)
    return template

# A função abaixo é um teste comum do CDK
# def test_lambda_props():
#     app = core.App()
#     stack = PysimpleStack(app, "pysimple")
#     template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::Lambda::Function", {
#         "Runtime": "python3.11",
#     })

# A função abaixo é um teste CDK otimizado para:
    # Checagem da versão do Python
def test_lambda_props(simple_template):
    simple_template.has_resource_properties("AWS::Lambda::Function", {
        "Runtime": "python3.11",
    })

    # Checagem da quantidade de recursos dentro da stack
    simple_template.resource_count_is("AWS::Lambda::Function", 1) # checa se a quantidade de lambdas é igual a 1
