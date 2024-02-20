import feedparser
from bson import ObjectId




class BbcRSS:
    
        
    async def get_bbc_news_feed():
        
        # URL of the BBS RSS feed
        rss_url = "https://feeds.bbci.co.uk/news/rss.xml?edition=us"

        # Parsing the RSS feed
        feed = feedparser.parse(rss_url)

        # Extracting the list of news items
        news_items = feed.entries
                
        feed_items = []
        
        # organize feed items and add to feed items list
        for item in news_items:
            feed_item = {
                'id': str(ObjectId()),
                "title": getattr(item, 'title', ''),
                "description": getattr(item, 'description', ''),
                "link": getattr(item, 'link', ''),
                "publicationDate": getattr(item, 'published', ''),
                "authors": [],
                "guid": item.id,
                "systemId": f"bbc-{item.id}",
            }
            
            feed_items.append(feed_item)
        
        return feed_items
    
        