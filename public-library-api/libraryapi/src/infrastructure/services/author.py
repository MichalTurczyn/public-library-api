"""Module containing author service implementation."""

from typing import Iterable
from src.core.domain.author import Author
from src.core.repositories.iauthor import IAuthorRepository
from src.infrastructure.services.iauthor import IAuthorService
from src.infrastructure.dto.authordto import AuthorDTO
from src.core.domain.author import AuthorIn


class AuthorService(IAuthorService):
    """A class implementing the author service."""

    _repository: IAuthorRepository

    def __init__(self, repository: IAuthorRepository) -> None:
        """
        The initializer of the `author service`.

        Args:
            repository (IAuthorRepository): The reference to the repository.
        """
        self._repository = repository

    async def add_author(self, author: Author) -> Author:
        """
        Adds a new author to the repository.

        Args:
            author (Author): The author data to add.

        Returns:
            Author: The newly created author object.
        """
        return await self._repository.add_author(author)

    async def get_author_by_id(self, author_id: int) -> AuthorDTO | None:
        """
        Fetches an author by their id.

        Args:
            author_id (int): The id of the author.

        Returns:
            AuthorDTO | None: The author object if found, otherwise None.
        """
        author = await self._repository.get_author_by_id(author_id)
        return AuthorDTO(**author.dict()) if author else None

    async def get_books_by_author(self, author_id: int) -> list:
        """
        Fetches all books written by the specified author.

        Args:
            author_id (int): The id of the author.

        Returns:
            list: A list of books written by the author.
        """
        return await self._repository.get_books_by_author(author_id)

    async def list_authors(self) -> Iterable[AuthorDTO]:
        """
        Lists all authors available in the repository.

        Returns:
            Iterable[AuthorDTO]: A collection of all authors.
        """
        authors = await self._repository.list_authors()
        return [AuthorDTO(**author.dict()) for author in authors]
    
    async def update_author(self, author_id: int, data: AuthorIn) -> AuthorDTO:
        """
        Deletes an author by their id.

        Args:
            author_id (int): The id of the author.

        Returns:
            bool: True if deletion was successful, otherwise False.
        """
        return await self._repository.update_author(author_id, data)

    async def delete_author(self, author_id: int) -> bool:
        """
        Deletes an author by their id.

        Args:
            author_id (int): The id of the author.

        Returns:
            bool: True if deletion was successful, otherwise False.
        """
        return await self._repository.delete_author(author_id)