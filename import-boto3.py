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
