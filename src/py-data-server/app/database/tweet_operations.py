from beanie import PydanticObjectId
from pydantic import ValidationError
from typing import List, Union
from bson import ObjectId
from datetime import datetime, timedelta

from app.models.Tweet import Tweet, UpdateTweetModel


tweet_collection = Tweet

class TweetOperations:

    async def add_tweet(new_tweet: Tweet) -> Tweet:
        new_tweet.id = str(ObjectId())
        tweet = await new_tweet.create()
        return tweet


    async def retrieve_all_tweets() -> List[Tweet]:
        tweets = await tweet_collection.all().to_list()
        return tweets


    async def retrieve_tweet(id: Tweet) -> Tweet:
        tweet = await tweet_collection.get(str(id))
        if tweet:
            return tweet
        
    
    async def retrieve_tweets_paginated(page_size: int, page: int) -> List[Tweet]:
        # Calculate the number of documents to skip
        skip = (page - 1) * page_size
        # Query the database with skip and limit for pagination
        tweets = await Tweet.find().sort("-_id").skip(skip).limit(page_size).to_list()
        return tweets
    

    async def delete_tweet(id: PydanticObjectId) -> bool:
        try:
            tweet = await tweet_collection.get(str(id))
        except ValidationError as e:
            print(e.json())
        if tweet:
            await tweet.delete()
            return True


    async def update_tweet_data(id: PydanticObjectId, data: dict) -> Union[bool, Tweet]:
        des_body = {k: v for k, v in data.items() if v is not None}
        update_query = {"$set": {
            field: value for field, value in des_body.items()
        }}
        tweet = await tweet_collection.get(str(id))
        if tweet:
            await tweet.update(update_query)
            return tweet
        return False


    async def check_tweet_content_exists(content_str: str) -> bool:
        """
            Checks if any entry in the database has a 'content' attribute with the same string as content_str.
        """
        existing_entry = await tweet_collection.find_one({"content": content_str})
        return existing_entry is not None
    
    
    async def find_tweets_in_last_x_minutes(lookback_window: int) -> List[Tweet]:
        # Calculate the datetime for x minutes ago
        x_minutes_ago = datetime.utcnow() - timedelta(minutes=lookback_window)
        
        # Query the collection for tweets newer than x_minutes_ago
        cursor = tweet_collection.find({"time": {"$gt": x_minutes_ago}})
        
        tweets = []
        async for tweet in cursor:
            tweets.append(tweet) 
        
        return tweets