import feedparser
from bson import ObjectId




class ReutersRSS:
    
        
    async def get_reuters_financial_news_rss_feed():
        
        # URL of the Reuters RSS feed
        rss_url = "https://ir.thomsonreuters.com/rss/news-releases.xml?items=15"

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
                "authors": item.authors,
                "guid": item.id,
                "systemId": f"reuters-financial-{item.id}",
            }
            
            feed_items.append(feed_item)
        
        return feed_items
    
        
        
    async def get_reuters_event_calendar_rss_feed():
        #TODO: Reuters Calendar Events RSS Feed
        return {}
    
    
    async def get_reuters_sec_filings_rss_feed():
        #TODO: Reuters SEC Filings RSS Feed
        return {}
    
    
    pass