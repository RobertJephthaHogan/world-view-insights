from app.services.rss import RssService as RSS
from app.database.feed_item_operations import FeedItemOperations
from app.models.FeedItem import FeedItem


class RSSCollector:
    
    
    async def collect_all_rss_feeds(self):
        await self.collect_reuters_financial_news()
        await self.collect_zdnet_news()
        await self.collect_bbc_news()
        await self.collect_venture_beat_news()
        await self.collect_bloomberg_news()
        
    
    
    async def collect_reuters_financial_news(self):
        
        # get most recent feed items from Reuters Financial news feed
        reuters_feed = await RSS.ReutersRSS.get_reuters_financial_news_rss_feed()

        # Check if each feed item exists, if not, add the feed entry        
        for feed_item in reuters_feed:
            
            existing_feed_entry = await FeedItemOperations.retrieve_feed_item_by_system_id(feed_item['systemId'])
            
            if not existing_feed_entry:
                item_instance = FeedItem(**feed_item)
                await FeedItemOperations.add_feed_item(item_instance)
            
        return {"status": "complete"}
    
    
    async def collect_zdnet_news(self):
        
        # get most recent feed items from ZDNet news feed
        zdnet_feed = await RSS.ZDNetRSS.get_zdnet_feed()

        # Check if each feed item exists, if not, add the feed entry        
        for feed_item in zdnet_feed:
            
            existing_feed_entry = await FeedItemOperations.retrieve_feed_item_by_system_id(feed_item['systemId'])
            
            if not existing_feed_entry:
                item_instance = FeedItem(**feed_item)
                await FeedItemOperations.add_feed_item(item_instance)
            
        return {"status": "complete"}
    
    
    async def collect_bbc_news(self):
        
        # get most recent feed items from BBC news feed
        bbc_feed = await RSS.BbcRSS.get_bbc_news_feed()

        # Check if each feed item exists, if not, add the feed entry        
        for feed_item in bbc_feed:
            
            existing_feed_entry = await FeedItemOperations.retrieve_feed_item_by_system_id(feed_item['systemId'])
            
            if not existing_feed_entry:
                item_instance = FeedItem(**feed_item)
                await FeedItemOperations.add_feed_item(item_instance)
            
        return {"status": "complete"}
    
        
    async def collect_venture_beat_news(self):
        
        # get most recent feed items from Venture Beat news feed
        venture_beat_feed = await RSS.VentureBeatRSS.get_venture_beat_news_feed()

        # Check if each feed item exists, if not, add the feed entry        
        for feed_item in venture_beat_feed:
            
            existing_feed_entry = await FeedItemOperations.retrieve_feed_item_by_system_id(feed_item['systemId'])
            
            if not existing_feed_entry:
                item_instance = FeedItem(**feed_item)
                await FeedItemOperations.add_feed_item(item_instance)
            
        return {"status": "complete"}
        
            
    async def collect_bloomberg_news(self):
        
        # get most recent feed items from Bloomberg news feed
        bloomberg_feed = await RSS.BloombergRSS.get_bloomberg_news_rss_feed()

        # Check if each feed item exists, if not, add the feed entry        
        for feed_item in bloomberg_feed:
            
            existing_feed_entry = await FeedItemOperations.retrieve_feed_item_by_system_id(feed_item['systemId'])
            
            if not existing_feed_entry:
                item_instance = FeedItem(**feed_item)
                await FeedItemOperations.add_feed_item(item_instance)
            
        return {"status": "complete"}
        
    
    
    
    
    