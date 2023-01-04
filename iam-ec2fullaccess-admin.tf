/* To create an IAM role with Amazon EC2 full access and administrator access using Terraform, 
you can use the following configuration: */

resource "aws_iam_role" "ec2_full_access_admin" {
  name = "EC2FullAccessAdmin"
  assume_role_policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "ec2.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
EOF
}

resource "aws_iam_policy_attachment" "ec2_full_access_admin" {
  name = "EC2FullAccessAdmin"
  roles = [aws_iam_role.ec2_full_access_admin.name]
  policy_arn = "arn:aws:iam::aws:policy/AdministratorAccess"
}

/* This configuration will create an IAM role named "EC2FullAccessAdmin" with the 
permissions specified in the AdministratorAccess policy. The role will have the permissions 
to perform any action on any resource in your AWS account.

You can then use this role to launch EC2 instances with the permissions specified in the role.

Please note that the AdministratorAccess policy provides full access to all AWS services and 
resources, so be sure to use it with caution. It is recommended to use more granular 
permissions policies when possible to ensure that your users and resources have the 
minimum required permissions. */
