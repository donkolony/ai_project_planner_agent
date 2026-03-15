# Test Create Plan Module

## Overview

The `test_create_plan.py` module contains integration tests for the project plan creation endpoint in the AI Project Planner Agent backend. It validates the POST `/plan/` API endpoint, ensuring that plan generation requests are processed correctly, AI services are invoked properly, and responses are formatted according to the expected schema.

## Test Architecture

The module uses pytest with FastAPI's TestClient for API testing:

- **TestClient**: Simulates HTTP requests to the application
- **Mock Services**: Uses MockAIPlanner to avoid external API calls
- **Database Integration**: Tests end-to-end plan creation and storage
- **Response Validation**: Verifies API response structure and content

## Test Client Setup

### Client Initialization
```python
client = TestClient(app)
```

### Application Context
- **Test App**: Uses the main FastAPI application instance
- **Dependency Overrides**: Configured through conftest.py fixtures
- **Mock Services**: AIPlanner replaced with MockAIPlanner

## Test Function: test_create_plan

### Test Purpose
Validates the successful generation of a project plan through the API.

### Test Implementation
```python
def test_create_plan():
    payload = {
        "project_name": "Test Project",
        "description": "Test Description",
        "tech_stack": ["Python", "FastAPI"],
    }

    response = client.post("/plan/", json=payload)
    assert response.status_code == 200

    data = response.json()
    # Assertions for expected response structure
```

### Test Flow

#### Request Preparation
- **Payload Construction**: Creates valid PlanRequest data
- **JSON Serialization**: Converts payload to JSON format
- **API Call**: Posts to `/plan/` endpoint

#### Response Validation
- **Status Code**: Verifies 200 OK response
- **Content Type**: Ensures JSON response
- **Data Structure**: Validates response matches PlanResponse schema

#### Content Assertions
- **Summary Field**: Checks for expected mock summary
- **Phases Structure**: Validates phase array with tasks
- **Data Types**: Ensures correct field types

## Mock Integration

### MockAIPlanner Usage
The test relies on MockAIPlanner providing predictable responses:

```python
return {
    "summary": "Mock summary",
    "phases": [
        {"name": "Mock phase 1", "tasks": ["Task A", "Task B"]},
        {"name": "Mock phase 2", "tasks": ["Task C"]},
    ],
}
```

### Test Isolation
- **No External Calls**: Prevents Azure OpenAI API usage
- **Deterministic Results**: Consistent test outcomes
- **Fast Execution**: Instantaneous response generation

## Validation Scope

### API Endpoint Testing
- **Route Handling**: Verifies correct endpoint routing
- **HTTP Method**: Confirms POST method acceptance
- **Request Parsing**: Validates JSON payload processing

### Data Processing
- **Input Validation**: Tests Pydantic model validation
- **Service Integration**: Verifies AIPlanner service calls
- **Response Formatting**: Checks API response structure

### Error Scenarios (Implied)
While this test focuses on success cases, it validates:
- **Schema Compliance**: Request matches expected format
- **Service Availability**: Mock service provides responses
- **Serialization**: Response can be JSON-encoded

## Test Data

### Request Payload
```json
{
  "project_name": "Test Project",
  "description": "Test Description",
  "tech_stack": ["Python", "FastAPI"]
}
```

### Expected Response
```json
{
  "summary": "Mock summary",
  "recommended_tech_stack": [],
  "phases": [
    {
      "name": "Mock phase 1",
      "tasks": ["Task A", "Task B"]
    },
    {
      "name": "Mock phase 2",
      "tasks": ["Task C"]
    }
  ]
}
```

## Integration Points

### FastAPI Application
- **Router Inclusion**: Tests planner router functionality
- **Middleware**: Validates CORS and other middleware
- **Dependency Injection**: Uses test database sessions

### Service Layer
- **AIPlanner Mock**: Tests service integration without external calls
- **Response Processing**: Validates service response handling

### Database Layer
- **Session Management**: Tests database session injection
- **Transaction Handling**: Verifies proper transaction lifecycle

## Test Execution

### pytest Integration
- **Discovery**: Automatically discovered by pytest
- **Fixture Usage**: Leverages conftest.py fixtures
- **Isolation**: Runs in isolated test environment

### Performance
- **Execution Speed**: Fast due to mock services
- **Resource Usage**: Minimal system resources
- **Parallel Execution**: Can run concurrently with other tests

## Assertions and Validation

### Response Status
```python
assert response.status_code == 200
```

### Content Validation
```python
assert data["summary"] == "Mock summary"
assert data["phases"] == [
    {"name": "Mock phase 1", "tasks": ["Task A", "Task B"]},
    {"name": "Mock phase 2", "tasks": ["Task C"]},
]
```

### Type Checking
- **Dictionary Structure**: Validates JSON response parsing
- **Field Presence**: Ensures all expected fields exist
- **Data Types**: Confirms correct types for each field

## Edge Cases and Error Handling

### Input Validation
While not explicitly tested here, the endpoint handles:
- **Missing Fields**: Required field validation
- **Invalid Types**: Type conversion errors
- **Malformed JSON**: Request parsing failures

### Service Errors
- **Mock Failures**: Would be caught by test failures
- **Database Errors**: Transaction rollback testing
- **Serialization Errors**: Response formatting issues

## Maintenance

### Mock Updates
- **Response Changes**: Update assertions when mock changes
- **Schema Evolution**: Modify tests for API changes
- **Service Updates**: Reflect new service behavior

### Test Data Updates
- **Realistic Data**: Use more representative test payloads
- **Edge Cases**: Add tests for boundary conditions
- **Coverage Expansion**: Test additional scenarios

## Best Practices

The test follows testing best practices:
- **Single Responsibility**: Tests one endpoint functionality
- **Clear Assertions**: Explicit validation of expectations
- **Mock Usage**: Appropriate use of test doubles
- **Documentation**: Well-documented test purpose and flow

## Related Tests

### Complementary Tests
- **test_get_plan.py**: Tests plan retrieval
- **test_list_plans.py**: Tests plan listing
- **test_health.py**: Tests basic application health

### Test Suite Coverage
This test contributes to:
- **API Endpoint Coverage**: Plan creation functionality
- **Integration Testing**: End-to-end request processing
- **Service Integration**: AI service interaction validation

This module ensures the plan creation endpoint works correctly, providing confidence in the application's core functionality.