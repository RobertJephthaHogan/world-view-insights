from app.services.fmp import FmpService





class PriceHistoryService:
    
    
    async def get_stock_price_history(symbol):
        stock_price_data = await FmpService.StockPrices.get_company_one_minute_candles(symbol)
        return stock_price_data
    
    
    pass