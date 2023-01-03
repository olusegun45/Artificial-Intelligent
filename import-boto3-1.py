# Write a lambda step function to shut down a server
# Here is an example of a AWS Lambda function written in Python that can be used as a step in an AWS Step Functions state machine to shut down a server:

import boto3

def shutdown_server(event, context):
    # Replace "instance_id" with the ID of the instance you want to shut down
    instance_id = "instance_id"
    
    # Get the EC2 client
    ec2 = boto3.client("ec2")
    
    # Use the EC2 client to stop the instance
    ec2.stop_instances(InstanceIds=[instance_id])
    
    # Return the instance ID
    return {"instance_id": instance_id}

# This function stops an EC2 instance with the specified instance_id. You will need to replace instance_id with the actual ID of the instance you want to shut down.

# You can then use this function in an AWS Step Functions state machine by creating a task state that invokes the function using the AWS::Lambda::Function resource.

# For example:

{
  "StartAt": "ShutdownServer",
  "States": {
    "ShutdownServer": {
      "Type": "Task",
      "Resource": "arn:aws:lambda:REGION:ACCOUNT_ID:function:shutdown_server",
      "End": true
    }
  }
}

# This state machine will start at the ShutdownServer state, which invokes 
# the shutdown_server function using the specified ARN. The state machine will then terminate 
# after the function has been invoked.