import json

# import requests


def lambda_handler(event, context):

    print(event)
    data = json.loads(event['Records'][0]['body'])

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world",
            # "location": ip.text.replace("\n", "")
        }),
    }
