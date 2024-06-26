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
        # verificando cada nó visitado
        # print(f'Visiting {node.__class__.__name__}')

        # Verifica se o nó é uma instância de CfnPolicy
        if isinstance(node, iam.CfnPolicy):
            # Resolve o documento da política para obter a versão final
            resolvedDoc = Stack.of(node).resolve(node.policy_document)
            # Converte o documento resolvido para JSON formatado
            resolvedDocJson = json.dumps(resolvedDoc, indent=2)

            # procurando por ações proibidas no documento
            # print(resolvedDocJson) 

            # Verifica se a ação "GetBucket" está presente no documento resolvido
            if "GetBucket" in resolvedDocJson:
                # Adiciona um aviso se a ação proibida for encontrada
                Annotations.of(node).add_warning_v2("warning",
                "Ação Proibida" + "GetBucket"
                )