"""Module containing author service abstractions."""

from abc import ABC, abstractmethod
from typing import Iterable
from pydantic import UUID4

from src.core.domain.author import Author
from src.infrastructure.dto.authordto import AuthorDTO


class IAuthorService(ABC):
    """An abstract class representing the protocol for author services."""

    @abstractmethod
    async def add_author(self, author_data: Author) -> Author | None:
        """Adds a new author to the repository.

        Args:
            author_data (Author): The details of the author to add.

        Returns:
            Author | None: The newly added author details.
        """

    @abstractmethod
    async def get_author_by_id(self, author_id: UUID4) -> AuthorDTO | None:
        """Fetches an author's details using their UUID.

        Args:
            author_id (UUID4): The UUID of the author.

        Returns:
            AuthorDTO | None: The author details if found.
        """

    @abstractmethod
    async def list_authors(self) -> Iterable[AuthorDTO]:
        """Lists all authors in the repository.

        Returns:
            Iterable[AuthorDTO]: A list of all authors.
        """

    @abstractmethod
    async def get_books_by_author(self, author_id: UUID4) -> list:
        """Fetches all books written by the specified author.

        Args:
            author_id (UUID4): The UUID of the author.

        Returns:
            list: A list of books written by the author.
        """

    @abstractmethod
    async def delete_author(self, author_id: UUID4) -> bool:
        """Deletes an author by their UUID.

        Args:
            author_id (UUID4): The UUID of the author to delete.

        Returns:
            bool: True if deletion was successful, otherwise False.
        """