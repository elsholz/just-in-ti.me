import json
import auth
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

get_secret_value_response = client.get_secret_value(
    SecretId=secret_name
)['SecretString']

print('Secret String:', get_secret_value_response)

DB_USER = get_secret_value_response['DB_USER']
DB_PASSWORD = get_secret_value_response['DB_PASSWORD']

client = MongoClient(
    f"mongodb+srv://{DB_USER}:{DB_PASSWORD}@cluster0.mtoqrjz.mongodb.net/just-in-time"
)

print(client)


def lambda_handler(event, context):
    """Sample pure Lambda function

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """

    print('Check Auth returned:', auth.check_auth(event))
    userid = auth.check_auth(event)

    db = client['just-in-time']
    print("Getting Items from DB")
    for user in db.userdata.find():
        print(user)
    print("End Items from DB")

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Ja moin",
        }),
    }
