from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware





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
    
    
    
# Root Render
@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Hello! Welcome to World View Insights - Python Data Server."}