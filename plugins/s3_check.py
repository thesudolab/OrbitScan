import boto3

class S3Check:
    def __init__(self):
        self.name = "S3 Public Access Check"
    
    async def run(self):
        # Boto3 logic goes here
        # Return a standard format for the UI to consume
        return {"service": "S3", "status": "PASS", "info": "Bucket is private"}