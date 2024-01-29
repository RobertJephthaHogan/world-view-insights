import feedparser
from bson import ObjectId




class ZDNetRSS:
    
        
    async def get_zdnet_feed():
        
        # URL of the Reuters RSS feed
        rss_url = "https://www.zdnet.com/news/rss.xml"

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
                "authors": item.media_credit,
                "guid": item.id,
                "systemId": f"zdnet-{item.id}",
            }
            
            feed_items.append(feed_item)
        
        return feed_items
    
        