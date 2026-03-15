# Database Core Module

## Overview

The `database.py` module provides database connection management and session handling for the AI Project Planner Agent backend using SQLModel. It establishes the data persistence layer, supporting multiple database backends (SQLite for development, SQL Server for production) with appropriate configuration and optimization settings.

## Architecture

The module implements a database abstraction layer that:

- Creates SQLModel engine instances with environment-specific configurations
- Manages database connections and connection pooling
- Provides session management utilities for data operations
- Handles schema creation and initialization

## Database Engine Configuration

### Engine Creation
```python
engine = create_engine(DATABASE_URL, **engine_kwargs)
```

### Environment-Specific Settings

#### SQLite (Development)
- Simple file-based database
- No connection pooling required
- Debug echo based on settings
- Default: `sqlite:///./plans.db`

#### SQL Server (Production)
- Connection pooling with `pool_pre_ping`
- Connection recycling (3600 seconds)
- Optimized for Azure SQL Database
- Enhanced reliability settings

## Database URL Configuration

### Dynamic URL Selection
The module uses the database URL from application settings:
```python
DATABASE_URL = settings.database_url
```

### Supported Formats
- SQLite: `sqlite:///./plans.db`
- SQL Server: `mssql+pyodbc://username:password@server/database`

## Schema Management

### Table Creation
The `init_db()` function initializes the database schema:
```python
def init_db():
    from app.models.db_models import PlanDB
    SQLModel.metadata.create_all(engine)
```

### Model Import
Imports database models locally to avoid circular dependencies during application startup.

## Session Management

### Session Creation
Provides transactional database sessions:
```python
def get_session():
    with Session(engine) as session:
        yield session
```

### FastAPI Integration
Used as a dependency in API endpoints:
```python
async def endpoint(session: Session = Depends(get_session)):
    # Database operations
```

### Transaction Handling
- Automatic session cleanup
- Transaction rollback on errors
- Connection pooling management

## Connection Pooling

### Development (SQLite)
- No pooling required
- Direct file access
- Minimal overhead

### Production (SQL Server)
- `pool_pre_ping=True`: Validates connections before use
- `pool_recycle=3600`: Recycles connections hourly
- Prevents stale connections in long-running applications

## Error Handling

### Connection Failures
- Engine creation handles invalid URLs
- Connection validation through `pool_pre_ping`
- Graceful failure for database unavailability

### Schema Issues
- Table creation errors logged appropriately
- Migration support for schema updates

## Performance Optimization

### Connection Management
- Efficient connection reuse
- Pool size optimization for load
- Connection validation to prevent failures

### Query Optimization
- SQLModel provides efficient query generation
- Index support through model definitions
- Batch operations for bulk data handling

## Security Considerations

### Connection Security
- Credentials managed through environment variables
- SSL/TLS support for SQL Server connections
- Secure connection strings

### Data Protection
- SQL injection prevention through SQLModel
- Parameterized queries
- Safe data serialization

## Testing Support

### Test Database
Supports isolated testing with dedicated database:
- Test-specific SQLite database
- Clean schema between tests
- Session fixtures for test functions

### Mock Sessions
Test modules can override database dependencies:
```python
app.dependency_overrides[get_session] = get_test_session_override
```

## Migration and Schema Evolution

### Schema Updates
Current implementation uses `create_all()` for simplicity:
- Creates missing tables
- Does not handle complex migrations
- Suitable for current application scope

### Future Migration Support
Designed for extension to migration tools like Alembic for:
- Schema versioning
- Data migrations
- Rollback capabilities

## Integration Points

### Model Layer
Works with `db_models.py` for:
- Table definitions
- Relationship management
- Data validation

### API Layer
Provides sessions to API endpoints in `planner.py`:
- Plan creation and storage
- Plan retrieval operations
- Transaction management

### Application Lifecycle
Integrated in `main.py` for:
- Application startup initialization
- Database availability verification

## Monitoring and Logging

### Connection Monitoring
- Connection pool statistics (future enhancement)
- Query performance logging
- Error tracking for database operations

### Health Checks
Database connectivity can be monitored through:
- Connection validation
- Query execution tests
- Schema integrity checks

## Deployment Considerations

### Development Deployment
- SQLite for simplicity
- Local file storage
- Easy setup and teardown

### Production Deployment
- SQL Server/Azure SQL Database
- Connection string configuration
- Performance monitoring
- Backup and recovery planning

## Extensibility

### Multiple Databases
Architecture supports:
- Read/write database separation
- Multiple database connections
- Database sharding (future scalability)

### Advanced Features
Can be extended for:
- Connection retry logic
- Query result caching
- Database monitoring
- Performance profiling

## Best Practices

The database module follows best practices:
- Environment-specific configurations
- Proper connection management
- Transaction safety
- Security through parameterization
- Testing isolation
- Performance optimization

## Maintenance

### Database Maintenance
- Regular connection monitoring
- Schema backup procedures
- Performance tuning
- Version upgrades

### Code Maintenance
- Dependency updates
- Security patches
- Feature enhancements
- Documentation updates

This module provides a robust and flexible database foundation, supporting the application's data persistence needs across different environments and scales.