### Estrutura dos Arquivos Terraform/OpenTofu

Criando uma infraestrutura simples que inclui VPC, Lambda, DynamoDB e S3. 

#### 1. `variables.tf`
```hcl
variable "region" {
  description = "AWS region to deploy resources"
  type        = string
  default     = "us-east-1"
}

variable "vpc_cidr" {
  description = "CIDR block for the VPC"
  type        = string
  default     = "10.0.0.0/16"
}

# variable "lambda_s3_bucket" {
#   description = "S3 bucket where the Lambda function code is stored"
#   type        = string
#   default     = "my-lambda-bucket"
# }

# variable "lambda_s3_key" {
#   description = "S3 key for the Lambda function code"
#   type        = string
#   default     = "my-lambda.zip"
# }

# variable "lambda_role_name" {
#   description = "IAM role name for the Lambda function"
#   type        = string
#   default     = "my-lambda-role"
# }

# variable "lambda_function_name" {
#   description = "Name of the Lambda function"
#   type        = string
#   default     = "my-lambda-function"
# }

# variable "lambda_handler" {
#   description = "Handler for the Lambda function"
#   type        = string
#   default     = "index.handler"
# }

# variable "lambda_runtime" {
#   description = "Runtime for the Lambda function"
#   type        = string
#   default     = "nodejs16.x"
# }

variable "dynamodb_name" {
  description = "The name of the DynamoDB table"
  default     = "eiji_dynamodb"
}```

#### 2. `provider.tf`
```hcl
provider "aws" {
  region = var.region
}
```

#### 3. `vpc.tf`
```hcl
resource "aws_vpc" "main" {
  cidr_block = var.vpc_cidr

  tags = {
    Name = "main-vpc"
  }
}

resource "aws_subnet" "public" {
  vpc_id            = aws_vpc.main.id
  cidr_block        = "10.0.1.0/24"
  availability_zone = "us-west-2a"

  tags = {
    Name = "public-subnet"
  }
}

resource "aws_subnet" "private" {
  vpc_id            = aws_vpc.main.id
  cidr_block        = "10.0.2.0/24"
  availability_zone = "us-west-2a"

  tags = {
    Name = "private-subnet"
  }
}
```

#### 4. `s3.tf`
```hcl
resource "aws_s3_bucket" "lambda_bucket" {
  bucket = var.lambda_s3_bucket

  tags = {
    Name = "lambda-code-bucket"
  }
}
```

#### 5. `dynamodb.tf`
```hcl
resource "aws_dynamodb_table" "main" {
  name           = "main-table"
  billing_mode   = "PAY_PER_REQUEST"
  hash_key       = "id"

  attribute {
    name = "id"
    type = "S"
  }

  tags = {
    Name = "main-dynamodb-table"
  }
}
```

#### 6. `lambda.tf`
```hcl
resource "aws_iam_role" "lambda_exec_role" {
  name = "lambda_exec_role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = "sts:AssumeRole"
        Effect = "Allow"
        Principal = {
          Service = "lambda.amazonaws.com"
        }
      }
    ]
  })
}

resource "aws_iam_role_policy_attachment" "lambda_policy" {
  role       = aws_iam_role.lambda_exec_role.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
}

resource "aws_lambda_function" "main" {
  function_name = "main-lambda"
  s3_bucket     = var.lambda_s3_bucket
  s3_key        = var.lambda_s3_key
  handler       = "index.handler"
  runtime       = "python3.8"
  role          = aws_iam_role.lambda_exec_role.arn

  tags = {
    Name = "main-lambda-function"
  }
}
```

#### 7. `vpc_endpoint.tf`
```hcl
resource "aws_vpc_endpoint" "dynamodb" {
  vpc_id       = aws_vpc.main.id
  service_name = "com.amazonaws.${var.region}.dynamodb"
  vpc_endpoint_type = "Gateway"

  route_table_ids = [aws_subnet.public.id, aws_subnet.private.id]

  tags = {
    Name = "dynamodb-vpc-endpoint"
  }
}
```

### Instruções para Adicionar os Arquivos à Infraestrutura

1. Crie um diretório para o projeto Terraform/OpenTofu, por exemplo, `simple_infra`.
2. Dentro do diretório, crie os arquivos mencionados acima: `variables.tf`, `provider.tf`, `vpc.tf`, `s3.tf`, `dynamodb.tf`, `lambda.tf`, `vpc_endpoint.tf`.
3. Preencha os valores das variáveis no arquivo `variables.tf` conforme necessário.
4. Execute os comandos do Terraform/OpenTofu na seguinte ordem:

```sh
tofu init
tofu plan
tofu apply
```

Esses passos criarão a infraestrutura descrita, incluindo uma VPC, sub-redes, uma função Lambda que buscará o código no bucket S3, uma tabela DynamoDB e um VPC Endpoint para DynamoDB.
