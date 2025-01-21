"""Module containing the implementation of fine services."""

from typing import Iterable
from pydantic import UUID4

from src.core.domain.fine import Fine, FineIn
from src.infrastructure.dto.finedto import FineDTO
from src.infrastructure.services.ifine import IFineService


class FineService(IFineService):
    """A service class implementing the IFineService protocol."""

    async def add_fine(self, fine_data: FineIn) -> Fine | None:
        """Adds a new fine to the repository."""
        # Implementation logic for adding a fine
        pass

    async def get_fine_by_id(self, fine_id: UUID4) -> FineDTO | None:
        """Fetches a fine using its UUID."""
        # Implementation logic for fetching a fine by UUID
        pass

    async def list_fines(self) -> Iterable[FineDTO]:
        """Lists all fines."""
        # Implementation logic for listing all fines
        pass

    async def update_fine(self, fine_id: UUID4, fine_data: FineIn) -> Fine | None:
        """Updates an existing fine."""
        # Implementation logic for updating a fine
        pass

    async def delete_fine(self, fine_id: UUID4) -> bool:
        """Deletes a fine by its UUID."""
        # Implementation logic for deleting a fine
        pass

    async def get_fines_by_user(self, user_id: UUID4) -> Iterable[FineDTO]:
        """Fetches all fines associated with a specific user."""
        # Implementation logic for fetching fines by user
        pass

    async def list_unpaid_fines_by_user(self, user_id: UUID4) -> list[Fine]:
        return await self.repository.list_unpaid_fines_by_user(user_id)

    async def mark_fine_as_paid(self, fine_id: UUID4) -> bool:
        return await self.repository.mark_fine_as_paid(fine_id)

    async def get_total_unpaid_fines(self, user_id: UUID4) -> float:
        return await self.repository.get_total_unpaid_fines(user_id)