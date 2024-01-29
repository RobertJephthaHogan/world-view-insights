import feedparser
from bson import ObjectId




class VentureBeatRSS:
    
        
    async def get_venture_beat_news_feed():
        
        # URL of the Reuters RSS feed
        rss_url = "https://venturebeat.com/feed/"

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
                "authors": [item.author],
                "guid": item.id,
                "systemId": f"venture-beat-{item.id}",
            }
            
            feed_items.append(feed_item)
        
        return feed_items
    
        