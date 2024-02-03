from app.database.leaders_snapshot_operations import LeadersSnapshotOperations
from app.database.index_snapshot_operations import IndexSnapshotOperations
from app.database.notable_quote_snapshot_operations import NotableQuotesSnapshotOperations
from app.database.gainer_price_snapshot_operations import GainerPriceSnapshotOperations
from app.database.loser_price_snapshot_operations import LoserPriceSnapshotOperations
from app.database.leaders_table_snapshot_operations import LeadersTableSnapshotOperations

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
    
    async def get_stored_gainers_price_table():
        current = await GainerPriceSnapshotOperations().retrieve_most_recent_gainer_price_snapshot()
        return current.data
        
    async def get_stored_losers_price_table():
        current = await LoserPriceSnapshotOperations().retrieve_most_recent_loser_price_snapshot()
        return current.data
            
    async def get_stored_leaders_table():
        current = await LeadersTableSnapshotOperations().retrieve_most_recent_leader_table_snapshot()
        return current.data