# Tests Folder Overview

## Introduction

The `tests` folder contains the comprehensive test suite for the AI Project Planner Agent backend. It employs pytest as the testing framework, with a focus on integration testing to validate the application's API endpoints, database interactions, and service integrations. The tests are designed to run in isolation using a dedicated test database, ensuring reliable and repeatable results.

## Structure

The tests folder is organized as follows:

### Configuration and Fixtures

- **conftest.py**: Provides pytest fixtures and configuration for the entire test suite. It sets up a test database using SQLite, manages database lifecycle (creation and cleanup), and overrides application dependencies to use mock services instead of production infrastructure.

### Test Modules

- **test_health.py**: Contains tests for basic application health and connectivity. It verifies that the root endpoint is accessible and returns the expected status information.

- **test_create_plan.py**: Tests the project plan creation endpoint. It validates that the API correctly processes plan generation requests and returns properly structured responses using mocked AI services.

- **test_get_plan.py**: Focuses on testing the retrieval of individual project plans by ID. It ensures that plans stored in the database can be accurately fetched and deserialized through the API.

- **test_list_plans.py**: Tests the endpoint for retrieving all stored project plans. It validates bulk data retrieval and ensures that multiple plans are correctly serialized in the response.

- **test_ai_planner.py**: Appears to be a duplicate or alternative configuration file, potentially containing additional test setup or fixtures related to AI planner functionality.

### Mocks Directory

- **mocks/mock_ai_planner.py**: Provides a mock implementation of the AIPlanner service. It returns predetermined responses to simulate AI-generated project plans without requiring actual API calls to Azure OpenAI, enabling fast and reliable testing.

## Testing Approach

### Integration Testing Focus
The test suite emphasizes integration testing over unit testing, validating the interaction between different application components including:
- API endpoints and routing
- Database operations and data persistence
- Service layer integrations
- Request/response serialization

### Database Isolation
Tests utilize a dedicated SQLite database that is created fresh for each test session and reset between individual tests. This ensures test isolation and prevents data contamination between test cases.

### Dependency Mocking
Critical external dependencies, such as the Azure OpenAI service, are mocked to:
- Avoid external API calls during testing
- Provide predictable, consistent responses
- Enable testing of error conditions and edge cases
- Reduce test execution time and external dependencies

### Test Data Management
Tests seed the database with known data structures to validate:
- Data insertion and retrieval
- JSON serialization/deserialization of complex objects
- Database query operations
- API response formatting

## Key Testing Scenarios

### Health Checks
- Verification of application startup and basic routing
- Validation of environment-specific configurations

### Plan Management
- Creation of new project plans with various input combinations
- Retrieval of individual plans by unique identifiers
- Bulk retrieval of all stored plans
- Handling of non-existent plan requests

### Data Integrity
- Proper storage and retrieval of complex data structures
- JSON encoding/decoding of plan phases and metadata
- Database constraint validation

## Test Execution

The tests are designed to be run using pytest with the following command from the backend directory:

```
pytest
```

The conftest.py file ensures that:
- Database tables are created before tests begin
- Tables are dropped after test completion
- Dependencies are properly overridden for testing
- Each test starts with a clean database state

## Benefits

This testing structure provides:
- Confidence in application functionality through comprehensive coverage
- Rapid feedback during development through fast execution
- Isolation from external services reducing test fragility
- Validation of end-to-end workflows from API request to database persistence

## Maintenance

The modular test structure makes it straightforward to:
- Add new tests for additional endpoints or functionality
- Update mock responses as the application evolves
- Modify test data to cover new scenarios
- Extend coverage to new components or services