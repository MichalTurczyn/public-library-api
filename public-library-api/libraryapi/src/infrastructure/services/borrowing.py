"""Module containing the implementation of borrowing services."""

from typing import Iterable
from datetime import date

from src.core.domain.borrowing import Borrowing, BorrowingIn
from src.infrastructure.dto.borrowingdto import BorrowingDTO
from src.infrastructure.services.iborrowing import IBorrowingService
from src.core.repositories.iborrowing import IBorrowingRepository


class BorrowingService(IBorrowingService):
    """A service class implementing the IBorrowingService protocol."""
    _repository: IBorrowingService

    def __init__(self, repository: IBorrowingRepository) -> None:
        self._repository = repository

    async def create_borrowing(self, borrowing_data: Borrowing) -> Borrowing | None:
        """
        Creates a new borrowing record.

        Args:
            borrowing_data (Borrowing): The data for the new borrowing.

        Returns:
            Borrowing | None: The newly created borrowing record if successful, otherwise None.
        """
        return await self._repository.create_borrowing(borrowing_data)

    async def get_borrowing_by_id(self, borrowing_id: int) -> BorrowingDTO | None:
        """
        Retrieves a borrowing record by its ID.

        Args:
            borrowing_id (int): The ID of the borrowing.

        Returns:
            BorrowingDTO | None: The borrowing record if found, otherwise None.
        """
        return await self._repository.get_borrowing_by_id(borrowing_id)

    async def get_active_borrowings_by_user(self, user_id: int) -> Iterable[BorrowingDTO]:
        """
        Retrieves all active borrowings for a specific user.

        Args:
            user_id (int): The ID of the user.

        Returns:
            Iterable[BorrowingDTO]: A list of active borrowings for the user.
        """
        return await self._repository.get_active_borrowings_by_user(user_id)

    async def list_all_borrowings(self) -> Iterable[BorrowingDTO]:
        """
        Lists all borrowing records in the repository.

        Returns:
            Iterable[BorrowingDTO]: A list of all borrowings.
        """
        return await self._repository.list_all_borrowings()
    
    async def mark_borrowing_as_returned(self, borrowing_id: int, return_date: date) -> bool:
        """Marks a borrowing as returned.

        Args:
            borrowing_id (int): ID of the borrowing to mark as returned.
            return_date (date): The actual return date.

        Returns:
            bool: True if the update was successful, otherwise False.
        """
        return await self._repository.mark_borrowing_as_returned(borrowing_id, return_date)
    
    async def get_borrowing_history_by_user(self, user_id: int) -> list[Borrowing]:
        """
        Retrieves the borrowing history for a specific user.

        Args:
            user_id (int): The ID of the user.

        Returns:
            list[Borrowing]: A list of completed borrowings for the user.
        """
        return await self._repository.get_borrowing_history_by_user(user_id)
    
    async def delete_borrowing(self, borrowing_id: int) -> bool:
        """
        Deletes a borrowing record by its ID.

        Args:
            borrowing_id (int): The ID of the borrowing to delete.

        Returns:
            bool: True if the deletion was successful, otherwise False.
        """
        return await self._repository.delete_borrowing(borrowing_id)

    async def update_borrowing(
        self, borrowing_id: int, borrowing_data: BorrowingIn
    ) -> BorrowingDTO:
        """
        Updates an existing borrowing record.

        Args:
            borrowing_id (int): ID of the borrowing to update.
            borrowing_data (BorrowingIn): The updated borrowing data.

        Returns:
            BorrowingDTO: The updated borrowing record if successful.
        """
        return await self._repository.update_borrowing(borrowing_id, borrowing_data)