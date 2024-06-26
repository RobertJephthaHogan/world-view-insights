import datetime
from typing import Dict, List, Optional, Any, Union
from beanie import Document
from pydantic import BaseModel, EmailStr, Field


class NotableQuotesSnapshot(Document):
    id: Optional[str] = Field(...)
    data: Dict[Any, Any] = Field(...)
    creationDate: Union[str, datetime.datetime] = Field(...)
    
    class Settings:
        name = "NotableQuotesSnapshot"

    class Config:
        json_schema_extra = {
            "example": {
                "id": "6382e2abc07256ef099af572",
                "data": {},
                "creationDate": "",
            }
        }


class UpdateNotableQuotesSnapshotModel(BaseModel):
    id: Optional[str]
    title: Optional[Dict[Any, Any]]
    creationDate: Optional[Union[str, datetime.datetime]]

    class Config:
        json_schema_extra = {
            "example": {
                "id": "6382e2abc07256ef099af572",
                "data": {},
                "creationDate": "",
            }
        }

