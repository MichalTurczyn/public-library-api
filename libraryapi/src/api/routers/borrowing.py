from datetime import date
from fastapi import APIRouter, Depends, HTTPException
from dependency_injector.wiring import inject, Provide
from src.container import Container

from src.infrastructure.dto.borrowingdto import BorrowingDTO
from src.core.domain.borrowing import Borrowing, BorrowingIn
from src.infrastructure.services.iborrowing import IBorrowingService

router = APIRouter(prefix="/borrowings", tags=["borrowings"])


@router.post("/", response_model=BorrowingDTO, status_code=201)
@inject
async def create_borrowing(
    borrowing: BorrowingIn,
    service: IBorrowingService = Depends(Provide[Container.borrowing_service]),
) -> Borrowing:
    return await service.create_borrowing(borrowing)

@router.get("/{borrowing_id}", response_model=BorrowingDTO, status_code=200)
@inject
async def get_borrowing_by_id(
    borrowing_id: int,
    service: IBorrowingService = Depends(Provide[Container.borrowing_service]),
) -> BorrowingDTO:
    borrowing = await service.get_borrowing_by_id(borrowing_id)
    if not borrowing:
        raise HTTPException(status_code=404, detail="Borrowing not found.")
    return borrowing

@router.get("/active/{user_id}", response_model=list[Borrowing], status_code=200)
@inject
async def get_active_borrowings_by_user(
    user_id: int,
    service: IBorrowingService = Depends(Provide[Container.borrowing_service]),
) -> list[Borrowing]:
    active_borrowings = await service.get_active_borrowings_by_user(user_id)
    return active_borrowings

@router.get("/", response_model=list[BorrowingDTO], status_code=200)
@inject
async def list_all_borrowings(
    service: IBorrowingService = Depends(Provide[Container.borrowing_service]),
) -> list[BorrowingDTO]:
    return await service.list_all_borrowings()

@router.patch("/{borrowing_id}/return", status_code=200)
@inject
async def mark_borrowing_as_returned(
    borrowing_id: int,
    return_date: date,
    service: IBorrowingService = Depends(Provide[Container.borrowing_service]),
) -> dict:
    success = await service.mark_borrowing_as_returned(borrowing_id, return_date)
    if not success:
        raise HTTPException(status_code=404, detail="Borrowing not found or update failed.")
    return {"message": "Borrowing marked as returned successfully."}


@router.get("/history/{user_id}", summary="Get borrowing history by user", status_code=200)
@inject
async def get_borrowing_history_by_user(
    user_id: int,
    service: IBorrowingService = Depends(Provide[Container.borrowing_service]),
):
    """
    Endpoint to fetch borrowing history for a user.

    Args:
        user_id (int): id of the user.
        service (IBorrowingService): Injected borrowing service.

    Returns:
        List[Borrowing]: A list of completed borrowings for the user.
    """
    return await service.get_borrowing_history_by_user(user_id)

@router.delete("/{borrowing_id}", status_code=204)
@inject
async def delete_borrowing(
    borrowing_id: int,
    service: IBorrowingService = Depends(Provide[Container.borrowing_service]),
) -> None:
    success = await service.delete_borrowing(borrowing_id)
    if not success:
        raise HTTPException(status_code=404, detail="Borrowing not found.")
    
@router.put("/{borrowing_id}", response_model=Borrowing, status_code=200)
@inject
async def update_borrowing(
    borrowing_id: int,
    borrowing_data: BorrowingIn,
    service: IBorrowingService = Depends(Provide[Container.borrowing_service]),
) -> Borrowing:
    borrowing = await service.update_borrowing(borrowing_id, borrowing_data)
    if not borrowing:
        raise HTTPException(status_code=404, detail="Borrowing not found.")
    return borrowing