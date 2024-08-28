import os
bucket_name="gemstone.artifacts.bucket"
artifact_folder="./artifacts"

os.system(f"aws s3 sync {artifact_folder} s3://{bucket_name}/artifact")