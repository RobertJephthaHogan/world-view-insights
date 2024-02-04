import json
from fastapi import APIRouter

from app.services.data import DataService



router = APIRouter()

class DataController:
    
    # Get Market Leader Quotes (populates ticker banner component)
    @router.get("/get_market_leader_quotes/{limit}")
    async def get_market_leader_quotes(limit):
        data = await DataService.Storage.get_stored_market_leader_quotes(limit)
        return data
    
    # Get Major Index Overview (populates index banner component)
    @router.get("/get_major_index_overview/")
    async def get_major_index_overview():
        data = await DataService.Storage.get_stored_major_index_overview()
        return data
    
    # Get Notable Quotes (populates notable quote component)
    @router.get("/get_notable_quotes/")
    async def get_notable_quotes():
        data = await DataService.Storage.get_stored_notable_quotes()
        return data

    # Get Gainers Price Table (populates gainers price table component)
    @router.get("/gainers_price_table/")
    async def get_gainers_price_table():
        data = await DataService.Storage.get_stored_gainers_price_table()
        return data
    
    # Get Losers Price Table (populates losers price table component)
    @router.get("/losers_price_table/")
    async def get_losers_price_table():
        data = await DataService.Storage.get_stored_losers_price_table()
        return data

    # Get Leaders Price Table (populates leaders price table component)
    @router.get("/leaders_table/")
    async def get_leaders_price_table():
        data = await DataService.Storage.get_stored_leaders_table()
        return data
    
    # Get Leaders Price Table (populates leaders price table component)
    @router.get("/most_active_table/")
    async def get_most_active_price_table():
        data = await DataService.Storage.get_stored_most_active_table()
        return data

