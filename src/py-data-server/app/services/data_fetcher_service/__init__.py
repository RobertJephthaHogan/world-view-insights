import requests
from app.config import Settings






class DataFetcherService:


    def getStockQuote(ticker):
        url = f'https://financialmodelingprep.com/api/v3/quote/{ticker}?apikey={Settings().FMP_KEY}'
        r = requests.get(url)
        try:
            print('r', r.json())
            p = r.json()[0]["price"]
        except IndexError:
            p = "Not Available" 
            print(f'Price not available for symbol: {ticker}')
        except KeyError:
            p = "Not Available" 
            print(f'Price not available for symbol: {ticker}')
        return p 


    def getMarketCap(ticker):
        url = f'https://financialmodelingprep.com/api/v3/market-capitalization/{ticker}?apikey={Settings().FMP_KEY}'
        r = requests.get(url)
        try:
            mc = r.json()[0]["marketCap"]
        except IndexError as ex:
            mc = "Not Available" 
            print(f'MC not available for symbol: {ticker}')
        except KeyError:
            mc = "Not Available" 
            print(f'MC not available for symbol: {ticker}')
        return mc 


    def get_float(ticker):
        url = f'https://financialmodelingprep.com/api/v4/shares_float?symbol={ticker}?apikey={Settings().FMP_KEY}'
        r = requests.get(url)
        return r


    def get_floats_for_all_companies_available(ticker):
        url = f'https://financialmodelingprep.com/api/v4/shares_float/all?apikey={Settings().FMP_KEY}'
        r = requests.get(url)
        return r


    def getUpcomingEarningsCalendar():
        url = f'https://financialmodelingprep.com/api/v3/earning_calendar/?apikey={Settings().FMP_KEY}'
        r = requests.get(url).json()
        print(r)
        return r


    def getETFholdings(ticker):
        url = f'https://financialmodelingprep.com/api/v3/etf-holder/{ticker}?apikey={Settings().FMP_KEY}'
        r = requests.get(url).json()
        print(r)
        return r
