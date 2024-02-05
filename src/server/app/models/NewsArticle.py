import datetime
from typing import Dict, List, Optional, Any, Union
from beanie import Document
from pydantic import BaseModel, Field


class NewsArticle(Document):
    id: Optional[str] = Field(...)
    title: str = Field(...)
    datePosted: datetime.datetime = Field(...)
    creationDate: Union[str, datetime.datetime] = Field(...)
    content: str = Field(...)
    link: str = Field(...)
    tickers: Union[str, List[ Any]] = Field(...) 
    image: str = Field(...)
    author: str = Field(...)
    category: str = Field(...)
    sourceName: str = Field(...)
    sourceLink: str = Field(...)
    
    
    class Settings:
        name = "NewsArticle"

    class Config:
        json_schema_extra = {
            "example": {
                "id": "6382e2abc07256ef099af572",
                "title": "Article Title",
                "datePosted": "2022-12-22T16:09:23.443Z",
                "creationDate": "2022-12-22T16:09:23.443Z",
                "content": "Article Content",
                "link": "link",
                "tickers": "AAPL",
                "image": "image url here",
                "author": "John Doe",
                "category": "business",
                "sourceName": "sourceName",
                "sourceLink": "sourceLink"
            }
        }


class UpdateNewsArticleModel(BaseModel):
    id: Optional[str]
    title: Optional[str]
    datePosted: Optional[datetime.datetime]
    creationDate: Optional[datetime.datetime]
    content: Optional[str]
    link: Optional[str]
    tickers: Optional[Union[str, List[ Any]]]
    image: Optional[str]
    author: Optional[str]
    category: Optional[str]
    sourceName: Optional[str]
    sourceLink: Optional[str]
        

    class Config:
        json_schema_extra = {
            "example": {
                "id": "6382e2abc07256ef099af572",
                "title": "Article Title",
                "datePosted": "2022-12-22T16:09:23.443Z",
                "creationDate": "2022-12-22T16:09:23.443Z",
                "content": "Article Content",
                "link": "link",
                "tickers": "AAPL",
                "image": "image url here",
                "author": "John Doe",
                "category": "business",
                "sourceName": "sourceName",
                "sourceLink": "sourceLink"
            }
        }

