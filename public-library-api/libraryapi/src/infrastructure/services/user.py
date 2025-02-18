"""A module containing user service."""
from typing import Iterable
from src.core.domain.user import UserIn
from src.core.repositories.iuser import IUserRepository
from src.infrastructure.dto.userdto import UserDTO
from src.infrastructure.dto.tokendto import TokenDTO
from src.infrastructure.services.iuser import IUserService
from src.infrastructure.utils.password import verify_password
from src.infrastructure.utils.token import generate_user_token


class UserService(IUserService):
    """An abstract class for user service."""

    _repository: IUserRepository

    def __init__(self, repository: IUserRepository) -> None:
        self._repository = repository

    async def register_user(self, user: UserIn) -> UserDTO | None:
        """A method registering a new user.

        Args:
            user (UserIn): The user input data.

        Returns:
            UserDTO | None: The user DTO model.
        """

        return await self._repository.register_user(user)

    async def authenticate_user(self, user: UserIn) -> TokenDTO | None:
        """The method authenticating the user.

        Args:
            user (UserIn): The user data.

        Returns:
            TokenDTO | None: The token details.
        """

        if user_data := await self._repository.get_user_by_email(user.email):
            if verify_password(user.password, user_data.password):
                token_details = generate_user_token(user_data.id)
                return TokenDTO(token_type="Bearer", **token_details)

            return None

        return None
    
    async def list_users(self) -> Iterable[UserDTO]:
        """Lists all users available in the repository.

        Returns:
            Iterable[UserDTO]: A collection of all users.
        """
        users = await self._repository.list_users()
        return [UserDTO(**user.dict()) for user in users]

    async def get_user_by_id(self, id: int) -> UserDTO | None:
        """A method getting user by id.

        Args:
            id (id5): The id of the user.

        Returns:
            UserDTO | None: The user data, if found.
        """

        return await self._repository.get_user_by_id(id)

    async def get_user_by_email(self, email: str) -> UserDTO | None:
        """A method getting user by email.

        Args:
            email (str): The email of the user.

        Returns:
            UserDTO | None: The user data, if found.
        """

        return await self._repository.get_user_by_email(email)
    
    async def update_user(self, user_id: int, user_data: UserIn) -> UserDTO | None:
        """Update user data."""
        updated_user = await self._repository.update_user(user_id, user_data)
        if updated_user:
            return UserDTO(**updated_user.dict())
        return None

    async def delete_user(self, user_id: int) -> bool:
        """Delete user."""
        return await self._repository.delete_user(user_id)