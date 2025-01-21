"""A repository for borrowing entity."""

from abc import ABC, abstractmethod
from typing import Any, List
from pydantic import UUID4
from datetime import date
from src.core.domain.borrowing import Borrowing


class IBorrowingRepository(ABC):
    """An abstract repository class for borrowing."""

    @abstractmethod
    async def create_borrowing(self, borrowing: Borrowing) -> Any:
        """Creates a new borrowing record.

        Args:
            borrowing (Borrowing): The borrowing data.

        Returns:
            Any: The created borrowing record.
        """

    @abstractmethod
    async def get_active_borrowings_by_user(self, user_id: UUID4) -> list[Borrowing]:
        """Fetches active borrowings for a user.

        Args:
            user_id (UUID4): The user's UUID.

        Returns:
            list[Borrowing]: A list of active borrowings.
        """

    @abstractmethod
    async def mark_borrowing_as_returned(self, borrowing_id: UUID4, return_date: date) -> bool:
        """Marks a borrowing as returned.

        Args:
            borrowing_id (UUID4): The borrowing's UUID.
            return_date (date): The return date.

        Returns:
            bool: True if updated successfully, False otherwise.
        """

    @abstractmethod
    async def get_borrowing_history(self, user_id: UUID4) -> List[Borrowing]:
        """Fetches borrowing history for a user.

        Args:
            user_id (UUID4): The user's UUID.

        Returns:
            List[Borrowing]: A list of past borrowings for the user.
        """
        pass