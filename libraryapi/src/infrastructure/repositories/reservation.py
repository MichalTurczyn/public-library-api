"""A repository for reservation entity."""

from typing import Any
from pydantic import UUID4
from src.core.domain.reservation import Reservation, ReservationIn
from src.core.repositories.ireservation import IReservationRepository
from src.db import reservation_table, database


class ReservationRepository(IReservationRepository):
    """A class implementing the database reservation repository."""

    async def reserve_book(self, data: ReservationIn) -> Any | None:
        query = reservation_table.insert().values(**data.model_dump())
        new_reservation_id = await database.execute(query)
        return await self.get_by_uuid(new_reservation_id)

    async def cancel_reservation(self, reservation_id: UUID4) -> bool:
        query = reservation_table.delete().where(reservation_table.c.id == reservation_id)
        result = await database.execute(query)
        return result > 0

    async def get_by_uuid(self, reservation_id: UUID4) -> Any | None:
        query = reservation_table.select().where(reservation_table.c.id == reservation_id)
        reservation = await database.fetch_one(query)
        return Reservation(**dict(reservation)) if reservation else None

    async def list_active_reservations(self) -> list[Reservation]:
        query = reservation_table.select().where(reservation_table.c.status == "active")
        reservations = await database.fetch_all(query)
        return [Reservation(**dict(reservation)) for reservation in reservations]
