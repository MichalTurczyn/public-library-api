from abc import ABC, abstractmethod
from typing import Any
from src.core.domain.user import UserIn


class IUserService(ABC):
    """An abstract service class for users."""

    @abstractmethod
    async def register_user(self, data: UserIn) -> Any:
        """Register a new user.

        Args:
            data (UserIn): The user input data.

        Returns:
            Any: The created user.
        """

    @abstractmethod
    async def authenticate_user(self, email: str, password: str) -> Any:
        """Authenticate a user.

        Args:
            email (str): The user's email.
            password (str): The user's password.

        Returns:
            Any: The user details with a token if authenticated.
        """

    @abstractmethod
    async def get_user_by_id(self, user_id: int) -> Any:
        """Get a user by their ID.

        Args:
            user_id (int): The user's ID.

        Returns:
            Any: The user details.
        """

    @abstractmethod
    async def update_user(self, user_id: int, user_data: UserIn) -> Any:
        """Update user information.

        Args:
            user_id (UUID4): The user's ID to update.
            user_data (UserIn): The updated user data.

        Returns:
            Any: The updated user details.
        """
        pass

    @abstractmethod
    async def delete_user(self, user_id: int) -> bool:
        """Delete a user by UUID.

        Args:
            user_id (UUID4): The user's ID to delete.

        Returns:
            bool: True if the user was successfully deleted, False otherwise.
        """
        pass
