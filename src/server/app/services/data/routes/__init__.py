import json
from fastapi import APIRouter

from app.services.data import DataService



router = APIRouter()

class DataController:
    
    # Get Price Target
    @router.get("/get_market_leader_quotes/{limit}")
    async def get_market_leader_quotes(limit):
        data = await DataService.get_market_leader_quotes(limit)
        return data
    
    pass