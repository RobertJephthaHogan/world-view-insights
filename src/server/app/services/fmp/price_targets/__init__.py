import requests
from app.config import Settings


fmp_key = Settings().FMP_API_KEY

class PriceTargets:

    async def getPriceTarget(symbol):
        url = f'https://financialmodelingprep.com/api/v4/price-target?symbol={symbol}&apikey={fmp_key}'
        return requests.get(url)

    async def getPriceTargetSummary(symbol):
        url = f'https://financialmodelingprep.com/api/v4/price-target-summary?symbol={symbol}&apikey={fmp_key}'
        return requests.get(url)
    
    async def getPriceTargetByAnalystName(name):
        url = f'https://financialmodelingprep.com/api/v4/price-target-analyst-name?name={name}&apikey={fmp_key}'
        return requests.get(url)
    
    async def getPriceTargetByAnalystCompany(company):
        url = f'https://financialmodelingprep.com/api/v4/price-target-analyst-company?name={company}&apikey={fmp_key}'
        return requests.get(url)

    async def getPriceTargetConsensus(symbol):
        url = f'https://financialmodelingprep.com/api/v4/price-target-consensus?symbol={symbol}&apikey={fmp_key}'
        return requests.get(url)