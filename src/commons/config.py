import json
import os

# from dotenv import load_dotenv

# load .env file
# from pathlib import Path
#
# # get project root directory
# BASE_DIR = Path(__file__).resolve().parent.parent
#
# # construct env file path
# env_path = BASE_DIR / ".loca-variable-env"

# load env file
# load_dotenv(".loca-variable-env")

# Use this code snippet in your app.
# If you need more information about configurations
# or implementing the sample code, visit the AWS docs:
# https://aws.amazon.com/developer/language/python/

import boto3
from botocore.exceptions import ClientError


def get_secret():

    secret_name = "dev/mysql-details"
    region_name = "us-west-2"

    # Create a Secrets Manager client
    session = boto3.session.Session()
    client = session.client(service_name="secretsmanager", region_name=region_name)

    try:
        get_secret_value_response = client.get_secret_value(SecretId=secret_name)
    except ClientError as e:
        # For a list of exceptions thrown, see
        # https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetSecretValue.html
        raise e

    secret = get_secret_value_response["SecretString"]
    return json.loads(secret)
    # Your code goes here.


result = get_secret()
print(result)

ENV = os.getenv("APP_ENV", "dev")
if ENV == "dev":
    user = result.get("DB_NAME")
    password = result.get("DB_PASSWORD")
    host = result.get("DB_HOST")
    port = result.get("DB_PORT", 3306)
    schema = result.get("schema")


BUCKET = "batch89-etl"
KEY = "org-1/2026"


DEBUG = "true"

DB_USER = user
DB_PASSWORD = password
DB_HOST = host
DB_PORT = port

AWS_REGION = "ap-south-1"
SQS_QUEUE_URL = "https://sqs.ap-south-1.amazonaws.com/123/queue"

if __name__ == "__main__":
    print("Server: ", ENV)
    print("DB_NAME: ", DB_USER)
    print("DB_PASSWORD: ", DB_PASSWORD)
    print("DB_HOST: ", DB_HOST)
    print("DB_PORT: ", DB_PORT)
