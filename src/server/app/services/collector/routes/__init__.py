import json
from fastapi import APIRouter

from app.services.collector import CollectorService as Collector



router = APIRouter()

class CollectorController:
    
    # Get Market Leader Quotes (populates ticker banner component)
    @router.get("/test_collector/")
    async def test_rss():
        data = await Collector.LeadersSnapshotCollector().collect_leaders_snapshot()
        return data