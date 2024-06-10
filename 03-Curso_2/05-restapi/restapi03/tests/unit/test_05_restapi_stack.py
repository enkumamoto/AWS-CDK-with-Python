import aws_cdk as core
import aws_cdk.assertions as assertions

from 05_restapi.05_restapi_stack import 05RestapiStack

# example tests. To run these tests, uncomment this file along with the example
# resource in 05_restapi/05_restapi_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = 05RestapiStack(app, "05-restapi")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
