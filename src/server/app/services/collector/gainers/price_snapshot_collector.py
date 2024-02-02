from app.services.rss import RssService as RSS
from app.database.gainer_price_snapshot_operations import GainerPriceSnapshotOperations
from app.services.data import DataService
from app.models.GainerPriceSnapshot import GainerPriceSnapshot
from bson import ObjectId
from datetime import datetime


class GainerPriceSnapshotCollector:
    
    
    async def collect_gainer_price_snapshots(self):
        
        # get the data for the snapshot
        data = await DataService.get_gainers_price_table()

        # store the data        
        dto = {
            'id': str(ObjectId()),
            'data': data,
            'creationDate': datetime.now()
        }
        snapshot = GainerPriceSnapshot(**dto)
        await GainerPriceSnapshotOperations.add_gainer_price_snapshot(snapshot)
            
        return {"status": "complete"}
    
    