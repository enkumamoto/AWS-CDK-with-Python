import jsii
from aws_cdk import (
    IAspect,
    aws_iam as iam,
    Stack,
    Annotations
)
import json

@jsii.implements(IAspect)
class PolicyChecker:

    def visit(self, node):
        # print(f'Visiting {node.__class__.__name__}')

        if isinstance(node, iam.CfnPolicy):
            resolvedDoc = Stack.of(node).resolve(node.policy_document)
            resolvedDocJson = json.dumps(resolvedDoc, indent=2)

            # print(resolvedDocJson) 

            if "GetBucket" in resolvedDocJson:
                Annotations.of(node).add_warning_v2("warning",
                "Forbidden Action" + "GetBucket"
                )