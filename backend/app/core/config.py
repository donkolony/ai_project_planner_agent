"""
Application configuration and environment settings.

This module uses Pydantic Settings to load, validate, and manage environment
variables from the host environment or a local `.env` file.
"""

from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field


class Settings(BaseSettings):
    """
    Application settings model defining required and optional environment variables.

    Attributes:
        app_name (str): The name of the application.
        environment (str): The current runtime environment (e.g., development, production).
        debug (bool): Flag to enable or disable debug mode.
        azure_openai_endpoint (str): The Azure OpenAI service endpoint URL.
        azure_openai_api_key (str): The API key for Azure OpenAI authentication.
        azure_openai_deployment (str): The name of the Azure OpenAI model deployment.
        azure_openai_api_version (str): The API version string for Azure OpenAI.
        database_url (str): The connection string for the SQL database.
        frontend_url (str): The allowed CORS origin URL for the frontend application.
    """

    app_name: str = Field(default="AI Project Planner Agent", alias="APP_NAME")
    environment: str = Field(default="development", alias="ENVIRONMENT")
    debug: bool = Field(default=False, alias="DEBUG")

    azure_openai_endpoint: str = Field(..., alias="AZURE_OPENAI_ENDPOINT")
    azure_openai_api_key: str = Field(..., alias="AZURE_OPENAI_API_KEY")
    azure_openai_deployment: str = Field(..., alias="AZURE_OPENAI_DEPLOYMENT")
    azure_openai_api_version: str = Field(..., alias="AZURE_OPENAI_API_VERSION")

    database_url: str = Field(default="sqlite:///./plans.db", alias="DATABASE_URL")

    frontend_url: str = Field(default="http://localhost:5173", alias="FRONTEND_URL")

    model_config = SettingsConfigDict(env_file=".env", case_sensitive=False)


@lru_cache
def get_settings() -> Settings:
    """
    Retrieve the cached application settings.

    Uses `@lru_cache` to ensure the settings are only instantiated and the
    `.env` file is only read once during the application lifecycle, improving performance.

    Returns:
        Settings: The application settings instance.
    """
    return Settings()
