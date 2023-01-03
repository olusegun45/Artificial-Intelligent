# Artificial-Intelligent

# Python to create lambda step function to start and shutdown server
To create a Lambda function that starts and stops an EC2 instance, you will need to first create an IAM role with permissions to manage EC2 instances.

Here is some sample code that demonstrates how to create a Lambda function using the boto3 library to start and stop an EC2 instance:
<!-- 
import boto3

def lambda_handler(event, context):
    # Replace with the ID of your EC2 instance
    instance_id = 'INSTANCE_ID'

    # Replace with your AWS access key and secret key
    aws_access_key_id = 'ACCESS_KEY'
    aws_secret_access_key = 'SECRET_KEY'

    # Create an EC2 client
    ec2 = boto3.client('ec2', aws_access_key_id=aws_access_key_id,
                       aws_secret_access_key=aws_secret_access_key)

    if event['RequestType'] == 'StartInstance':
        # Start the EC2 instance
        ec2.start_instances(InstanceIds=[instance_id])
        print('Started instance')
    elif event['RequestType'] == 'StopInstance':
        # Stop the EC2 instance
        ec2.stop_instances(InstanceIds=[instance_id])
        print('Stopped instance')
 -->

You can then use this Lambda function in a CloudFormation stack or as a custom resource in another CloudFormation stack. When the stack is created or deleted, the Lambda function will start or stop the EC2 instance accordingly.

Alternatively, you can use the awscli command-line tool to start and stop EC2 instances. Here is an example of how to start an EC2 instance using the awscli:

<!-- aws ec2 start-instances --instance-ids INSTANCE_ID -->

And here is an example of how to stop an EC2 instance using the awscli:

<!-- aws ec2 stop-instances --instance-ids INSTANCE_ID -->

=========================================================================================================================================

Terraform to deploy to a docker server 
----------------------------------------

To deploy a Docker container to an EC2 instance using Terraform, you can use the aws_ecs_task_definition, aws_ecs_service, and aws_ecs_cluster resources.

Here is an example of how you can use these resources to deploy a Docker container to an EC2 instance running Amazon Elastic Container Service (ECS):

# Create a task definition for the Docker container
resource "aws_ecs_task_definition" "example" {
  family                   = "example"
  execution_role_arn       = "arn:aws:iam::ACCOUNT_ID:role/ecsTaskExecutionRole"
  network_mode             = "awsvpc"
  requires_compatibilities = ["FARGATE"]
  memory                   = "256"
  cpu                      = "256"

  container_definitions = <<EOF
[
  {
    "name": "example",
    "image": "nginx:latest",
    "portMappings": [
      {
        "containerPort": 80,
        "hostPort": 80
      }
    ]
  }
]
EOF
}

# Create an ECS cluster
resource "aws_ecs_cluster" "example" {
  name = "example"
}

# Create an ECS service to run the task on the cluster
resource "aws_ecs_service" "example" {
  name            = "example"
  cluster         = aws_ecs_cluster.example.id
  task_definition = aws_ecs_task_definition.example.arn
  desired_count   = 1
  launch_type     = "FARGATE"

  network_configuration {
    security_groups = [aws_security_group.ecs.id]
    subnets         = [aws_subnet.ecs.*.id]
  }
}

==========================================================================================================================================

This example creates a task definition for a Docker container running Nginx, a cluster to run the task on, and a service to deploy the task to the cluster. The task is configured to run on Fargate, which is a serverless compute engine for Amazon ECS that allows you to run containers without the need to manage the underlying EC2 instances.

You will need to replace ACCOUNT_ID with your own AWS account ID and configure the security_groups and subnets to match your VPC and security group settings.

I hope this helps! Let me know if you have any questions or need further assistance.






