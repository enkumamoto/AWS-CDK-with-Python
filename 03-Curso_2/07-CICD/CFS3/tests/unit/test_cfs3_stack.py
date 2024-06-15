import aws_cdk as core
import aws_cdk.assertions as assertions

from cfs3.cfs3_stack import Cfs3Stack

# example tests. To run these tests, uncomment this file along with the example
# resource in cfs3/cfs3_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = Cfs3Stack(app, "cfs3")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
