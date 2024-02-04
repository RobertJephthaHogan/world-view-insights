import requests
from app.config import Settings


fmp_key = Settings().FMP_API_KEY

class News:

    async def get_fmp_articles(page=0):
        url = f'https://financialmodelingprep.com/api/v3/fmp/articles?page={page}&size=20&apikey={fmp_key}'
        return requests.get(url)
    
    async def get_general_news(page=0):
        url = f'https://financialmodelingprep.com/api/v4/general_news?page={page}&apikey={fmp_key}'
        return requests.get(url)
    
    async def get_stock_news(page=0):
        url = f'https://financialmodelingprep.com/api/v3/stock_news?page={page}&apikey={fmp_key}'
        return requests.get(url)
    
    async def get_stock_news_sentiment_rss(page=0):
        url = f'https://financialmodelingprep.com/api/v4/stock-news-sentiments-rss-feed?page={page}&apikey={fmp_key}'
        return requests.get(url)
    
    async def get_forex_news(page=0):
        url = f'https://financialmodelingprep.com/api/v4/forex_news?page={page}&apikey={fmp_key}'
        return requests.get(url)
    
    async def get_crypto_news(page=0):
        url = f'https://financialmodelingprep.com/api/v4/crypto_news?page={page}&apikey={fmp_key}'
        return requests.get(url)


    # TODO: ADD PRESS RELEASES (eh)
    # TODO: ADD HISTORICAL SOCIAL SENTIMENT
    # TODO: ADD TRENDING SOCIAL SENTIMENT
    # TODO: ADD SOCIAL SENTIMENT CHANGES


