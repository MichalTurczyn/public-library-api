"""A repository for reservation entity."""

from abc import ABC, abstractmethod
from pydantic import UUID4

from src.core.domain.reservation import Reservation, ReservationIn


class IReservationRepository(ABC):
    """An abstract repository class for reservation."""

    @abstractmethod
    async def create_reservation(self, reservation: ReservationIn) -> Reservation:
        """Creates a new reservation.

        Args:
            reservation (ReservationIn): The reservation input data.

        Returns:
            Reservation: The created reservation object.
        """

    @abstractmethod
    async def list_reservations_by_user(self, user_id: UUID4) -> list[Reservation]:
        """Lists all reservations for a user.

        Args:
            user_id (UUID4): The user's UUID.

        Returns:
            list[Reservation]: A list of reservations.
        """


    @abstractmethod
    async def cancel_reservation(self, reservation_id: UUID4) -> bool:
        """Cancels a reservation by its ID.

        Args:
            reservation_id (UUID4): The UUID of the reservation.

        Returns:
            bool: True if the reservation was successfully canceled, False otherwise.
        """

    @abstractmethod
    async def get_by_uuid(self, reservation_id: UUID4) -> Reservation | None:
        """Fetches a reservation by its UUID.

        Args:
            reservation_id (UUID4): UUID of the reservation.

        Returns:
            Reservation | None: The reservation object if found.
        """

    @abstractmethod
    async def list_active_reservations(self) -> list[Reservation]:
        """Lists all active reservations.

        Returns:
            list[Reservation]: A list of active reservations.
        """
