from pydantic import UUID4
from datetime import date
from fastapi import APIRouter, Depends, HTTPException, status
from dependency_injector.wiring import inject, Provide
from src.container import Container
from src.core.domain.borrowing import Borrowing
from src.infrastructure.services.iborrowing import IBorrowingService

router = APIRouter(prefix="/borrowings", tags=["borrowings"])


@router.post("/", response_model=Borrowing, status_code=status.HTTP_201_CREATED)
@inject
async def create_borrowing(
    borrowing: Borrowing,
    service: IBorrowingService = Depends(Provide[Container.borrowing_service]),
) -> Borrowing:
    """
    Endpoint do tworzenia nowego wypożyczenia.

    Args:
        borrowing (Borrowing): Dane dotyczące nowego wypożyczenia.
        service (IBorrowingService): Serwis do obsługi wypożyczeń.

    Returns:
        Borrowing: Utworzone wypożyczenie.
    """
    new_borrowing = await service.create_borrowing(borrowing)
    return new_borrowing


@router.get("/active/{user_id}", response_model=list[Borrowing], status_code=status.HTTP_200_OK)
@inject
async def get_active_borrowings_by_user(
    user_id: UUID4,
    service: IBorrowingService = Depends(Provide[Container.borrowing_service]),
) -> list[Borrowing]:
    """
    Endpoint do pobierania aktywnych wypożyczeń użytkownika.

    Args:
        user_id (UUID): UUID użytkownika.
        service (IBorrowingService): Serwis do obsługi wypożyczeń.

    Returns:
        list[Borrowing]: Lista aktywnych wypożyczeń.
    """
    active_borrowings = await service.get_active_by_user(user_id)
    return active_borrowings


@router.patch("/{borrowing_id}/return", status_code=status.HTTP_200_OK)
@inject
async def mark_borrowing_as_returned(
    borrowing_id: UUID4,
    return_date: date,
    service: IBorrowingService = Depends(Provide[Container.borrowing_service]),
) -> dict:
    """
    Endpoint do oznaczania wypożyczenia jako zwrócone.

    Args:
        borrowing_id (UUID): UUID wypożyczenia.
        return_date (date): Data zwrotu.
        service (IBorrowingService): Serwis do obsługi wypożyczeń.

    Raises:
        HTTPException: 404 jeśli wypożyczenie nie istnieje lub aktualizacja się nie powiodła.

    Returns:
        dict: Komunikat o sukcesie.
    """
    success = await service.mark_as_returned(borrowing_id, return_date)
    if not success:
        raise HTTPException(status_code=404, detail="Borrowing not found or update failed.")
    return {"message": "Borrowing marked as returned successfully."}


@router.get("/history/{user_id}", summary="Get borrowing history")
@inject
async def get_borrowing_history(
    user_id: UUID4,
    service: IBorrowingService = Depends(Provide[Container.borrowing_service]),
):
    """
    Endpoint to fetch borrowing history for a user.

    Args:
        user_id (UUID4): UUID of the user.
        service (IBorrowingService): Injected borrowing service.

    Returns:
        List[Borrowing]: A list of completed borrowings for the user.
    """
    return await service.get_borrowing_history(user_id)