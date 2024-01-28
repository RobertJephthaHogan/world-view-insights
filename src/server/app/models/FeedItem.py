import datetime
from typing import List, Optional, Any, Union
from beanie import Document
from pydantic import BaseModel, EmailStr, Field


class FeedItem(Document):
    id: Optional[str] = Field(...)
    title: str = Field(...)
    description: str = Field(...)
    link: str = Field(...)
    publicationDate: Union[str, datetime.datetime] = Field(...)
    authors: List = Field(...)
    guid: Optional[str] = Field(...)
    systemId: Optional[str] = Field(...)
    
    class Settings:
        name = "FeedItem"

    class Config:
        json_schema_extra = {
            "example": {
                "id": "6382e2abc07256ef099af572",
                "title": "Feed item title",
                "description": "description",
                "link": "https://example.com",
                "publicationDate": "https://example.com",
                "authors": "John Doe",
                "guid": "articleId123",
                "systemId": "articleId123",
            }
        }


class UpdateFeedItemModel(BaseModel):
    id: Optional[str]
    title: Optional[str]
    description: Optional[str]
    link: Optional[str]
    publicationDate: Optional[Union[str, datetime.datetime]]
    authors: Optional[List]
    guid: Optional[str]
    systemId: Optional[str]

    class Config:
        json_schema_extra = {
            "example": {
                "id": "6382e2abc07256ef099af572",
                "title": "Feed item title",
                "description": "description",
                "link": "https://example.com",
                "publicationDate": "https://example.com",
                "authors": "John Doe",
                "guid": "articleId123",
                "systemId": "articleId123",
            }
        }

