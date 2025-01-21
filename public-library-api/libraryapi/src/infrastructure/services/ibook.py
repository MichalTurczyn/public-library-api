"""Module containing book service abstractions."""

from abc import ABC, abstractmethod
from typing import Iterable, List
from pydantic import UUID4

from src.core.domain.book import Book
from src.infrastructure.dto.bookdto import BookDTO


class IBookService(ABC):
    """An abstract class representing the protocol for book services."""

    @abstractmethod
    async def add_book(self, book_data: Book) -> Book | None:
        """Adds a new book to the repository.

        Args:
            book_data (Book): The details of the book to add.

        Returns:
            Book | None: The newly added book details.
        """

    @abstractmethod
    async def get_book_by_uuid(self, book_id: UUID4) -> BookDTO | None:
        """Fetches a book's details using its UUID.

        Args:
            book_id (UUID4): The UUID of the book.

        Returns:
            BookDTO | None: The book details if found.
        """

    @abstractmethod
    async def list_books(self) -> Iterable[BookDTO]:
        """Lists all books in the repository.

        Returns:
            Iterable[BookDTO]: A list of all books.
        """

    @abstractmethod
    async def update_book(self, book_id: UUID4, book_data: Book) -> Book | None:
        """Updates an existing book's information.

        Args:
            book_id (UUID4): The UUID of the book to update.
            book_data (Book): The updated details of the book.

        Returns:
            Book | None: The updated book details if successful.
        """

    @abstractmethod
    async def delete_book(self, book_id: UUID4) -> bool:
        """Deletes a book by its UUID.

        Args:
            book_id (UUID4): The UUID of the book to delete.

        Returns:
            bool: True if deletion was successful, otherwise False.
        """

    @abstractmethod
    async def search_book_by_title(self, title: str) -> List[Book]:
        """Searches books by title.

        Args:
            title (str): Title of the book.

        Returns:
            List[Book]: A list of books matching the title.
        """
        pass

    @abstractmethod
    async def search_book_by_author(self, author_id: UUID4) -> List[Book]:
        """Searches books by author.

        Args:
            author_id (UUID4): UUID of the author.

        Returns:
            List[Book]: A list of books written by the author.
        """
        pass

    @abstractmethod
    async def search_book_by_category(self, category_id: UUID4) -> List[Book]:
        """Searches books by category.

        Args:
            category_id (UUID4): UUID of the category.

        Returns:
            List[Book]: A list of books belonging to the category.
        """
        pass