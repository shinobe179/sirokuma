import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError
from sirokuma.source import Source


class Bucket(Source):
    def __init__(self, bucket_name, prefix):
        self.bucket_name = bucket_name
        self.s3_client = boto3.client('s3')
        self.prefix = prefix

    def read_object(self, object_key):
        try:
            response = self.s3_client.get_object(Bucket=self.bucket_name, Key=object_key)
            return response['Body'].read()
        except NoCredentialsError:
            raise Exception("AWS credentials not found.")
        except PartialCredentialsError:
            raise Exception("Incomplete AWS credentials provided.")
        except Exception as e:
            raise Exception(f"Error reading object from S3: {str(e)}")

    def crawl(self):
        try:
            objects = self.s3_client.list_objects_v2(Bucket=self.bucket_name, Prefix=self.prefix)
            if 'Contents' in objects:
                for obj in objects['Contents']:
                    object_key = obj['Key']
                    yield self.read_object(object_key)
        except Exception as e:
            raise Exception(f"Error crawling S3 bucket: {str(e)}")
