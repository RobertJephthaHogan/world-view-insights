import requests
from app.config import Settings


fmp_key = Settings().FMP_API_KEY

class FundHoldings:

    # Get ETF Constituents
    async def get_etf_constituents(etf_symbol):
        url = f'https://financialmodelingprep.com/api/v3/etf-holder/{etf_symbol}?apikey={fmp_key}'
        return requests.get(url)

    # Get ETF Expense Ratio
    async def get_etf_expense_ratio(etf_symbol):
        url = f'https://financialmodelingprep.com/api/v4/etf-info?symbol={etf_symbol}?apikey={fmp_key}'
        return requests.get(url)

    # Get Institutional Holders Of A Company
    async def get_institutional_holders_of_a_company(symbol):
        url = f'https://financialmodelingprep.com/api/v3/institutional-holder/{symbol}?apikey={fmp_key}'
        return requests.get(url)

    # Get Mutual Fund Holders Of A Company
    async def get_mutual_fund_holders_of_a_company(symbol):
        url = f'https://financialmodelingprep.com/api/v3/mutual-fund-holder/{symbol}?apikey={fmp_key}'
        return requests.get(url)

    # Get ETF Sector Weightings
    async def get_etf_sector_weightings(etf_symbol):
        url = f'https://financialmodelingprep.com/api/v3/etf-sector-weightings/{etf_symbol}?apikey={fmp_key}'
        return requests.get(url)

    # Get ETF Country Weightings
    async def get_etf_country_weightings(etf_symbol):
        url = f'https://financialmodelingprep.com/api/v3/etf-country-weightings/{etf_symbol}?apikey={fmp_key}'
        return requests.get(url)

    # Get ETFs With Exposure To A Stock
    async def get_stock_exposure_list(symbol):
        url = f'https://financialmodelingprep.com/api/v3/etf-stock-exposure/{symbol}?apikey={fmp_key}'
        return requests.get(url)
