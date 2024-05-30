import aws_cdk as core
import aws_cdk.assertions as assertions

from serverless_app_lambdatodynamodb.serverless_app_lambdatodynamodb_stack import ServerlessAppLambdatodynamodbStack

# example tests. To run these tests, uncomment this file along with the example
# resource in serverless_app_lambdatodynamodb/serverless_app_lambdatodynamodb_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = ServerlessAppLambdatodynamodbStack(app, "serverless-app-lambdatodynamodb")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
