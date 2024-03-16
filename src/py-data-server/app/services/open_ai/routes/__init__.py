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
    
    
    # Write Competitor Article
    @router.get("/write_competitor_article/")
    async def write_competitor_article():
        
        test_article = 'Adobe Systems (NASDAQ:ADBE) shares dropped more than 14% intra-day today after it released guidance for the current quarter that fell short of expectations regarding a crucial revenue metric, sparking concerns over increasing competition affecting its growth trajectory. For the fiscal second quarter, Adobe has set a target for digital media net new revenue, at $440 million, which is below the approximately $460 million expected by analysts. The company has forecasted adjusted earnings per share (EPS) to be between $4.35 and $4.40, with revenue projections ranging from $5.25 billion to $5.30 billion. These figures compare less favorably with analyst predictions of $4.39 in EPS and $5.31 billion in revenue. This subdued forecast comes despite Adobe posting fiscal first-quarter results that exceeded analyst expectations, with an EPS of $4.48 on revenue of $5.18 billion, against forecasts of $4.38 in EPS on $5.14 billion in revenue.'
        
        data = await OpenAiService.write_competitor_article(test_article)
        return data