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
}