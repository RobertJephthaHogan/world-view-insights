from .rss_collector import RSSCollector
from .leaders_snapshot_collector import LeadersSnapshotCollector
from .index_snapshot_collector import IndexSnapshotCollector
from .notable_quotes_snapshot_collector import NotableQuotesSnapshotCollector
from .gainers.price_snapshot_collector import GainerPriceSnapshotCollector


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