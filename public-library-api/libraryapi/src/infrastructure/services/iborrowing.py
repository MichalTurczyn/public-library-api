"""Module containing borrowing service abstractions."""

from abc import ABC, abstractmethod
from typing import Iterable
from datetime import date, datetime

from src.core.domain.borrowing import Borrowing
from src.infrastructure.dto.borrowingdto import BorrowingDTO


class IBorrowingService(ABC):
    """An abstract class representing the protocol for borrowing services."""

    @abstractmethod
    async def create_borrowing(self, borrowing_data: Borrowing) -> Borrowing | None:
        """Adds a new borrowing record to the repository.

        Args:
            borrowing_data (Borrowing): The details of the borrowing.

        Returns:
            Borrowing | None: The newly created borrowing record.
        """

    @abstractmethod
    async def get_borrowing_by_id(self, borrowing_id: int) -> BorrowingDTO | None:
        """Fetches a borrowing record using its id.

        Args:
            borrowing_id (int): The id of the borrowing.

        Returns:
            BorrowingDTO | None: The borrowing details if found.
        """

    @abstractmethod
    async def get_active_borrowings_by_user(self, user_id: int) -> list[Borrowing]:
        """Fetches active borrowings for a specific user.

        Args:
            user_id (int): The id of the user.

        Returns:
            list[Borrowing]: A list of active borrowings for the user.
        """

    @abstractmethod
    async def list_all_borrowings(self) -> Iterable[BorrowingDTO]:
        """Lists all borrowing records.

        Returns:
            Iterable[BorrowingDTO]: A collection of all borrowing records.
        """

    @abstractmethod
    async def mark_borrowing_as_returned(self, borrowing_id: int, return_date: date) -> bool:
        """Marks a borrowing as returned.

        Args:
            borrowing_id (int): The id of the borrowing to mark as returned.
            return_date (str): The date of return.

        Returns:
            bool: True if the update was successful, otherwise False.
        """

    @abstractmethod
    async def get_borrowing_history_by_user(self, user_id: int) -> list[Borrowing]:
        """
        Retrieves the borrowing history for a specific user.

        Args:
            user_id (int): The ID of the user whose borrowing history is to be fetched.

        Returns:
            list[Borrowing]: A list of borrowings with status 'returned' for the specified user.
        """

    @abstractmethod
    async def delete_borrowing(self, borrowing_id: int) -> bool:
        """Deletes a borrowing record by its id.

        Args:
            borrowing_id (int): The id of the borrowing to delete.

        Returns:
            bool: True if the deletion was successful, otherwise False.
        """

    @abstractmethod
    async def update_borrowing(
        self, borrowing_id: int
    ) -> BorrowingDTO:
        """Updates an existing borrowing record.

        Args:
            borrowing_id (int): The id of the borrowing to update.
            borrowing_data (Borrowing): The updated borrowing details.

        Returns:
            Borrowing | None: The updated borrowing record if successful.
        """