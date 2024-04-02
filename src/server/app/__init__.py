from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.services.scheduled_service import ScheduledServiceService
from .config import initiate_database

from app.services.user.routes import router as UserRouter
from app.services.edgar.routes import router as EdgarRouter
from app.services.fmp.routes import router as FMPRouter
from app.services.data.routes import router as DataRouter
from app.services.rss.routes import router as RssRouter
from app.services.collector.routes import router as CollectorRouter
from app.services.news.routes import router as NewsRouter
from app.services.stock_data.routes import router as StockDataRouter
from app.services.price_history.routes import router as PriceHistoryRouter


# Create the App
app = FastAPI()

# Apply CORS Middleware / Allow Origins
origins = [ 
           'http://localhost:3000',
           'http://localhost:3008',
           'https://worldviewinsights.com',
           'https://www.worldviewinsights.com' 
        ]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials= True,
    allow_methods=['*'],
    allow_headers=['*'],
)


# Start Up Events
@app.on_event("startup")
async def startup_event():
    print("Starting Server...")
    print("Initiating Database...")
    await initiate_database()
    print("Starting Service Scheduler...")
    ScheduledServiceService().startScheduler()
    
    
# Root Render
@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Hello! Welcome to World View Insights."}


# Add service routers to app router
app.include_router(UserRouter, tags=["User"], prefix="/user")
app.include_router(EdgarRouter, tags=["Edgar"], prefix="/edgar")
app.include_router(DataRouter, tags=["Data"], prefix="/data")
app.include_router(RssRouter, tags=["RSS"], prefix="/rss")
app.include_router(NewsRouter, tags=["News"], prefix="/news")
app.include_router(PriceHistoryRouter, tags=["Price History"], prefix="/price-history")
app.include_router(StockDataRouter, tags=["Stock Data"], prefix="/stock")
app.include_router(CollectorRouter, tags=["Collector"], prefix="/collector")
app.include_router(FMPRouter, tags=["FMP"], prefix="/fmp")
