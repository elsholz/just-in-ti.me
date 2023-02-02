import json
import auth
import database
from jsonschema import validate, ValidationError
import schemas


def lambda_handler(event, context):
    try:
        try:
            userid = auth.check_auth(event)
        except Exception as e:
            print(e)
            return {
                "statusCode": 401,
                "body": "Not Authorized"
            }

        print(event)
        method = event['httpMethod']

        if method == 'GET':
            try:
                userdata = database.userdata_collection.find_one({
                    '_id': userid
                })
            except Exception as e:
                print(e)
                try:
                    userdata = {
                        "_id": userid,
                        "hours": {}
                    }
                    database.userdata_collection.insert_one(userdata)
                    return {
                        "statusCode": 200,
                        "body": json.dumps(userdata, ensure_ascii=False, indent=4),
                    }
                except Exception as e:
                    print(e)
                    return {"statusCode": 500, "body": "Internal Server Error"}
        elif method == 'PATCH':
            try:
                data = json.loads(event.get('body', None))
                try:
                    validate(instance=data, schema=schemas.patch_request_schema)

                    year, month, day = data['year'], data['month'], data['day']
                    hours = data['hours']

                    database.userdata_collection.update_one({
                        "_id": userid,
                    }, {
                        "$set": {
                            f'{year}.{str(month).zfill(2)}.{str(day).zfill(2)}': hours
                        }
                        # f'{year}': {
                        #     f'{month}': {
                        #         f'{day}': hours
                        #     }
                        # }
                    }, {
                        "upsert": True
                    })

                    return {
                        "statusCode": 200,
                        "body": "OK"
                    }
                except ValidationError as e:
                    print(e)
                    return {
                        "statusCode": 401,
                        "body": ""
                    }
                except Exception as e:
                    print(e)
                    return {
                        "statusCode": 500,
                        "body": ""
                    }
            except Exception as e:
                print(e)
                return {
                    "statusCode": 401,
                    "body": ""
                }

        elif method == 'DELETE':
            pass
        else:
            print("Invalid Method:", method)
            return {
                "statusCode": 501,
                "body": json.dumps({
                    "message": "Method not implemented",
                }),
            }

    except Exception as e:
        print(e)
        return {
            "statusCode": 500,
            "body": json.dumps({
                "message": "Internal Server Error",
            }),
        }
