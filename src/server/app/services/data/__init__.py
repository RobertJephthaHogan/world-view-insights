



import json
from app.services.fmp import FmpService


class DataService:
    

    async def get_market_leader_quotes(limit):

        # get the largest {x} companies by market cap
        companies = FmpService.CompanyData.stock_screener(
            {
                'marketCapMoreThan': 1000000000, 
                'limit': limit }
            )
        companies = companies.json()
        
        # Get quote data for each company and add it to the company data
        for co in companies:
            quote_data = await FmpService.StockPrices.get_company_quote(co['symbol']) # get quote for entry
            co.update(quote_data.json()[0]) # add quote data to company data
        
        return companies
    
    
    async def get_major_index_overview():
        # TODO: Index data to provide to index banner api
        data = await FmpService.MarketIndexes.get_all_major_indexes()
        objects = data.json()
        
        indexes_needed = ['^DJI', '^GSPC', '^NDX', '^W5000']
        
        matches = [obj for obj in objects if obj['symbol'] in indexes_needed]

        print('matches', matches)
        
        return matches
    
    
    async def get_notable_quotes():
        # TODO: Quotes for top 5 market leaders
        # TODO: Quotes for top 5 gainers
        # TODO: Quotes for top 5 losers
        pass
    
    pass