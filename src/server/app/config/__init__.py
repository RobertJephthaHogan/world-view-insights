from typing import Optional
import os
from dotenv import load_dotenv
from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic_settings import BaseSettings

from app.models.User import User
from app.models.FeedItem import FeedItem
from app.models.ScheduledService import ScheduledService
from app.models.LeadersSnapshot import LeadersSnapshot
from app.models.IndexSnapshot import IndexSnapshot
from app.models.NotableQuotesSnapshot import NotableQuotesSnapshot
from app.models.GainerPriceSnapshot import GainerPriceSnapshot
from app.models.LoserPriceSnapshot import LoserPriceSnapshot
from app.models.LeadersTableSnapshot import LeadersTableSnapshot

# Load the environment variables
load_dotenv()

class Settings(BaseSettings):


    # database configurations
    DATABASE_URL: Optional[str] = os.getenv("MONGO_DETAILS")

    # keys
    FMP_API_KEY: Optional[str] = os.getenv("FMP_KEY")

    # JWT
    SECRET_KEY: str
    algorithm: str = "HS256"

    # On Start-up Configuration 
    should_run_startup_tests: int = 0

    # Config Class
    class Config:
        env_file = ".env"
        from_attributes = True
        extra="allow"


async def initiate_database():
    client = AsyncIOMotorClient(Settings().DATABASE_URL)
    await init_beanie(database=client.world_view_insights,
                        document_models=[
                                            User,
                                            FeedItem,
                                            ScheduledService,
                                            LeadersSnapshot,
                                            IndexSnapshot,
                                            NotableQuotesSnapshot,
                                            GainerPriceSnapshot,
                                            LoserPriceSnapshot,
                                            LeadersTableSnapshot
                                        ])
