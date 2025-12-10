"""
Application-wide dependency declarations for FastAPI.

Contains reusable annotated dependencies for:
- Database sessions (AsyncSession)
- Pagination parameters
"""

from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from book_api.database import get_session
from book_api.schemas.books import PaginationParams

# ------------------------------------------------------------------------------
# Database session dependency
# ------------------------------------------------------------------------------

SessionDep = Annotated[AsyncSession, Depends(get_session)]

"""
Dependency for injecting an async SQLAlchemy session.

Usage:
    async def endpoint(session: SessionDep):
"""

# ------------------------------------------------------------------------------
# Pagination dependency
# ------------------------------------------------------------------------------

PaginationDep = Annotated[PaginationParams, Depends(PaginationParams)]

"""
Dependency for validating pagination query parameters.

Usage:
    async def endpoint(pagination: PaginationDep): 
"""