from .rss_collector import RSSCollector
from .leaders_snapshot_collector import LeadersSnapshotCollector
from .index_snapshot_collector import IndexSnapshotCollector
from .notable_quotes_snapshot_collector import NotableQuotesSnapshotCollector



class CollectorService:
        
    class RSSCollector(RSSCollector):
        pass
    
    class LeadersSnapshotCollector(LeadersSnapshotCollector):
        pass
    
    class IndexSnapshotCollector(IndexSnapshotCollector):
        pass
    
    class NotableQuotesSnapshotCollector(NotableQuotesSnapshotCollector):
        pass
    
    