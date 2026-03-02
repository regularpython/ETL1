import json
from src.services.car_rental_service import CarRental


# import requests


def lambda_handler(event, context):
    print("hello this is new item")
    body = json.loads(event["Records"][0]["body"])
    car = CarRental()

    car.read(body)
    car.transform()
    car.load()
    return {
        "statusCode": 200,
        "body": json.dumps(
            {
                "message": "hello world",
                # "location": ip.text.replace("\n", "")
            }
        ),
    }
