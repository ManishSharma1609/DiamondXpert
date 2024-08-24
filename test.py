import os
import boto3
from dotenv import load_dotenv

load_dotenv()

s3 = boto3.client("s3")

bucket_name = os.getenv("BUCKET")
print(bucket_name)

path = "./artifacts/"

for root, dir, files in os.walk(path):
    for file in files:
        s3.upload_file(os.path.join(root, file), bucket_name, file) 