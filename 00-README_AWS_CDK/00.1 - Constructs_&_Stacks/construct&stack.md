# Conceitos de Contruções e Stacks

No AWS CDK (Cloud Development Kit), os conceitos de **construções** (constructs) e **stacks** são fundamentais para a organização e gerenciamento de recursos da infraestrutura como código.

### Construções (Constructs)

**Construções** são os blocos de construção básicos do AWS CDK. Elas representam componentes ou padrões reutilizáveis da infraestrutura. Podem ser desde recursos individuais da AWS (como uma instância EC2 ou um bucket S3) até conjuntos mais complexos de recursos que trabalham juntos para cumprir um propósito específico (como uma aplicação web completa).

Existem três níveis de construções no AWS CDK:

1. **Nível 1 (L1) - Constructs de Nível Baixo**:
   - Representam diretamente os recursos da AWS.
   - São gerados a partir dos arquivos CloudFormation.
   - Exemplo: `s3.CfnBucket` representa um bucket S3 no nível CloudFormation.

2. **Nível 2 (L2) - Constructs de Nível Médio**:
   - São abstrações opinativas dos recursos de nível 1, oferecendo interfaces mais amigáveis e funcionalidades integradas.
   - Exemplo: `s3.Bucket` é uma construção L2 que facilita a criação e configuração de um bucket S3.

3. **Nível 3 (L3) - Constructs de Nível Alto**:
   - São padrões completos que combinam múltiplos recursos para resolver casos de uso específicos.
   - Exemplo: `aws_solutions_constructs.aws_s3_lambda` que configura um bucket S3 junto com uma função Lambda que responde a eventos desse bucket.

### Stacks

**Stacks** são as unidades de implantação no AWS CDK. Elas representam a coleção de construções que formam a sua aplicação ou uma parte dela. Cada stack é convertida em um modelo do CloudFormation quando você implanta a aplicação CDK.

- **Stack** é uma coleção de recursos que você quer implantar juntos. 
- Cada stack é implementada como uma classe que herda de `cdk.Stack`.
- Você pode definir múltiplas stacks dentro de uma aplicação CDK para separar diferentes partes da sua infraestrutura.

#### Exemplo de uma Stack com Construções

Aqui está um exemplo básico em Python, onde criamos uma stack com um bucket S3 usando uma construção de nível 2:

```python
from aws_cdk import (
    Stack,
    aws_s3 as s3,
    Duration,
    CfnOutput,
)

class MyFirstStack(Stack):

   def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
      super().__init__(scope, construct_id, **kwargs)

      bucket = s3.Bucket(self, "TestBucket",
               lifecycle_rules = [
                  s3.LifecycleRule(
                     expiration = Duration.days(3)
                  )
               ]
               )
      CfnOutput(self, "BucketName", 
               value = bucket.bucket_name)

app = cdk.App()
MyFirstStack(app, "MyFirstStack")
app.synth()
```

Neste exemplo:
- Definimos uma classe `MyFirstStack` que herda de `Stack`.
- Dentro do construtor da stack, criamos um bucket S3 usando a construção de nível 2 `s3.Bucket`.
- A stack `MyFirstStack` é então instanciada e adicionada ao aplicativo CDK (`app`), e o método `synth()` é chamado para sintetizar o modelo CloudFormation.
- s3.LifecycleRule determina que os arquivos no s# expiram em 3 dias

### Resumo

- **Construções** são blocos de construção reutilizáveis que representam componentes da infraestrutura.
- **Stacks** são coleções de construções que formam uma unidade de implantação.

Esses conceitos permitem a você estruturar, organizar e gerenciar a infraestrutura de forma eficiente e modular no AWS CDK.