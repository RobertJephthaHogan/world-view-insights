from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .config import initiate_database

from app.services.user.routes import router as UserRouter
from app.services.fmp.routes import router as FMPRouter
from app.services.data.routes import router as DataRouter
from app.services.rss.routes import router as RssRouter


# Create the App
app = FastAPI()

# Apply CORS Middleware / Allow Origins
origins = [ 
           'http://localhost:3000',
           'http://localhost:3005',
           'https://cher-ami.roberthogan.io',
           'https://www.cher-ami.roberthogan.io' 
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
    
    
# Root Render
@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Hello! Welcome to World View Insights."}


# Add service routers to app router
app.include_router(UserRouter, tags=["User"], prefix="/user")
app.include_router(DataRouter, tags=["Data"], prefix="/data")
app.include_router(RssRouter, tags=["RSS"], prefix="/rss")
app.include_router(FMPRouter, tags=["FMP"], prefix="/fmp")
