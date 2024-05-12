import aws_cdk as core
import aws_cdk.assertions as assertions

from my_sample_app.my_sample_app_stack import MySampleAppStack

# example tests. To run these tests, uncomment this file along with the example
# resource in my_sample_app/my_sample_app_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = MySampleAppStack(app, "my-sample-app")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
