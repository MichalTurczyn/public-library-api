from typing import Any, Iterable
from src.core.repositories.ireservation import IReservationRepository
from src.core.domain.reservation import ReservationIn
from src.infrastructure.services.ireservation import IReservationService


class ReservationService(IReservationService):
    """A service for managing reservations."""

    def __init__(self, repository: IReservationRepository):
        self.repository = repository

    async def create_reservation(self, data: ReservationIn) -> Any:
        """Create a new reservation."""
        return await self.repository.add_reservation(data)

    async def get_reservations_by_user(self, user_id: int) -> Iterable[Any]:
        """Get all reservations for a specific user."""
        return await self.repository.get_reservations_by_user(user_id)

    async def cancel_reservation(self, reservation_id: int) -> bool:
        """Cancel a reservation."""
        return await self.repository.delete_reservation(reservation_id)
