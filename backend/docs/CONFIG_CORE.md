# Config Core Module

## Overview

The `config.py` module provides centralized configuration management for the AI Project Planner Agent backend using Pydantic Settings. It handles environment variable loading, validation, and provides type-safe access to application settings across different deployment environments. This module ensures secure and flexible configuration without hard-coded values.

## Architecture

The module uses Pydantic's `BaseSettings` with `SettingsConfigDict` to create a robust configuration system that:

- Loads settings from environment variables and `.env` files
- Provides validation and type conversion
- Supports default values for optional settings
- Enables environment-specific configurations

## Settings Class

### Class Definition
```python
class Settings(BaseSettings):
    # Configuration fields with validation and defaults
```

### Configuration Fields

#### Application Settings
- `app_name: str` - Application name (default: "AI Project Planner Agent")
- `environment: str` - Runtime environment (default: "development")
- `debug: bool` - Debug mode flag (default: False)

#### Azure OpenAI Integration
- `azure_openai_endpoint: str` - Azure OpenAI service endpoint URL (required)
- `azure_openai_api_key: str` - API key for authentication (required)
- `azure_openai_deployment: str` - Model deployment name (required)
- `azure_openai_api_version: str` - API version string (required)

#### Database Configuration
- `database_url: str` - Database connection string (default: "sqlite:///./plans.db")

#### Frontend Integration
- `frontend_url: str` - CORS-allowed frontend URL (default: "http://localhost:5173")

## Configuration Sources

### Environment Variables
Settings are loaded from environment variables with case-insensitive matching:
- Supports both `APP_NAME` and `app_name` formats
- Required fields must be set in the environment
- Optional fields use sensible defaults

### .env File
- Automatic loading from `.env` file in the project root
- Overrides environment variables if present
- Useful for local development and testing

### Default Values
Provides safe defaults for development:
- Local SQLite database
- Development environment mode
- Local frontend URL

## Validation and Type Safety

### Pydantic Validation
- Automatic type conversion and validation
- Required field enforcement
- Custom validation rules for complex settings

### Field Aliases
Uses field aliases for environment variable mapping:
```python
app_name: str = Field(default="AI Project Planner Agent", alias="APP_NAME")
```

## Security Considerations

### Sensitive Data Handling
- API keys and credentials loaded from environment
- No hard-coded secrets in source code
- Environment variable isolation for different deployments

### Validation Security
- Input sanitization through Pydantic
- Type checking prevents injection attacks
- Required field validation prevents incomplete configurations

## Usage Pattern

### Singleton Pattern
The module implements a singleton pattern using `@lru_cache`:
```python
@lru_cache
def get_settings() -> Settings:
    return Settings()
```

### Global Access
Settings are accessed throughout the application:
```python
from app.core.config import get_settings

settings = get_settings()
app_name = settings.app_name
```

## Environment-Specific Configuration

### Development Environment
- SQLite database for simplicity
- Debug mode enabled
- Local frontend URLs allowed
- Relaxed CORS policies

### Production Environment
- SQL Server database for scalability
- Debug mode disabled
- Production frontend URLs
- Strict CORS configuration

## Integration Points

### Application Initialization
Used in `main.py` for:
- FastAPI app configuration
- CORS middleware setup
- Environment-specific routing

### Service Layer
Consumed by `ai_services.py` for:
- Azure OpenAI client configuration
- API endpoint and authentication setup

### Database Layer
Used in `database.py` for:
- Database URL selection
- Engine configuration based on environment

## Error Handling

### Validation Errors
- Pydantic raises `ValidationError` for invalid configurations
- Clear error messages for missing required fields
- Type conversion failures are reported with context

### Missing Configuration
- Application fails to start with missing required settings
- Detailed error messages guide configuration setup

## Testing Support

### Test Configuration
Settings can be overridden for testing:
- Environment variable mocking
- Custom `.env` files for test scenarios
- Isolated configuration for test suites

### Mock Settings
Test modules can provide mock configurations:
```python
# Override settings for testing
test_settings = Settings(azure_openai_api_key="test_key")
```

## Deployment Considerations

### Environment Variables
Production deployments require:
- Secure storage of API keys
- Database connection strings
- Environment-specific URLs

### Configuration Management
Supports various configuration management tools:
- Docker environment files
- Kubernetes secrets
- Cloud platform environment variables

## Extensibility

### Adding New Settings
New configuration fields can be added:
```python
new_setting: str = Field(default="value", alias="NEW_SETTING")
```

### Custom Validation
Pydantic validators can be added for complex validation:
```python
@field_validator('database_url')
def validate_database_url(cls, v):
    # Custom validation logic
    return v
```

## Best Practices

The configuration module follows best practices:
- Single source of truth for all settings
- Type-safe configuration access
- Environment variable security
- Clear separation of concerns
- Comprehensive validation
- Documentation of all settings

## Maintenance

### Version Compatibility
- Pydantic version compatibility
- Environment variable naming consistency
- Backward compatibility for existing deployments

### Documentation Updates
- Settings documentation kept current
- Environment setup guides updated
- Deployment instructions maintained

This module provides a solid foundation for application configuration, ensuring reliability, security, and maintainability across different environments.