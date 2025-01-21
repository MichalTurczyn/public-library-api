from abc import ABC, abstractmethod
from typing import Any, Iterable
from src.core.domain.reservation import ReservationIn


class IReservationService(ABC):
    """An abstract service class for reservations."""

    @abstractmethod
    async def create_reservation(self, data: ReservationIn) -> Any:
        """Create a new reservation.

        Args:
            data (ReservationIn): The reservation input data.

        Returns:
            Any: The created reservation.
        """

    @abstractmethod
    async def get_reservations_by_user(self, user_id: int) -> Iterable[Any]:
        """Get all reservations for a specific user.

        Args:
            user_id (int): The user's ID.

        Returns:
            Iterable[Any]: The reservations for the user.
        """

    @abstractmethod
    async def cancel_reservation(self, reservation_id: int) -> bool:
        """Cancel a reservation.

        Args:
            reservation_id (int): The reservation ID.

        Returns:
            bool: Success of the operation.
        """
