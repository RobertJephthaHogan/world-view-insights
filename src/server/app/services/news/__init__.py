from app.services.fmp import FmpService
from bson import ObjectId
from datetime import datetime
import re




class NewsService:
    
    
    async def get_business_news_articles():
        # TODO: Get Business News Articles
        
        # Get News Articles From News Sources
        fmp_articles = await FmpService.News.get_fmp_articles()
        fmp_articles = fmp_articles.json()['content']

        # Standardize entries with "BusinessNewsArticle" model
        standardized_articles = []
        for article in fmp_articles:
            article_id = str(ObjectId())
            standardized = {
                "id": article_id,
                "title": article["title"],
                "datePosted": article["date"],
                "creationDate": datetime.now(),
                "content": re.sub('<[^<]+?>', '', article['content']),
                "link": f"https://worldviewinsights.com/article/{article_id}",
                "tickers": article['tickers'].split(':', 1)[1] if ':' in article['tickers'] else '',
                "image": article['image'],
                "author": article['author'],
                "category": "business",
                "sourceName": article['site'],
                "sourceLink": article['link']
            }
            standardized_articles.append(standardized)
        
        # return entries array
        
        return standardized_articles
    
    
    async def get_tech_news_articles():
        # TODO: Get Tech News Articles
        
        # Get News Articles From News Sources
        # Standardize entries with "TechNewsArticle" model
        # return entries array
        
        pass
    
        
    async def get_political_news_articles():
        # TODO: Get Political News Articles
        
        # Get News Articles From News Sources
        # Standardize entries with "PoliticalNewsArticle" model
        # return entries array
        
        pass
    