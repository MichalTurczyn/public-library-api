"""Module containing book service abstractions."""

from abc import ABC, abstractmethod
from typing import Iterable, List

from src.core.domain.book import Book
from src.infrastructure.dto.bookdto import BookDTO
from src.core.domain.book import BookIn


class IBookService(ABC):
    """An abstract class representing the protocol for book services."""

    @abstractmethod
    async def add_book(self, book_data: Book) -> BookDTO | None:
        """Adds a new book to the repository.

        Args:
            book_data (Book): The details of the book to add.

        Returns:
            Book | None: The newly added book details.
        """

    @abstractmethod
    async def get_book_by_id(self, book_id: int) -> BookDTO | None:
        """Fetches a book's details using its id.

        Args:
            book_id (int): The id of the book.

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
    async def search_book_by_title(self, title: str) -> List[BookDTO]:
        """Searches books by title.

        Args:
            title (str): Title of the book.

        Returns:
            List[Book]: A list of books matching the title.
        """

    @abstractmethod
    async def search_book_by_author(self, author_id: int) -> List[BookDTO]:
        """Searches books by author.

        Args:
            author_id (int): id of the author.

        Returns:
            List[Book]: A list of books written by the author.
        """

    @abstractmethod
    async def search_book_by_category(self, category_id: int) -> List[BookDTO]:
        """Searches books by category.

        Args:
            category_id (int): id of the category.

        Returns:
            List[Book]: A list of books belonging to the category.
        """

    @abstractmethod
    async def update_book(self, book_id: int, book_data: BookIn) -> BookDTO | None:
        """Updates an existing book's information.

        Args:
            book_id (int): The id of the book to update.
            book_data (Book): The updated details of the book.

        Returns:
            Book | None: The updated book details if successful.
        """

    @abstractmethod
    async def delete_book(self, book_id: int) -> bool:
        """Deletes a book by its id.

        Args:
            book_id (int): The id of the book to delete.

        Returns:
            bool: True if deletion was successful, otherwise False.
        """