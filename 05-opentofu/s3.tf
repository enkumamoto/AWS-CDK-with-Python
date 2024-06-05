resource "aws_s3_bucket" "my-bucket" {
  bucket = "eiji-tf-test-bucket"

  tags = {
    Name        = "Eiji bucket"
    Environment = "Dev"
  }
}