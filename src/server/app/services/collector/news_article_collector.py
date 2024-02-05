from app.database.news_article_operations import NewsArticleOperations
from app.services.news import NewsService
from app.models.NewsArticle import NewsArticle
from bson import ObjectId
from datetime import datetime


class NewsArticleCollector:
    

    async def collect_business_news_articles():
        
        # get the news articles to collect
        articles = await NewsService.get_business_news_articles()

        # iterate through articles, store articles that are not already stored       
        for article in articles:
            # check if article exists by title, if so pass, if not, add the article
            article_exists = await NewsArticleOperations().retrieve_news_article_by_title(article['title'])
            if article_exists:
                pass 
            else :
                article_instance = NewsArticle(**article)
                await NewsArticleOperations.add_news_article(article_instance)
                
        return {"status": "complete"}
    