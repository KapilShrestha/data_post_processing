import logging
from fastapi import FastAPI
from api.routes import router

# Set up basic logging configuration
logging.basicConfig(level=logging.INFO)

app = FastAPI()

# Include the routes
app.include_router(router)
