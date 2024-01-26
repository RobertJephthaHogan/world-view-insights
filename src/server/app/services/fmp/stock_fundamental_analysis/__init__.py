import requests
from app.config import Settings


fmp_key = Settings().FMP_API_KEY

class FmpStockFundamentalAnalysis:

    # Ratios
    async def getCompanyTtmRatios(symbol):
        url = f'https://financialmodelingprep.com/api/v3/ratios-ttm/{symbol}?apikey={fmp_key}'
        return requests.get(url)

    async def getCompanyFinancialRatios(symbol):
        url = f'https://financialmodelingprep.com/api/v3/ratios/{symbol}?apikey={fmp_key}'
        return requests.get(url)

    async def getCompanyQuarterlyFinancialRatios(symbol):
        url = f'https://financialmodelingprep.com/api/v3/ratios/{symbol}?period=quarter&apikey={fmp_key}'
        return requests.get(url)

    # Scores
    async def getStockFinancialScores(symbol):
        url = f'https://financialmodelingprep.com/api/v4/score?{symbol}&apikey={fmp_key}'
        return requests.get(url)

    async def getOwnersEarnings(symbol):
        url = f'https://financialmodelingprep.com/api/v4/owner_earnings?{symbol}&apikey={fmp_key}'
        return requests.get(url)

    # Enterprise Value
    async def getCompanyAnnualEnterpriseValue(symbol):
        url = f'https://financialmodelingprep.com/api/v3/enterprise-values/{symbol}?apikey={fmp_key}'
        return requests.get(url)

    # Financial Statements Growth
    async def getIncomeStatementGrowth(symbol):
        url = f'https://financialmodelingprep.com/api/v3/income-statement-growth/{symbol}?apikey={fmp_key}'
        return requests.get(url)
    
    async def getBalanceSheetGrowth(symbol):
        url = f'https://financialmodelingprep.com/api/v3/balance-sheet-statement-growth/{symbol}?apikey={fmp_key}'
        return requests.get(url)

    async def getCashFlowStatementGrowth(symbol):
        url = f'https://financialmodelingprep.com/api/v3/cash-flow-statement-growth/{symbol}?apikey={fmp_key}'
        return requests.get(url)

    # Key Metrics
    async def getCompanyTtmKeyMetrics(symbol):
        url = f'https://financialmodelingprep.com/api/v3/key-metrics-ttm/{symbol}?apikey={fmp_key}'
        return requests.get(url)

    async def getCompanyAnnualKeyMetrics(symbol):
        url = f'https://financialmodelingprep.com/api/v3/key-metrics/{symbol}?apikey={fmp_key}'
        return requests.get(url)

    async def getCompanyQuarterlyKeyMetrics(symbol):
        url = f'https://financialmodelingprep.com/api/v3/key-metrics/{symbol}?period=quarter&limit=130&apikey={fmp_key}'
        return requests.get(url)


    # Financial Growth
    async def getCompanyFinancialGrowth(symbol):
        url = f'https://financialmodelingprep.com/api/v3/financial-growth/{symbol}?limit=100&apikey={fmp_key}'
        return requests.get(url)
    
    async def getCompanyQuarterlyFinancialGrowth(symbol):
        url = f'https://financialmodelingprep.com/api/v3/financial-growth/{symbol}?period=quarter&limit=100&apikey={fmp_key}'
        return requests.get(url)

    # Rating
    async def getCompanyRating(symbol):
        url = f'https://financialmodelingprep.com/api/v3/rating/{symbol}?&apikey={fmp_key}'
        return requests.get(url)

    async def getHistoricalCompanyRating(symbol):
        url = f'https://financialmodelingprep.com/api/v3/historical-rating/{symbol}?&apikey={fmp_key}'
        return requests.get(url)


    # DCF
    async def getDCFValue(symbol):
        url = f'https://financialmodelingprep.com/api/v3/discounted-cash-flow/{symbol}?apikey={fmp_key}'
        return requests.get(url)

    # Advanced Cash Flow Projection Including WACC
    async def getAdvancedCashFlowProjectionIncludingWACC(symbol):
        url = f'https://financialmodelingprep.com/api/v4/advanced_discounted_cash_flow?symbol={symbol}&apikey={fmp_key}'
        return requests.get(url)

    # Advanced Levered Cash Flow Projection Including WACC
    async def getAdvancedLeveredCashFlowProjectionIncludingWACC(symbol):
        url = f'https://financialmodelingprep.com/api/v4/advanced_levered_discounted_cash_flow?symbol={symbol}&apikey={fmp_key}'
        return requests.get(url)

    # Companies Annual Historical Discounted Cash Flow value
    async def getCompanyHistoricalDiscountedCashFlowValue(symbol):
        url = f'https://financialmodelingprep.com/api/v3/historical-discounted-cash-flow-statement/{symbol}?apikey={fmp_key}'
        return requests.get(url)

    # Companies Quarterly Historical Discounted Cash Flow value
    async def getCompanyHistoricalQuarterlyDiscountedCashFlowValue(symbol):
        url = f'https://financialmodelingprep.com/api/v3/historical-discounted-cash-flow-statement/{symbol}?period=quarter&apikey={fmp_key}'
        return requests.get(url)

    # Companies Historical Daily Discounted Cash Flow value
    async def getCompanyHistoricalDailyDiscountedCashFlowValue(symbol):
        url = f'https://financialmodelingprep.com/api/v3/historical-daily-discounted-cash-flow/{symbol}?limit=1000&apikey={fmp_key}'
        return requests.get(url)