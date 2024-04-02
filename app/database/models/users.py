from pydantic import BaseModel, validator, Field
from typing import Optional
from enum import Enum
from datetime import datetime, date
from dataclasses import asdict
from typing import Union
import bcrypt


class Gender(str, Enum):
    MALE = "male"
    FEMALE = "female"
    OTHER = "other"


class User(BaseModel):
    firstName: str = Field(...)
    middleName: Optional[str] = None
    lastName: str = Field(...)
    emailId: str = Field(...)
    phoneNumber: str = Field(...)
    dob: str = Field(...)
    gender: Gender = Field(...)
    password: str = Field(...)

    class Config:
        populate_by_name = True
        json_schema_extra = {
            "example": {
                "firstName": "John",
                "middleName": "Doe",
                "lastName": "Smith",
                "emailId": "johnsmith@gmail.com",
                "phoneNumber": "1234567890",
                "dob": "01-01-2000",
                "gender": "male",
                "password": "Password123",
            }
        }

    @validator("firstName", "middleName", "lastName")
    def validate_first_name(cls, first_name):
        if not first_name.isalpha():
            raise ValueError("First name must contain only alphabets")
        return first_name

    @validator("phoneNumber")
    def validate_phone_number(cls, phone_number):
        if not phone_number.isdigit():
            raise ValueError("Phone number must contain only digits")
        if len(phone_number) != 10:
            raise ValueError("Phone number must be 10 digits long")
        return phone_number

    @validator("emailId", always=True)
    def validate_email_id(cls, email_id):
        if "@" not in email_id:
            raise ValueError("Invalid email format")
        return email_id.lower()

    @validator("dob")
    def validate_dob(cls, dob):
        try:
            validated_dob = datetime.strptime(dob, "%d-%m-%Y")
        except ValueError:
            raise ValueError("Invalid date format. Please use DD-MM-YYYY format.")
        return validated_dob

    @validator('password')
    def validate_password(cls, password):
        if len(password) < 8:
            raise ValueError("Password must be at least 8 characters long")
        hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        return hashed_password


class Login(BaseModel):
    emailId: str = Field(...)
    password: str = Field(...)

    class Config:
        populate_by_name = True
        json_schema_extra = {
            "example": {"emailId": "johnsmith@gmail.com", "password": "Password123"}
        }
    
    @validator("emailId", always=True)
    def validate_email_id(cls, email_id):
        if "@" not in email_id:
            raise ValueError("Invalid email format")
        return email_id.lower()