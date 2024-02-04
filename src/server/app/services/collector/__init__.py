from .rss_collector import RSSCollector
from .leaders_snapshot_collector import LeadersSnapshotCollector
from .index_snapshot_collector import IndexSnapshotCollector
from .notable_quotes_snapshot_collector import NotableQuotesSnapshotCollector
from .gainers.price_snapshot_collector import GainerPriceSnapshotCollector
from .losers.price_snapshot_collector import LoserPriceSnapshotCollector
from .leaders.leaders_table_snapshot_collector import LeadersTableSnapshotCollector
from .active.price_snapshot_collector import MostActiveSnapshotCollector
from .news import NewsSnapshotCollector

class CollectorService:
        
    class RSSCollector(RSSCollector):
        pass
    
    class LeadersSnapshotCollector(LeadersSnapshotCollector):
        pass
    
    class IndexSnapshotCollector(IndexSnapshotCollector):
        pass
    
    class NotableQuotesSnapshotCollector(NotableQuotesSnapshotCollector):
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
    
    
    ###################
    # News Collection #
    ###################
    
    class NewsSnapshotCollector(NewsSnapshotCollector):
        pass