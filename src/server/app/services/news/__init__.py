from app.services.fmp import FmpService
from .storage import Storage 




class NewsService:
    
    class Storage(Storage):
        pass
    
    # Get News Articles from FMP
    async def get_latest_fmp_articles():
        fmp_articles = await FmpService.News.get_fmp_articles()
        
        return fmp_articles.json()['content']
    
    