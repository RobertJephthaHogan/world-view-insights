



import json
from app.services.fmp import FmpService
from app.services.dfs import DataFetcherService as DFS
from app.database.gainer_price_snapshot_operations import GainerPriceSnapshotOperations
from app.models.GainerPriceSnapshot import GainerPriceSnapshot
from app.helpers.decorators.timer import timer
from .storage import Storage
from datetime import datetime
from bson import ObjectId


class DataService:
    
    class Storage(Storage):
        pass
    
    
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
    
    @timer
    async def get_major_index_overview():
        
        # Get today's date
        today_date = datetime.now()

        # Format the date for start and end times
        formatted_date = today_date.strftime('%Y-%m-%d')
        
        # get major equity market index data
        data = await FmpService.MarketIndexes.get_all_major_indexes()
        objects = data.json()
        indexes_needed = ['^DJI', '^GSPC', '^NDX', '^W5000']
        index_to_etf_map = {
            '^DJI': 'DIA', 
            '^GSPC': 'SPY', 
            '^NDX': 'QQQ', 
            '^W5000': 'VTI',
        }
        matches = [obj for obj in objects if obj['symbol'] in indexes_needed]

        # get Bitcoin data        
        btc_data = await DFS.CryptoData.CoinGecko(**{'id': "bitcoin"}).get_current_data_for_a_coin()
        
        # format required bitcoin data to avoid unnecessary data in payload
        btc_dto = {"title": "Bitcoin"}
        btc_dto['price_change_24h'] = btc_data['market_data']['price_change_24h']
        btc_dto['price_change_percentage_24h'] = btc_data['market_data']['price_change_percentage_24h']
        btc_dto['current_price'] = btc_data['market_data']['current_price']['usd']
        
        # add btc price history to the dto
        btc_price_data = await FmpService.StockPrices.get_company_historical_daily_prices('BTCUSD', formatted_date, formatted_date)
        btc_dto['intraday_price_history'] = btc_price_data.json()
                
        # construct dto list        
        dto_list = []
        dto_list.append(btc_dto)
                
        # standardize equity market index data
        for match in matches:
            
            price_symbol = match['symbol'] if not '^W5000' else index_to_etf_map[match['symbol']]
            
            # add index's price data to dto entry
            price_data = await FmpService.StockPrices.get_company_historical_daily_prices(price_symbol, formatted_date, formatted_date)
            
            dta = {
                "title": match['name'],
                "price_change_24h": match['change'],
                "price_change_percentage_24h": match['changesPercentage'],
                "current_price": match['price'],
                "intraday_price_history": price_data.json(),
            }
            dto_list.append(dta)
        
        return dto_list
    
    @timer
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
    
    
    ##################################
    # Gainer Data Fetching Functions #
    ##################################
    
    @timer
    async def get_gainers_price_table():
        
        gainer_data = await FmpService.MarketPerformance.get_largest_gainers()
        gainer_data = gainer_data.json()
        
        gainer_price_snapshots = []
        
        for gainer in gainer_data:
            quote_date = await FmpService.StockPrices.get_company_quote(gainer['symbol'])
            quote_date = quote_date.json()[0]
            price_snapshot = {
                "name": gainer["name"],
                "symbol": gainer["symbol"],
                "change": gainer["change"],
                "price": gainer["price"],
                "changesPercentage": gainer["changesPercentage"],
                "dayHigh": quote_date['dayHigh'],
                "dayLow": quote_date['dayLow'],
                "yearHigh": quote_date['yearHigh'],
                "yearLow": quote_date['yearLow'],
                "volume": quote_date['volume'],
                "time": quote_date['timestamp'],
                "avgVolume": quote_date['avgVolume'],
            }
            gainer_price_snapshots.append(price_snapshot)
        
        return gainer_price_snapshots
    
    
    #################################
    # Loser Data Fetching Functions #
    #################################
    
    @timer
    async def get_losers_price_table():
        
        loser_data = await FmpService.MarketPerformance.get_largest_losers()
        loser_data = loser_data.json()
        
        gainer_price_snapshots = []
        
        for gainer in loser_data:
            quote_date = await FmpService.StockPrices.get_company_quote(gainer['symbol'])
            quote_date = quote_date.json()[0]
            price_snapshot = {
                "name": gainer["name"],
                "symbol": gainer["symbol"],
                "change": gainer["change"],
                "price": gainer["price"],
                "changesPercentage": gainer["changesPercentage"],
                "dayHigh": quote_date['dayHigh'],
                "dayLow": quote_date['dayLow'],
                "yearHigh": quote_date['yearHigh'],
                "yearLow": quote_date['yearLow'],
                "volume": quote_date['volume'],
                "time": quote_date['timestamp'],
                "avgVolume": quote_date['avgVolume'],
            }
            gainer_price_snapshots.append(price_snapshot)
        
        return gainer_price_snapshots
    
    
    
    ##################################
    # Most Active Fetching Functions #
    ##################################
    
    @timer
    async def get_most_active():
        
        most_active = await FmpService.MarketPerformance.get_most_active()
        most_active = most_active.json()
        
        snapshots = []
        
        for stock in most_active:
            quote_date = await FmpService.StockPrices.get_company_quote(stock['symbol'])
            quote_date = quote_date.json()[0]
            price_snapshot = {
                "name": stock["name"],
                "symbol": stock["symbol"],
                "change": stock["change"],
                "price": stock["price"],
                "changesPercentage": stock["changesPercentage"],
                "dayHigh": quote_date['dayHigh'],
                "dayLow": quote_date['dayLow'],
                "yearHigh": quote_date['yearHigh'],
                "yearLow": quote_date['yearLow'],
                "volume": quote_date['volume'],
                "time": quote_date['timestamp'],
                "avgVolume": quote_date['avgVolume'],
            }
            snapshots.append(price_snapshot)
        
        return snapshots
    
    
    ###################################
    # Leaders Data Fetching Functions #
    ###################################
    
    async def get_leaders_price_table():
        
        # Get quotes for top market leaders
        # get the largest {X} companies by market cap from nyse and nasdaq
        nyseCompanies = FmpService.CompanyData.stock_screener(
            {
                'marketCapMoreThan': 100000000000, 
                'limit': 30,
                'isEtf' : False,
                'exchange': 'nyse'
            }
        )
        nyseCompanies = nyseCompanies.json()
        
        nasdaqCompanies = FmpService.CompanyData.stock_screener(
            {
                'marketCapMoreThan': 100000000000, 
                'limit': 30,
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
                
        return sorted_data