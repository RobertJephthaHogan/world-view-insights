import requests
from app.config import Settings


fmp_key = Settings().FMP_API_KEY

class MarketPerformance:

    # Get Sector PE Ratios
    async def getSectorPERatios(symbol):
        url = f'https://financialmodelingprep.com/api/v4/sector_price_earnings_ratio?apikey={fmp_key}'
        return requests.get(url)

    # Get Industry PE Ratios
    async def getIndustriesPERatios(symbol):
        url = f'https://financialmodelingprep.com/api/v4/industry_price_earnings_ratio?apikey={fmp_key}'
        return requests.get(url)

    # Get Stock Market Sector Performance
    # async def getIndustriesPERatios(symbol):
    #     url = f'https://financialmodelingprep.com/api/v4/industry_price_earnings_ratio?apikey={fmp_key}'
    #     return requests.get(url)

    # Get Largest Gainers
    async def getLargestGainers():
        url = f'https://financialmodelingprep.com/api/v3/stock_market/gainers?apikey={fmp_key}'
        return requests.get(url)

    # Get Largest Losers
    async def getLargestLosers():
        url = f'https://financialmodelingprep.com/api/v3/stock_market/losers?apikey={fmp_key}'
        return requests.get(url)

    # Get Most Active
    async def getMostActive():
        url = f'https://financialmodelingprep.com/api/v3/stock_market/actives?apikey={fmp_key}'
        return requests.get(url)