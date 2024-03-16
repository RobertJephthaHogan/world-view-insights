import requests
from app.config import Settings


fmp_key = Settings().FMP_API_KEY

class Symbols:

    # All Companies ticker symbols available in Financial Modeling Prep
    async def get_fmp_symbols():
        url = f'https://financialmodelingprep.com/api/v3/stock/list?apikey={fmp_key}'
        return requests.get(url)

    # All Tradable Symbols
    async def get_fmp_tradable_symbols():
        url = f'https://financialmodelingprep.com/api/v3/available-traded/list?apikey={fmp_key}'
        return requests.get(url)

    # Get ETF List
    async def get_fmp_etf_list():
        url = f'https://financialmodelingprep.com/api/v3/etf/list?apikey={fmp_key}'
        return requests.get(url)
