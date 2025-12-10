"""
FastAPI application entry point.
Mounts all API routers and initializes application settings.
"""

from fastapi import FastAPI
from book_api.api import main_router

app = FastAPI()

# Register API routers
app.include_router(main_router)



