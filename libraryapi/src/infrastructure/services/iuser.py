from abc import ABC, abstractmethod
from typing import Iterable

from src.core.domain.user import UserIn
from src.infrastructure.dto.userdto import UserDTO
from src.infrastructure.dto.tokendto import TokenDTO


class IUserService(ABC):
    """An abstract service class for users."""

    @abstractmethod
    async def register_user(self, user: UserIn) -> UserDTO | None:
        """Register a new user.

        Args:
            data (UserIn): The user input data.

        Returns:
            Any: The created user.
        """

    @abstractmethod
    async def authenticate_user(self, user: UserIn) -> TokenDTO | None:
        """Authenticate a user.

        Args:
            email (str): The user's email.
            password (str): The user's password.

        Returns:
            Any: The user details with a token if authenticated.
        """

    @abstractmethod
    async def list_users(self) -> Iterable[UserDTO]:
        """Lists all users in the repository.

        Returns:
            Iterable[UserDTO]: A list of all users.
        """

    @abstractmethod
    async def get_user_by_id(self, user_id: int) -> UserDTO | None:
        """Get a user by their ID.

        Args:
            user_id (int): The user's ID.

        Returns:
            Any: The user details.
        """

    @abstractmethod
    async def get_user_by_email(self, user_id: int) -> UserDTO | None:
        """Get a user by their ID.

        Args:
            user_id (int): The user's ID.

        Returns:
            Any: The user details.
        """

    @abstractmethod
    async def update_user(self, user_id: int, user_data: UserIn) -> UserDTO | None:
        """Update user information.

        Args:
            user_id (int): The user's ID to update.
            user_data (UserIn): The updated user data.

        Returns:
            Any: The updated user details.
        """

    @abstractmethod
    async def delete_user(self, user_id: int) -> bool:
        """Delete a user by id.

        Args:
            user_id (int): The user's ID to delete.

        Returns:
            bool: True if the user was successfully deleted, False otherwise.
        """