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
    
    # Stock Screener
    def stock_screener(ticker):
        url = f'https://financialmodelingprep.com/api/v3/stock-screener?apikey={fmp_key}'
        return requests.get(url)
