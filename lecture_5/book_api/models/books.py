"""
SQLAlchemy ORM model definitions for Book entities.
"""

from sqlalchemy.orm import Mapped, mapped_column

from book_api.database import Base


class BookModel(Base):
    """
        Represents a book record stored in the database.

        Attributes:
            id (int): Primary key (autoincrement).
            title (str): Book title.
            author (str): Book author.
            year (int | None): Publication year.
        """

    __tablename__ = "book"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(nullable=False)
    author: Mapped[str] = mapped_column(nullable=False)
    year : Mapped[int | None]