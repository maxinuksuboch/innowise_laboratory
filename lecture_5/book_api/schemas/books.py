"""
Pydantic schemas (DTOs) for Book API endpoints.
Used for validation, serialization and documentation.
"""

from pydantic import BaseModel, Field


# ------------------------------------------------------------------------------
# Base schemas
# ------------------------------------------------------------------------------

class BookAddSchema(BaseModel):
    """Schema for adding a new book."""
    title: str
    author: str
    year: int | None = Field(None, ge=0, le=2025, description="Publication year must be between 0 and 2025")

class BookSchema(BookAddSchema):
    """Schema returned for book operations including ID."""
    id: int

class BookGetSchema(BaseModel):
    """Schema used when returning a list of books."""
    id: int
    title: str
    author: str
    year: int | None = Field(None, ge=0, le=2025, description="Publication year must be between 0 and 2025")

class BookUpdateSchema(BaseModel):
    """Schema for replacing book fields (PUT)."""
    title: str | None = Field(None, description="New title")
    author: str | None = Field(None, description="New author")
    year: int | None = Field(None, ge=0, le=2025, description="Publication year must be between 0 and 2025")

class BookSearchSchema(BaseModel):
    """Optional fields for flexible search queries."""
    title: str | None = None
    author: str | None = None
    year: int | None = Field(None, ge=0, le=2025, description="Publication year must be between 0 and 2025")

# ------------------------------------------------------------------------------
# Pagination schema
# --------------------------------------------------------------------------

class PaginationParams(BaseModel):
    """
        Pagination query parameters.

        Attributes:
            limit (int): Number of items per page.
            offset (int): Starting position for results.
    """

    limit: int = Field(5, ge=0, le=100, description="Кол-во элементов на странице")
    offset: int = Field(0, ge=0, description="Смещение для пагинации")