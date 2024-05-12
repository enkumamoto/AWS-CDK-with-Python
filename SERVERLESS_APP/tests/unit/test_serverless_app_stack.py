import aws_cdk as core
import aws_cdk.assertions as assertions

from serverless_app.serverless_app_stack import ServerlessAppStack

# example tests. To run these tests, uncomment this file along with the example
# resource in serverless_app/serverless_app_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = ServerlessAppStack(app, "serverless-app")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
