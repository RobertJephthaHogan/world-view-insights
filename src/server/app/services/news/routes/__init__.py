import json
from fastapi import APIRouter

from .. import NewsService



router = APIRouter()

class NewsServiceController:
    
    # Fetch Business News Articles from sources
    @router.get("/get_business_news_articles/{limit}")
    async def get_business_news_articles(limit):
        data = await NewsService.Storage.get_stored_business_news_articles(limit)
        return data
    