import json
from fastapi import APIRouter

from app.services.edgar import EdgarService 



router = APIRouter()



class EdgarController:
    
    
    # Get Recent Filings
    @router.get("/get_recent_filings/{form}")
    async def test_rss(form):
        data = await EdgarService.getRecentFilings(form, "", "")
        return data
    
    