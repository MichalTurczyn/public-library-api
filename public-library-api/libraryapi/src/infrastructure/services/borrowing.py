"""Module containing the implementation of borrowing services."""

from typing import Iterable
from pydantic import UUID4

from src.core.domain.borrowing import Borrowing
from src.infrastructure.dto.borrowingdto import BorrowingDTO
from src.infrastructure.services.iborrowing import IBorrowingService


class BorrowingService(IBorrowingService):
    """A service class implementing the IBorrowingService protocol."""

    async def create_borrowing(self, borrowing_data: Borrowing) -> Borrowing | None:
        """Adds a new borrowing record to the repository."""
        # Implementation logic for adding a borrowing record
        pass

    async def get_borrowing_by_id(self, borrowing_id: UUID4) -> BorrowingDTO | None:
        """Fetches a borrowing record using its UUID."""
        # Implementation logic for fetching a borrowing record by UUID
        pass

    async def list_borrowings(self) -> Iterable[BorrowingDTO]:
        """Lists all borrowing records."""
        # Implementation logic for listing all borrowings
        pass

    async def get_borrowings_by_user(self, user_id: UUID4) -> Iterable[BorrowingDTO]:
        """Fetches all borrowing records for a specific user."""
        # Implementation logic for fetching borrowings by user
        pass

    async def update_borrowing(
        self, borrowing_id: UUID4, borrowing_data: Borrowing
    ) -> Borrowing | None:
        """Updates an existing borrowing record."""
        # Implementation logic for updating a borrowing record
        pass

    async def delete_borrowing(self, borrowing_id: UUID4) -> bool:
        """Deletes a borrowing record by its UUID."""
        # Implementation logic for deleting a borrowing record
        pass

    async def get_borrowing_history(self, user_id: UUID4) -> list[Borrowing]:
        return await self.get_borrowing_history(user_id)