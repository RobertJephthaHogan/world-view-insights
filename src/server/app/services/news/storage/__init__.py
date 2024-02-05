from app.database.news_article_operations import NewsArticleOperations




class Storage:
    
    async def get_stored_business_news_articles(limit):
        current = await NewsArticleOperations().retrieve_recent_news_articles(int(limit))
        return current
    
