from pymongo import MongoClient

import boto3
from botocore.exceptions import ClientError


secret_name = "JITKeys"
region_name = "eu-central-1"

session = boto3.session.Session()
client = session.client(
    service_name='secretsmanager',
    region_name=region_name,
)

get_secret_value_response = json.loads(client.get_secret_value(
    SecretId=secret_name
)['SecretString'])

DB_USER = get_secret_value_response['DB_USER']
DB_PASSWORD = get_secret_value_response['DB_PASSWORD']

client = MongoClient(
    f"mongodb+srv://{DB_USER}:{DB_PASSWORD}@cluster0.mtoqrjz.mongodb.net/just-in-time"
)
db = client['just-in-time']
userdata_collection = db.userdata
