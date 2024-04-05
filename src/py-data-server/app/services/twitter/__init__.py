from typing import List, Union

from app.database.news_article_operations import NewsArticleOperations
from bson import ObjectId
from app.config import Settings
import tweepy
from bson import ObjectId
from datetime import datetime
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
    
    
    async def tweet_new_tweet(self, content):
        
        # Create the new tweet
        response = twitter_client.create_tweet(text=content)
        
        return response
    

    ####################################
    # Tweet DB op function usage below #
    ####################################

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
    

    ####################################
    # News Bot service functions below #
    ####################################


    async def execute_news_bot(self):

        # Get the last {x} news articles

        recent_news_articles = await NewsArticleOperations.retrieve_news_articles_paginated(5, 1)

        # for each of the news articles
        for news_article in recent_news_articles:

            link_to_wvi = f"https://worldviewinsights.com/"

            # generate the tweet string from the article
            tweet_content = f" ${news_article.tickers} - {news_article.title}. See more at {link_to_wvi} #{news_article.tickers}"
            
            tweet_info = {
                "id": str(ObjectId()),
                "title": 'News Article Notification Tweet',
                "type": 'news-article-tweet',
                "content": tweet_content,
                "time": datetime.now()
            }

            
            # check if the tweet has been tweeted before by matching the tweets content, If so, it is not a new tweet
            tweet_exists = await TweetOperations.check_tweet_content_exists(tweet_content)

            # if it is new, and meets tweet requirements, tweet the tweet
            if tweet_exists:
                # Do not create a duplicate tweet if the tweet content already exists
                pass

            if not tweet_exists:
                # Create the tweet, if it is posted successfully, create the db entry                
                try:
                    resp = await self.tweet_new_tweet(tweet_info['content'])
                    tweet_obj = Tweet(**tweet_info)
                    await TweetOperations.add_tweet(tweet_obj)
                    
                except Exception as e:
                    print('error', e)

        pass


    ##########################################
    # Insider TX Bot service functions below #
    ##########################################

    def extract_transaction_dates(self, transactions_dict):
        # Initialize an empty list to store the dates
        transaction_dates = []
        
        # Iterate over each transaction in the dictionary
        for transaction in transactions_dict.values():
            # Extract the transaction date and add it to the list
            transaction_dates.append(transaction['transactionDate'])
        
        return transaction_dates
    
    
    async def determine_num_transactions_clause(self, derivative_table, non_derivative_table):
        
        # Determine total number of transactions listed in the filing
        total_transactions = len(derivative_table['derivativeTransactions']) + len(non_derivative_table['nonDerivativeTransactions'])
        
        # Extract the filing dates
        non_derivative_transaction_dates = self.extract_transaction_dates(non_derivative_table['nonDerivativeTransactions'])
        derivative_transaction_dates = self.extract_transaction_dates(derivative_table['derivativeTransactions'])
        transaction_dates = non_derivative_transaction_dates + derivative_transaction_dates
        
        # determine if all transactions are on one date or on multiple dates
        parsed_days = [datetime.strptime(date, "%Y-%m-%d") for date in transaction_dates]
        all_same_day = all(date == parsed_days[0] for date in parsed_days)

        single_tx_date = None
        first_date_str = None
        first_date_str = None
        num_transactions_clause = None
        
        # if multiple dates, get the first and last date for clause creation
        if not all_same_day:
            first_date = min(parsed_days)
            last_date = max(parsed_days)
            # Convert back to strings 
            first_date_str = first_date.strftime("%Y-%m-%d")
            last_date_str = last_date.strftime("%Y-%m-%d")
            num_transactions_clause = f"{total_transactions} transactions from {first_date_str} to {last_date_str}"
        
        if all_same_day:
            single_tx_date = max(parsed_days)
            single_tx_date_str = single_tx_date.strftime("%Y-%m-%d")
            num_transactions_clause = f"{total_transactions} transactions on {single_tx_date_str}"
        
        return num_transactions_clause
        
        
    async def format_and_round(self, number):
        # Check if the number is a float and if its decimal part is non-zero
        if isinstance(number, float) and (number % 1 != 0):
            formatted_number = "{:,.0f}".format(round(number))
        else:
            formatted_number = "{:,.0f}".format(number)

        return formatted_number
    
    
    def format_as_usd(self, amount):
        # Format the number as USD currency
        formatted_currency = "${:,.2f}".format(amount)
        return formatted_currency
    

    async def execute_insider_tx_tweet_bot(self):
        
        # Get the last {x} purchase or sale transactions
        lookback_window = 1
        form_fours = await FormFourOperations.retrieve_form_fours_by_tx_type_paginated(lookback_window, 1, ['P', 'S'])
        
        # Go through each entry and generate a tweet dict for it
        for form_four in form_fours:
                        
            # Standard Transaction data for string generation
            filing_system_id = form_four.id
            symbol = form_four.issuerTradingSymbol
            rpt_owner_name = form_four.rptOwnerName
            purchase_or_sale = 'purchased' if form_four.transactionType == 'P' else 'sold'
            total_number_shares = await self.format_and_round(form_four.totalTransactionShares )
            security_type = form_four.securityTitle 
            total_tx_value = self.format_as_usd(form_four.totalTransactionSize)
            
            # Logic to determine number of transactions clause
            num_tx_clause = await self.determine_num_transactions_clause(form_four.derivativeTable, form_four.nonDerivativeTable)
            
            # Link to the filing
            link_to_filing = f"https://worldviewinsights.com/markets/insider-tx/{filing_system_id}"
            
            # Construct Link Content
            tweet_content = f"${symbol} - {rpt_owner_name} {purchase_or_sale} {total_number_shares} shares of {security_type} worth {total_tx_value} in {num_tx_clause}. See {link_to_filing} for more info. #{symbol}"
            number_of_characters = len(tweet_content)
            
            basic_content = f"${symbol} - Insider Trade detected on #{symbol} - See More at "
            
            
            tweet_info = {
                "id": str(ObjectId()),
                "title": 'Form Four Notification Tweet',
                "type": 'form-four-filing',
                "content": tweet_content,
                "time": datetime.now()
            }
            
            # Check if a tweet has been made in the last {x} minutes
            tweets_in_last_30 = await TweetOperations.find_tweets_in_last_x_minutes(30)
            
            # Check how many tweets have been made in the last 24 hours
            tweets_in_last_day = await TweetOperations.find_tweets_in_last_x_minutes(1440)
            is_below_cutoff_threshold = len(tweets_in_last_day) < 40
            
            # check if the tweet has been tweeted before by matching the tweets content, If so, it is not a new tweet
            tweet_exists = await TweetOperations.check_tweet_content_exists(tweet_content)
            
            if tweet_exists:
                # Do not create a duplicate tweet if the tweet content already exists
                pass
            
            # if the tweet does not exist and there has not been a tweet in the last 30 minutes, tweet the tweet
            if not tweet_exists and is_below_cutoff_threshold and not tweets_in_last_30:
                
                # Create the tweet, if it is posted successfully, create the db entry                
                try:
                    resp = await self.tweet_new_tweet(tweet_info['content'])
                    tweet_obj = Tweet(**tweet_info)
                    await TweetOperations.add_tweet(tweet_obj)
                    
                except Exception as e:
                    print('error', e)
                
                
            # other handling here if needed
        
        pass