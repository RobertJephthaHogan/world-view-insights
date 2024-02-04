from app.services.rss import RssService as RSS
from app.database.most_active_snapshot_operations import MostActiveSnapshotOperations
from app.services.data import DataService
from app.models.MostActiveSnapshot import MostActiveSnapshot
from bson import ObjectId
from datetime import datetime


class MostActiveSnapshotCollector:
    
    
    async def collect_most_active_snapshots(self):
        
        # get the data for the snapshot
        data = await DataService.get_most_active()

        # store the data        
        dto = {
            'id': str(ObjectId()),
            'data': data,
            'creationDate': datetime.now()
        }
        snapshot = MostActiveSnapshot(**dto)
        await MostActiveSnapshotOperations.add_most_active_snapshot(snapshot)
            
        return {"status": "complete"}
    
    