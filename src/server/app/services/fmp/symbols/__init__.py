import requests
from app.config import Settings


fmp_key = Settings().FMP_API_KEY

class Symbols:

    # All Companies ticker symbols available in Financial Modeling Prep
    async def getFMPSymbols():
        url = f'https://financialmodelingprep.com/api/v3/stock/list?apikey={fmp_key}'
        return requests.get(url)

    # All Tradable Symbols
    async def getFMPTradableSymbols():
        url = f'https://financialmodelingprep.com/api/v3/available-traded/list?apikey={fmp_key}'
        return requests.get(url)

    # Get ETF List
    async def getFMPETFList():
        url = f'https://financialmodelingprep.com/api/v3/etf/list?apikey={fmp_key}'
        return requests.get(url)