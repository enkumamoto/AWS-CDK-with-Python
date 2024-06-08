import aws_cdk as core
import aws_cdk.assertions as assertions

from intrinsic_functions.intrinsic_functions_stack import IntrinsicFunctionsStack

# example tests. To run these tests, uncomment this file along with the example
# resource in intrinsic_functions/intrinsic_functions_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = IntrinsicFunctionsStack(app, "intrinsic-functions")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
