import boto3
from botocore.exceptions import NoCredentialsError
from sirokuma.destination import Destination
import tempfile
import gzip
import os
from datetime import datetime

class S3Bucket(Destination):
    def __init__(self, region_name, bucket_name, compress=False):
        self.bucket_name = bucket_name
        self.s3_client = boto3.client('s3', region_name=region_name)
        self.compress = compress

    def upload_file(self, file_name, object_name=None):
        if object_name is None:
            object_name = file_name
        try:
            self.s3_client.upload_file(file_name, self.bucket_name, object_name)
            print(f"File {file_name} uploaded to s3://{self.bucket_name}/{object_name}.")
        except FileNotFoundError:
            print(f"The file {file_name} was not found.")
        except NoCredentialsError:
            print("Credentials not available.")

    def save(self, data: bytes):
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            if self.compress:
                with gzip.GzipFile(fileobj=temp_file, mode='wb') as gz_file:
                    gz_file.write(data)
                temp_file_path = temp_file.name
            else:
                temp_file.write(data)
                temp_file_path = temp_file.name
        
        prefix = datetime.now().strftime("%Y/%m/%d/%H/%M/")
        object_name = prefix + datetime.now().strftime("%Y%m%dT%H%M")
        if self.compress: object_name += '.gz'
        
        if os.path.exists(temp_file_path):
            self.upload_file(temp_file_path, object_name)
        else:
            print(f"The temporary file {temp_file_path} was not found.")
