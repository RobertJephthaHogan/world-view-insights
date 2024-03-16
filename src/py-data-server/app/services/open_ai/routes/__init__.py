import json
from fastapi import APIRouter

from .. import OpenAiService 



router = APIRouter()

class OpenAiController:
    
    # Test open ai prompt 
    @router.get("/test_open_ai/")
    async def test_open_ai():
        data = await OpenAiService.test_open_ai()
        return data