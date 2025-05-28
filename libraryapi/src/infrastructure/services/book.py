"""Module containing the implementation of book services."""

from typing import Iterable

from src.core.domain.book import Book
from src.infrastructure.dto.bookdto import BookDTO
from src.infrastructure.services.ibook import IBookService
from src.core.repositories.ibook import IBookRepository
from src.core.domain.book import BookIn


class BookService(IBookService):
    """A service class implementing the IBookService protocol."""
    _repository: IBookRepository
    def __init__(self, repository: IBookRepository):
        self._repository = repository

    async def add_book(self, book_data: Book) -> Book | None:
        """
        Adds a new book to the repository.

        Args:
            book_data (Book): The book data to add.

        Returns:
            BookDTO | None: The newly created book object if successful, otherwise None.
        """
        return await self._repository.add_book(book_data)

    async def get_book_by_id(self, book_id: int) -> BookDTO | None:
        """
        Retrieves a book by its ID.

        Args:
            book_id (int): The ID of the book.

        Returns:
            BookDTO | None: The book object if found, otherwise None.
        """
        return await self._repository.get_book_by_id(book_id)

    async def list_books(self) -> Iterable[BookDTO]:
        """
        Lists all books available in the repository.

        Returns:
            Iterable[BookDTO]: A collection of all book objects.
        """
        return await self._repository.list_book()
    
    async def search_book_by_title(self, title: str) -> Iterable[BookDTO]:
        """
        Searches for books by their title.

        Args:
            title (str): The title or part of the title to search for.

        Returns:
            Iterable[BookDTO]: A collection of books matching the search criteria.
        """
        return await self._repository.search_book_by_title(title)

    async def search_book_by_author(self, author_id: int) -> Iterable[BookDTO]:
        """
        Searches for books by their author.

        Args:
            author_id (int): The ID of the author.

        Returns:
            Iterable[BookDTO]: A collection of books written by the specified author.
        """
        return await self._repository.search_book_by_author(author_id)

    async def search_book_by_category(self, category_id: int) -> Iterable[BookDTO]:
        """
        Searches for books by their category.

        Args:
            category_id (int): The ID of the category.

        Returns:
            Iterable[BookDTO]: A collection of books belonging to the specified category.
        """
        return await self._repository.search_book_by_category(category_id)
    
    async def update_book(self, book_id: int, book_data: BookIn) -> BookDTO | None:
        """
        Updates an existing book record.

        Args:
            book_id (int): The ID of the book to update.
            book_data (BookIn): The updated book data.

        Returns:
            BookDTO | None: The updated book object if successful, otherwise None.
        """
        return await self._repository.update_book(book_id, book_data)

    async def delete_book(self, book_id: int) -> bool:
        """
        Deletes a book by its ID.

        Args:
            book_id (int): The ID of the book to delete.

        Returns:
            bool: True if the deletion was successful, otherwise False.
        """
        return await self._repository.delete_book(book_id)