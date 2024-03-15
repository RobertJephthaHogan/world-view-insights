import json
from fastapi import APIRouter

from .. import TwitterService 



router = APIRouter()

class CollectorController:
    
    # Test creating a new tweet
    @router.get("/test_tweet_new_tweet/")
    async def test_tweet_new_tweet():
        data = await TwitterService.tweet_new_tweet()
        return data