import json
from fastapi import APIRouter

from .. import NewsService



router = APIRouter()

class NewsServiceController:
    
    
    # Get Article By Id
    @router.get("/get_article_by_id/{id}")
    async def get_business_news_articles(id):
        data = await NewsService.get_article_by_id(id)
        print('data', data)
        return data
    
    
    # Fetch Business News Articles from sources
    @router.get("/get_business_news_articles/{limit}")
    async def get_business_news_articles(limit):
        data = await NewsService.Storage.get_stored_business_news_articles(limit)
        return data
    