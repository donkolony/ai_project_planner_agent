# Backend Overview

## Introduction

The backend of the AI Project Planner Agent is a FastAPI-based web application designed to generate and manage AI-driven project plans. It integrates with Azure OpenAI to create structured project roadmaps based on user-provided project descriptions and technology stacks. The application supports both development and production environments, with configurable database backends (SQLite for local development and SQL Server for production).

## Architecture

The backend follows a modular architecture organized into the following main directories:

### Core Components

- **app/main.py**: The main entry point of the FastAPI application. It initializes the FastAPI instance, configures CORS middleware for cross-origin requests, and includes API routers for health checks and planner functionality.

- **app/core/config.py**: Handles application configuration using Pydantic Settings. It loads environment variables for settings such as Azure OpenAI credentials, database connections, and environment-specific configurations.

- **app/core/database.py**: Manages database connections and session handling using SQLModel. It supports both SQLite for development and SQL Server for production deployments.

### API Layer

- **app/api/health.py**: Provides a simple health check endpoint to verify the application's operational status.

- **app/api/planner.py**: Contains the core API endpoints for project plan generation and retrieval. It includes endpoints for creating new plans via AI and fetching existing plans from the database.

### Data Models

- **app/models/plan.py**: Defines Pydantic schemas for API request/response validation, including the PlanResponse model that structures the output of generated project plans.

- **app/models/db_models.py**: Defines the database schema using SQLModel, with the PlanDB model representing stored project plans in the database.

### Services

- **app/services/ai_services.py**: Encapsulates the logic for interacting with Azure OpenAI. It constructs prompts, handles API calls, and parses AI-generated responses into structured project plans.

### Testing

- **tests/**: Contains unit tests for the application, including tests for AI planner functionality, plan creation, retrieval, and health checks. Uses pytest as the testing framework.

## Technologies Used

- **FastAPI**: Web framework for building the REST API.
- **SQLModel**: ORM for database interactions, supporting both SQLite and SQL Server.
- **Azure OpenAI**: AI service for generating project plans.
- **Pydantic**: Data validation and serialization.
- **Uvicorn**: ASGI server for running the application.
- **Python 3.11+**: Programming language.

## API Endpoints

- `GET /`: Root endpoint providing basic API metadata.
- `GET /health/`: Health check endpoint.
- `POST /plan/`: Generate a new project plan based on user input.
- `GET /plan/{plan_id}`: Retrieve a specific project plan by ID.
- `GET /plan/`: Retrieve all stored project plans.

## Configuration

The application uses environment variables for configuration, loaded via Pydantic Settings. Key settings include:

- Azure OpenAI endpoint, API key, deployment name, and API version.
- Database URL (supports SQLite and SQL Server).
- Environment mode (development/production).
- Frontend URL for CORS configuration.

## Deployment

The backend is configured for deployment on Azure App Service, with support for production databases and environment-specific settings. Configuration files include:

- **web.config**: IIS configuration for Azure deployment.
- **startup.sh**: Startup script for Linux-based deployments.
- **requirements-prod.txt**: Production-specific Python dependencies.

## Development

To run the backend locally:

1. Install dependencies: `pip install -r requirements.txt`
2. Set up environment variables in a `.env` file.
3. Run the application: `uvicorn app.main:app --reload`

The application includes comprehensive testing with pytest to ensure functionality across all components.