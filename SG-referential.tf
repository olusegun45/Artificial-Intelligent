/* terraform script to create 2 aws security group with the second security group to ingress the 
first security group
Here is an example of a Terraform script that creates two security groups, with the second 
security group allowing incoming traffic from the first security group: */

resource "aws_security_group" "sg1" {
  name        = "sg1"
  description = "First security group"

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_security_group" "sg2" {
  name        = "sg2"
  description = "Second security group"

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    security_groups = ["${aws_security_group.sg1.id}"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}


/* This script creates two security groups: sg1 and sg2. sg1 has an inbound rule that
allows incoming traffic on port 80 (HTTP) from any IP address, and an outbound rule that
allows all outbound traffic to any IP address. sg2 has an inbound rule that allows incoming
traffic on port 80 (HTTP) from the security group sg1, and an outbound rule that allows all 
outbound traffic to any IP address.

Note that the security group specified in the security_groups attribute must already exist. 
You can also specify multiple security groups by providing a list of security group IDs. */

