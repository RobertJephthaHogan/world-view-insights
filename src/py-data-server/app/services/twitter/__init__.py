from typing import List, Union
from bson import ObjectId
from app.config import Settings
import tweepy
from app.models.Tweet import Tweet, UpdateTweetModel
from app.database.tweet_operations import TweetOperations
from app.database.form_four_operations import FormFour, FormFourOperations

wvi_insights_api_key = Settings().WVI_INSIGHTS_API_KEY
wvi_insights_api_key_secret = Settings().WVI_INSIGHTS_API_KEY_SECRET
wvi_insights_bearer_token = Settings().WVI_INSIGHTS_BEARER_TOKEN
wvi_insights_access_token = Settings().WVI_INSIGHTS_ACCESS_TOKEN
wvi_insights_access_token_secret = Settings().WVI_INSIGHTS_ACCESS_TOKEN_SECRET



twitter_client = tweepy.Client(
                                #bearer_token=wvi_insights_bearer_token,
                                consumer_key=wvi_insights_api_key,
                                consumer_secret=wvi_insights_api_key_secret,
                                access_token=wvi_insights_access_token,
                                access_token_secret=wvi_insights_access_token_secret
                               )



class TwitterService:
    
    
    async def tweet_new_tweet():
        # TODO: ATTEMPT CONNECTION AND PRINT OUT INFO TO CONFIRM WORKING
        
        print('wvi_insights_api_key', wvi_insights_api_key)
        print('wvi_insights_api_key_secret', wvi_insights_api_key_secret)
        print('wvi_insights_access_token', wvi_insights_access_token)
        print('wvi_insights_access_token_secret', wvi_insights_access_token_secret)
        response = twitter_client.create_tweet(text="Test")

        
        return {}
    
    
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
        
    
    async def execute_tweet_bot():
        
        # Get the last 20 purchase or sale transactions
        form_fours = await FormFourOperations.retrieve_form_fours_by_tx_type_paginated(1, 1, ['P', 'S'])
        
        #print('form_fours', form_fours)
        
        # Go through each entry and generate a tweet dict for it
        for form_four in form_fours:
                        
            symbol = form_four.issuerTradingSymbol
            rpt_owner_name = form_four.rptOwnerName
            purchase_or_sale = "purchased" #TODO
            total_number_shares = "100" #TODO
            security_type = "Common Stock" #TODO
            total_tx_value = "100,000" #TODO
            num_transactions = "123" #TODO
            
            #TODO : Finish final tweet content string
            tweet_content = f"${symbol} - {rpt_owner_name} {purchase_or_sale} {total_number_shares} shares of {security_type} worth {total_tx_value} in {num_transactions}"
            
            basic_content = f"${symbol} - Insider Trade detected on #{symbol} - See More at "
            
            tweet_info = {
                "content": basic_content
            }
            
            # check if the tweet has been tweeted before by matching the tweets content, If so, it is not a new tweet
            tweet_exists = await TweetOperations.check_tweet_content_exists(basic_content)
            print('tweet_exists', tweet_exists)
            
            if tweet_exists:
                # Do not create a duplicate tweet if the tweet content already exists
                pass
            
            if not tweet_exists:
                # TODO: Create the tweet, if it is posted successfully, create the db entry
                pass
        
            # if the tweet has not been tweeted before, it is new and you 
        
        pass