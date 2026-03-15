# Core Folder Overview

## Introduction

The `core` folder contains the foundational infrastructure components of the AI Project Planner Agent backend. It provides essential services for configuration management and database connectivity, establishing the core dependencies that other application modules rely upon. This separation ensures clean architecture and facilitates environment-specific deployments.

## Structure

The core folder consists of two critical modules:

### Configuration Module

- **config.py**: Manages application configuration through Pydantic Settings. It handles environment variable loading, validation, and provides a centralized configuration interface for the entire application.

### Database Module

- **database.py**: Handles database connection setup and session management using SQLModel. It configures database engines for different environments and provides session utilities for data operations.

## Key Components

### Configuration Management

The config.py module implements a robust configuration system that:

- Uses Pydantic's BaseSettings for type-safe configuration
- Loads settings from environment variables and .env files
- Provides validation and default values for all configuration parameters
- Supports different environments (development, production) with appropriate settings

### Database Infrastructure

The database.py module establishes the data persistence layer by:

- Creating SQLModel engine instances with environment-specific configurations
- Supporting multiple database backends (SQLite for development, SQL Server for production)
- Implementing connection pooling and optimization settings
- Providing session management utilities for database operations

## Configuration Parameters

The application supports the following key configuration settings:

- **Application Settings**: App name, environment mode, debug flags
- **AI Integration**: Azure OpenAI endpoint, API key, deployment name, and version
- **Database**: Connection URL supporting SQLite and SQL Server
- **Frontend Integration**: CORS-allowed origins for frontend applications

## Database Support

### Development Environment
- Uses SQLite for local development
- Provides fast, file-based database operations
- Simplifies setup and testing

### Production Environment
- Supports SQL Server (Azure SQL Database)
- Implements connection pooling and pre-ping for reliability
- Configures appropriate timeouts and recycling settings

## Integration Points

### Application Initialization
The core modules are imported early in the application lifecycle, providing configuration and database access to all other components.

### Dependency Injection
Database sessions are provided through FastAPI dependency injection, ensuring proper session management and transaction handling across API endpoints.

### Service Layer
Configuration settings are consumed by service modules (such as AI services) to establish connections to external APIs and services.

## Security Considerations

### Environment Variables
Sensitive configuration like API keys and database credentials are managed through environment variables, preventing hard-coded secrets in source code.

### Validation
Pydantic validation ensures that all required configuration parameters are present and correctly formatted before application startup.

## Error Handling

The core modules implement appropriate error handling for:
- Missing or invalid configuration values
- Database connection failures
- Environment-specific setup issues

## Testing Support

The core infrastructure is designed to support testing by:
- Allowing database URL overrides for test environments
- Providing session fixtures for isolated testing
- Supporting mock configurations during test execution

## Deployment Flexibility

The modular design enables:
- Easy switching between development and production configurations
- Support for different cloud providers and database services
- Environment-specific optimizations and settings

## Maintenance and Extensibility

The core folder structure facilitates:
- Addition of new configuration parameters
- Integration with additional database backends
- Implementation of new infrastructure services
- Environment-specific customizations

This foundation ensures that the application remains configurable, maintainable, and adaptable to different deployment scenarios.