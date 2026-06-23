# core/discovery.py
import boto3

def get_resources():
    """Returns a dictionary of discovered AWS resources."""
    s3 = boto3.client('s3')
    ec2 = boto3.client('ec2')
    
    return {
        "s3_buckets": [b['Name'] for b in s3.list_buckets().get('Buckets', [])],
        "ec2_instances": [i['InstanceId'] for r in ec2.describe_instances().get('Reservations', []) for i in r['Instances']]
    }