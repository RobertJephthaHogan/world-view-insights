from app.database.fmp_news_snapshot_operations import FmpNewsSnapshotOperations




class Storage:
    
        
    async def get_stored_fmp_articles():
        current = await FmpNewsSnapshotOperations().retrieve_most_recent_fmp_news_snapshot()
        return current.data
    
    