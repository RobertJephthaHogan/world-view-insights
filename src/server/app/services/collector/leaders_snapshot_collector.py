from app.services.rss import RssService as RSS
from app.database.leaders_snapshot_operations import LeadersSnapshotOperations
from app.models.FeedItem import FeedItem
from app.services.data import DataService
from app.models.LeadersSnapshot import LeadersSnapshot
from bson import ObjectId
from datetime import datetime


class LeadersSnapshotCollector:
    
    
    async def collect_all_rss_feeds(self):
        await self.collect_leaders_snapshot()

    
    async def collect_leaders_snapshot(self):
        
        # get the data for the snapshot
        data = await DataService.get_market_leader_quotes(10)

        # store the data        
        dto = {
            'id': str(ObjectId()),
            'data': data,
            'creationDate': datetime.now()
        }
        snapshot = LeadersSnapshot(**dto)
        await LeadersSnapshotOperations.add_leaders_snapshot(snapshot)
            
        return {"status": "complete"}
    
    