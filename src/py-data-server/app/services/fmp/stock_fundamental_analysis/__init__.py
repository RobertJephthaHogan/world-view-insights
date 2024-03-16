import requests
from app.config import Settings


fmp_key = Settings().FMP_API_KEY

class FmpStockFundamentalAnalysis:

    # Ratios
    async def get_company_ttm_ratios(symbol):
        url = f'https://financialmodelingprep.com/api/v3/ratios-ttm/{symbol}?apikey={fmp_key}'
        return requests.get(url)

    async def get_company_financial_ratios(symbol):
        url = f'https://financialmodelingprep.com/api/v3/ratios/{symbol}?apikey={fmp_key}'
        return requests.get(url)

    async def get_company_quarterly_financial_ratios(symbol):
        url = f'https://financialmodelingprep.com/api/v3/ratios/{symbol}?period=quarter&apikey={fmp_key}'
        return requests.get(url)

    # Scores
    async def get_stock_financial_scores(symbol):
        url = f'https://financialmodelingprep.com/api/v4/score?{symbol}&apikey={fmp_key}'
        return requests.get(url)

    async def get_owners_earnings(symbol):
        url = f'https://financialmodelingprep.com/api/v4/owner_earnings?{symbol}&apikey={fmp_key}'
        return requests.get(url)

    # Enterprise Value
    async def get_company_annual_enterprise_value(symbol):
        url = f'https://financialmodelingprep.com/api/v3/enterprise-values/{symbol}?apikey={fmp_key}'
        return requests.get(url)

    # Financial Statements Growth
    async def get_income_statement_growth(symbol):
        url = f'https://financialmodelingprep.com/api/v3/income-statement-growth/{symbol}?apikey={fmp_key}'
        return requests.get(url)
    
    async def get_balance_sheet_growth(symbol):
        url = f'https://financialmodelingprep.com/api/v3/balance-sheet-statement-growth/{symbol}?apikey={fmp_key}'
        return requests.get(url)

    async def get_cash_flow_statement_growth(symbol):
        url = f'https://financialmodelingprep.com/api/v3/cash-flow-statement-growth/{symbol}?apikey={fmp_key}'
        return requests.get(url)

    # Key Metrics
    async def get_company_ttm_key_metrics(symbol):
        url = f'https://financialmodelingprep.com/api/v3/key-metrics-ttm/{symbol}?apikey={fmp_key}'
        return requests.get(url)

    async def get_company_annual_key_metrics(symbol):
        url = f'https://financialmodelingprep.com/api/v3/key-metrics/{symbol}?apikey={fmp_key}'
        return requests.get(url)

    async def get_company_quarterly_key_metrics(symbol):
        url = f'https://financialmodelingprep.com/api/v3/key-metrics/{symbol}?period=quarter&limit=130&apikey={fmp_key}'
        return requests.get(url)

    # Financial Growth
    async def get_company_financial_growth(symbol):
        url = f'https://financialmodelingprep.com/api/v3/financial-growth/{symbol}?limit=100&apikey={fmp_key}'
        return requests.get(url)
    
    async def get_company_quarterly_financial_growth(symbol):
        url = f'https://financialmodelingprep.com/api/v3/financial-growth/{symbol}?period=quarter&limit=100&apikey={fmp_key}'
        return requests.get(url)

    # Rating
    async def get_company_rating(symbol):
        url = f'https://financialmodelingprep.com/api/v3/rating/{symbol}?&apikey={fmp_key}'
        return requests.get(url)

    async def get_historical_company_rating(symbol):
        url = f'https://financialmodelingprep.com/api/v3/historical-rating/{symbol}?&apikey={fmp_key}'
        return requests.get(url)

    # DCF
    async def get_dcf_value(symbol):
        url = f'https://financialmodelingprep.com/api/v3/discounted-cash-flow/{symbol}?apikey={fmp_key}'
        return requests.get(url)

    # Advanced Cash Flow Projection Including WACC
    async def get_advanced_cash_flow_projection_including_wacc(symbol):
        url = f'https://financialmodelingprep.com/api/v4/advanced_discounted_cash_flow?symbol={symbol}&apikey={fmp_key}'
        return requests.get(url)

    # Advanced Levered Cash Flow Projection Including WACC
    async def get_advanced_levered_cash_flow_projection_including_wacc(symbol):
        url = f'https://financialmodelingprep.com/api/v4/advanced_levered_discounted_cash_flow?symbol={symbol}&apikey={fmp_key}'
        return requests.get(url)

    # Companies Annual Historical Discounted Cash Flow value
    async def get_company_historical_discounted_cash_flow_value(symbol):
        url = f'https://financialmodelingprep.com/api/v3/historical-discounted-cash-flow-statement/{symbol}?apikey={fmp_key}'
        return requests.get(url)

    # Companies Quarterly Historical Discounted Cash Flow value
    async def get_company_historical_quarterly_discounted_cash_flow_value(symbol):
        url = f'https://financialmodelingprep.com/api/v3/historical-discounted-cash-flow-statement/{symbol}?period=quarter&apikey={fmp_key}'
        return requests.get(url)

    # Companies Historical Daily Discounted Cash Flow value
    async def get_company_historical_daily_discounted_cash_flow_value(symbol):
        url = f'https://financialmodelingprep.com/api/v3/historical-daily-discounted-cash-flow/{symbol}?limit=1000&apikey={fmp_key}'
        return requests.get(url)
