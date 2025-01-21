"""An abstract repository for author entity."""

from abc import ABC, abstractmethod
from typing import List
from pydantic import UUID4
from src.core.domain.author import Author, AuthorIn


class IAuthorRepository(ABC):
    """An abstract repository class for author."""

    @abstractmethod
    async def add_author(self, author: AuthorIn) -> Author:
        """Adds a new author.

        Args:
            author (AuthorIn): The input data for the author.

        Returns:
            Author: The created author object.
        """
        pass

    @abstractmethod
    async def get_by_uuid(self, author_id: UUID4) -> Author | None:
        """Fetches an author by their UUID.

        Args:
            author_id (UUID4): UUID of the author.

        Returns:
            Author | None: The author object if found, otherwise None.
        """
        pass

    @abstractmethod
    async def list_authors(self) -> List[Author]:
        """Lists all authors.

        Returns:
            List[Author]: A list of all authors.
        """
        pass

    @abstractmethod
    async def get_books_by_author(self, author_id: UUID4) -> List[str]:
        """Fetches the books written by a specific author.

        Args:
            author_id (UUID4): UUID of the author.

        Returns:
            List[str]: A list of book titles written by the author.
        """
        pass

    @abstractmethod
    async def delete_author(self, author_id: UUID4) -> bool:
        """Deletes an author by their UUID.

        Args:
            author_id (UUID4): UUID of the author to delete.

        Returns:
            bool: True if the author was successfully deleted, False otherwise.
        """
        pass
