from typing import Any, Dict, Optional, Union
from beanie import Document
from fastapi.security import HTTPBasicCredentials
from pydantic import BaseModel, EmailStr, Field


class User(Document):
    id: Optional[str] = Field(...)
    firstName: str = Field(...)
    lastOrBusinessName: str = Field(...)
    email: EmailStr = Field(...)
    password: str = Field(...)
    role: str = Field(...)

    class Settings:
        name = "User"

    class Config:
        json_schema_extra = {
            "example": {
                "id": "6276c8a63de1b5229336df5c",
                "firstName": "John",
                "lastOrBusinessName": "Doe",
                "email": "johndoe@gmail.com",
                "password": "password123",
                "role": "user"
            }
        }


class UserSignIn(HTTPBasicCredentials):
    class Config:
        json_schema_extra = {
            "example": {
                "username": "user@user.dev",
                "password": "password"
            }
        }


class UserData(BaseModel):
    id: Optional[str] 
    firstName: str = Field(...)
    lastOrBusinessName: str = Field(...)
    email: EmailStr = Field(...)
    password: str = Field(...)
    role: str = Field(...)

    class Config:
        json_schema_extra = {
            "example": {
                "id": "6276c8a63de1b5229336df5c",
                "firstName": "John",
                "lastOrBusinessName": "Doe",
                "email": "johndoe@gmail.com",
                "password": "password123",
                "role": "user"
            }
        }


class UpdateUserModel(BaseModel):
    id: Optional[str]
    firstName: Optional[str]
    lastOrBusinessName: Optional[str]
    receiveToEmail: Optional[EmailStr]
    receiveToPhone: Optional[str]
    sendFromEmailAddresses: Optional[list]
    sendFromPhoneNumbers: Optional[list]
    twilioCredentials: Optional[Union[str, Dict[Any, Any]]]
    password: Optional[str]
    role: Optional[str]

    class Config:
        json_schema_extra = {
            "example": {
                "id": "6276c8a63de1b5229336df5c",
                "firstName": "John",
                "lastOrBusinessName": "Doe",
                "receiveToEmail": "John@user.dev",
                "receiveToPhone": "4042222222",
                "sendFromEmailAddresses": [],
                "sendFromPhoneNumbers": [],
                "twilioCredentials": {},
                "password": "password",
                "role": "user"
            }
        }

