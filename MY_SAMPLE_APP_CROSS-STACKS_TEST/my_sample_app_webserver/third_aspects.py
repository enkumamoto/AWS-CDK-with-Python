import jsii
from aws_cdk import (
    IAspect,
    Stack,
    Annotations,
    aws_ec2 as ec2
)

@jsii.implements(IAspect)
class SSHAnywhereChecker:
    def visit(self, node):

        if isinstance(node, ec2.CfnSecurityGroup):
            rules = Stack.of(node).resolve(node.security_group_ingress)
            for rule in rules:
                if rule['ipProtocol'] == 'tcp' and rule['fromPort'] <= 22 and rule['toPort'] >= 22:
                    if rule['cidrIp'] != '0.0.0.0/0':
                        Annotations.of(node).add_warning(f"O acesso SSH deve ser permitido para o IP 0.0.0.0/0")