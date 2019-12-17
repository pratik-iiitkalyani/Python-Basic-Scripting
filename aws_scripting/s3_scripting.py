import boto3

s3 = boto3.resource('s3')

# create s3 bucket
bucket_name = 'bucketsdmjfbfb'

try:
    response = s3.create_bucket(Bucket = bucket_name, CreateBucketConfiguration = {
        'LocationConstraint': 'us-east-2',
    })
    print(response)

except Exception as error:
    print(error)

