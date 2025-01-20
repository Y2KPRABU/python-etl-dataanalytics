import os
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
import logging
import boto3
from botocore.exceptions import NoCredentialsError

# Env variables
from dotenv import load_dotenv

# Logger initialization
logging.basicConfig(format='[%(levelname)s]: %(message)s', level=logging.DEBUG)

# Recover env variables
load_dotenv()

# Replace with your details
aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID')
aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY')
bucket_name = os.getenv('BUCKET_NAME')
file_name = os.getenv('FILE_NAME')
local_file_path = os.getenv('LOCAL_FILE_PATH')

# Create a DataFrame

def createFileFromdata(pandas_dataframe):
    # Convert the DataFrame to a Parquet file
    table = pa.Table.from_pandas(pandas_dataframe)
    pq.write_table(table, local_file_path)

# Function to upload the Parquet file to S3

def upload_file_to_s3(local_file_path, bucket_name, file_name, aws_access_key_id, aws_secret_access_key):
    s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)

    try:
        s3.upload_file(local_file_path, bucket_name, file_name)
        logging.info(f"File {file_name} uploaded to S3 bucket {bucket_name}.")
    except FileNotFoundError:
        logging.error(f"The file {local_file_path} was not found.")
    except NoCredentialsError:
        logging.error("Credentials not available.")


def pushtoS3():
    upload_file_to_s3(local_file_path, bucket_name, file_name, aws_access_key_id, aws_secret_access_key)