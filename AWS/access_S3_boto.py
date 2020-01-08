import pandas as pd
import boto3

bucket = "prod-search-ranking-ml"
file_name = "data.csv"
import boto3
session = boto3.Session(
    aws_access_key_id=<your key here>,
    aws_secret_access_key=<your key here>,
)

s3 = session.client('s3')
print(s3)

# 's3' is a key word. create connection to S3 using default config and all buckets within S3

obj = s3.get_object(Bucket= bucket, Key= file_name) 
# get object and file (key) from bucket

initial_df = pd.read_csv(obj['Body'])


def downloadDirectoryFroms3(bucketName,remoteDirectoryName):
    s3_resource = session.resource('s3')
    bucket = s3_resource.Bucket(bucketName) 
    for object in bucket.objects.filter(Prefix = remoteDirectoryName):
        if not os.path.exists(os.path.dirname(object.key)):
            os.makedirs(os.path.dirname(object.key))
        bucket.download_file(object.key,object.key)
