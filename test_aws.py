import boto3

# This automatically loads credentials from ~/.aws/credentials
s3 = boto3.client('s3')

# Try to list your buckets
try:
    response = s3.list_buckets()
    print("Successfully connected to AWS!")
    print(f"Buckets found: {len(response['Buckets'])}")
except Exception as e:
    print(f"Connection failed: {e}")