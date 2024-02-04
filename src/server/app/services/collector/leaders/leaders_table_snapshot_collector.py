from app.services.rss import RssService as RSS
from app.database.leaders_table_snapshot_operations import LeadersTableSnapshotOperations
from app.services.data import DataService
from app.models.LeadersTableSnapshot import LeadersTableSnapshot
from bson import ObjectId
from datetime import datetime


class LeadersTableSnapshotCollector:
    
    
    async def collect_leader_price_snapshots(self):
        
        # get the data for the snapshot
        data = await DataService.get_leaders_price_table()
        
        # store the data        
        dto = {
            'id': str(ObjectId()),
            'data': data,
            'creationDate': datetime.now()
        }
        snapshot = LeadersTableSnapshot(**dto)
        await LeadersTableSnapshotOperations.add_leader_table_snapshot(snapshot)
            
        return {"status": "complete"}
    
    