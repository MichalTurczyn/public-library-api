
from pydantic import UUID4
from fastapi import APIRouter, Depends, HTTPException, status
from dependency_injector.wiring import inject, Provide

from src.container import Container
from src.core.domain.user import User, UserIn
from src.infrastructure.services.iuser import IUserService
from src.infrastructure.repositories.user import UserRepository


router = APIRouter(prefix="/users", tags=["users"])
user_repository = UserRepository()


@router.post("/register", response_model=User, status_code=status.HTTP_201_CREATED)
@inject
async def register_user(
        user: UserIn,
        service: IUserService = Depends(Provide[Container.user_service]),
) -> User:
    """
    Endpoint do rejestracji nowego użytkownika.

    Args:
        user (UserIn): Dane użytkownika do rejestracji.
        service (IUserService): Wstrzyknięta zależność serwisu użytkowników.

    Returns:
        User: Zarejestrowany użytkownik.
    """
    existing_user = await service.get_by_email(user.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="User with this email already exists.")

    new_user = await service.register_user(user)
    if new_user:
        return new_user
    raise HTTPException(status_code=400, detail="Unable to register user")


@router.get("/{user_id}", response_model=User, status_code=status.HTTP_200_OK)
@inject
async def get_user_by_uuid(
        user_id: UUID4,
        service: IUserService = Depends(Provide[Container.user_service]),
) -> User:
    """
    Endpoint do pobierania użytkownika na podstawie identyfikatora UUID.

    Args:
        user_id (UUID): Identyfikator UUID użytkownika.
        service (IUserService): Wstrzyknięta zależność serwisu użytkowników.

    Raises:
        HTTPException: 404 jeśli użytkownik nie istnieje.

    Returns:
        User: Szczegóły użytkownika.
    """
    user = await service.get_by_uuid(user_id)
    if user:
        return user
    raise HTTPException(status_code=404, detail="User not found")


@router.get("/email/{email}", response_model=User, status_code=status.HTTP_200_OK)
@inject
async def get_user_by_email(
        email: str,
        service: IUserService = Depends(Provide[Container.user_service]),
) -> User:
    """
    Endpoint do pobierania użytkownika na podstawie adresu e-mail.

    Args:
        email (str): Adres e-mail użytkownika.
        service (IUserService): Wstrzyknięta zależność serwisu użytkowników.

    Raises:
        HTTPException: 404 jeśli użytkownik nie istnieje.

    Returns:
        User: Szczegóły użytkownika.
    """
    user = await service.get_by_email(email)
    if user:
        return user
    raise HTTPException(status_code=404, detail="User not found")


@router.put("/users/{user_id}", tags=["Users"], summary="Update user data")
async def update_user(user_id: UUID4, user_data: UserIn):
    updated_user = await user_repository.update_user(user_id, user_data)
    if not updated_user:
        raise HTTPException(status_code=404, detail="User not found")
    return updated_user


@router.delete("/users/{user_id}", tags=["Users"], summary="Delete user")
async def delete_user(user_id: UUID4):
    success = await user_repository.delete_user(user_id)
    if not success:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted successfully"}