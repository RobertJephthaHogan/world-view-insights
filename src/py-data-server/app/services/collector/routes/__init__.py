import json
from fastapi import APIRouter

from .. import CollectorService as Collector



router = APIRouter()

class CollectorController:
    
    # Test Collector
    @router.get("/test_collector/")
    async def test_collector():
        data = await Collector.collect_form_fours()
        return data