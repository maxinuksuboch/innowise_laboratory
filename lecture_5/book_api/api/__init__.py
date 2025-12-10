"""
API router aggregator.
Imports all subrouters into a unified main router.
"""

from fastapi import APIRouter

from book_api.api.books import router as books_router

main_router = APIRouter()

main_router.include_router(books_router)