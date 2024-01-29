import feedparser
from bson import ObjectId




class BloombergRSS:
    
        
    async def get_bloomberg_news_rss_feed():
        
        # URL of the Bloomberg News RSS feed via google news
        rss_url = "https://news.google.com/rss/search?q=when:24h+allinurl:bloomberg.com&hl=en-US&gl=US&ceid=US:en"

        # Parsing the RSS feed
        feed = feedparser.parse(rss_url)

        # Extracting the list of news items
        news_items = feed.entries
                
        feed_items = []
        
        # organize feed items and add to feed items list
        for item in news_items:
            feed_item = {
                'id': str(ObjectId()),
                "title": item.title,
                "description": item.description,
                "link": item.link,
                "publicationDate": item.published,
                "authors": [item.source],
                "guid": item.id,
                "systemId": f"bloomberg-{item.id}",
            }
            
            feed_items.append(feed_item)
        
        return feed_items
    
        