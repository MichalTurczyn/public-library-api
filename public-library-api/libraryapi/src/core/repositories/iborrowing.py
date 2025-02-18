"""A repository for borrowing entity."""

from abc import ABC, abstractmethod
from typing import Any, List
from datetime import date
from src.core.domain.borrowing import Borrowing, BorrowingIn


class IBorrowingRepository(ABC):
    """An abstract repository class for borrowing."""

    @abstractmethod
    async def create_borrowing(self, borrowing: BorrowingIn) -> Any:
        """Creates a new borrowing record.

        Args:
            borrowing (Borrowing): The borrowing data.

        Returns:
            Any: The created borrowing record.
        """

    @abstractmethod
    async def get_borrowing_by_id(self, borrowing_id: int) -> Borrowing | None:
        """Fetches a borrowing record by its ID.

        Args:
            borrowing_id (int): The borrowing's ID.

        Returns:
            Borrowing | None: The borrowing record if found, otherwise None.
        """

    @abstractmethod
    async def get_active_borrowings_by_user(self, user_id: int) -> list[Borrowing]:
        """Fetches active borrowings for a user.

        Args:
            user_id (int): The user's id.

        Returns:
            list[Borrowing]: A list of active borrowings.
        """

    @abstractmethod
    async def list_all_borrowings(self) -> List[Borrowing]:
        """Lists all borrowing records.

        Returns:
            List[Borrowing]: A list of all borrowings.
        """

    @abstractmethod
    async def mark_borrowing_as_returned(self, borrowing_id: int, return_date: date) -> bool:
        """Marks a borrowing as returned.

        Args:
            borrowing_id (int): The borrowing's id.
            return_date (date): The return date.

        Returns:
            bool: True if updated successfully, False otherwise.
        """

    @abstractmethod
    async def get_borrowing_history_by_user(self, user_id: int) -> List[Borrowing]:
        """Fetches borrowing history for a user.

        Args:
            user_id (int): The user's id.

        Returns:
            List[Borrowing]: A list of past borrowings for the user.
        """

    @abstractmethod
    async def delete_borrowing(self, borrowing_id: int) -> bool:
        """Deletes a borrowing record by its id.

        Args:
            borrowing_id (int): The borrowing's id.

        Returns:
            bool: True if the deletion was successful, otherwise False.
        """

    @abstractmethod
    async def update_borrowing(self, borrowing_id: int, borrowing_data: BorrowingIn) -> Borrowing | None:
        """Updates an existing borrowing record.

        Args:
            borrowing_id (int): The borrowing's id to update.
            borrowing_data (BorrowingIn): The updated borrowing data.

        Returns:
            Borrowing | None: The updated borrowing record if successful, otherwise None.
        """