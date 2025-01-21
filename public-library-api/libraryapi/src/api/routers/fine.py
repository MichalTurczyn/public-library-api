from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException, status
from dependency_injector.wiring import inject, Provide

from src.container import Container
from src.core.domain.fine import Fine, FineIn
from src.infrastructure.services.ifine import IFineService

router = APIRouter(prefix="/fines", tags=["fines"])


@router.post("/", response_model=Fine, status_code=status.HTTP_201_CREATED)
@inject
async def create_fine(
    fine: FineIn,
    service: IFineService = Depends(Provide[Container.fine_service]),
) -> Fine:
    """
    Endpoint do tworzenia nowej kary (fine).

    Args:
        fine (FineIn): Dane wejściowe dotyczące kary.
        service (IFineService): Serwis do obsługi kary.

    Returns:
        Fine: Utworzony obiekt kary.
    """
    new_fine = await service.create_fine(fine)
    return new_fine


@router.get("/user/{user_id}", response_model=list[Fine], status_code=status.HTTP_200_OK)
@inject
async def list_fines_by_user(
    user_id: UUID,
    service: IFineService = Depends(Provide[Container.fine_service]),
) -> list[Fine]:
    """
    Endpoint do pobierania listy kar dla danego użytkownika.

    Args:
        user_id (UUID): UUID użytkownika.
        service (IFineService): Serwis do obsługi kary.

    Raises:
        HTTPException: 404 jeśli użytkownik nie ma żadnych kar.

    Returns:
        list[Fine]: Lista obiektów kary.
    """
    fines = await service.list_fines_by_user(user_id)
    if not fines:
        raise HTTPException(status_code=404, detail="No fines found for this user.")
    return fines


@router.get("/unpaid/{user_id}", summary="List unpaid fines for a user")
@inject
async def list_unpaid_fines(
    user_id: UUID,
    service: IFineService = Depends(Provide[Container.fine_service]),
):
    fines = await service.list_unpaid_fines_by_user(user_id)
    return fines

@router.patch("/{fine_id}/pay", summary="Mark a fine as paid")
@inject
async def mark_fine_as_paid(
    fine_id: UUID,
    service: IFineService = Depends(Provide[Container.fine_service]),
):
    success = await service.mark_fine_as_paid(fine_id)
    if not success:
        raise HTTPException(status_code=404, detail="Fine not found")
    return {"message": "Fine marked as paid"}

@router.get("/unpaid/total/{user_id}", summary="Get total unpaid fines for a user")
@inject
async def get_total_unpaid_fines(
    user_id: UUID,
    service: IFineService = Depends(Provide[Container.fine_service]),
):
    total = await service.get_total_unpaid_fines(user_id)
    return {"total": total}