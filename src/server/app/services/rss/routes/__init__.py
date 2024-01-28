import json
from fastapi import APIRouter

from app.services.rss import RssService



router = APIRouter()

class RSSController:
    
    # Get Market Leader Quotes (populates ticker banner component)
    @router.get("/test_rss/")
    async def test_rss():
        data = await RssService.ReutersRSS.get_reuters_financial_news_rss_feed()
        return data