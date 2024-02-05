from beanie import PydanticObjectId
from pydantic import ValidationError
from typing import List, Union, Any
from bson import ObjectId


from app.models.NewsArticle import NewsArticle, UpdateNewsArticleModel


news_article_collection = NewsArticle

class NewsArticleOperations:

    async def add_news_article(new_news_article: NewsArticle) -> NewsArticle:
        new_news_article.id = str(ObjectId())
        news_article = await new_news_article.create()
        return news_article


    async def retrieve_all_news_articles() -> List[NewsArticle]:
        news_articles = await news_article_collection.all().to_list()
        return news_articles

    # Convert to multi
    async def retrieve_most_recent_news_article(self) -> Union[NewsArticle, None]:
        most_recent_snapshot = await news_article_collection.find().sort("-creationDate").limit(1).to_list()
        if most_recent_snapshot:
            return most_recent_snapshot[0]
        return None


    async def retrieve_news_article_by_title(self, title: str) -> Union[NewsArticle, None]:
            news_article = await news_article_collection.find_one(NewsArticle.title == title)
            return news_article
        
    
    async def retrieve_recent_news_articles(self, limit: int) -> List[NewsArticle]:
        recent_news_articles = await news_article_collection.find().sort("-datePosted").limit(limit).to_list()
        return recent_news_articles
        

    async def retrieve_news_article(id: NewsArticle) -> NewsArticle:
        news_article = await news_article_collection.get(str(id))
        if news_article:
            return news_article
        

    async def delete_news_article(id: PydanticObjectId) -> bool:
        try:
            news_article = await news_article_collection.get(str(id))
        except ValidationError as e:
            print(e.json())
        if news_article:
            await news_article.delete()
            return True


    async def update_news_article_data(id: PydanticObjectId, data: dict) -> Union[bool, NewsArticle]:
        des_body = {k: v for k, v in data.items() if v is not None}
        update_query = {"$set": {
            field: value for field, value in des_body.items()
        }}
        news_article = await news_article_collection.get(str(id))
        if news_article:
            await news_article.update(update_query)
            return news_article
        return False

