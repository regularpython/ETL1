import os
from dotenv import load_dotenv

# load .env file
# from pathlib import Path
#
# # get project root directory
# BASE_DIR = Path(__file__).resolve().parent.parent
#
# # construct env file path
# env_path = BASE_DIR / ".loca-variable-env"

# load env file
load_dotenv(".loca-variable-env")


ENV = os.getenv("APP_ENV")
if ENV == "dev":
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    host = os.getenv("DB_HOST")
    port = os.getenv("DB_PORT", 3306)
    schema = os.getenv("schema")


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
