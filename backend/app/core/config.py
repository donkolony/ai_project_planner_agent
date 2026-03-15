from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field


class Settings(BaseSettings):
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
    return Settings()
