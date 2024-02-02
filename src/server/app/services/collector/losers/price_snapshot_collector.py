from app.services.rss import RssService as RSS
from app.database.loser_price_snapshot_operations import LoserPriceSnapshotOperations
from app.services.data import DataService
from app.models.LoserPriceSnapshot import LoserPriceSnapshot
from bson import ObjectId
from datetime import datetime


class LoserPriceSnapshotCollector:
    
    
    async def collect_loser_price_snapshots(self):
        
        # get the data for the snapshot
        data = await DataService.get_losers_price_table()

        # store the data        
        dto = {
            'id': str(ObjectId()),
            'data': data,
            'creationDate': datetime.now()
        }
        snapshot = LoserPriceSnapshot(**dto)
        await LoserPriceSnapshotOperations.add_loser_price_snapshot(snapshot)
            
        return {"status": "complete"}
    
    