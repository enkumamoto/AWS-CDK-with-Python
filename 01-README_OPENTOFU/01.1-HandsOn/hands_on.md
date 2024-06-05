### Estrutura dos Arquivos Terraform/OpenTofu

Criando uma infraestrutura simples que inclui VPC e S3. 

#### 1. `variables.tf`
```hcl
variable "region" {
  description = "AWS region to deploy resources"
  type        = string
  default     = "us-aest-1"
}

variable "vpc_cidr" {
  description = "CIDR block for the VPC"
  type        = string
  default     = "10.0.0.0/16"
}
```

#### 2. `provider.tf`
```hcl
terraform {
  required_providers {
    aws = {
      source = "hashicorp/aws"
      version = "5.52.0"
    }
  }
}

provider "aws" {
  # Configuration options
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

#### 4. `aws_subnet.tf`
```hcl
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

#### 5. `s3.tf`
```hcl
resource "aws_s3_bucket" "my-bucket" {
  bucket = "eiji-tf-test-bucket"

  tags = {
    Name        = "Eiji bucket"
    Environment = "Dev"
  }
}
```

#### 6. `dynamodb.tf`
```hcl
resource "aws_dynamodb_table" "basic-dynamodb-table" {
  name           = var.dynamodb_name
  billing_mode   = "PROVISIONED"
  read_capacity  = 20
  write_capacity = 20
  hash_key       = "UserId"
  range_key      = "GameTitle"

  attribute {
    name = "UserId"
    type = "S"
  }

  attribute {
    name = "GameTitle"
    type = "S"
  }

  attribute {
    name = "TopScore"
    type = "N"
  }

  ttl {
    attribute_name = "TimeToExist"
    enabled        = false
  }

  global_secondary_index {
    name               = "GameTitleIndex"
    hash_key           = "GameTitle"
    range_key          = "TopScore"
    write_capacity     = 10
    read_capacity      = 10
    projection_type    = "INCLUDE"
    non_key_attributes = ["UserId"]
  }

  tags = {
    Name        = "dynamodb-table-1"
    Environment = "production"
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