import aws_cdk as core
import aws_cdk.assertions as assertions

from my_sample_app_webserver.my_sample_app_webserver_stack import MySampleAppWebserverStack

# example tests. To run these tests, uncomment this file along with the example
# resource in my_sample_app_webserver/my_sample_app_webserver_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = MySampleAppWebserverStack(app, "my-sample-app-webserver")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
