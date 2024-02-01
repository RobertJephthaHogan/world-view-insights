from app.services.rss import RssService as RSS
from app.database.index_snapshot_operations import IndexSnapshotOperations
from app.models.FeedItem import FeedItem
from app.services.data import DataService
from app.models.IndexSnapshot import IndexSnapshot
from bson import ObjectId
from datetime import datetime


class IndexSnapshotCollector:
    
    
    async def collect_index_snapshots(self):
        
        # get the data for the snapshot
        data = await DataService.get_major_index_overview()

        # store the data        
        dto = {
            'id': str(ObjectId()),
            'data': data,
            'creationDate': datetime.now()
        }
        snapshot = IndexSnapshot(**dto)
        await IndexSnapshotOperations.add_index_snapshot(snapshot)
            
        return {"status": "complete"}
    
    