import json
from fastapi import APIRouter

from app.services.price_history import PriceHistoryService 



router = APIRouter()

class PriceHistoryController:
    
    # Get Price History For a Stock
    @router.get("/get_stock_price_history/{symbol}")
    async def test_rss(symbol):
        data = await PriceHistoryService.get_stock_price_history(symbol)
        return data.json()