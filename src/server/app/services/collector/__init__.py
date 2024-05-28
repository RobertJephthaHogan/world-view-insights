from app.database.gainer_price_snapshot_operations import GainerPriceSnapshotOperations
from app.database.index_snapshot_operations import IndexSnapshotOperations
from app.database.leaders_snapshot_operations import LeadersSnapshotOperations
from app.database.notable_quote_snapshot_operations import NotableQuotesSnapshotOperations
from app.database.leaders_table_snapshot_operations import LeadersTableSnapshotOperations
from app.database.loser_price_snapshot_operations import LoserPriceSnapshotOperations
from app.database.most_active_snapshot_operations import MostActiveSnapshotOperations
from .rss_collector import RSSCollector
from .leaders_snapshot_collector import LeadersSnapshotCollector
from .index_snapshot_collector import IndexSnapshotCollector
from .notable_quotes_snapshot_collector import NotableQuotesSnapshotCollector
from .gainers.price_snapshot_collector import GainerPriceSnapshotCollector
from .losers.price_snapshot_collector import LoserPriceSnapshotCollector
from .leaders.leaders_table_snapshot_collector import LeadersTableSnapshotCollector
from .active.price_snapshot_collector import MostActiveSnapshotCollector
from .news_article_collector import NewsArticleCollector
from datetime import datetime


class CollectorService:
        
    class RSSCollector(RSSCollector):
        pass
    
    class LeadersSnapshotCollector(LeadersSnapshotCollector):
        pass
    
    class IndexSnapshotCollector(IndexSnapshotCollector):
        pass
    
    class NotableQuotesSnapshotCollector(NotableQuotesSnapshotCollector):
        pass
    
    class NewsArticleCollector(NewsArticleCollector):
        pass
    
    
    ##########################
    # Gainer Data Collection #
    ##########################
    
    class GainerPriceSnapshotCollector(GainerPriceSnapshotCollector):
        pass
    
    
    #########################
    # Loser Data Collection #
    #########################
    
    class LoserPriceSnapshotCollector(LoserPriceSnapshotCollector):
        pass
    
    
    ##########################
    # Leader Data Collection #
    ##########################
    
    class LeadersTableSnapshotCollector(LeadersTableSnapshotCollector):
        pass
    
        
    ###############################
    # Most Active Data Collection #
    ###############################
    
    class MostActiveSnapshotCollector(MostActiveSnapshotCollector):
        pass
    
    
    async def prune_unnecessary_entries():
        # Every day the system collects various kinds of data for quick
        # access as to not overload api requests from the provider.
        # We need to clear these extra entries out daily to keep
        # query times low
        
        # Check if today is not Saturday or Sunday
        not_weekend = datetime.today().weekday() < 5
        
        
        if not_weekend:
            
            # Prune Gainer Snapshots
            await GainerPriceSnapshotOperations.delete_old_entries(24)
                
            # Prune Index Snapshots
            await IndexSnapshotOperations.delete_old_entries(24)
        
            # Prune Leader Snapshots
            await LeadersSnapshotOperations.delete_old_entries(24)
            
            # Prune Notable Quote Snapshots
            await NotableQuotesSnapshotOperations.delete_old_entries(24)
        
            # Prune Leader Table Snapshots
            await LeadersTableSnapshotOperations.delete_old_entries(24)
        
            # Prune Loser Price Snapshots
            await LoserPriceSnapshotOperations.delete_old_entries(24)
        
            # Prune Most Active Snapshots
            await MostActiveSnapshotOperations.delete_old_entries(24)
        
        # Prune News Article Snapshots Every 90 Days
        #await MostActiveSnapshotOperations.delete_old_entries(2160)
        
        
        return {"status": "complete"}
