import json
from fastapi import APIRouter

from .. import NewsService



router = APIRouter()

class NewsServiceController:
    
    # Fetch Business News Articles from sources
    @router.get("/get_business_news_articles/")
    async def get_business_news_articles():
        data = await NewsService.get_business_news_articles()
        return data
    