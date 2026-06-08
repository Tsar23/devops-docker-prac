provider "aws" {
  region = "eu-central-1"
}

resource "aws_instance" "agro_backend" {
  ami           = "ami-0abcdef1234567890"
  instance_type = "t3.micro"

  tags = {
    Name        = "AgroControl-Prod"
    Environment = "Production"
  }
}