



import json
from app.services.fmp import FmpService
from app.services.dfs import DataFetcherService as DFS

class DataService:
    

    async def get_market_leader_quotes(limit):

        # get the largest {x} companies by market cap from nyse and nasdaq
        nyseCompanies = FmpService.CompanyData.stock_screener(
            {
                'marketCapMoreThan': 100000000000, 
                'limit': limit,
                'isEtf' : False,
                'exchange': 'nyse'
            }
        )
        nyseCompanies = nyseCompanies.json()
        
        nasdaqCompanies = FmpService.CompanyData.stock_screener(
            {
                'marketCapMoreThan': 100000000000, 
                'limit': limit,
                'isEtf' : False,
                'exchange': 'nasdaq'
            }
        )
        nasdaqCompanies = nasdaqCompanies.json()

        # Concatenate the company lists
        companies = nyseCompanies + nasdaqCompanies
        
        # Filter out objects where 'sector' is null
        companies = [obj for obj in companies if obj.get('sector') is not None]
                
        # Get quote data for each company and add it to the company data
        for co in companies:
            quote_data = await FmpService.StockPrices.get_company_quote(co['symbol']) # get quote for entry
            co.update(quote_data.json()[0]) # add quote data to company data
        
        return companies
    
    
    async def get_major_index_overview():
        
        # get major equity market index data
        data = await FmpService.MarketIndexes.get_all_major_indexes()
        objects = data.json()
        indexes_needed = ['^DJI', '^GSPC', '^NDX', '^W5000']
        matches = [obj for obj in objects if obj['symbol'] in indexes_needed]

        # get Bitcoin data        
        btc_data = await DFS.CryptoData.CoinGecko(**{'id': "bitcoin"}).get_current_data_for_a_coin()
        
        # format required bitcoin data to avoid unnecessary data in payload
        btc_dto = {"title": "Bitcoin"}
        btc_dto['price_change_24h'] = btc_data['market_data']['price_change_24h']
        btc_dto['price_change_percentage_24h'] = btc_data['market_data']['price_change_percentage_24h']
        btc_dto['current_price'] = btc_data['market_data']['current_price']['usd']
                
        # construct dto list        
        dto_list = []
        dto_list.append(btc_dto)
                
        # standardize equity market index data
        for match in matches:
            dta = {
                "title": match['name'],
                "price_change_24h": match['change'],
                "price_change_percentage_24h": match['changesPercentage'],
                "current_price": match['price'],
                "intraday_price_history": [],
            }
            dto_list.append(dta)
                    
        return dto_list
    
    
    async def get_notable_quotes():
        
        dto = {}
        
        # Get quotes for top 5 market leaders
        # get the largest 5 companies by market cap from nyse and nasdaq
        nyseCompanies = FmpService.CompanyData.stock_screener(
            {
                'marketCapMoreThan': 100000000000, 
                'limit': 5,
                'isEtf' : False,
                'exchange': 'nyse'
            }
        )
        nyseCompanies = nyseCompanies.json()
        
        nasdaqCompanies = FmpService.CompanyData.stock_screener(
            {
                'marketCapMoreThan': 100000000000, 
                'limit': 5,
                'isEtf' : False,
                'exchange': 'nasdaq'
            }
        )
        nasdaqCompanies = nasdaqCompanies.json()

        # Concatenate the company lists
        companies = nyseCompanies + nasdaqCompanies
        
        # Filter out objects where 'sector' is null
        companies = [obj for obj in companies if obj.get('sector') is not None]

        # Get quote data for each company and add it to the company data
        for co in companies:
            quote_data = await FmpService.StockPrices.get_company_quote(co['symbol']) # get quote for entry
            co.update(quote_data.json()[0]) # add quote data to company data
            
        # Sort the companies by 'marketCap' in descending order
        sorted_data = sorted(companies, key=lambda x: x['marketCap'], reverse=True)
        
        # Add market leader quotes to dto
        dto['marketLeaderQuotes'] = sorted_data[0:5]

        
        # Quotes for top 5 gainers
        gainer_data = await FmpService.MarketPerformance.get_largest_gainers()
        dto['gainerQuotes'] = gainer_data.json()[0:5]
        
        # Quotes for top 5 losers
        loser_data = await FmpService.MarketPerformance.get_largest_losers()
        dto['loserQuotes'] = loser_data.json()[0:5]
        
        return dto
    
    