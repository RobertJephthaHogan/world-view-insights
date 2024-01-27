import requests
from app.config import Settings


fmp_key = Settings().FMP_API_KEY

class MarketIndexes:

    # Get All Major Indexes
    async def get_all_major_indexes():
        url = f'https://financialmodelingprep.com/api/v3/quotes/index?apikey={fmp_key}'
        return requests.get(url)

    # Get All S&P 500 Companies
    async def get_all_spx_constituents():
        url = f'https://financialmodelingprep.com/api/v3/sp500_constituents?apikey={fmp_key}'
        return requests.get(url)

    # Get All Nasdaq 100 Companies
    async def get_all_ndx_constituents():
        url = f'https://financialmodelingprep.com/api/v3/nasdaq_constituents?apikey={fmp_key}'
        return requests.get(url)
