



import json
from app.services.fmp import FmpService
from app.services.dfs import DataFetcherService as DFS

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
        
        # get major equity market index data
        data = await FmpService.MarketIndexes.get_all_major_indexes()
        objects = data.json()
        indexes_needed = ['^DJI', '^GSPC', '^NDX', '^W5000']
        matches = [obj for obj in objects if obj['symbol'] in indexes_needed]

        # get Bitcoin data        
        coin_data = await DFS.CryptoData.CoinGecko.get_coins_list()
        btc_data = await DFS.CryptoData.CoinGecko(**{'id': "bitcoin"}).get_current_data_for_a_coin()
        
        # format required bitcoin data to avoid unnecessary data in payload
        btc_dto = {"title": "Bitcoin"}
        btc_dto['price_change_24h'] = btc_data['market_data']['price_change_24h']
        btc_dto['price_change_percentage_24h'] = btc_data['market_data']['price_change_percentage_24h']
        btc_dto['current_price'] = btc_data['market_data']['current_price']['usd']
                
        # construct dto list        
        dto_list = []
        dto_list.append(btc_dto)
        
        for match in matches:
            dta = {
                "title": match['name'],
                "price_change_24h": match['changesPercentage'],
                "price_change_percentage_24h": match['changesPercentage'],
                "current_price": "",
                "intraday_price_history": [],
            }
            dto_list.append(dta)
                    
        return dto_list
    
    
    async def get_notable_quotes():
        # TODO: Quotes for top 5 market leaders
        # TODO: Quotes for top 5 gainers
        # TODO: Quotes for top 5 losers
        pass
    
    pass