# Mock AI Planner Module

## Overview

The `mock_ai_planner.py` module provides a mock implementation of the AIPlanner service for testing purposes in the AI Project Planner Agent backend. It simulates the behavior of the Azure OpenAI integration without making external API calls, enabling fast and reliable testing of application components that depend on AI functionality.

## Architecture

The module implements a simple mock class that mimics the AIPlanner interface:

- **Deterministic Responses**: Provides consistent, predictable output
- **No External Dependencies**: Eliminates Azure OpenAI API requirements
- **Fast Execution**: Instantaneous response generation
- **Test Isolation**: Enables testing without network calls

## MockAIPlanner Class

### Class Definition
```python
class MockAIPlanner:
    # Mock implementation of AIPlanner
```

### Interface Compatibility
The mock implements the same public interface as the real AIPlanner:

- **Method Signatures**: Identical to AIPlanner.generate_plan()
- **Parameter Handling**: Accepts same input parameters
- **Return Format**: Returns equivalent data structure

## Core Method: generate_plan

### Method Signature
```python
def generate_plan(self, project_name: str, description: str, tech_stack: list[str]):
    # Mock implementation
```

### Parameters
- **project_name** (str): Project name (accepted but not used)
- **description** (str): Project description (accepted but not used)
- **tech_stack** (list[str]): Technology stack (accepted but not used)

### Return Value
```python
return {
    "summary": "Mock summary",
    "phases": [
        {"name": "Mock phase 1", "tasks": ["Task A", "Task B"]},
        {"name": "Mock phase 2", "tasks": ["Task C"]},
    ],
}
```

### Response Characteristics
- **Fixed Content**: Always returns the same mock data
- **Valid Structure**: Matches expected AI response format
- **Complete Data**: Includes all required fields

## Mock Data Structure

### Summary Field
- **Content**: "Mock summary"
- **Purpose**: Provides recognizable mock content
- **Type**: String matching real AI responses

### Phases Array
- **Structure**: Two mock phases with different task counts
- **Phase 1**: "Mock phase 1" with tasks ["Task A", "Task B"]
- **Phase 2**: "Mock phase 2" with tasks ["Task C"]
- **Format**: Matches PlanResponse phase structure

## Usage in Testing

### Dependency Injection
Replaces the real AIPlanner in test configuration:

```python
# In conftest.py
planner_module.ai_planner = MockAIPlanner()
```

### Test Scenarios
Enables testing of:
- **API Endpoints**: Plan creation without external calls
- **Data Processing**: Response handling and validation
- **Integration**: Service layer interactions
- **Error Handling**: Focus on application logic, not AI failures

## Benefits

### Testing Advantages
- **Speed**: Eliminates network latency
- **Reliability**: No external service dependencies
- **Consistency**: Predictable test results
- **Cost**: No API usage charges

### Development Benefits
- **Offline Development**: Work without internet connectivity
- **CI/CD**: Reliable automated testing
- **Debugging**: Focus on application logic
- **Parallel Testing**: No rate limiting concerns

## Integration Points

### Test Configuration
- **conftest.py**: Service override setup
- **Test Modules**: Used in plan creation and related tests
- **Fixture System**: Integrated with pytest fixtures

### Application Components
- **API Layer**: Tests planner endpoints with mock responses
- **Service Layer**: Validates service integration
- **Database Layer**: Tests data persistence with mock input

## Response Validation

### API Tests
Mock responses are validated in tests like test_create_plan.py:

```python
assert data["summary"] == "Mock summary"
assert data["phases"] == [
    {"name": "Mock phase 1", "tasks": ["Task A", "Task B"]},
    {"name": "Mock phase 2", "tasks": ["Task C"]},
]
```

### Schema Compliance
- **Structure**: Matches PlanResponse model
- **Types**: Correct data types for all fields
- **Completeness**: All required fields present

## Limitations

### Realism
- **Fixed Responses**: Doesn't simulate AI variability
- **No Errors**: Doesn't test AI service failures
- **Limited Scenarios**: Single response pattern

### Testing Scope
- **Success Cases**: Primarily tests happy path
- **Edge Cases**: Doesn't cover AI-specific edge cases
- **Performance**: Doesn't test AI response times

## Maintenance

### Response Updates
- **Content Changes**: Update mock data when real responses change
- **Schema Evolution**: Modify structure for API changes
- **Test Alignment**: Keep mock responses consistent with tests

### Enhancement Opportunities
- **Multiple Responses**: Add different mock scenarios
- **Error Simulation**: Include failure case mocks
- **Parameter Sensitivity**: Make responses vary by input

## Best Practices

The mock follows testing best practices:
- **Interface Compliance**: Matches real service interface
- **Predictable Behavior**: Consistent, reliable responses
- **Documentation**: Clear mock data structure
- **Isolation**: Enables focused unit testing

## Related Components

### Real Implementation
- **ai_services.py**: The actual AIPlanner class
- **Configuration**: Azure OpenAI settings
- **Integration**: External API communication

### Test Suite
- **test_create_plan.py**: Uses mock for plan creation testing
- **conftest.py**: Manages mock service injection
- **Other Tests**: Benefit from mock stability

## Future Improvements

### Enhanced Mocking
- **Parameterized Responses**: Different responses based on input
- **Error Scenarios**: Mock API failures and timeouts
- **Response Variation**: Multiple mock response patterns

### Advanced Features
- **Stateful Mocking**: Remember previous calls
- **Performance Simulation**: Add artificial delays
- **Validation**: Check input parameters

This module provides essential testing infrastructure, enabling reliable and efficient testing of AI-dependent functionality without external service dependencies.