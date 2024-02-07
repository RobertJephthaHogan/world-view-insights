import json
from fastapi import APIRouter

from app.services.collector import CollectorService as Collector
from .. import StockDataService



router = APIRouter()

class StockDataController:
    
    
    @router.get("/get_stock_page_data/{ticker}")
    async def get_stock_page_data(ticker):
        data = await StockDataService.get_stock_page_data_by_ticker(ticker)
        return data