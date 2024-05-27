import boto3

myec2 = boto3.resource(
    "ec2",
    region_name="ap-south-1",
    aws_access_key_id="AKIA2HLBVAZKY3KK6AVU",
    aws_secret_access_key="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"
)

def osLaunch():
    myec2.create_instances(
        InstanceType="t2.micro",
        ImageId="ami-0cc9838aa7ab1dce7",
        MaxCount=1,
        MinCount=1
    )

# Call the function to launch the EC2 instance
osLaunch()

