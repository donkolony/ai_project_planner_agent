# Test AI Planner Module

## Overview

The `test_ai_planner.py` module contains pytest configuration and global fixtures for the AI Project Planner Agent backend test suite. It establishes the testing infrastructure, manages test database lifecycle, and configures dependency overrides to ensure isolated and reliable testing of application components.

## Note on Content

This module appears to be a duplicate or alternative implementation of the `conftest.py` module, providing similar pytest fixtures and configuration. While it contains equivalent functionality, the primary configuration is maintained in `conftest.py` for consistency.

## Architecture

The module implements pytest fixtures and configuration with the same structure as conftest.py:

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
- **SQLite**: Lightweight, file-based database for testing
- **Test Isolation**: Dedicated database file
- **Performance**: Fast setup and teardown

## Session-Level Fixtures

### create_test_db Fixture
**Scope**: session

**Purpose**: Manages database lifecycle

**Implementation**: Identical to conftest.py implementation

### override_dependencies Fixture
**Scope**: session

**Purpose**: Configures application dependencies

**Implementation**: Same dependency injection setup as conftest.py

## Function-Level Fixtures

### clean_db Fixture
**Scope**: function

**Purpose**: Ensures clean database state

**Implementation**: Identical database reset logic

### get_test_session Fixture
**Scope**: function

**Purpose**: Provides database session

**Implementation**: Same session management as conftest.py

## Dependency Override Functions

### get_test_session_override Function
**Purpose**: Session factory for FastAPI dependency injection

**Implementation**: Equivalent to conftest.py function

## Mock Service Integration

### MockAIPlanner Import
```python
from tests.mocks.mock_ai_planner import MockAIPlanner
```

### Service Replacement
- **Original Service**: Replaces AIPlanner with mock
- **Test Service**: Uses MockAIPlanner for deterministic responses

## Relationship to conftest.py

### Primary Configuration
- **conftest.py**: Main pytest configuration file
- **test_ai_planner.py**: Duplicate/alternative implementation
- **Recommendation**: Use conftest.py for consistency

### Functional Equivalence
- **Fixtures**: Identical functionality
- **Overrides**: Same dependency injection
- **Database**: Equivalent setup

## Usage Considerations

### Test Execution
This module can be used as an alternative to conftest.py, but conftest.py is preferred as it follows pytest conventions for configuration files.

### Maintenance
- **Synchronization**: Keep both files in sync if both are maintained
- **Consolidation**: Consider removing this duplicate in favor of conftest.py

## Integration

### Test Modules
Provides the same infrastructure as conftest.py for:
- Database session management
- Service mocking
- Test isolation

### Test Execution
Supports the same test execution patterns as conftest.py.

## Best Practices

While functional, this module represents duplicate code. Best practices recommend:
- **Single Source of Truth**: Use conftest.py as the primary configuration
- **Code Deduplication**: Remove duplicate implementations
- **Consistency**: Follow pytest conventions

## Maintenance Notes

### File Status
- **Status**: Duplicate of conftest.py
- **Recommendation**: Consolidate into single configuration file
- **Compatibility**: Maintains same interface for existing tests

This module provides equivalent testing infrastructure but should be consolidated with conftest.py for better maintainability.