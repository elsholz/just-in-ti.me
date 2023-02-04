from pymongo import MongoClient
import json
import boto3
from botocore.exceptions import ClientError
import globals


secret_name = "JITKeys"

session = boto3.session.Session()
client = session.client(
    service_name='secretsmanager',
    region_name=globals.REGION,
)

secret_value = json.loads(client.get_secret_value(
    SecretId=secret_name
)['SecretString'])

dbs_for_env = {}

for env in [globals.PROD, globals.DEV]:
    DB_USER = secret_value[f'DB_USER_{env}']
    DB_PASSWORD = secret_value[f'DB_PASSWORD_{env}']
    DB_ADDRESS = secret_value[f'DB_ADDRESS_{env}']
    DB_NAME = secret_value[f'DB_NAME_{env}']
    # 'cluster0.mtoqrjz.mongodb.net'

    client = MongoClient(
        f"mongodb+srv://{DB_USER}:{DB_PASSWORD}@{DB_ADDRESS}/{DB_NAME}?retryWrites=true&w=majority"
    )
    db = client[DB_NAME]
    dbs_for_env = {
        env: db.userdata
    }


def get_userdata_collection(env):
    assert env in [globals.PROD, globals.DEV]
    return dbs_for_env[env]
