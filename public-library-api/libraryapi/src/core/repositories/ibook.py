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
    async def get_book_by_uuid(self, uuid: UUID4) -> Book | None:
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

    @abstractmethod
    async def search_book_by_title(self, title: str) -> Any:
        """Searches for books by title.

        Args:
            title (str): Title of the book.

        Returns:
            Any: A list of books matching the title.
        """
        pass

    @abstractmethod
    async def search_book_by_author(self, author_id: UUID4) -> Any:
        """Searches for books by author.

        Args:
            author_id (UUID4): UUID of the author.

        Returns:
            Any: A list of books written by the specified author.
        """
        pass

    @abstractmethod
    async def search_book_by_category(self, category_id: UUID4) -> Any:
        """Searches for books by category.

        Args:
            category_id (UUID4): UUID of the category.

        Returns:
            Any: A list of books belonging to the specified category.
        """
        pass