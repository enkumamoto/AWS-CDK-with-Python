import aws_cdk as core
import aws_cdk.assertions as assertions

from monitoring.monitoring_stack import MonitoringStack

# example tests. To run these tests, uncomment this file along with the example
# resource in monitoring/monitoring_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = MonitoringStack(app, "monitoring")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
