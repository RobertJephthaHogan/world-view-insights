from fastapi import APIRouter
import asyncio

from .. import FmpService
from ..price_targets import PriceTargets
from ..stock_prices import StockPrices
from ..stock_fundamental_analysis import FmpStockFundamentalAnalysis
from ..economics import Economics
from ..market_indexes import MarketIndexes
from ..market_performance import MarketPerformance
from ..fund_holdings import FundHoldings
from ..symbols import Symbols
from ..company_data import CompanyData
from ..calendars import Calendars

router = APIRouter()


class FmpController:
            
    def __init__(self, **kwargs):
        self.kwargs = kwargs
        self.tags = ['FMP']

    # Get all quarterly financial statements as reported
    @router.get("/quarterly_financial_statements_as_reported/{ticker}")
    async def get_all_quarterly_financial_statements_as_reported(ticker):
        return await FmpService.FmpAggregatedFinancialStatements.getAllQuarterlyFinancialStatementsAsReported(ticker)

    # Get all standardized quarterly financial statements 
    @router.get("/quarterly_standardized_financial_statements/{ticker}")
    async def get_all_standardized_quarterly_financial_statements(ticker):
        return await FmpService.FmpAggregatedFinancialStatements.getAllQuarterlyStandardizedFinancialStatements(ticker)

    # Get Price Target
    @router.get("/get_price_target/{symbol}")
    async def get_price_target(symbol):
        data = await PriceTargets.getPriceTarget(symbol)
        return data.json()

    # Get Price Target Summary
    @router.get("/get_price_target_summary/{symbol}")
    async def get_price_target_summary(symbol):
        data = await PriceTargets.getPriceTargetSummary(symbol)
        return data.json()

    # Get Price Target By Analyst Name
    @router.get("/get_price_target_by_analyst_name/{name}")
    async def get_price_target_by_analyst_name(name):
        data = await PriceTargets.getPriceTargetByAnalystName(name)
        return data.json()

    # Get Price Target By Analyst Company
    @router.get("/get_price_target_by_analyst_company/{company}")
    async def get_price_target_by_analyst_company(company):
        data = await PriceTargets.getPriceTargetByAnalystCompany(company)
        return data.json()

    # Get Price Target Consensus
    @router.get("/get_price_target_consensus/{symbol}")
    async def get_price_target_consensus(symbol):
        data = await PriceTargets.getPriceTargetConsensus(symbol)
        return data.json()

    # Get Company Quote
    @router.get("/get_company_quote/{symbol}")
    async def get_company_quote(symbol):
        data = await StockPrices.getCompanyQuote(symbol)
        return data.json()

    # Get Company Stock Price Change
    @router.get("/get_company_stock_price_change/{symbol}")
    async def get_company_stock_price_change(symbol):
        data = await StockPrices.getCompanyStockPriceChange(symbol)
        return data.json()

    # Get Company 1 Minute Candles
    @router.get("/get_company_one_minute_candles/{symbol}")
    async def get_company_one_minute_candles(symbol):
        data = await StockPrices.getCompanyOneMinuteCandles(symbol)
        return data.json()
    
    # Get Company 5 Minute Candles
    @router.get("/get_company_five_minute_candles/{symbol}")
    async def get_company_five_minute_candles(symbol):
        data = await StockPrices.getCompanyFiveMinuteCandles(symbol)
        return data.json()

    # Get Company 15 Minute Candles
    @router.get("/get_company_fifteen_minute_candles/{symbol}")
    async def get_company_fifteen_minute_candles(symbol):
        data = await StockPrices.getCompanyFifteenMinuteCandles(symbol)
        return data.json()

    # Get Company 30 Minute Candles
    @router.get("/get_company_thirty_minute_candles/{symbol}")
    async def get_company_thirty_minute_candles(symbol):
        data = await StockPrices.getCompanyThirtyMinuteCandles(symbol)
        return data.json()

    # Get Company 1 hour Candles
    @router.get("/get_company_one_hour_candles/{symbol}")
    async def get_company_one_hour_candles(symbol):
        data = await StockPrices.getCompanyOneHourCandles(symbol)
        return data.json()

    # Get Company 4 hour Candles
    @router.get("/get_company_four_hour_candles/{symbol}")
    async def get_company_four_hour_candles(symbol):
        data = await StockPrices.getCompanyFourHourCandles(symbol)
        return data.json()

    # Get Company Daily Candles
    @router.get("/get_company_historical_daily_prices/{symbol}")
    async def get_company_historical_daily_prices(symbol):
        data = await StockPrices.getCompanyHistoricalDailyPrices(symbol)
        return data.json()

    # Get Company TTM Ratios
    @router.get("/get_company_ttm_ratios/{symbol}")
    async def get_company_ttm_ratios(symbol):
        data = await FmpStockFundamentalAnalysis.getCompanyTtmRatios(symbol)
        return data.json()

    # Get Company Financial Ratios
    @router.get("/get_company_financial_ratios/{symbol}")
    async def get_company_financial_ratios(symbol):
        data = await FmpStockFundamentalAnalysis.getCompanyFinancialRatios(symbol)
        return data.json()

    # Get Company Quarterly Financial Ratios
    @router.get("/get_company_quarterly_financial_ratios/{symbol}")
    async def get_company_quarterly_financial_ratios(symbol):
        data = await FmpStockFundamentalAnalysis.getCompanyQuarterlyFinancialRatios(symbol)
        return data.json()

    # Get Company Financial Scores
    @router.get("/get_company_financial_scores/{symbol}")
    async def get_company_financial_scores(symbol):
        data = await FmpStockFundamentalAnalysis.getStockFinancialScores(symbol)
        return data.json()

    # Get Company Owners Earnings
    @router.get("/get_company_owners_earnings/{symbol}")
    async def get_company_owners_earnings(symbol):
        data = await FmpStockFundamentalAnalysis.getOwnersEarnings(symbol)
        return data.json()

    # Get Company Enterprise Value
    @router.get("/get_company_enterprise_value/{symbol}")
    async def get_company_enterprise_value(symbol):
        data = await FmpStockFundamentalAnalysis.getCompanyAnnualEnterpriseValue(symbol)
        return data.json()

    # Get Income Statement Growth
    @router.get("/get_income_statement_growth/{symbol}")
    async def get_income_statement_growth(symbol):
        data = await FmpStockFundamentalAnalysis.getIncomeStatementGrowth(symbol)
        return data.json()

    # Get Balance Sheet  Growth
    @router.get("/get_balance_sheet_statement_growth/{symbol}")
    async def get_balance_sheet_statement_growth(symbol):
        data = await FmpStockFundamentalAnalysis.getBalanceSheetGrowth(symbol)
        return data.json()

    # Get Cash Flow Statement Growth
    @router.get("/get_cash_flow_statement_growth/{symbol}")
    async def get_cash_flow_statement_growth(symbol):
        data = await FmpStockFundamentalAnalysis.getCashFlowStatementGrowth(symbol)
        return data.json()

    # Get Company Ttm Key Metrics
    @router.get("/get_company_ttm_key_metrics/{symbol}")
    async def get_company_ttm_key_metrics(symbol):
        data = await FmpStockFundamentalAnalysis.getCompanyTtmKeyMetrics(symbol)
        return data.json()

    # Get Company Annual Key Metrics
    @router.get("/get_company_annual_key_metrics/{symbol}")
    async def get_company_annual_key_metrics(symbol):
        data = await FmpStockFundamentalAnalysis.getCompanyAnnualKeyMetrics(symbol)
        return data.json()

    # Get Company Quarterly Key Metrics
    @router.get("/get_company_quarterly_key_metrics/{symbol}")
    async def get_company_quarterly_key_metrics(symbol):
        data = await FmpStockFundamentalAnalysis.getCompanyQuarterlyKeyMetrics(symbol)
        return data.json()

    # Get Company Financial Growth
    @router.get("/get_company_financial_growth/{symbol}")
    async def get_company_financial_growth(symbol):
        data = await FmpStockFundamentalAnalysis.getCompanyFinancialGrowth(symbol)
        return data.json()

    # Get Company Quarterly Financial Growth
    @router.get("/get_company_quarterly_financial_growth/{symbol}")
    async def get_company_quarterly_financial_growth(symbol):
        data = await FmpStockFundamentalAnalysis.getCompanyQuarterlyFinancialGrowth(symbol)
        return data.json()

    # Get Company Rating
    @router.get("/get_company_rating/{symbol}")
    async def get_company_rating(symbol):
        data = await FmpStockFundamentalAnalysis.getCompanyRating(symbol)
        return data.json()

    # Get Historical Company Rating
    @router.get("/get_historical_company_rating/{symbol}")
    async def get_historical_company_rating(symbol):
        data = await FmpStockFundamentalAnalysis.getHistoricalCompanyRating(symbol)
        return data.json()

    # Get Discounted Cash Flow Value
    @router.get("/get_discounted_cash_flow_value/{symbol}")
    async def get_discounted_cash_flow_value(symbol):
        data = await FmpStockFundamentalAnalysis.getDCFValue(symbol)
        return data.json()

    # Get Advanced Cash Flow Projection Including WACC
    @router.get("/get_advanced_cash_flow_projection_including_wacc/{symbol}")
    async def get_advanced_cash_flow_projection_including_wacc(symbol):
        data = await FmpStockFundamentalAnalysis.getAdvancedCashFlowProjectionIncludingWACC(symbol)
        return data.json()

    # Get Advanced Levered Cash Flow Projection Including WACC
    @router.get("/get_advanced_levered_cash_flow_projection_including_wacc/{symbol}")
    async def get_advanced_levered_cash_flow_projection_including_wacc(symbol):
        data = await FmpStockFundamentalAnalysis.getAdvancedLeveredCashFlowProjectionIncludingWACC(symbol)
        return data.json()

    # Get Companies Annual Historical Discounted Cash Flow value
    @router.get("/get_annual_historical_dcf_values/{symbol}")
    async def get_annual_historical_dcf_values(symbol):
        data = await FmpStockFundamentalAnalysis.getCompanyHistoricalDiscountedCashFlowValue(symbol)
        return data.json()

    # Get Companies Quarterly Historical Discounted Cash Flow value
    @router.get("/get_quarterly_historical_dcf_values/{symbol}")
    async def get_quarterly_historical_dcf_values(symbol):
        data = await FmpStockFundamentalAnalysis.getCompanyHistoricalQuarterlyDiscountedCashFlowValue(symbol)
        return data.json()

    # Get Companies Historical Daily Discounted Cash Flow value
    @router.get("/get_daily_historical_dcf_values/{symbol}")
    async def get_daily_historical_dcf_values(symbol):
        data = await FmpStockFundamentalAnalysis.getCompanyHistoricalDailyDiscountedCashFlowValue(symbol)
        return data.json()

    # Get Market Risk Premium for each country
    @router.get("/get_market_risk_premium_for_all_countries/")
    async def get_market_risk_premium_for_all_countries():
        data = await Economics.getMarketRiskPremiumForAllCountries()
        return data.json()

    # Get All Major Indexes
    @router.get("/get_all_major_indexes/")
    async def get_all_major_indexes():
        data = await MarketIndexes.getAllMajorIndexes()
        return data.json()
    
    # Get All S&P 500 Constituents
    @router.get("/get_all_spx_constituents/")
    async def get_all_spx_constituents():
        data = await MarketIndexes.getAllSPXConstituents()
        return data.json()

    # Get All Nasdaq Constituents
    @router.get("/get_all_ndx_constituents/")
    async def get_all_ndx_constituents():
        data = await MarketIndexes.getAllNDXConstituents()
        return data.json()

    # Get All ETF Constituents
    @router.get("/get_all_etf_constituents/{etf_symbol}")
    async def get_all_etf_constituents(etf_symbol):
        data = await FundHoldings.getETFConstituents(etf_symbol)
        return data.json()

    # Get ETF Expense Ratio
    @router.get("/get_etf_expense_ratio/{etf_symbol}")
    async def get_etf_expense_ratio(etf_symbol):
        data = await FundHoldings.getETFExpenseRatio(etf_symbol)
        return data.json()

    # Get Institutional Holders Of A Company
    @router.get("/get_institutional_holders/{symbol}")
    async def get_institutional_holders(symbol):
        data = await FundHoldings.getInstitutionalHoldersOfACompany(symbol)
        return data.json()

    # Get Mutual Fund Holders Of A Company
    @router.get("/get_mutual_fund_holders/{symbol}")
    async def get_mutual_fund_holders(symbol):
        data = await FundHoldings.getMutualFundHoldersOfACompany(symbol)
        return data.json()

    # Get ETF Sector Weightings
    @router.get("/get_etf_sector_weightings/{symbol}")
    async def get_etf_sector_weightings(symbol):
        data = await FundHoldings.getETFSectorWeightings(symbol)
        return data.json()

    # Get ETF Country Weightings
    @router.get("/get_etf_country_weightings/{symbol}")
    async def get_etf_country_weightings(symbol):
        data = await FundHoldings.getETFCountryWeightings(symbol)
        return data.json()

    # Get ETFs With Exposure To A Stock
    @router.get("/get_stock_exposure_list/{symbol}")
    async def get_stock_exposure_list(symbol):
        data = await FundHoldings.getStockExposureList(symbol)
        return data.json()

    # Get FMP Symbols
    @router.get("/get_fmp_symbols/")
    async def get_fmp_symbols():
        data = await Symbols.getSymbols()
        return data.json()

    # All Tradable Symbols
    @router.get("/get_all_tradable_symbols/")
    async def get_all_tradable_symbols():
        data = await Symbols.getFMPTradableSymbols()
        return data.json()

    # Get ETF List
    @router.get("/get_etf_list/")
    async def get_etf_list():
        data = await Symbols.getFMPETFList()
        return data.json()

    # Get Sector PE Ratios
    @router.get("/get_sector_pe_ratios/")
    async def get_sector_pe_ratios():
        data = await MarketPerformance.getSectorPERatios()
        return data.json()

    # Get Industry PE Ratios
    @router.get("/get_industry_pe_ratios/")
    async def get_industry_pe_ratios():
        data = await MarketPerformance.getIndustriesPERatios()
        return data.json()

    # Get Largest Gainers
    @router.get("/get_largest_gainers/")
    async def get_largest_gainers():
        data = await MarketPerformance.getLargestGainers()
        return data.json()

    # Get Largest Losers
    @router.get("/get_largest_losers/")
    async def get_largest_losers():
        data = await MarketPerformance.getLargestLosers()
        return data.json()

    # Get Most Active
    @router.get("/get_most_active/")
    async def get_most_active():
        data = await MarketPerformance.getMostActive()
        return data.json()

    # Get Stock Peers
    @router.get("/get_stock_peers/{symbol}")
    async def get_stock_peers(symbol):
        data = await CompanyData.getStockPeers()
        return data.json()

    # Get Core Company Information
    @router.get("/get_core_company_information/{symbol}")
    async def get_core_company_information(symbol):
        data = await CompanyData.getCoreCompanyInformation()
        return data.json()

    # Get Earnings Calendar
    @router.get("/get_earnings_calendar")
    async def get_earnings_calendar():
        data = await Calendars.getEarningsCalendar()
        return data.json()

    # Get Earnings Calendar Confirmed
    @router.get("/get_earnings_calendar_confirmed")
    async def get_earnings_calendar_confirmed():
        data = await Calendars.getEarningsCalendarConfirmed()
        return data.json()

    # Get IPO Calendar 
    @router.get("/get_ipo_calendar")
    async def get_ipo_calendar():
        data = await Calendars.getIPOCalendar()
        return data.json()

    # Get IPO Calendar Confirmed
    @router.get("/get_ipo_calendar_confirmed")
    async def get_ipo_calendar_confirmed():
        data = await Calendars.getIPOCalendarConfirmed()
        return data.json()

    # Get Stock Split Calendar
    @router.get("/get_stock_split_calendar")
    async def get_stock_split_calendar():
        data = await Calendars.getStockSplitCalendar()
        return data.json()

    # Get Dividend Calendar
    @router.get("/get_dividend_calendar")
    async def get_dividend_calendar():
        data = await Calendars.getDividendCalendar()
        return data.json()

    # Get Economic Calendar
    @router.get("/get_economic_calendar")
    async def get_economic_calendar():
        data = await Calendars.getEconomicCalendar()
        return data.json()