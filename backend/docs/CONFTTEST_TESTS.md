# Conftest Tests Module

## Overview

The `conftest.py` module provides pytest configuration and fixtures for the AI Project Planner Agent backend test suite. It establishes the testing infrastructure, manages test database lifecycle, and configures dependency overrides to ensure isolated and reliable testing of application components.

## Architecture

The module implements pytest fixtures and configuration:

- **Session-level fixtures** for database setup/teardown
- **Function-level fixtures** for test isolation
- **Dependency overrides** for service mocking
- **Test database management** with SQLite

## Test Database Configuration

### Database Engine
```python
TEST_SQLITE_URL = "sqlite:///./test.db"
engine = create_engine(TEST_SQLITE_URL, echo=False)
```

### Database Choice
- **SQLite**: Lightweight, file-based database
- **Test Isolation**: Dedicated database file for tests
- **Performance**: Fast setup and teardown
- **Compatibility**: Same SQLModel operations as production

## Session-Level Fixtures

### create_test_db Fixture
**Scope**: session

**Purpose**: Manages database lifecycle for entire test suite

**Implementation**:
```python
@pytest.fixture(scope="session", autouse=True)
def create_test_db():
    SQLModel.metadata.create_all(engine)
    yield
    SQLModel.metadata.drop_all(engine)
```

**Behavior**:
- **Setup**: Creates all database tables before tests run
- **Teardown**: Drops all tables after test suite completion
- **Auto-use**: Applied automatically to all tests

### override_dependencies Fixture
**Scope**: session

**Purpose**: Configures application dependencies for testing

**Implementation**:
```python
@pytest.fixture(scope="session", autouse=True)
def override_dependencies():
    # Dependency injection setup
    app.dependency_overrides[get_session] = get_test_session_override
    planner_module.ai_planner = MockAIPlanner()
```

**Overrides**:
- **Database Session**: Replaces production session with test session
- **AI Service**: Replaces AIPlanner with MockAIPlanner
- **Isolation**: Prevents external API calls and database conflicts

## Function-Level Fixtures

### clean_db Fixture
**Scope**: function

**Purpose**: Ensures clean database state between tests

**Implementation**:
```python
@pytest.fixture(scope="function", autouse=True)
def clean_db():
    SQLModel.metadata.drop_all(engine)
    SQLModel.metadata.create_all(engine)
```

**Behavior**:
- **Pre-test**: Resets database schema
- **Isolation**: Prevents data leakage between tests
- **Consistency**: Same schema for every test

### get_test_session Fixture
**Scope**: function

**Purpose**: Provides database session for individual tests

**Implementation**:
```python
@pytest.fixture()
def get_test_session():
    with Session(engine) as session:
        yield session
```

**Usage**:
- **Injection**: Passed to test functions needing database access
- **Transaction**: Automatic session management
- **Isolation**: Separate session per test

## Dependency Override Functions

### get_test_session_override Function
**Purpose**: Provides session factory for FastAPI dependency injection

**Implementation**:
```python
def get_test_session_override():
    with Session(engine) as session:
        yield session
```

**Integration**:
- **FastAPI Override**: Replaces `get_session` dependency
- **Test Context**: Uses test database engine
- **Session Management**: Proper cleanup and transaction handling

## Mock Service Integration

### MockAIPlanner Import
```python
from tests.mocks.mock_ai_planner import MockAIPlanner
```

### Service Replacement
- **Original Service**: `planner_module.ai_planner = AIPlanner()`
- **Test Service**: `planner_module.ai_planner = MockAIPlanner()`
- **Purpose**: Deterministic responses without external API calls

## Test Infrastructure Benefits

### Database Isolation
- **Clean State**: Each test starts with empty database
- **No Interference**: Tests don't affect each other
- **Predictable Results**: Consistent test data

### Service Mocking
- **External Dependencies**: No Azure OpenAI API calls
- **Fast Execution**: Instantaneous mock responses
- **Reliable Testing**: Predictable behavior

### Performance Optimization
- **Fast Setup**: SQLite database creation is quick
- **Minimal Overhead**: Lightweight test infrastructure
- **Parallel Execution**: Supports pytest parallel testing

## Configuration Management

### Import Strategy
```python
# Late imports to avoid import-time side effects
from app.core.database import get_session
from app.api import planner as planner_module
```

### Import Timing
- **Late Imports**: Prevents circular dependencies
- **Conditional Loading**: Only loads when fixtures are used
- **Test Isolation**: Doesn't affect main application imports

## Integration with Test Modules

### Shared Fixtures
All test modules benefit from conftest.py setup:
- **test_health.py**: Uses basic app testing
- **test_create_plan.py**: Uses database and mock services
- **test_get_plan.py**: Uses database session fixtures
- **test_list_plans.py**: Uses database and session management

### Test Execution Flow
1. **Session Setup**: Database tables created
2. **Dependencies Overridden**: Mock services activated
3. **Test Execution**: Individual tests run with clean database
4. **Cleanup**: Database reset between tests
5. **Session Teardown**: Database tables dropped

## Error Handling

### Database Errors
- **Creation Failures**: Logged and handled gracefully
- **Connection Issues**: Test environment isolation
- **Schema Conflicts**: Clean reset prevents conflicts

### Import Errors
- **Late Imports**: Reduces import-time failures
- **Optional Dependencies**: Graceful handling of missing modules

## Extensibility

### Adding New Fixtures
New fixtures can be added for additional test needs:
```python
@pytest.fixture()
def custom_fixture():
    # Custom test setup
    yield
    # Cleanup
```

### Service Mocking
Additional service mocks can be integrated:
```python
# Additional service overrides
app.dependency_overrides[some_service] = mock_service
```

## Best Practices

The conftest.py follows testing best practices:
- **Fixture Scoping**: Appropriate session vs function scopes
- **Auto-use**: Automatic application of essential fixtures
- **Clean Separation**: Test infrastructure separate from test logic
- **Resource Management**: Proper cleanup and teardown

## Maintenance

### Database Schema Updates
- **Schema Changes**: Update table creation in fixtures
- **Migration Testing**: Ensure fixtures reflect current schema
- **Compatibility**: Maintain backward compatibility

### Service Updates
- **Mock Updates**: Update mocks when services change
- **Dependency Changes**: Modify overrides for new dependencies
- **Version Compatibility**: Ensure compatibility with application changes

## Debugging Support

### Logging Configuration
- **Echo Setting**: `echo=False` prevents SQL logging clutter
- **Error Logging**: Database errors are logged appropriately
- **Debug Mode**: Can be enabled for troubleshooting

### Test Isolation
- **Clean State**: Easy to identify test interference
- **Predictable Behavior**: Consistent test execution
- **Failure Isolation**: Individual test failures don't affect others

This module provides a solid foundation for reliable and maintainable testing, ensuring the application can be tested efficiently and effectively across all components.