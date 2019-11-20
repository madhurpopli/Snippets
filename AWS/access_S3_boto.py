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
