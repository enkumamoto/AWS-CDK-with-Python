import aws_cdk as core
import aws_cdk.assertions as assertions

from 04_crossstacks.04_crossstacks_stack import 04CrossstacksStack

# example tests. To run these tests, uncomment this file along with the example
# resource in 04_crossstacks/04_crossstacks_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = 04CrossstacksStack(app, "04-crossstacks")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
