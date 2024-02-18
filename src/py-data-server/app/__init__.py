from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .config import initiate_database


from app.services.edgar.routes import router as EdgarRouter
from app.services.collector.routes import router as CollectorRouter



# Create the App
app = FastAPI()

# Apply CORS Middleware / Allow Origins
origins = [ 
           'http://localhost:3000',
           'http://localhost:3008',
           'http://localhost:8008',
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
    print("Starting Py Data Server...")
    print("Initiating Database...")
    await initiate_database()
    
    
# Root Render
@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Hello! Welcome to World View Insights - Python Data Server."}


# Add service routers to app router
app.include_router(EdgarRouter, tags=["Edgar"], prefix="/edgar")
app.include_router(CollectorRouter, tags=["Collector"], prefix="/collector")