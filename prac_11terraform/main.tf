# main.tf

# Налаштування провайдера AWS [cite: 715-719]
provider "aws" {
  region = "us-east-1"
}

# Ресурс: віртуальна машина EC2 [cite: 721-731]
resource "aws_instance" "example" {
  ami           = "ami-0c55b159cbfafe1f0" # Зверни увагу: AMI залежить від регіону
  instance_type = "t2.micro"             # Використовуємо Free Tier [cite: 732]

  tags = {
    Name = "TerraformExample"
  }
}