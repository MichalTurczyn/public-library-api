"""Configuration module for LibraryAPI."""

from typing import Optional
from pydantic_settings import BaseSettings, SettingsConfigDict



class BaseConfig(BaseSettings):
    """A class containing base settings configuration."""
    model_config = SettingsConfigDict(extra="ignore")



class AppConfig(BaseSettings):
    """A class containing app's configuration."""

    # Database settings
    DB_HOST: Optional[str] = None
    DB_NAME: Optional[str] = None
    DB_USER: Optional[str] = None
    DB_PASSWORD: Optional[str] = None

    # Security settings
    SECRET_KEY: Optional[str] = "your-secret-key"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    # Fine rate for overdue books
    FINE_RATE: float = 5.0

    # Debugging settings
    DEBUG: bool = True

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


config = AppConfig()
