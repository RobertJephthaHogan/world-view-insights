import requests
from app.config import Settings


fmp_key = Settings().FMP_API_KEY

class CompanyData:

    # Get Shares Float
    def get_shares_float(ticker):
        url = f'https://financialmodelingprep.com/api/v4/shares_float?symbol={ticker}&apikey={fmp_key}'
        return requests.get(url)

    # Get Stock Peers
    def get_stock_peers(ticker):
        url = f'https://financialmodelingprep.com/api/v4/stock_peers?symbol={ticker}&apikey={fmp_key}'
        return requests.get(url)

    # Get Core Company Information
    def get_core_company_information(ticker):
        url = f'https://financialmodelingprep.com/api/v4/company-core-information?symbol={ticker}&apikey={fmp_key}'
        return requests.get(url)
    
    # Get Company Outlook
    async def get_company_outlook(ticker):
        url = f'https://financialmodelingprep.com/api/v4/company-outlook?symbol={ticker}&apikey={fmp_key}'
        return requests.get(url)
    
    # Stock Screener
    # def stock_screener():
    #     url = f'https://financialmodelingprep.com/api/v3/stock-screener?apikey={fmp_key}'
    #     return requests.get(url)
    
    # Dynamic Stock Screener
    # Takes a params dict and adds them as query params to the request
    def stock_screener(params):        
        url = f"https://financialmodelingprep.com/api/v3/stock-screener?{'&'.join(f'{key}={value}' for key, value in params.items())}&apikey={fmp_key}"
        return requests.get(url)
