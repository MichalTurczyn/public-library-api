from typing import Any
from src.core.domain.book import Book, BookIn
from src.core.repositories.ibook import IBookRepository
from src.db import book_table, database


class BookRepository(IBookRepository):

    async def add_book(self, data: BookIn) -> Any | None:
        """
        Adds a new book to the database.

        Args:
            data (BookIn): The input data for the book.

        Returns:
            Any | None: The newly created book object if successful, otherwise None.
        """
        query = book_table.insert().values(**data.model_dump())
        new_book_id = await database.execute(query)
        return await self.get_book_by_id(new_book_id)
    
    async def list_book(self) -> list[Book]:
        """
        Retrieves a list of all books from the database.

        Returns:
            list[Book]: A list of all books in the database.
        """
        query = book_table.select()
        books = await database.fetch_all(query)
        return [Book(**dict(book)) for book in books]

    async def get_book_by_id(self, book_id: int) -> Any | None:
        """
        Retrieves a book by its ID.

        Args:
            book_id (int): The ID of the book to retrieve.

        Returns:
            Any | None: The book object if found, otherwise None.
        """
        query = book_table.select().where(book_table.c.id == book_id)
        book = await database.fetch_one(query)
        return Book(**dict(book)) if book else None

    async def search_book_by_title(self, title: str) -> Any:
        """
        Searches for books by their title.

        Args:
            title (str): The title or part of the title of the book to search for.

        Returns:
            Any: A list of books that match the search criteria.
        """
        query = book_table.select().where(book_table.c.title.ilike(f"%{title}%"))
        rows = await database.fetch_all(query)
        return [Book(**row) for row in rows]

    async def search_book_by_author(self, author_id: int) -> Any:
        """
        Searches for books by their author.

        Args:
            author_id (int): The ID of the author.

        Returns:
            Any: A list of books written by the specified author.
        """
        query = book_table.select().where(book_table.c.author_id == author_id)
        rows = await database.fetch_all(query)
        return [Book(**row) for row in rows]

    async def search_book_by_category(self, category_id: int) -> Any:
        """
        Searches for books by their category.

        Args:
            category_id (int): The ID of the category.

        Returns:
            Any: A list of books in the specified category.
        """
        query = book_table.select().where(book_table.c.category_id == category_id)
        rows = await database.fetch_all(query)
        return [Book(**row) for row in rows]
    
    async def update_book(self, book_id: int, data: BookIn) -> Any | None:
        """
        Updates the details of a book.

        Args:
            book_id (int): The ID of the book to update.
            data (BookIn): The updated data for the book.

        Returns:
            Any | None: The updated book object if successful, otherwise None.
        """
        query = book_table.update().where(book_table.c.id == book_id).values(**data.model_dump())
        await database.execute(query)
        return await self.get_book_by_id(book_id)

    async def delete_book(self, book_id: int) -> bool:
        """
        Deletes a book by its ID.

        Args:
            book_id (int): The ID of the book to delete.

        Returns:
            bool: True if the book was successfully deleted, otherwise False.
        """
        if self.get_book_by_id(id):
            query = book_table.delete().where(book_table.c.id == book_id)
            await database.execute(query)
            return True
        return False