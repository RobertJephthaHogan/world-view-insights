from fastapi import FastAPI, BackgroundTasks
from apscheduler.schedulers.asyncio  import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from datetime import datetime, timezone
import pytz
from app.services.collector import CollectorService
from app.services.twitter import TwitterService
import time




eastern_timezone = pytz.timezone('America/New_York')



class ScheduledServiceService:
    
    
    def startScheduler(self):
        scheduler = AsyncIOScheduler()
        scheduler.add_job(self.collect_news_articles, "interval", seconds=10)  # Check every 2 hours
        scheduler.add_job(self.collect_form_fours, "interval", seconds=10)  # Check every 10 seconds
        time.sleep(5)
        scheduler.add_job(self.execute_tweet_bot, "interval", seconds=10)  # Check every 10 seconds
        
        scheduler.start()
        
        
    async def perform_scheduled_task(self, service_id: int, action: str, target_id: str):
        print(f"Performing task for service {service_id}: {action} at {datetime.now()}")
        # Perform Scheduled Service Handling Based on 'action'

    
    async def collect_form_fours(self):
        print('Collecting Form Fours...')
        await CollectorService.collect_form_fours()
        
        
    async def execute_tweet_bot(self):
        print('Executing Tweet Bot...')
        await TwitterService().execute_insider_tx_tweet_bot()
    
    
    async def collect_news_articles(self):
        print('Collecting News Articles...')
        await CollectorService.collect_business_news_articles() 
        
        
    def shutdownScheduler(self):
        scheduler = AsyncIOScheduler()
        scheduler.shutdown()
        
    
    
    