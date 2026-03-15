# API Folder Overview

## Introduction

The `api` folder contains the FastAPI router modules that define the REST API endpoints for the AI Project Planner Agent backend. These routers handle HTTP requests and responses, integrating with the application's business logic, database, and external services. The folder follows FastAPI conventions for organizing API routes into logical modules.

## Structure

The API folder consists of two main router files:

### Health Router

- **health.py**: Defines a simple router for system health monitoring. It provides endpoints to check the operational status of the application, serving as a basic connectivity and availability test.

### Planner Router

- **planner.py**: Contains the core API endpoints for project planning functionality. It handles requests for generating AI-driven project plans and retrieving stored plans from the database.

## Key Components

### Router Definitions
Each file defines a FastAPI APIRouter instance with appropriate prefixes and tags for API documentation and organization.

### Endpoint Implementations
The routers implement HTTP methods (GET, POST) with proper request/response handling, including:
- Input validation using Pydantic models
- Dependency injection for database sessions
- Error handling and HTTP status codes
- Integration with service layers

### Data Flow
The API layer acts as the interface between external clients and internal application logic, managing:
- Request parsing and validation
- Business logic execution
- Response formatting and serialization
- Database transactions

## API Endpoints

### Health Endpoints
- `GET /health/`: Returns a status message confirming the backend is operational.

### Planner Endpoints
- `POST /plan/`: Accepts project details and generates a new AI-driven project plan.
- `GET /plan/{plan_id}`: Retrieves a specific project plan by its unique identifier.
- `GET /plan/`: Returns a list of all stored project plans.

## Request/Response Models

### PlanRequest
Used for plan generation requests, containing:
- project_name: Name of the proposed project
- description: Detailed project description
- tech_stack: Optional list of preferred technologies

### PlanResponse
Returned by plan-related endpoints, containing:
- summary: AI-generated project overview
- recommended_tech_stack: Suggested technologies
- phases: Structured list of development phases with tasks

## Integration Points

### Database Integration
Endpoints use SQLModel sessions for data persistence and retrieval, ensuring atomic operations and proper transaction management.

### Service Integration
The planner router integrates with the AIPlanner service for plan generation, abstracting complex AI interactions behind a clean API interface.

### Error Handling
Endpoints implement appropriate HTTP status codes and error responses for various scenarios, including:
- 404 for non-existent resources
- 200 for successful operations
- Proper error messages for client guidance

## Security and Validation

### Input Validation
All endpoints use Pydantic models for automatic request validation, ensuring data integrity and preventing malformed inputs.

### CORS Configuration
The API supports cross-origin requests through application-level CORS middleware, configured for both development and production environments.

## Documentation

The routers are tagged appropriately for automatic API documentation generation via FastAPI's built-in OpenAPI/Swagger UI, providing interactive documentation for developers.

## Testing

The API endpoints are thoroughly tested through integration tests in the tests folder, validating:
- Request/response cycles
- Data serialization
- Error conditions
- Database interactions

## Extensibility

The modular router structure makes it straightforward to:
- Add new endpoints within existing routers
- Create additional router modules for new features
- Modify request/response schemas
- Implement new HTTP methods

This organization ensures clean separation of concerns and maintainable API development.