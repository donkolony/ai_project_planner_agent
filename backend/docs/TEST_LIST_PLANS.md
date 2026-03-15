# Test List Plans Module

## Overview

The `test_list_plans.py` module contains integration tests for the project plan listing endpoint in the AI Project Planner Agent backend. It validates the GET `/plan/` API endpoint, ensuring that all stored project plans can be retrieved correctly and returned in the proper format.

## Test Architecture

The module uses pytest with database fixtures for bulk data testing:

- **TestClient**: Simulates HTTP requests to the application
- **Bulk Data Creation**: Seeds multiple test plans in database
- **Response Validation**: Verifies array response structure
- **Data Integrity**: Ensures all plans are returned accurately

## Test Client Setup

### Client Initialization
```python
client = TestClient(app)
```

### Application Context
- **Test App**: Uses the main FastAPI application instance
- **Database Session**: Leverages get_test_session fixture
- **Clean State**: Database reset ensures test isolation

## Test Function: test_list_plans

### Test Purpose
Validates the retrieval of all stored project plans.

### Test Implementation
```python
def test_list_plans(get_test_session):
    session = get_test_session

    # Create multiple test plans
    plans = [...]
    session.add_all(plans)
    session.commit()

    # Test API retrieval
    response = client.get("/plan/")
    assert response.status_code == 200

    # Validate response
    data = response.json()
    # Assertions...
```

### Test Flow

#### Data Preparation
- **Multiple Plans**: Creates several PlanDB instances
- **Varied Data**: Uses different project names and data
- **Database Insertion**: Adds all plans to test session
- **Session Commit**: Persists data for API testing

#### API Request
- **Endpoint**: Calls GET `/plan/` without parameters
- **Bulk Retrieval**: Requests all stored plans
- **Response Capture**: Stores array response for validation

#### Response Validation
- **Status Code**: Verifies 200 OK for successful retrieval
- **Content Type**: Ensures JSON array response
- **Data Completeness**: Confirms all plans are returned

## Database Integration

### Bulk Data Creation
```python
plans = [
    PlanDB(
        id=str(uuid4()),
        project_name=f"Project {i}",
        description="Desc",
        tech_stack=json.dumps(["Python"]),
        summary=f"Summary {i}",
        phases=json.dumps([{"name": f"Phase {i}", "tasks": ["Task 1"]}]),
    )
    for i in range(2)
]
session.add_all(plans)
```

### Data Characteristics
- **Unique IDs**: Each plan has distinct UUID
- **Varied Content**: Different names, summaries, and phases
- **Consistent Structure**: All plans follow same schema
- **JSON Serialization**: Complex data stored as strings

### Session Management
- **Batch Operations**: add_all for efficient insertion
- **Transaction Scope**: Single commit for all plans
- **Fixture Usage**: get_test_session provides database access

## Validation Scope

### API Endpoint Testing
- **Route Handling**: Validates list endpoint routing
- **HTTP Method**: Confirms GET method for retrieval
- **No Parameters**: Tests parameter-less bulk retrieval

### Database Operations
- **Query Execution**: Verifies SELECT all operation
- **Result Processing**: Tests multiple record handling
- **Serialization**: Validates bulk JSON deserialization

### Response Processing
- **Array Formatting**: Tests list response structure
- **Individual Items**: Validates each plan's data integrity
- **Ordering**: Ensures consistent result ordering

## Test Data Structure

### Database Records
```json
[
  {
    "id": "uuid-1",
    "project_name": "Project 0",
    "description": "Desc",
    "tech_stack": "[\"Python\"]",
    "summary": "Summary 0",
    "phases": "[{\"name\": \"Phase 0\", \"tasks\": [\"Task 1\"]}]"
  },
  {
    "id": "uuid-2",
    "project_name": "Project 1",
    "description": "Desc",
    "tech_stack": "[\"Python\"]",
    "summary": "Summary 1",
    "phases": "[{\"name\": \"Phase 1\", \"tasks\": [\"Task 1\"]}]"
  }
]
```

### API Response
```json
[
  {
    "summary": "Summary 0",
    "recommended_tech_stack": [],
    "phases": [{"name": "Phase 0", "tasks": ["Task 1"]}]
  },
  {
    "summary": "Summary 1",
    "recommended_tech_stack": [],
    "phases": [{"name": "Phase 1", "tasks": ["Task 1"]}]
  }
]
```

## Assertions and Validation

### Response Status
```python
assert response.status_code == 200
```

### Content Validation
```python
data = response.json()
assert isinstance(data, list)
assert len(data) == 2
for i, plan in enumerate(data):
    # Validate each plan's structure
```

### Array Properties
- **Type Checking**: Ensures response is a list
- **Length Verification**: Confirms correct number of plans
- **Individual Validation**: Checks each plan's data structure

## Integration Points

### Database Layer
- **Bulk Queries**: Tests SQLModel query operations
- **Result Iteration**: Validates result set handling
- **Session Management**: Proper connection lifecycle

### API Layer
- **Router Functionality**: Tests planner router list endpoint
- **Response Serialization**: Validates bulk PlanResponse creation
- **Performance**: Tests handling of multiple records

### Test Infrastructure
- **Fixture Integration**: Uses conftest.py database setup
- **Data Seeding**: Creates necessary test data
- **Cleanup**: Automatic database reset

## Test Execution

### pytest Integration
- **Automatic Discovery**: Found by pytest naming convention
- **Fixture Requirements**: Depends on get_test_session
- **Execution Isolation**: Independent test execution

### Performance
- **Database Load**: Tests with small dataset
- **Response Size**: Validates reasonable payload sizes
- **Query Efficiency**: Ensures fast bulk retrieval

## Maintenance

### Test Data Scaling
- **Larger Datasets**: Test with more plans for performance
- **Edge Cases**: Empty list, single plan scenarios
- **Data Variety**: More diverse test data structures

### Assertion Updates
- **Schema Changes**: Update for new response fields
- **Ordering Changes**: Modify if result ordering changes
- **Performance Metrics**: Add timing assertions if needed

## Best Practices

The test follows testing best practices:
- **Bulk Testing**: Validates multi-record operations
- **Data Seeding**: Creates realistic test scenarios
- **Comprehensive Assertions**: Validates both structure and content
- **Isolation**: Uses fixtures for test independence

## Related Tests

### Complementary Tests
- **test_create_plan.py**: Tests individual plan creation
- **test_get_plan.py**: Tests single plan retrieval
- **test_health.py**: Tests basic application health

### Test Suite Coverage
This test contributes to:
- **Bulk Operations**: Multi-record API testing
- **Database Performance**: Query optimization validation
- **Response Formatting**: Array serialization testing

This module ensures that bulk plan retrieval works correctly, validating the application's ability to handle multiple records and provide comprehensive data access.