"""A repository for user entity."""

from abc import ABC, abstractmethod
from typing import Any
from typing import List
from src.core.domain.user import UserIn, User


class IUserRepository(ABC):
    """An abstract repository class for user."""

    @abstractmethod
    async def register_user(self, user: UserIn) -> Any | None:
        """A method registering new user.

        Args:
            user (UserIn): The user input data.

        Returns:
            Any | None: The new user object.
        """


    async def authenticate_user(self, user: UserIn) -> Any | None:
        """A method authenticating a user.

        Args:
            user (UserIn): The user input data (e.g., email and password).

        Returns:
            Any | None: Token or user object if authentication is successful, None otherwise.
        """

    @abstractmethod
    async def list_users(self) -> List[User]:
        """Lists all users.

        Returns:
            List[User]: A list of all users.
        """

    @abstractmethod
    async def get_user_by_id(self, id: int) -> Any | None:
        """A method getting user by id.

        Args:
            id (int): id of the user.

        Returns:
            Any | None: The user object if exists.
        """

    @abstractmethod
    async def get_user_by_email(self, email: str) -> Any | None:
        """A method getting user by email.

        Args:
            email (str): The email of the user.

        Returns:
            Any | None: The user object if exists.
        """

    @abstractmethod
    async def update_user(self, id: int, user_data: UserIn) -> Any | None:
        """A method updating user information.

        Args:
            id (int): id of the user to update.
            user_data (UserIn): The updated user data.

        Returns:
            Any | None: The updated user object if the operation was successful.
        """

    @abstractmethod
    async def delete_user(self, id: int) -> bool:
        """A method deleting a user by id.

        Args:
            id (int): id of the user to delete.

        Returns:
            bool: True if the user was successfully deleted, False otherwise.
        """