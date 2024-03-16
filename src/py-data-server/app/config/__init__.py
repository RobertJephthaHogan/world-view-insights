from typing import Optional
import os
from dotenv import load_dotenv
from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic_settings import BaseSettings

from app.models.FormFour import FormFour
from app.models.Tweet import Tweet


# Load the environment variables
load_dotenv()

class Settings(BaseSettings):


    # database configurations
    DATABASE_URL: Optional[str] = os.getenv("MONGO_DETAILS")
    
    # User Agent for SEC.gov requests
    USER_AGENT: Optional[str] = os.getenv("USER_AGENT")

    # FMP API key:
    FMP_KEY: Optional[str] = os.getenv("FMP_KEY")
    
    # WVI Insights Twitter Keys
    WVI_INSIGHTS_API_KEY: Optional[str] = os.getenv("WVI_INSIGHTS_API_KEY")
    WVI_INSIGHTS_API_KEY_SECRET: Optional[str] = os.getenv("WVI_INSIGHTS_API_KEY_SECRET")
    WVI_INSIGHTS_BEARER_TOKEN: Optional[str] = os.getenv("WVI_INSIGHTS_BEARER_TOKEN")
    WVI_INSIGHTS_ACCESS_TOKEN: Optional[str] = os.getenv("WVI_INSIGHTS_ACCESS_TOKEN")
    WVI_INSIGHTS_ACCESS_TOKEN_SECRET: Optional[str] = os.getenv("WVI_INSIGHTS_ACCESS_TOKEN_SECRET")
    
    WVI_INSIGHTS_CLIENT_ID: Optional[str] = os.getenv("WVI_INSIGHTS_CLIENT_ID")
    WVI_INSIGHTS_CLIENT_SECRET: Optional[str] = os.getenv("WVI_INSIGHTS_CLIENT_SECRET")
    
    WVI_OPENAI_API_KEY: Optional[str] = os.getenv("WVI_OPENAI_API_KEY")


    # JWT
    SECRET_KEY: str
    algorithm: str = "HS256"



    # Config Class
    class Config:
        env_file = ".env"
        from_attributes = True
        extra="allow"
        
        
async def initiate_database():
    client = AsyncIOMotorClient(Settings().DATABASE_URL)
    await init_beanie(database=client.world_view_insights,
                        document_models=[
                                            FormFour,
                                            Tweet
                                        ])
