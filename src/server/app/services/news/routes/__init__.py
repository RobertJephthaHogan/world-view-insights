


import json
from fastapi import APIRouter
from .. import NewsService


router = APIRouter()

class NewsController:
    
    # Get Stored News Articles from FMP
    @router.get("/fmp_articles/")
    async def get_fmp_articles():
        data = await NewsService.Storage.get_stored_fmp_articles()
        return data