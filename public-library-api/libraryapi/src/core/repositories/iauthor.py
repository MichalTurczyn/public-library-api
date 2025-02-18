"""An abstract repository for author entity."""

from abc import ABC, abstractmethod
from typing import List
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

    @abstractmethod
    async def get_author_by_id(self, author_id: int) -> Author | None:
        """Fetches an author by their id.

        Args:
            author_id (int): id of the author.

        Returns:
            Author | None: The author object if found, otherwise None.
        """

    @abstractmethod
    async def get_books_by_author(self, author_id: int) -> List[str]:
        """Fetches the books written by a specific author.

        Args:
            author_id (int): id of the author.

        Returns:
            List[str]: A list of book titles written by the author.
        """

    @abstractmethod
    async def list_authors(self) -> List[Author]:
        """Lists all authors.

        Returns:
            List[Author]: A list of all authors.
        """

    @abstractmethod
    async def update_author(self, author_id: int, updated_data: AuthorIn) -> Author | None:
        """Updates an author's data.

        Args:
            author_id (int): id of the author to update.
            updated_data (AuthorIn): Updated author data.

        Returns:
            Author | None: The updated author object if successful, otherwise None.
        """

    @abstractmethod
    async def delete_author(self, author_id: int) -> bool:
        """Deletes an author by their id.

        Args:
            author_id (int): id of the author to delete.

        Returns:
            bool: True if the author was successfully deleted, False otherwise.
        """