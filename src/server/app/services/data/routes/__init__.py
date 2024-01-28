import json
from fastapi import APIRouter

from app.services.data import DataService



router = APIRouter()

class DataController:
    
    # Get Market Leader Quotes (populates ticker banner component)
    @router.get("/get_market_leader_quotes/{limit}")
    async def get_market_leader_quotes(limit):
        data = await DataService.get_market_leader_quotes(limit)
        return data
    
    # Get Major Index Overview (populates index banner component)
    @router.get("/get_major_index_overview/")
    async def get_major_index_overview():
        data = await DataService.get_major_index_overview()
        return data
    
        
    # Get Notable Quotes (populates notable quote component)
    @router.get("/get_notable_quotes/")
    async def get_notable_quotes():
        data = await DataService.get_notable_quotes()
        return data

