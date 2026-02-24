from pydantic import BaseModel, field_validator
from typing import List


class CarRentalVehicle(BaseModel):
    vehicle_id: int
    make: str
    model: str
    year: int
    license_plate: str
    status: str

    @field_validator("status")
    @classmethod
    def check_availablity(cls, value):
        if value.lower() not in ["available", "unavailable"]:
            raise ValueError("status shold be a valid one")
        return value

    @field_validator("year")
    @classmethod
    def check_year(cls, value):
        if value >= 1990 and value <= 2026:
            return value
        else:
            raise  ValueError("Year should be betrween dvkndsknv")


class CarRentalBody(BaseModel):
    vehicles: List[CarRentalVehicle]


class CarRentalHeader(BaseModel):
    eventName: str
    publisher: str
    organizationId: str
    source: str
    timestamp: str


class CarRentalSchema(BaseModel):
    header: CarRentalHeader
    body: CarRentalBody

