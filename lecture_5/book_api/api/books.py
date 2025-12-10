from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy import select, update, and_

from book_api.api.dependencies import SessionDep, PaginationDep

from book_api.database import setup_database
from book_api.models.books import BookModel
from book_api.schemas.books import (
    BookAddSchema,
    BookSchema,
    BookGetSchema,
    BookUpdateSchema,
    BookSearchSchema
)

router = APIRouter()

# ------------------------------------------------------------------------------
# Database Initialization
# ------------------------------------------------------------------------------

@router.post('/setup_database')
async def setup_db() -> dict:
    """
    Drops and recreates the database tables.
    Intended only for local development or demo purposes.

    :return:
        dict: Status message
    """
    await setup_database()
    return {"message": "Database setup completed"}

# ------------------------------------------------------------------------------
# Create Book
# ------------------------------------------------------------------------------

@router.post('/books', response_model=BookSchema)
async def add_book(data: BookAddSchema, session: SessionDep) -> BookSchema:
    """
    Create a new book record

        :param data: Incoming validated data for a new book.
        :param session: Database session dependency.

    :return:
            BookSchema: Created book with assigned ID.
    """

    new_book = BookModel(
        title=data.title,
        author=data.author,
        year=data.year,
    )

    session.add(new_book)
    await session.commit()
    await session.refresh(new_book)  # Ensure ID and defaults are loaded
    return new_book


# ------------------------------------------------------------------------------
# Get Books (with pagination)
# ------------------------------------------------------------------------------

@router.get('/books', response_model=list[BookGetSchema])
async def get_books(
        session: SessionDep,
        pagination: PaginationDep,
) -> list[BookGetSchema]:
    """
    Retrieve a paginated list of all books.

    :param session: Database session.
    :param pagination: Pagination parameters (limit/offset).
    :return:
            list[BookGetSchema]: List of book objects.
    """

    query = (
        select(BookModel)
        .limit(pagination.limit)
        .offset(pagination.offset)
    )

    result = await session.execute(query)
    return result.scalars().all()

# ------------------------------------------------------------------------------
# Delete Book by ID
# ------------------------------------------------------------------------------

@router.delete('/books/{book_id}')
async def delete_books(book_id : int, session: SessionDep) -> dict:
    """
    Delete a book by its ID.

    :param book_id: ID of the book to delete.
    :param session: Database session.

    :raises: HTTPException: If the book is not found.

    :return: dict: Confirmation message.
    """

    query = select(BookModel).where(BookModel.id == book_id)
    result = await session.execute(query)
    book = result.scalar_one_or_none()

    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    await session.delete(book)
    await session.commit()

    return {"ok": True, "deleted_id": book_id}

# ------------------------------------------------------------------------------
# Update Book by ID
# ------------------------------------------------------------------------------

@router.put('/books/{book_id}', response_model=BookSchema)
async def update_book(book_id : int,
                      data : BookUpdateSchema,
                      session : SessionDep) -> BookSchema:
    """
    Update a book's details.

    :param book_id: ID of the book to update.
    :param data: New values for the book fields.
    :param session: Database session.
    :raises: HTTPException: If no such book exists.

    :return:
            BookSchema: Updated book object.
    """
    query = select(BookModel).where(BookModel.id == book_id)
    result = await session.execute(query)
    book = result.scalar_one_or_none()

    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    # Assign new values
    book.title = data.title
    book.author = data.author
    book.year = data.year

    await session.commit()

    return book

# ------------------------------------------------------------------------------
# Search Books
# ------------------------------------------------------------------------------

@router.get('/books/search/', tags=["Books"])
async def search_book(
    session: SessionDep,
    pagination: PaginationDep,
    title: str | None = None,
    author: str | None = None,
    year: int | None = None,
) -> list[BookSchema]:
    """
    Search for books partially matching title/author or by exact year.
    Supports pagination.

    :param session: Database session
    :param pagination: Pagination (limit/offset).
    :param title: Partial match for title.
    :param author: Partial match for author.
    :param year: Exact match for year.

    :return:
            list[BookSchema]: List of found books (may be empty).
    """

    query = select(BookModel)
    filters = []

    # Add filters dynamically only if the user supplied values
    if title:
        filters.append(BookModel.title.ilike(f"%{title}%"))
    if author:
        filters.append(BookModel.author.ilike(f"%{author}%"))
    if year:
        filters.append(BookModel.year == year)

    # If at least one filter exists → apply WHERE
    if filters:
        query = query.where(and_(*filters))
    else:
        raise HTTPException(400, "Provide at least one search parameter")


    query = query.limit(pagination.limit).offset(pagination.offset)

    result = await session.execute(query)
    books = result.scalars().all()

    return books



