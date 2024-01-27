import requests
from app.config import Settings


fmp_key = Settings().FMP_API_KEY

class StockPrices:

    async def get_company_quote(symbol):
        url = f'https://financialmodelingprep.com/api/v3/quote/{symbol}?apikey={fmp_key}'
        return requests.get(url)

    async def get_company_stock_price_change(symbol):
        url = f'https://financialmodelingprep.com/api/v3/stock-price-change/{symbol}?apikey={fmp_key}'
        return requests.get(url)

    async def get_company_one_minute_candles(symbol):
        url = f'https://financialmodelingprep.com/api/v3/historical-chart/1min/{symbol}?apikey={fmp_key}'
        return requests.get(url)

    async def get_company_five_minute_candles(symbol):
        url = f'https://financialmodelingprep.com/api/v3/historical-chart/5min/{symbol}?apikey={fmp_key}'
        return requests.get(url)

    async def get_company_fifteen_minute_candles(symbol):
        url = f'https://financialmodelingprep.com/api/v3/historical-chart/15min/{symbol}?apikey={fmp_key}'
        return requests.get(url)

    async def get_company_thirty_minute_candles(symbol):
        url = f'https://financialmodelingprep.com/api/v3/historical-chart/30min/{symbol}?apikey={fmp_key}'
        return requests.get(url)

    async def get_company_one_hour_candles(symbol):
        url = f'https://financialmodelingprep.com/api/v3/historical-chart/1hour/{symbol}?apikey={fmp_key}'
        return requests.get(url)

    async def get_company_four_hour_candles(symbol):
        url = f'https://financialmodelingprep.com/api/v3/historical-chart/4hour/{symbol}?apikey={fmp_key}'
        return requests.get(url)

    async def get_company_historical_daily_prices(symbol):
        url = f'https://financialmodelingprep.com/api/v3/historical-price-full/{symbol}?apikey={fmp_key}'
        return requests.get(url)
