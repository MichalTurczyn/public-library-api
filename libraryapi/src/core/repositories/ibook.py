"""A repository for book entity."""

from abc import ABC, abstractmethod
from typing import Any
from pydantic import UUID4

from src.core.domain.book import Book, BookIn


class IBookRepository(ABC):
    """An abstract repository class for book."""

    @abstractmethod
    async def add_book(self, book: BookIn) -> Any:
        """Adds a new book to the repository.

        Args:
            book (BookIn): The book input data.

        Returns:
            Any: The created book object.
        """

    @abstractmethod
    async def get_by_uuid(self, uuid: UUID4) -> Book | None:
        """Fetches a book by its UUID.

        Args:
            uuid (UUID4): UUID of the book.

        Returns:
            Book | None: The book object if found.
        """

    @abstractmethod
    async def list_books(self) -> list[Book]:
        """Lists all books in the repository.

        Returns:
            list[Book]: A list of all books.
        """

    @abstractmethod
    async def update_book(self, uuid: UUID4, book_data: dict) -> Book | None:
        """Updates an existing book.

        Args:
            uuid (UUID4): UUID of the book to update.
            book_data (dict): Fields to update.

        Returns:
            Book | None: The updated book object.
        """

    @abstractmethod
    async def delete_book(self, uuid: UUID4) -> bool:
        """Deletes a book by UUID.

        Args:
            uuid (UUID4): UUID of the book.

        Returns:
            bool: True if the book was deleted, False otherwise.
        """
