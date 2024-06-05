resource "aws_vpc_endpoint" "dynamodb" {
  vpc_id       = aws_vpc.main.id
  service_name = "com.amazonaws.${var.region}.dynamodb"
  vpc_endpoint_type = "Gateway"

  route_table_ids = [aws_subnet.public.id, aws_subnet.private.id]

  tags = {
    Name = "dynamodb-vpc-endpoint"
  }
}