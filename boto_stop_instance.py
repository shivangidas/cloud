import boto3
import sys
ec2 = boto3.client('ec2')
response = ec2.stop_instances(InstanceIds=[sys.argv[1]])
print(response)

# response = client.stop_instances(
#     InstanceIds=[
#         'string',
#     ],
#     Hibernate=True | False,
#     DryRun=True | False,
#     Force=True | False
# )
