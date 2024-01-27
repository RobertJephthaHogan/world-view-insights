import requests
from app.config import Settings


fmp_key = Settings().FMP_API_KEY

class Economics:

    # Market Risk Premium for each country
    async def get_market_risk_premium_for_all_countries():
        url = f'https://financialmodelingprep.com/api/v4/market_risk_premium?apikey={fmp_key}'
        return requests.get(url)
