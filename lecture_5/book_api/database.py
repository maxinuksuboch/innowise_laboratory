"""
Database configuration for async SQLAlchemy engine and session maker.
Handles initialization and schema creation.
"""

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase

DATABASE_URL = 'sqlite+aiosqlite:///./book_api/books.db'

# Create an asynchronous engine for a SQLite database
engine = create_async_engine(DATABASE_URL, echo=False)

new_session = async_sessionmaker(bind=engine, expire_on_commit=False, class_=AsyncSession)

async def get_session() -> AsyncSession:
    async with new_session() as session:
        yield session

# ------------------------------------------------------------------------------
# Base model class
# ------------------------------------------------------------------------------

class Base(DeclarativeBase):
    pass

# ------------------------------------------------------------------------------
# Database setup
# ------------------------------------------------------------------------------

async def setup_database() -> None:
    """
        Drops and recreates all tables.
        Use only for debugging, demos or tests.
    """

    async with engine.connect() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
        await conn.commit()





