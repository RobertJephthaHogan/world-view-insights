import requests
from app.config import Settings


fmp_key = Settings().FMP_API_KEY

class StockPrices:

    async def getCompanyQuote(symbol):
        url = f'https://financialmodelingprep.com/api/v3/quote/{symbol}?apikey={fmp_key}'
        return requests.get(url)

    async def getCompanyStockPriceChange(symbol):
        url = f'https://financialmodelingprep.com/api/v3/stock-price-change/{symbol}?apikey={fmp_key}'
        return requests.get(url)

    async def getCompanyOneMinuteCandles(symbol):
        url = f'https://financialmodelingprep.com/api/v3/historical-chart/1min/{symbol}?apikey={fmp_key}'
        return requests.get(url)

    async def getCompanyFiveMinuteCandles(symbol):
        url = f'https://financialmodelingprep.com/api/v3/historical-chart/5min/{symbol}?apikey={fmp_key}'
        return requests.get(url)

    async def getCompanyFifteenMinuteCandles(symbol):
        url = f'https://financialmodelingprep.com/api/v3/historical-chart/15min/{symbol}?apikey={fmp_key}'
        return requests.get(url)

    async def getCompanyThirtyMinuteCandles(symbol):
        url = f'https://financialmodelingprep.com/api/v3/historical-chart/30min/{symbol}?apikey={fmp_key}'
        return requests.get(url)

    async def getCompanyOneHourCandles(symbol):
        url = f'https://financialmodelingprep.com/api/v3/historical-chart/1hour/{symbol}?apikey={fmp_key}'
        return requests.get(url)

    async def getCompanyFourHourCandles(symbol):
        url = f'https://financialmodelingprep.com/api/v3/historical-chart/4hour/{symbol}?apikey={fmp_key}'
        return requests.get(url)

    async def getCompanyHistoricalDailyPrices(symbol):
        url = f'https://financialmodelingprep.com/api/v3/historical-price-full/{symbol}?apikey={fmp_key}'
        return requests.get(url)