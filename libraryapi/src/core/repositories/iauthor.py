"""A repository for author entity."""

from abc import ABC, abstractmethod
from typing import Any
from pydantic import UUID4

from src.core.domain.author import Author


class IAuthorRepository(ABC):
    """An abstract repository class for author."""

    @abstractmethod
    async def add_author(self, author: Author) -> Any:
        """Adds a new author to the repository.

        Args:
            author (Author): The author data.

        Returns:
            Any: The created author object.
        """

    @abstractmethod
    async def get_books_by_author(self, author_uuid: UUID4) -> list:
        """Fetches all books written by the specified author.

        Args:
            author_uuid (UUID4): The UUID of the author.

        Returns:
            list: A list of books written by the author.
        """

    @abstractmethod
    async def get_by_uuid(self, uuid: UUID4) -> Author | None:
        """Fetches an author by UUID.

        Args:
            uuid (UUID4): The UUID of the author.

        Returns:
            Author | None: The author object if found.
        """

    @abstractmethod
    async def list_authors(self) -> list[Author]:
        """Lists all authors in the repository.

        Returns:
            list[Author]: A list of all authors.
        """
