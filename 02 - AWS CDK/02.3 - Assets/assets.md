# Conceito de Assets

No AWS CDK (Cloud Development Kit), **assets** são recursos que permitem incluir arquivos externos, como arquivos estáticos, imagens de contêiner, código-fonte de aplicações Lambda, entre outros, diretamente nas suas stacks. Eles são utilizados para empacotar e implantar esses arquivos juntamente com sua infraestrutura definida pelo CDK.

### Tipos de Assets

Existem dois tipos principais de assets no AWS CDK:

1. **Assets de Arquivo**: Permitem incluir arquivos ou diretórios do sistema de arquivos local no seu aplicativo CDK. Esses arquivos são carregados para o Amazon S3 e referenciados nas suas stacks.

2. **Assets de Imagem de Contêiner**: Permitem construir e carregar imagens de contêiner Docker para o Amazon Elastic Container Registry (ECR), facilitando a implantação de aplicações baseadas em contêiner.

### Uso de Assets de Arquivo

Um uso comum de assets de arquivo é empacotar o código-fonte para funções AWS Lambda. Aqui está um exemplo de como utilizar assets para uma função Lambda:

#### Exemplo de Uso de Assets para uma Função Lambda

1. **Estrutura de Diretórios**:
    ```
    my-cdk-app/
    ├── app.py
    ├── cdk.json
    ├── lambda/
    │   └── handler.py
    ├── my_cdk_app/
    │   ├── __init__.py
    │   └── my_cdk_app_stack.py
    └── requirements.txt
    ```

2. **Arquivo `lambda/handler.py`**:
    ```python
    def handler(event, context):
        return {
            'statusCode': 200,
            'body': 'Hello from Lambda!'
        }
    ```

3. **Definindo a Stack com Assets no `my_cdk_app/my_cdk_app_stack.py`**:
    ```python
    from aws_cdk import core
    from aws_cdk import aws_lambda as _lambda

    class MyCdkAppStack(core.Stack):

        def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
            super().__init__(scope, id, **kwargs)

            # Definição da função Lambda utilizando assets
            lambda_function = _lambda.Function(
                self, 'MyLambdaFunction',
                runtime=_lambda.Runtime.PYTHON_3_8,
                handler='handler.handler',
                code=_lambda.Code.from_asset('lambda')
            )
    ```

### Uso de Assets de Imagem de Contêiner

Para assets de imagem de contêiner, você pode usar o AWS CDK para construir e carregar imagens Docker para o ECR.

#### Exemplo de Uso de Assets para uma Imagem de Contêiner

1. **Estrutura de Diretórios**:
    ```
    my-cdk-app/
    ├── Dockerfile
    ├── app.py
    ├── cdk.json
    ├── my_cdk_app/
    │   ├── __init__.py
    │   └── my_cdk_app_stack.py
    └── requirements.txt
    ```

2. **Arquivo `Dockerfile`**:
    ```Dockerfile
    FROM public.ecr.aws/lambda/python:3.8
    COPY app.py ${LAMBDA_TASK_ROOT}
    CMD ["app.handler"]
    ```

3. **Definindo a Stack com Assets no `my_cdk_app/my_cdk_app_stack.py`**:
    ```python
    from aws_cdk import core
    from aws_cdk import aws_lambda as _lambda

    class MyCdkAppStack(core.Stack):

        def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
            super().__init__(scope, id, **kwargs)

            # Definição da função Lambda utilizando uma imagem Docker
            lambda_function = _lambda.DockerImageFunction(
                self, 'MyDockerLambdaFunction',
                code=_lambda.DockerImageCode.from_image_asset('.')
            )
    ```

### Funcionamento Interno dos Assets

Quando você usa assets no AWS CDK:

1. **Empacotamento**: Os arquivos especificados (ou a imagem Docker) são empacotados no seu diretório local.
2. **Carregamento**: Os assets são carregados para um bucket S3 (para arquivos) ou para o ECR (para imagens Docker) gerenciado pelo CDK.
3. **Referenciamento**: O CDK gera automaticamente as permissões necessárias e os metadados para que os recursos da AWS possam acessar esses assets.

### Resumo

- **Assets de Arquivo**: Empacotam e carregam arquivos ou diretórios locais para o S3.
- **Assets de Imagem de Contêiner**: Constroem e carregam imagens Docker para o ECR.
- **Utilização**: Facilitam a inclusão de arquivos externos, como código-fonte para Lambda ou imagens Docker, nas suas stacks CDK.
- **Automatização**: O CDK cuida de empacotar, carregar e gerenciar permissões para os assets, simplificando o processo de implantação.

Essa funcionalidade é poderosa para gerenciar e implantar componentes complexos da infraestrutura com facilidade e eficiência no AWS CDK.