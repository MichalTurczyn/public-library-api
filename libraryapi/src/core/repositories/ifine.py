"""A repository for fine entity."""

from abc import ABC, abstractmethod
from pydantic import UUID4

from src.core.domain.fine import Fine, FineIn


class IFineRepository(ABC):
    """An abstract repository class for fine."""

    @abstractmethod
    async def create_fine(self, fine: FineIn) -> Fine:
        """Creates a new fine record.

        Args:
            fine (FineIn): The fine input data.

        Returns:
            Fine: The created fine object.
        """

    @abstractmethod
    async def list_fines_by_user(self, user_id: UUID4) -> list[Fine]:
        """Lists all fines for a user.

        Args:
            user_id (UUID4): The user's UUID.

        Returns:
            list[Fine]: A list of fines.
        """
