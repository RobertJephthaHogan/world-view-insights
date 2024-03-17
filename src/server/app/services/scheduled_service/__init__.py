from fastapi import FastAPI, BackgroundTasks
from apscheduler.schedulers.asyncio  import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from datetime import datetime, timezone
from app.database.scheduled_service_operations import ScheduledServiceOperations
from app.services.collector.rss_collector import RSSCollector
from app.services.collector.leaders_snapshot_collector import LeadersSnapshotCollector
from app.services.collector.index_snapshot_collector import IndexSnapshotCollector
from app.services.collector.notable_quotes_snapshot_collector import NotableQuotesSnapshotCollector
from app.services.collector.gainers.price_snapshot_collector import GainerPriceSnapshotCollector
from app.services.collector.losers.price_snapshot_collector import LoserPriceSnapshotCollector
from app.services.collector.leaders.leaders_table_snapshot_collector import LeadersTableSnapshotCollector
from app.services.collector.active.price_snapshot_collector import MostActiveSnapshotCollector
from app.services.collector.news_article_collector import NewsArticleCollector
from app.services.collector import CollectorService
import pytz
import time



eastern_timezone = pytz.timezone('America/New_York')






class ScheduledServiceService: # as agonizing as this class name is, I'll continue to follow the convention I have been 
    
    def startScheduler(self):
        scheduler = AsyncIOScheduler()
        scheduler.add_job(self.collect_leaders_snapshot, "interval", seconds=60)  # Check every 60 seconds
        time.sleep(5) # space out minute interval services
        scheduler.add_job(self.collect_index_snapshots, "interval", seconds=60)  # Check every 60 seconds
        time.sleep(5) # space out minute interval services
        scheduler.add_job(self.collect_notable_quote_snapshots, "interval", seconds=60)  # Check every 60 seconds
        time.sleep(5) # space out minute interval services
        scheduler.add_job(self.collect_gainer_price_snapshots,  "interval", seconds=290) # Check every 290 seconds
        scheduler.add_job(self.collect_loser_price_snapshots,  "interval", seconds=310) # Check every 310 seconds
        scheduler.add_job(self.collect_leader_price_snapshots,  "interval", seconds=330) # Check every 330 seconds
        scheduler.add_job(self.collect_most_active_price_snapshots,  "interval", seconds=350) # Check every 350 seconds
        scheduler.add_job(self.collect_all_rss_feeds, "interval", seconds=900)  # update rss feeds every 15 min
        scheduler.add_job(self.check_scheduled_tasks, "interval", seconds=10)  # Check every 10 seconds
        scheduler.add_job(self.prune_old_collections, "interval", seconds=3600)

        # scheduler.add_job( # prune old collections every hour
        #     self.prune_old_collections, 
        #     trigger=CronTrigger(hour=23, minute=0, timezone=eastern_timezone)
        # )
        
        scheduler.start()
        
        
    async def perform_scheduled_task(self, service_id: int, action: str, target_id: str):
        print(f"Performing task for service {service_id}: {action} at {datetime.now()}")
        # Perform Scheduled Service Handling Based on 'action'
        
    
    async def collect_all_rss_feeds(self):
        print('Collecting RSS Feeds...')
        await RSSCollector().collect_all_rss_feeds()    
        
        
    async def collect_leaders_snapshot(self):
        # Check if today is not Saturday or Sunday
        not_weekend = datetime.today().weekday() < 5
        
        eastern = pytz.timezone('US/Eastern') # set tz eastern
        current_time_eastern = datetime.now(eastern) # current time in Eastern tz

        # Define the target time to start and stop collecting (8:00 AM , 5:15PM) 
        start_time = current_time_eastern.replace(hour=8, minute=0, second=0, microsecond=0)
        end_time = current_time_eastern.replace(hour=17, minute=15, second=0, microsecond=0)

        # Check if the current time is after the start_time and before end_time
        after_start_time = current_time_eastern > start_time
        before_end_time = current_time_eastern < end_time
        
        # if so, collect the current leaders snapshot
        if after_start_time and before_end_time and not_weekend:
            print('Collecting Leaders Snapshot...')
            await LeadersSnapshotCollector().collect_leaders_snapshot()    
        else:
            pass # do not collect if not in collection time range
        
        
    async def collect_index_snapshots(self):
        # Check if today is not Saturday or Sunday
        not_weekend = datetime.today().weekday() < 5
        
        eastern = pytz.timezone('US/Eastern') # set tz eastern
        current_time_eastern = datetime.now(eastern) # current time in Eastern tz

        # Define the target time to start and stop collecting (8:00 AM , 5:15PM) 
        start_time = current_time_eastern.replace(hour=8, minute=0, second=0, microsecond=0)
        end_time = current_time_eastern.replace(hour=17, minute=15, second=0, microsecond=0)

        # Check if the current time is after the start_time and before end_time
        after_start_time = current_time_eastern > start_time
        before_end_time = current_time_eastern < end_time
        
        # if so, collect the index snapshot
        if after_start_time and before_end_time and not_weekend:
            print('Collecting Index Snapshot...')
            await IndexSnapshotCollector().collect_index_snapshots()    
        else:
            pass # do not collect if not in collection time range

    
    async def collect_notable_quote_snapshots(self):
        # Check if today is not Saturday or Sunday
        not_weekend = datetime.today().weekday() < 5
        
        eastern = pytz.timezone('US/Eastern') # set tz eastern
        current_time_eastern = datetime.now(eastern) # current time in Eastern tz

        # Define the target time to start and stop collecting (8:00 AM , 5:15PM) 
        start_time = current_time_eastern.replace(hour=8, minute=0, second=0, microsecond=0)
        end_time = current_time_eastern.replace(hour=17, minute=15, second=0, microsecond=0)

        # Check if the current time is after the start_time and before end_time
        after_start_time = current_time_eastern > start_time
        before_end_time = current_time_eastern < end_time
        
        # if so, collect the notable quotes snapshot
        if after_start_time and before_end_time and not_weekend:
            print('Collecting Notable Quote Snapshot...')
            await NotableQuotesSnapshotCollector().collect_notable_quotes_snapshots()    
        else:
            pass # do not collect if not in collection time range
        
        
    async def collect_gainer_price_snapshots(self):
        # Check if today is not Saturday or Sunday
        not_weekend = datetime.today().weekday() < 5
        
        eastern = pytz.timezone('US/Eastern') # set tz eastern
        current_time_eastern = datetime.now(eastern) # current time in Eastern tz

        # Define the target time to start and stop collecting (8:00 AM , 5:15PM) 
        start_time = current_time_eastern.replace(hour=8, minute=0, second=0, microsecond=0)
        end_time = current_time_eastern.replace(hour=17, minute=15, second=0, microsecond=0)

        # Check if the current time is after the start_time and before end_time
        after_start_time = current_time_eastern > start_time
        before_end_time = current_time_eastern < end_time
        
        # if so, collect the gainer prices snapshot
        if after_start_time and before_end_time and not_weekend:
            print('Collecting Gainers Prices Snapshot...')
            await GainerPriceSnapshotCollector().collect_gainer_price_snapshots()    
        else:
            pass # do not collect if not in collection time range
        
    
            
    async def collect_loser_price_snapshots(self):
        # Check if today is not Saturday or Sunday
        not_weekend = datetime.today().weekday() < 5
        
        eastern = pytz.timezone('US/Eastern') # set tz eastern
        current_time_eastern = datetime.now(eastern) # current time in Eastern tz

        # Define the target time to start and stop collecting (8:00 AM , 5:15PM) 
        start_time = current_time_eastern.replace(hour=8, minute=0, second=0, microsecond=0)
        end_time = current_time_eastern.replace(hour=17, minute=15, second=0, microsecond=0)

        # Check if the current time is after the start_time and before end_time
        after_start_time = current_time_eastern > start_time
        before_end_time = current_time_eastern < end_time
        
        # if so, collect the loser prices snapshot
        if after_start_time and before_end_time and not_weekend:
            print('Collecting Losers Prices Snapshot...')
            await LoserPriceSnapshotCollector().collect_loser_price_snapshots()    
        else:
            pass # do not collect if not in collection time range
        
        
    async def collect_leader_price_snapshots(self):
        # Check if today is not Saturday or Sunday
        not_weekend = datetime.today().weekday() < 5
        
        eastern = pytz.timezone('US/Eastern') # set tz eastern
        current_time_eastern = datetime.now(eastern) # current time in Eastern tz

        # Define the target time to start and stop collecting (8:00 AM , 5:15PM) 
        start_time = current_time_eastern.replace(hour=8, minute=0, second=0, microsecond=0)
        end_time = current_time_eastern.replace(hour=17, minute=15, second=0, microsecond=0)

        # Check if the current time is after the start_time and before end_time
        after_start_time = current_time_eastern > start_time
        before_end_time = current_time_eastern < end_time
        
        # if so, collect the leader prices snapshot
        if after_start_time and before_end_time and not_weekend:
            print('Collecting Leaders Prices Snapshot...')
            await LeadersTableSnapshotCollector().collect_leader_price_snapshots()    
        else:
            pass # do not collect if not in collection time range
        
            
    async def collect_most_active_price_snapshots(self):
        # Check if today is not Saturday or Sunday
        not_weekend = datetime.today().weekday() < 5
        
        eastern = pytz.timezone('US/Eastern') # set tz eastern
        current_time_eastern = datetime.now(eastern) # current time in Eastern tz

        # Define the target time to start and stop collecting (8:00 AM , 5:15PM) 
        start_time = current_time_eastern.replace(hour=8, minute=0, second=0, microsecond=0)
        end_time = current_time_eastern.replace(hour=17, minute=15, second=0, microsecond=0)

        # Check if the current time is after the start_time and before end_time
        after_start_time = current_time_eastern > start_time
        before_end_time = current_time_eastern < end_time
        
        # if so, collect the most active stocks prices snapshot
        if after_start_time and before_end_time and not_weekend:
            print('Collecting Most Active Stocks Prices Snapshot...')
            await MostActiveSnapshotCollector().collect_most_active_snapshots()    
        else:
            pass # do not collect if not in collection time range
        
        
    async def collect_business_news_articles(self):
        print('Collecting Business News Articles...')
        await NewsArticleCollector.collect_business_news_articles() 
        
        
    async def prune_old_collections(self):
        await CollectorService.prune_unnecessary_entries()
        

    async def check_scheduled_tasks(self):
        current_time = datetime.now().astimezone(timezone.utc) # current time in utc
        scheduled_services = await ScheduledServiceOperations.retrieve_unexecuted_scheduled_services()
                
        for service in scheduled_services:
            task_time = service.time 
            
            # force utc compare
            current_time = current_time.replace(tzinfo=None)
            task_time = task_time.replace(tzinfo=None)
             
            is_past_task_time = current_time >= task_time         
               
            if is_past_task_time:
                await self.perform_scheduled_task(service.id, service.action, service.target_id)
        
    
    def shutdownScheduler(self):
        scheduler = AsyncIOScheduler()
        scheduler.shutdown()
        