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

def test_application_stack_web_server():
    app = core.App()
    root_stack = core.Stack(app, "RootStack")

    network_stack = NetworkStack(root_stack, 'NetworkStack')

    application_stack = MySampleAppWebserverStack(root_stack, "MySampleAppWebserverStack",
                                                  my_vpc = network_stack.vpc)

    template = assertions.Template.from_stack(application_stack)

    template.has_resource_properties('AWS::EC2::Instance', {
        'InstanceType': assertions.Match.string_like_regexp('(t2|t3).nano'),
        'ImageId': assertions.Match.any_value(),
        'KeyName': assertions.Match.absent()
    })

def test_web_server_security_group():
    app = core.App()

    root_stack = core.Stack(app, "RootStack")

    network_stack = NetworkStack(root_stack, 'NetworkStack')

    application_stack = MySampleAppWebserverStack(root_stack, "MySampleAppWebserverStack",
                                                    my_vpc = network_stack.vpc)

    template = assertions.Template.from_stack(application_stack)

    template.has_resource_properties('AWS::EC2::SecurityGroup', {
        'SecurityGroupIngress': assertions.Match.array_with([
            assertions.Match.object_like({
                'IpProtocol': 'tcp',
                'FromPort': 80,
                'ToPort': 80,
                'CidrIp': '0.0.0.0/0'
            })
        ])
    })

    template.has_resource_properties('AWS::EC2::SecurityGroup', {
        'SecurityGroupIngress': assertions.Match.array_with([
            assertions.Match.object_like({
                'IpProtocol': 'tcp',
                'FromPort': 80,
                'ToPort': 80,
                'CidrIp': '0.0.0.0/0'
            })
        ])
    })