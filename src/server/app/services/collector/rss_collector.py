from app.services.rss import RssService as RSS
from app.database.feed_item_operations import FeedItemOperations
from app.models.FeedItem import FeedItem


class RSSCollector:
    
    
    async def collect_all_rss_feeds(self):
        await self.collect_reuters_financial_news()
        
    
    
    async def collect_reuters_financial_news(self):
        
        # get most recent feed items from Reuters Financial news feed
        reuters_feed = await RSS.ReutersRSS.get_reuters_financial_news_rss_feed()

        # Check if each feed item exists, if not, add the feed entry        
        for feed_item in reuters_feed:
            print('feed_item', feed_item)
            
            existing_feed_entry = await FeedItemOperations.retrieve_feed_item_by_system_id(feed_item['systemId'])
            print('existing_feed_entry', existing_feed_entry)
            
            if not existing_feed_entry:
                item_instance = FeedItem(**feed_item)
                await FeedItemOperations.add_feed_item(item_instance)
            
            
        return {"status": "complete"}
        
        
    
    
    
    
    