import boto3

# # Let's use Amazon S3
# s3 = boto3.resource('s3')
# # Print out bucket names
# for bucket in s3.buckets.all():
#     print(bucket.name)

# Get the service resource
sqs = boto3.resource('sqs')

# Create the queue. This returns an SQS.Queue instance
#queue = sqs.create_queue(QueueName='test', Attributes={'DelaySeconds': '5'})

# You can now access identifiers and attributes
# print(queue.url)
# print(queue.attributes.get('DelaySeconds'))

# Get the queue. This returns an SQS.Queue instance
queue = sqs.get_queue_by_name(QueueName='test')
# You can now access identifiers and attributes
print(queue.url)
print(queue.attributes.get('DelaySeconds'))
# Print out each queue name, which is part of its ARN
# for queue in sqs.queues.all():
#     print(queue.url)


# Create a new message
response = queue.send_message(MessageBody='world')

# The response is NOT a resource, but gives you a message ID and MD5
print(response.get('MessageId'))
print(response.get('MD5OfMessageBody'))
queue.delete()
print("Finished")
