from .calendars import Calendars
from .company_data import CompanyData
from .economics import Economics
from .financial_statements import FmpFinancialStatements
from .financial_statements.aggregate_statements import FmpAggregateFinancialStatements
from .fund_holdings import FundHoldings
from .market_indexes import MarketIndexes
from .price_targets import PriceTargets
from .market_performance import MarketPerformance
from .news import News
from .stock_fundamental_analysis import FmpStockFundamentalAnalysis
from .stock_prices import StockPrices
from .symbols import Symbols

class FmpService:
    
    class Calendars(Calendars):
        pass
    
    class CompanyData(CompanyData):
        pass
    
    class Economics(Economics):
        pass

    class FmpFinancialStatements(FmpFinancialStatements):
        pass

    class FmpAggregatedFinancialStatements(FmpAggregateFinancialStatements):
        pass

    class FundHoldings(FundHoldings):
        pass
    
    class MarketIndexes(MarketIndexes):
        pass
    
    class MarketPerformance(MarketPerformance):
        pass
    
    class News(News):
        pass

    class PriceTargets(PriceTargets):
        pass
    
    class PriceTargets(PriceTargets):
        pass
    
    class FmpStockFundamentalAnalysis(FmpStockFundamentalAnalysis):
        pass
    
    class StockPrices(StockPrices):
        pass
    
    class Symbols(Symbols):
        pass