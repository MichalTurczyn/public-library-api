
from typing import Any
from src.core.domain.author import Author, AuthorIn
from src.core.repositories.iauthor import IAuthorRepository
from src.db import author_table, database, book_table


class AuthorRepository(IAuthorRepository):

    async def add_author(self, data: AuthorIn) -> Any | None:
        """
        Adds a new author to the database.

        Args:
            data (AuthorIn): The input data for the author.

        Returns:
            Any | None: The created author object if successful, otherwise None.
        """
        query = author_table.insert().values(**data.model_dump())
        new_author_id = await database.execute(query)
        return await self.get_author_by_id(new_author_id)

    async def get_author_by_id(self, author_id: int) -> Any | None:
        """
        Fetches an author by their ID.

        Args:
            author_id (int): The ID of the author to retrieve.

        Returns:
            Any | None: The author object if found, otherwise None.
        """
        query = author_table.select().where(author_table.c.id == author_id)
        author = await database.fetch_one(query)
        return Author(**dict(author)) if author else None
    
    async def get_books_by_author(self, author_id: int) -> list[dict]:
        """Fetches books written by a specific author.

        Args:
            author_id (int): id of the author.

        Returns:
            list[dict]: List of books written by the author.
        """
        query = book_table.select().where(book_table.c.author_id == author_id)
        books = await database.fetch_all(query)
        return [dict(book) for book in books] if books else []

    async def list_authors(self) -> list[Author]:
        """
        Retrieves all authors from the database.

        Returns:
            list[Author]: A list of all authors.
        """
        query = author_table.select()
        authors = await database.fetch_all(query)
        return [Author(**dict(author)) for author in authors]
    
    async def update_author(self, author_id: int, updated_data: AuthorIn) -> Author | None:
        """Updates an author's details.

        Args:
            author_id (int): id of the author to update.
            updated_data (AuthorIn): Updated author data.

        Returns:
            Author | None: Updated author object if successful, otherwise None.
        """
        query = author_table.update().where(author_table.c.id == author_id).values(**updated_data.dict())
        await database.execute(query)
        return await self.get_author_by_id(author_id)

    async def delete_author(self, author_id: int) -> bool:
        """
        Deletes an author by their ID.

        Args:
            author_id (int): The ID of the author to delete.

        Returns:
            bool: True if the author was successfully deleted, otherwise False.
        """
        if self.get_author_by_id(id):
            query = author_table.delete().where(author_table.c.id == author_id)
            await database.execute(query)
            return True
    
        return False