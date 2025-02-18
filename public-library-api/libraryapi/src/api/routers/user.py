from fastapi import APIRouter, Depends, HTTPException
from dependency_injector.wiring import inject, Provide
from src.container import Container
from typing import List

from src.core.domain.user import User, UserIn
from src.infrastructure.dto.tokendto import TokenDTO
from src.infrastructure.dto.userdto import UserDTO
from src.infrastructure.services.iuser import IUserService
from src.infrastructure.repositories.user import UserRepository


router = APIRouter(prefix="/User", tags=["User"])
user_repository = UserRepository()


@router.post("/register", response_model=UserDTO, status_code=201)
@inject
async def register_user(
        user: UserIn,
        service: IUserService = Depends(Provide[Container.user_service]),
) -> dict:
    if new_user := await service.register_user(user):
        return UserDTO(**dict(new_user)).model_dump()

    raise HTTPException(
        status_code=400,
        detail="The user with provided e-mail already exists",
    )


@router.post("/token", response_model=TokenDTO, status_code=200)
@inject
async def authenticate_user(
    user: UserIn,
    service: IUserService = Depends(Provide[Container.user_service]),
) -> dict:

    if token_details := await service.authenticate_user(user):
        print("user confirmed")
        return token_details.model_dump()

    raise HTTPException(
        status_code=401,
        detail="Provided incorrect credentials",
    )

@router.get("/", response_model=List[User], status_code=200)
@inject
async def list_users(
    service: IUserService = Depends(Provide[Container.user_service]),
) -> List[User]:
    """
    Returns list of all users.

    Args:
        service (IUserService): A service supporting operations on users.

    Returns:
        List[User]: List of all users.
    """
    return await service.list_users()

@router.get("/{user_id}", response_model=User, status_code=200)
@inject
async def get_user_by_id(
        user_id: int,
        service: IUserService = Depends(Provide[Container.user_service]),
) -> User:
    user = await service.get_user_by_id(user_id)
    if user:
        return user
    raise HTTPException(status_code=404, detail="User not found")


@router.get("/email/{email}", response_model=User, status_code=200)
@inject
async def get_user_by_email(
        email: str,
        service: IUserService = Depends(Provide[Container.user_service]),
) -> User:
    user = await service.get_user_by_email(email)
    if user:
        return user
    raise HTTPException(status_code=404, detail="User not found")


@router.put("/users/{user_id}", response_model=User, summary="Update user data", status_code=200)
async def update_user(user_id: int, user_data: UserIn):
    updated_user = await user_repository.update_user(user_id, user_data)
    if not updated_user:
        raise HTTPException(status_code=404, detail="User not found")
    return updated_user


@router.delete("/users/{user_id}", response_model=dict, summary="Delete user", status_code=200)
async def delete_user(user_id: int):
    success = await user_repository.delete_user(user_id)
    if not success:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted successfully"}

