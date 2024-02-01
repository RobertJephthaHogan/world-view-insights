from app.services.rss import RssService as RSS
from app.database.notable_quote_snapshot_operations import NotableQuotesSnapshotOperations
from app.models.FeedItem import FeedItem
from app.services.data import DataService
from app.models.NotableQuotesSnapshot import NotableQuotesSnapshot
from bson import ObjectId
from datetime import datetime


class NotableQuotesSnapshotCollector:
    
    
    async def collect_notable_quotes_snapshots(self):
        
        # get the data for the snapshot
        data = await DataService.get_notable_quotes()

        # store the data        
        dto = {
            'id': str(ObjectId()),
            'data': data,
            'creationDate': datetime.now()
        }
        snapshot = NotableQuotesSnapshot(**dto)
        await NotableQuotesSnapshotOperations.add_notable_quotes_snapshot(snapshot)
            
        return {"status": "complete"}
    
    