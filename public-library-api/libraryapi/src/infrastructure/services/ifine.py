"""Module containing fine service abstractions."""

from abc import ABC, abstractmethod
from typing import Iterable
from pydantic import UUID4

from src.core.domain.fine import Fine, FineIn
from src.infrastructure.dto.finedto import FineDTO


class IFineService(ABC):
    """An abstract class representing the protocol for fine services."""

    @abstractmethod
    async def add_fine(self, fine_data: FineIn) -> Fine | None:
        """Adds a new fine to the repository.

        Args:
            fine_data (FineIn): The details of the fine.

        Returns:
            Fine | None: The newly created fine.
        """

    @abstractmethod
    async def get_fine_by_id(self, fine_id: UUID4) -> FineDTO | None:
        """Fetches a fine using its UUID.

        Args:
            fine_id (UUID4): The UUID of the fine.

        Returns:
            FineDTO | None: The fine details if found.
        """

    @abstractmethod
    async def list_fines(self) -> Iterable[FineDTO]:
        """Lists all fines.

        Returns:
            Iterable[FineDTO]: A collection of all fines.
        """

    @abstractmethod
    async def update_fine(self, fine_id: UUID4, fine_data: FineIn) -> Fine | None:
        """Updates an existing fine.

        Args:
            fine_id (UUID4): The UUID of the fine to update.
            fine_data (FineIn): The updated fine details.

        Returns:
            Fine | None: The updated fine if successful.
        """

    @abstractmethod
    async def delete_fine(self, fine_id: UUID4) -> bool:
        """Deletes a fine by its UUID.

        Args:
            fine_id (UUID4): The UUID of the fine to delete.

        Returns:
            bool: True if the deletion was successful, otherwise False.
        """

    @abstractmethod
    async def get_fines_by_user(self, user_id: UUID4) -> Iterable[FineDTO]:
        """Fetches all fines associated with a specific user.

        Args:
            user_id (UUID4): The UUID of the user.

        Returns:
            Iterable[FineDTO]: A collection of fines for the user.
        """

    @abstractmethod
    async def list_unpaid_fines_by_user(self, user_id: UUID4) -> list[Fine]:
        pass

    @abstractmethod
    async def mark_fine_as_paid(self, fine_id: UUID4) -> bool:
        pass

    @abstractmethod
    async def get_total_unpaid_fines(self, user_id: UUID4) -> float:
        pass