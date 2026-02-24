import json

from src.schemas.car_rental_schema import CarRentalSchema
import boto3
from datetime import datetime


class CarRental:

    def __init__(self):
        self.body = None

    def read(self, data):
        self.body = data
        # Validation
        CarRentalSchema(**self.body)



    def transform(self):
        pass

    def load(self):
        data = self.body
        s3 = boto3.client('s3')
        s3.put_object(
            Bucket="batch89-etl",
            Key=f"org-1/2026/{datetime.now().strftime('%Y%m%d_%H%M%S')}.json",
            Body=json.dumps(data),
            ContentType='application/json'
        )

