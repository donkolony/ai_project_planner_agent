# Planner API Module

## Overview

The `planner.py` module defines a FastAPI router for project planning functionality in the AI Project Planner Agent backend. It provides endpoints for generating AI-driven project plans based on user requirements and retrieving stored plans from the database. This module serves as the primary interface for the application's core business functionality.

## Router Configuration

- **Router Instance**: `APIRouter(prefix="/plan", tags=["Planner"])`
- **Prefix**: `/plan`
- **Tags**: Planner (for API documentation grouping)

## Data Models

### PlanRequest
**Purpose**: Validates input for project plan generation requests.

**Fields**:
- `project_name` (str): Required. The name of the proposed project.
- `description` (str): Required. A detailed description of the project idea.
- `tech_stack` (List[str], optional): A list of technologies to be used. Defaults to empty list.

### PlanResponse
**Purpose**: Structures the response for project plan data.

**Fields**:
- `summary` (str): A high-level architectural and technical overview of the project.
- `recommended_tech_stack` (List[str], optional): A list of technologies suggested by the AI.
- `phases` (List[Phase]): A structured roadmap consisting of multiple development phases.

### Phase
**Purpose**: Represents individual development phases within a project plan.

**Fields**:
- `name` (str): The name of the phase (e.g., 'Setup', 'Frontend Development').
- `tasks` (List[str]): A list of specific actionable tasks belonging to this phase.

## Endpoints

### POST /plan/

**Purpose**: Generate a new AI-driven project plan based on user requirements.

**Method**: POST

**Path**: `/plan/`

**Request Body**: `PlanRequest`

**Response**: `PlanResponse`

**Status Codes**:
- 200: Successful plan generation
- 422: Validation error for malformed request data
- 500: Internal server error during AI processing

**Description**:
This endpoint accepts project details from the user and orchestrates the generation of a comprehensive project plan using AI services. The process involves:
1. Validating the input request
2. Calling the AIPlanner service with project details
3. Processing the AI response into structured phases
4. Returning the complete plan to the client

**Dependencies**: Requires database session for potential future plan storage.

### GET /plan/{plan_id}

**Purpose**: Retrieve a specific project plan by its unique identifier.

**Method**: GET

**Path**: `/plan/{plan_id}`

**Path Parameters**:
- `plan_id` (str): The unique identifier of the plan to retrieve

**Response**: `PlanResponse`

**Status Codes**:
- 200: Plan successfully retrieved
- 404: Plan not found
- 422: Invalid plan ID format

**Description**:
Retrieves a previously generated and stored project plan from the database. The endpoint:
1. Queries the database for the specified plan ID
2. Deserializes the stored JSON data into structured objects
3. Returns the plan in the standard response format

**Dependencies**: Requires database session for data retrieval.

### GET /plan/

**Purpose**: Retrieve all stored project plans.

**Method**: GET

**Path**: `/plan/`

**Response**: `List[PlanResponse]`

**Status Codes**:
- 200: Plans successfully retrieved
- 500: Database error during retrieval

**Description**:
Returns a complete list of all project plans stored in the database. This endpoint:
1. Queries all PlanDB records from the database
2. Deserializes each plan's JSON data
3. Returns an array of plan responses

**Dependencies**: Requires database session for bulk data retrieval.

## Implementation Details

### Dependencies
- `fastapi.APIRouter`: Router definition and endpoint creation
- `fastapi.HTTPException`: Error handling for API responses
- `pydantic.BaseModel`: Request/response data validation
- `sqlmodel.Session`: Database session management
- `app.services.ai_services.AIPlanner`: AI plan generation service
- `app.models.plan.PlanResponse`: Response data structure
- `app.models.db_models.PlanDB`: Database model for plan storage
- `app.core.database.get_session`: Database session dependency

### Service Integration
The module integrates with the AIPlanner service for plan generation:
```python
ai_planner = AIPlanner()
result = ai_planner.generate_plan(
    project_name=payload.project_name,
    description=payload.description,
    tech_stack=payload.tech_stack,
)
```

### Database Operations
Endpoints use SQLModel for database interactions:
- Session dependency injection for transaction management
- Query operations for data retrieval
- JSON serialization/deserialization for complex data structures

## Error Handling

### Validation Errors
- Pydantic automatically validates request data
- Returns 422 status with detailed validation messages

### Database Errors
- Handles missing records with 404 responses
- Logs database operation failures
- Maintains transaction integrity

### Service Errors
- AI service failures result in appropriate error responses
- Graceful degradation for external service issues

## Integration

### Application Registration
The planner router is included in the main FastAPI application:
```python
app.include_router(planner_router)
```

### API Documentation
All endpoints are documented in the OpenAPI schema with:
- Request/response schemas
- Example data structures
- Parameter descriptions
- Error response definitions

## Testing

The planner endpoints are comprehensively tested in:
- `test_create_plan.py`: Plan generation functionality
- `test_get_plan.py`: Individual plan retrieval
- `test_list_plans.py`: Bulk plan retrieval

Tests validate:
- Request/response validation
- Database operations
- AI service integration (using mocks)
- Error condition handling

## Usage Examples

### Create Plan
```python
import requests

payload = {
    "project_name": "E-commerce Platform",
    "description": "A modern online shopping platform with user authentication",
    "tech_stack": ["React", "Node.js", "MongoDB"]
}

response = requests.post("http://localhost:8000/plan/", json=payload)
plan = response.json()
```

### Get Plan
```python
response = requests.get(f"http://localhost:8000/plan/{plan_id}")
plan = response.json()
```

### List Plans
```python
response = requests.get("http://localhost:8000/plan/")
plans = response.json()
```

## Performance Considerations

- AI plan generation may take several seconds
- Database queries are optimized for the current data volume
- Response sizes scale with plan complexity
- Session management ensures connection efficiency

## Security

- Input validation prevents malformed data injection
- No authentication required for current implementation
- Database queries use parameterized statements
- Error messages avoid information disclosure

## Future Enhancements

The planner API is designed for extensibility:
- Plan update and deletion endpoints
- Filtering and search capabilities
- Plan versioning and history
- User-specific plan management
- Advanced AI configuration options

This module forms the core functionality of the AI Project Planner Agent, providing a robust and scalable API for project planning operations.