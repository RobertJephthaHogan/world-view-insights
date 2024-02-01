from app.database.leaders_snapshot_operations import LeadersSnapshotOperations
from app.database.index_snapshot_operations import IndexSnapshotOperations
from app.database.notable_quote_snapshot_operations import NotableQuotesSnapshotOperations


class Storage:
    
    async def get_stored_market_leader_quotes(limit):
        current = await LeadersSnapshotOperations().retrieve_most_recent_leaders_snapshot()
        return current.data
    
    async def get_stored_major_index_overview():
        current = await IndexSnapshotOperations().retrieve_most_recent_index_snapshot()
        return current.data
    
    async def get_stored_notable_quotes():
        current = await NotableQuotesSnapshotOperations().retrieve_most_recent_nc_snapshot()
        return current.data
        