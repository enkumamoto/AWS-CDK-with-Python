import aws_cdk as core
import aws_cdk.assertions as assertions

from my_sample_app_webserver.my_sample_app_webserver_stack import MySampleAppWebserverStack
from my_sample_app_webserver.network_stack import NetworkStack

def test_network_stack_counts():
    app = core.App()
    root_stack = core.Stack(app, "RootStack")

    network_stack = NetworkStack(root_stack, 'NetworkStack')

    application_stack = MySampleAppWebserverStack(root_stack, "MySampleAppWebserverStack",
                                                  my_vpc = network_stack.vpc)

    template = assertions.Template.from_stack(network_stack)

    template.resource_count_is('AWS::EC2::VPC', 1)

    template.resource_count_is('AWS::EC2::NatGateway', 0)