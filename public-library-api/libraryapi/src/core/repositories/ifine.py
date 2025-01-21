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

    @abstractmethod
    async def list_unpaid_fines_by_user(self, user_id: UUID4) -> list[Fine]:
        """Lists all unpaid fines for a specific user.

        Args:
            user_id (UUID4): The user's UUID.

        Returns:
            List[Fine]: A list of unpaid fines for the user.
        """
        pass

    @abstractmethod
    async def mark_fine_as_paid(self, fine_id: UUID4) -> bool:
        """Marks a fine as paid.

        Args:
            fine_id (UUID4): The fine's UUID.

        Returns:
            bool: True if the operation was successful, otherwise False.
        """
        pass

    @abstractmethod
    async def get_total_unpaid_fines(self, user_id: UUID4) -> float:
        """Calculates the total amount of unpaid fines for a user.

        Args:
            user_id (UUID4): The user's UUID.

        Returns:
            float: The total amount of unpaid fines.
        """
        pass