import boto3

# Create New Instances 

ec2 = boto3.resource('ec2')

# instance = ec2.create_instances(
#     ImageId = 'ami-0dacb0c129b49f529',
#     MinCount = 1,
#     MaxCount = 1,
#     InstanceType = 't2.micro'
# )

# print(instance[0].id)

# terminate the instances

instance_id = 'i-05f46ba638fe56d21'
instance = ec2.Instance(instance_id)
response = instance.terminate()
print(response)