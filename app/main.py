import logging
from fastapi import FastAPI
from api.routes import router

# Set up basic logging configuration
logging.basicConfig(level=logging.INFO)  # This will capture INFO level logs and above.

app = FastAPI()

# Include the routes
app.include_router(router)
