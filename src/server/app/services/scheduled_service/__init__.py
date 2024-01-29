from fastapi import FastAPI, BackgroundTasks
from apscheduler.schedulers.asyncio  import AsyncIOScheduler
from datetime import datetime, timezone
from app.database.scheduled_service_operations import ScheduledServiceOperations
from app.services.collector.rss_collector import RSSCollector





class ScheduledServiceService: # as agonizing as this class name is, I'll continue to follow the convention I have been 
    
    
    def startScheduler(self):
        scheduler = AsyncIOScheduler()
        scheduler.add_job(self.check_scheduled_tasks, "interval", seconds=10)  # Check every 10 seconds
        scheduler.add_job(self.collect_all_rss_feeds, "interval", seconds=3600)  # update rss feeds every hour
        scheduler.start()
        
        
    async def perform_scheduled_task(self, service_id: int, action: str, target_id: str):
        print(f"Performing task for service {service_id}: {action} at {datetime.now()}")
        # Perform Scheduled Service Handling Based on 'action'
        
    
    async def collect_all_rss_feeds(self):
        print('Collecting RSS Feeds...')
        await RSSCollector().collect_all_rss_feeds()    
    

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
        