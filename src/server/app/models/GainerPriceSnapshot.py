import datetime
from typing import Dict, List, Optional, Any, Union
from beanie import Document
from pydantic import BaseModel, EmailStr, Field


class GainerPriceSnapshot(Document):
    id: Optional[str] = Field(...)
    data: List[Any] = Field(...)
    creationDate: Union[str, datetime.datetime] = Field(...)
    
    class Settings:
        name = "GainerPriceSnapshot"

    class Config:
        json_schema_extra = {
            "example": {
                "id": "6382e2abc07256ef099af572",
                "data": [],
                "creationDate": "",
            }
        }


class UpdateGainerPriceSnapshotModel(BaseModel):
    id: Optional[str]
    title: Optional[List[Any]]
    creationDate: Optional[Union[str, datetime.datetime]]

    class Config:
        json_schema_extra = {
            "example": {
                "id": "6382e2abc07256ef099af572",
                "data": [],
                "creationDate": "",
            }
        }

