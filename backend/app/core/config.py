from pydantic_settings import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    app_name: str = "AI Project Planner Agent"
    environment: str = "development"  # development, staging, production
    debug: bool = False

    # Azure OpenAI Configuration
    azure_openai_endpoint: str | None = None
    azure_openai_api_key: str | None = None
    azure_openai_deployment: str | None = None
    azure_openai_api_version: str | None = None

    # Database Configuration
    database_url: str = "sqlite:///./plans.db"  # Default to SQLite for local development

    # Frontend URL for CORS
    frontend_url: str = "http://localhost:5173"

    model_config = {
        "env_file": ".env",
        "case_sensitive": False
    }


@lru_cache
def get_settings() -> Settings:
    return Settings()

