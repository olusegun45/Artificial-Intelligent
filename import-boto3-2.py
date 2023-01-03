# Write a python to deny access to s3 bucket 
# To deny access to an Amazon S3 bucket, you can use the Deny method of the s3.BucketPolicy class in the boto3 library.

# Here is an example Python script that denies access to an S3 bucket for an AWS account with the ID 123456789012:

import boto3

# Set the name of the S3 bucket and the AWS account ID
bucket_name = 'my-bucket'
account_id = '123456789012'

# Create an S3 client
s3 = boto3.client('s3')

# Create the bucket policy
policy = {
    'Version': '2012-10-17',
    'Statement': [{
        'Sid': 'DenyAccountAccess',
        'Action': 's3:*',
        'Effect': 'Deny',
        'Resource': f's3://{bucket_name}/*',
        'Principal': {
            'AWS': f'arn:aws:iam::{account_id}:root'
        }
    }]
}

# Set the bucket policy
s3.put_bucket_policy(Bucket=bucket_name, Policy=json.dumps(policy))

# This script creates a bucket policy that denies all actions ('Action': 's3:*') for the 
# specified AWS account ('Principal': { 'AWS': f'arn:aws:iam::{account_id}:root' }) on 
# all objects in the bucket ('Resource': f's3://{bucket_name}/*').

# Note that this script assumes that the AWS credentials used to run the script have the 
# necessary permissions to set the bucket policy.