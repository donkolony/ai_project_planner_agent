# App Folder Overview

## Introduction

The `app` folder contains the core application code for the AI Project Planner Agent backend. It is organized into modular components that handle API routing, business logic, data management, and configuration. This structure follows FastAPI best practices, separating concerns into distinct layers for maintainability and scalability.

## Architecture

The application is structured into the following subdirectories, each serving a specific purpose in the overall architecture:

### Main Entry Point

- **main.py**: Serves as the entry point for the FastAPI application. It initializes the FastAPI instance, sets up middleware for CORS handling, manages application lifespan events, and registers API routers. This file orchestrates the overall application setup and routing.

### API Layer

- **api/health.py**: Defines a simple router for health check endpoints. It provides a basic status check to verify that the application is running correctly.

- **api/planner.py**: Contains the primary API endpoints for project planning functionality. It handles requests for generating new AI-driven project plans and retrieving existing plans from the database. This module integrates with the AI services and database layers.

### Core Infrastructure

- **core/config.py**: Manages application configuration using Pydantic Settings. It loads and validates environment variables, providing a centralized way to access settings such as database connections, API keys, and environment-specific parameters.

- **core/database.py**: Handles database connection and session management. It uses SQLModel to create engine configurations that support both local SQLite databases and production SQL Server instances, with appropriate connection pooling and error handling.

### Data Models

- **models/db_models.py**: Defines the database schema using SQLModel. It includes the PlanDB model, which represents the structure of project plans stored in the database, including fields for project details, AI-generated content, and metadata.

- **models/plan.py**: Contains Pydantic models for API request and response validation. It defines schemas like PlanResponse and Phase, ensuring data integrity and proper serialization between the API and clients.

### Services Layer

- **services/ai_services.py**: Encapsulates the business logic for AI-powered project planning. It interfaces with Azure OpenAI to generate project plans based on user input, handles prompt construction, API communication, and response parsing.

## Key Components and Functionality

### Application Initialization
The main.py file sets up the FastAPI application with appropriate middleware and router inclusion. It configures CORS to allow cross-origin requests from specified frontend domains, adapting settings based on the environment (development vs. production).

### API Endpoints
The API layer provides RESTful endpoints for:
- Health monitoring
- Project plan generation using AI
- Retrieval of individual and multiple project plans

### Configuration Management
The core configuration module ensures secure and flexible environment variable handling, supporting different deployment scenarios without code changes.

### Database Operations
The database layer abstracts data persistence, allowing seamless switching between database types and providing session management for API dependencies.

### AI Integration
The services layer isolates AI-related logic, making it easier to maintain and update AI model interactions, prompt engineering, and response processing.

### Data Validation
Pydantic models ensure that all incoming and outgoing data conforms to expected schemas, providing runtime validation and automatic documentation generation.

## Dependencies and Integration

The app folder components integrate with external dependencies defined in the project's pyproject.toml and requirements files. Key integrations include:

- FastAPI for web framework functionality
- SQLModel for ORM and database operations
- Azure OpenAI for AI plan generation
- Pydantic for data validation

## Testing and Validation

While the app folder itself does not contain test files (which are located in the parent tests directory), the modular structure facilitates comprehensive unit testing of individual components, API endpoints, and service integrations.

## Development Considerations

The folder structure promotes clean architecture principles, making it straightforward to:
- Add new API endpoints
- Extend data models
- Integrate additional services
- Modify configuration settings
- Implement new business logic

This organization ensures that the codebase remains maintainable and scalable as the application evolves.