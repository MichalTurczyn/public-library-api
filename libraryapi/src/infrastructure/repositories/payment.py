"""A repository for payment entity."""

from typing import Any
from pydantic import UUID4
from src.core.domain.payment import Payment, PaymentIn
from src.core.repositories.ipayment import IPaymentRepository
from src.db import payment_table, database


class PaymentRepository(IPaymentRepository):
    """A class implementing the database payment repository."""

    async def add_payment(self, data: PaymentIn) -> Any | None:
        query = payment_table.insert().values(**data.model_dump())
        new_payment_id = await database.execute(query)
        return await self.get_by_uuid(new_payment_id)

    async def get_by_uuid(self, payment_id: UUID4) -> Any | None:
        query = payment_table.select().where(payment_table.c.id == payment_id)
        payment = await database.fetch_one(query)
        return Payment(**dict(payment)) if payment else None

    async def list_payments_by_user(self, user_id: UUID4) -> list[Payment]:
        query = payment_table.select().where(payment_table.c.user_id == user_id)
        payments = await database.fetch_all(query)
        return [Payment(**dict(payment)) for payment in payments]

    async def mark_payment_as_processed(self, payment_id: UUID4) -> bool:
        query = payment_table.update().where(payment_table.c.id == payment_id).values(is_processed=True)
        result = await database.execute(query)
        return result > 0
