

from app.services.rss import RssService as RSS
from app.database.fmp_news_snapshot_operations import FmpNewsSnapshotOperations
from app.services.news import NewsService
from app.models.FmpNewsSnapshot import FmpNewsSnapshot
from bson import ObjectId
from datetime import datetime


class NewsSnapshotCollector:
    
    
    async def collect_fmp_news_snapshots(self):
        
        # get the data for the snapshot
        data = await NewsService.get_latest_fmp_articles()

        # store the data        
        dto = {
            'id': str(ObjectId()),
            'data': data,
            'creationDate': datetime.now()
        }
        snapshot = FmpNewsSnapshot(**dto)
        await FmpNewsSnapshotOperations.add_fmp_news_snapshot(snapshot)
            
        return {"status": "complete"}
    
    