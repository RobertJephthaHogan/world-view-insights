import datetime
from typing import Dict, Optional, Any, Union
from beanie import Document
from pydantic import BaseModel, Field


class Tweet(Document):
    id: Optional[str] = Field(...)
    title: Optional[str] = Field(...)
    type: Optional[str] = Field(...)
    content: Optional[str] = Field(...)
    time: Optional[datetime.datetime] = Field(...)
    
    
    class Settings:
        name = "Tweet"

    class Config:
        json_schema_extra = {
            "example": {
                "id": "6382e2abc07256ef099af572",
                "title": 'Form Four Notification Tweet',
                "type": 'form-four-filing',
                "content": "Insider XYZ sold 123 shares at x price...",
                "time": "2022-12-22T16:09:23.443Z",
            }
        }


class UpdateTweetModel(BaseModel):
    id: Optional[str]
    title: Optional[str] 
    type: Optional[str] 
    content: Optional[str]
    time: Optional[datetime.datetime]

    class Config:
        json_schema_extra = {
            "example": {
                "id": "6382e2abc07256ef099af572",
                "title": 'Form Four Notification Tweet',
                "type": 'form-four-filing',
                "content": "Insider XYZ sold 123 shares at x price...",
                "time": "2022-12-22T16:09:23.443Z",
            }
        }

