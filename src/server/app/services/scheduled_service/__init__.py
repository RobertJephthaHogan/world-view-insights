from fastapi import FastAPI, BackgroundTasks
from apscheduler.schedulers.asyncio  import AsyncIOScheduler
from datetime import datetime, timezone
from app.database.scheduled_service_operations import ScheduledServiceOperations
from app.services.collector.rss_collector import RSSCollector
from app.services.collector.leaders_snapshot_collector import LeadersSnapshotCollector
from app.services.collector.index_snapshot_collector import IndexSnapshotCollector
from app.services.collector.notable_quotes_snapshot_collector import NotableQuotesSnapshotCollector
from app.services.collector.gainers.price_snapshot_collector import GainerPriceSnapshotCollector
import pytz
import time






class ScheduledServiceService: # as agonizing as this class name is, I'll continue to follow the convention I have been 
    
    
    def startScheduler(self):
        scheduler = AsyncIOScheduler()
        scheduler.add_job(self.collect_leaders_snapshot, "interval", seconds=60)  # Check every 60 seconds
        time.sleep(5) # space out minute interval services
        scheduler.add_job(self.collect_index_snapshots, "interval", seconds=60)  # Check every 60 seconds
        time.sleep(5) # space out minute interval services
        scheduler.add_job(self.collect_notable_quote_snapshots, "interval", seconds=60)  # Check every 60 seconds
        time.sleep(5) # space out minute interval services
        scheduler.add_job(self.collect_gainer_price_snapshots,  "interval", seconds=303) # Check every 303 seconds
        scheduler.add_job(self.collect_all_rss_feeds, "interval", seconds=900)  # update rss feeds every 15 min
        scheduler.add_job(self.check_scheduled_tasks, "interval", seconds=10)  # Check every 10 seconds
        scheduler.start()
        
        
    async def perform_scheduled_task(self, service_id: int, action: str, target_id: str):
        print(f"Performing task for service {service_id}: {action} at {datetime.now()}")
        # Perform Scheduled Service Handling Based on 'action'
        
    
    async def collect_all_rss_feeds(self):
        print('Collecting RSS Feeds...')
        await RSSCollector().collect_all_rss_feeds()    
        
        
    async def collect_leaders_snapshot(self):
        eastern = pytz.timezone('US/Eastern') # set tz eastern
        current_time_eastern = datetime.now(eastern) # current time in Eastern tz

        # Define the target time to start and stop collecting (8:00 AM , 5:15PM) 
        start_time = current_time_eastern.replace(hour=8, minute=0, second=0, microsecond=0)
        end_time = current_time_eastern.replace(hour=17, minute=15, second=0, microsecond=0)

        # Check if the current time is after the start_time and before end_time
        after_start_time = current_time_eastern > start_time
        before_end_time = current_time_eastern < end_time
        
        # if so, collect the current leaders snapshot
        if after_start_time and before_end_time:
            print('Collecting Leaders Snapshot...')
            await LeadersSnapshotCollector().collect_leaders_snapshot()    
        else:
            pass # do not collect if not in collection time range
        
        
    async def collect_index_snapshots(self):
        eastern = pytz.timezone('US/Eastern') # set tz eastern
        current_time_eastern = datetime.now(eastern) # current time in Eastern tz

        # Define the target time to start and stop collecting (8:00 AM , 5:15PM) 
        start_time = current_time_eastern.replace(hour=8, minute=0, second=0, microsecond=0)
        end_time = current_time_eastern.replace(hour=17, minute=15, second=0, microsecond=0)

        # Check if the current time is after the start_time and before end_time
        after_start_time = current_time_eastern > start_time
        before_end_time = current_time_eastern < end_time
        
        # if so, collect the current leaders snapshot
        if after_start_time and before_end_time:
            print('Collecting Index Snapshot...')
            await IndexSnapshotCollector().collect_index_snapshots()    
        else:
            pass # do not collect if not in collection time range

    
    async def collect_notable_quote_snapshots(self):
        eastern = pytz.timezone('US/Eastern') # set tz eastern
        current_time_eastern = datetime.now(eastern) # current time in Eastern tz

        # Define the target time to start and stop collecting (8:00 AM , 5:15PM) 
        start_time = current_time_eastern.replace(hour=8, minute=0, second=0, microsecond=0)
        end_time = current_time_eastern.replace(hour=17, minute=15, second=0, microsecond=0)

        # Check if the current time is after the start_time and before end_time
        after_start_time = current_time_eastern > start_time
        before_end_time = current_time_eastern < end_time
        
        # if so, collect the current leaders snapshot
        if after_start_time and before_end_time:
            print('Collecting Notable Quote Snapshot...')
            await NotableQuotesSnapshotCollector().collect_notable_quotes_snapshots()    
        else:
            pass # do not collect if not in collection time range
        
        
    async def collect_gainer_price_snapshots(self):
        eastern = pytz.timezone('US/Eastern') # set tz eastern
        current_time_eastern = datetime.now(eastern) # current time in Eastern tz

        # Define the target time to start and stop collecting (8:00 AM , 5:15PM) 
        start_time = current_time_eastern.replace(hour=8, minute=0, second=0, microsecond=0)
        end_time = current_time_eastern.replace(hour=17, minute=15, second=0, microsecond=0)

        # Check if the current time is after the start_time and before end_time
        after_start_time = current_time_eastern > start_time
        before_end_time = current_time_eastern < end_time
        
        # if so, collect the current leaders snapshot
        if after_start_time and before_end_time:
            print('Collecting Gainers Prices Snapshot...')
            await GainerPriceSnapshotCollector().collect_gainer_price_snapshots()    
        else:
            pass # do not collect if not in collection time range
        

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
        