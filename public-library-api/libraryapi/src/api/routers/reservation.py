from pydantic import UUID4
from fastapi import APIRouter, Depends, HTTPException, status
from dependency_injector.wiring import inject, Provide

from src.container import Container
from src.core.domain.reservation import Reservation, ReservationIn
from src.infrastructure.services.ireservation import IReservationService

router = APIRouter(prefix="/reservations", tags=["reservations"])


@router.post("/", response_model=Reservation, status_code=status.HTTP_201_CREATED)
@inject
async def create_reservation(
    reservation: ReservationIn,
    service: IReservationService = Depends(Provide[Container.reservation_service]),
) -> Reservation:
    """
    Endpoint do tworzenia nowej rezerwacji.

    Args:
        reservation (ReservationIn): Dane wejściowe dotyczące rezerwacji.
        service (IReservationService): Serwis do obsługi rezerwacji.

    Returns:
        Reservation: Utworzony obiekt rezerwacji.
    """
    new_reservation = await service.create_reservation(reservation)
    return new_reservation


@router.get("/user/{user_id}", response_model=list[Reservation], status_code=status.HTTP_200_OK)
@inject
async def list_reservations_by_user(
    user_id: UUID4,
    service: IReservationService = Depends(Provide[Container.reservation_service]),
) -> list[Reservation]:
    """
    Endpoint do pobierania listy rezerwacji dla użytkownika.

    Args:
        user_id (UUID): UUID użytkownika.
        service (IReservationService): Serwis do obsługi rezerwacji.

    Raises:
        HTTPException: 404 jeśli użytkownik nie ma żadnych rezerwacji.

    Returns:
        list[Reservation]: Lista rezerwacji dla danego użytkownika.
    """
    reservations = await service.list_reservations_by_user(user_id)
    if not reservations:
        raise HTTPException(status_code=404, detail="No reservations found for this user.")
    return reservations


@router.delete("/{reservation_id}", status_code=status.HTTP_204_NO_CONTENT)
@inject
async def cancel_reservation(
    reservation_id: UUID4,
    service: IReservationService = Depends(Provide[Container.reservation_service]),
) -> None:
    """
    Endpoint do anulowania rezerwacji.

    Args:
        reservation_id (UUID): UUID rezerwacji.
        service (IReservationService): Serwis do obsługi rezerwacji.

    Raises:
        HTTPException: 404 jeśli rezerwacja nie istnieje.
    """
    success = await service.cancel_reservation(reservation_id)
    if not success:
        raise HTTPException(status_code=404, detail="Reservation not found or already canceled.")
    return


@router.get("/active", response_model=list[Reservation], status_code=status.HTTP_200_OK)
@inject
async def list_active_reservations(
    service: IReservationService = Depends(Provide[Container.reservation_service]),
) -> list[Reservation]:
    """
    Endpoint do pobierania listy aktywnych rezerwacji.

    Args:
        service (IReservationService): Serwis do obsługi rezerwacji.

    Returns:
        list[Reservation]: Lista aktywnych rezerwacji.
    """
    reservations = await service.list_active_reservations()
    return reservations


@router.get("/{reservation_id}", response_model=Reservation, status_code=status.HTTP_200_OK)
@inject
async def get_reservation_by_id(
    reservation_id: UUID4,
    service: IReservationService = Depends(Provide[Container.reservation_service]),
) -> Reservation:
    """
    Endpoint do pobierania szczegółów rezerwacji po jej UUID.

    Args:
        reservation_id (UUID): UUID rezerwacji.
        service (IReservationService): Serwis do obsługi rezerwacji.

    Raises:
        HTTPException: 404 jeśli rezerwacja nie istnieje.

    Returns:
        Reservation: Szczegóły rezerwacji.
    """
    reservation = await service.get_by_uuid(reservation_id)
    if not reservation:
        raise HTTPException(status_code=404, detail="Reservation not found.")
    return reservation
