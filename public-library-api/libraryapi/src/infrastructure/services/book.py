"""Module containing the implementation of book services."""

from typing import Iterable
from pydantic import UUID4

from src.core.domain.book import Book
from src.infrastructure.dto.bookdto import BookDTO
from src.infrastructure.services.ibook import IBookService


class BookService(IBookService):
    """A service class implementing the IBookService protocol."""

    async def add_book(self, book_data: Book) -> Book | None:
        """Adds a new book to the repository."""
        # Implementation logic for adding a book
        pass

    async def get_book_by_uuid(self, book_id: UUID4) -> BookDTO | None:
        """Fetches a book's details using its UUID."""
        # Implementation logic for fetching a book by UUID
        pass

    async def list_books(self) -> Iterable[BookDTO]:
        """Lists all books in the repository."""
        # Implementation logic for listing all books
        pass

    async def update_book(self, book_id: UUID4, book_data: Book) -> Book | None:
        """Updates an existing book's information."""
        # Implementation logic for updating a book
        pass

    async def delete_book(self, book_id: UUID4) -> bool:
        """Deletes a book by its UUID."""
        # Implementation logic for deleting a book
        pass
    
    async def search_book_by_title(self, title: str) -> Iterable[BookDTO]:
        """Searches for books by title."""
        return await self.repository.search_by_title(title)

    async def search_book_by_author(self, author_id: UUID4) -> Iterable[BookDTO]:
        """Searches for books by author."""
        return await self.repository.search_by_author(author_id)

    async def search_book_by_category(self, category_id: UUID4) -> Iterable[BookDTO]:
        """Searches for books by category."""
        return await self.repository.search_by_category(category_id)