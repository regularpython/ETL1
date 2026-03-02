import pytest
from unittest.mock import patch, MagicMock
from src.services.car_rental_service import CarRental


# ------------------------------
# Test read() - Valid Data
# ------------------------------
@patch("src.schemas.car_rental_schema.CarRentalSchema")
def test_read_valid(mock_schema):
    car = CarRental()
    data = {
        "header": {
            "eventName": "carRentalEvent",
            "publisher": "abc12345-6789-0abc-def1-23456789abcd",
            "organizationId": "Rental Event",
            "source": "my.rental.service",
            "timestamp": "timestamp",
        },
        "body": {
            "vehicles": [
                {
                    "vehicle_id": 1,
                    "make": "SQS Cloud Test",
                    "model": "Camry",
                    "year": 2022,
                    "license_plate": "ABC1234",
                    "status": "available",
                }
            ]
        },
    }

    car.read(data)

    assert car.body == data
    mock_schema.assert_called_once_with(**data)


# ------------------------------
# Test read() - Invalid Data
# ------------------------------
@patch("src.schemas.car_rental_schema.CarRentalSchema")
def test_read_invalid(mock_schema):
    car = CarRental()
    data = {"invalid": "data"}

    mock_schema.side_effect = Exception("Validation Error")

    with pytest.raises(Exception):
        car.read(data)


# ------------------------------
# Test load() - S3 Called Properly
# ------------------------------
@patch("src.services.car_rental_service.boto3.client")
def test_load_success(mock_boto_client):
    car = CarRental()
    car.body = {
        "header": {
            "eventName": "carRentalEvent",
            "publisher": "abc12345-6789-0abc-def1-23456789abcd",
            "organizationId": "Rental Event",
            "source": "my.rental.service",
            "timestamp": "timestamp",
        },
        "body": {
            "vehicles": [
                {
                    "vehicle_id": 1,
                    "make": "SQS Cloud Test",
                    "model": "Camry",
                    "year": 2022,
                    "license_plate": "ABC1234",
                    "status": "available",
                }
            ]
        },
    }

    mock_s3 = MagicMock()
    mock_boto_client.return_value = mock_s3

    car.load()

    mock_boto_client.assert_called_once_with("s3")
    mock_s3.put_object.assert_called_once()

    args, kwargs = mock_s3.put_object.call_args

    assert "Bucket" in kwargs
    assert "Key" in kwargs
    assert "Body" in kwargs
    assert kwargs["ContentType"] == "application/json"
