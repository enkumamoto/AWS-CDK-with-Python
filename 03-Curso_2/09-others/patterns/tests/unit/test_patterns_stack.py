import aws_cdk as core
import aws_cdk.assertions as assertions

from patterns.patterns_stack import PatternsStack

# example tests. To run these tests, uncomment this file along with the example
# resource in patterns/patterns_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = PatternsStack(app, "patterns")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
