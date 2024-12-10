"""A repository for payment entity."""

from abc import ABC, abstractmethod
from pydantic import UUID4

from src.core.domain.payment import Payment, PaymentIn


class IPaymentRepository(ABC):
    """An abstract repository class for payment."""

    @abstractmethod
    async def process_payment(self, payment: PaymentIn) -> Payment:
        """Processes a payment.

        Args:
            payment (PaymentIn): The payment input data.

        Returns:
            Payment: The processed payment object.
        """

    @abstractmethod
    async def get_payment_by_id(self, payment_id: UUID4) -> Payment | None:
        """Fetches a payment by its ID.

        Args:
            payment_id (UUID4): The UUID of the payment.

        Returns:
            Payment | None: The payment object if found.
        """
