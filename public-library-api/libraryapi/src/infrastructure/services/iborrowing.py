"""Module containing borrowing service abstractions."""

from abc import ABC, abstractmethod
from typing import Iterable
from pydantic import UUID4

from src.core.domain.borrowing import Borrowing
from src.infrastructure.dto.borrowingdto import BorrowingDTO


class IBorrowingService(ABC):
    """An abstract class representing the protocol for borrowing services."""

    @abstractmethod
    async def add_borrowing(self, borrowing_data: Borrowing) -> Borrowing | None:
        """Adds a new borrowing record to the repository.

        Args:
            borrowing_data (Borrowing): The details of the borrowing.

        Returns:
            Borrowing | None: The newly created borrowing record.
        """

    @abstractmethod
    async def get_borrowing_by_id(self, borrowing_id: UUID4) -> BorrowingDTO | None:
        """Fetches a borrowing record using its UUID.

        Args:
            borrowing_id (UUID4): The UUID of the borrowing.

        Returns:
            BorrowingDTO | None: The borrowing details if found.
        """

    @abstractmethod
    async def list_borrowings(self) -> Iterable[BorrowingDTO]:
        """Lists all borrowing records.

        Returns:
            Iterable[BorrowingDTO]: A collection of all borrowing records.
        """

    @abstractmethod
    async def get_borrowings_by_user(self, user_id: UUID4) -> Iterable[BorrowingDTO]:
        """Fetches all borrowing records for a specific user.

        Args:
            user_id (UUID4): The UUID of the user.

        Returns:
            Iterable[BorrowingDTO]: A list of borrowing records for the user.
        """

    @abstractmethod
    async def update_borrowing(
        self, borrowing_id: UUID4, borrowing_data: Borrowing
    ) -> Borrowing | None:
        """Updates an existing borrowing record.

        Args:
            borrowing_id (UUID4): The UUID of the borrowing to update.
            borrowing_data (Borrowing): The updated borrowing details.

        Returns:
            Borrowing | None: The updated borrowing record if successful.
        """

    @abstractmethod
    async def delete_borrowing(self, borrowing_id: UUID4) -> bool:
        """Deletes a borrowing record by its UUID.

        Args:
            borrowing_id (UUID4): The UUID of the borrowing to delete.

        Returns:
            bool: True if the deletion was successful, otherwise False.
        """

    @abstractmethod
    async def get_borrowing_history(self, user_id: UUID4) -> list[Borrowing]:
        pass