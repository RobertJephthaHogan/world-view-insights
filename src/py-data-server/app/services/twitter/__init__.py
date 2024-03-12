from typing import List, Union
from bson import ObjectId
from app.models.Tweet import Tweet, UpdateTweetModel
from app.database.tweet_operations import TweetOperations



class TwitterService:
    
    async def add_tweet(new_tweet: Tweet) -> Tweet:
        tweet = await TweetOperations.add_tweet(new_tweet)
        return tweet


    async def retrieve_all_tweets() -> List[Tweet]:
        tweets = await TweetOperations.retrieve_all_tweets()
        return tweets


    async def retrieve_tweet(id: Tweet) -> Tweet:
        tweet = await TweetOperations.retrieve_tweet(id)
        if tweet:
            return tweet
        return None # if no tweet if found, return None
    
    
    async def retrieve_tweets_paginated(page_size: int, page: int):
        tweets = await TweetOperations.retrieve_tweets_paginated(page_size, page)
        return tweets
    
    
    async def delete_tweet(id):
        deleted_tweet = await TweetOperations.delete_tweet(id)
        return deleted_tweet
        