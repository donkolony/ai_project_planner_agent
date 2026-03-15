# Models Folder Overview

## Introduction

The `models` folder contains the data model definitions for the AI Project Planner Agent backend. It defines the structure and validation rules for data entities used throughout the application, separating data concerns from business logic and API handling. The folder uses both SQLModel for database schemas and Pydantic for API data validation.

## Structure

The models folder consists of two complementary modules:

### Database Models

- **db_models.py**: Defines the database schema using SQLModel. It specifies the persistent data structures stored in the database, including table definitions and relationships.

### API Models

- **plan.py**: Contains Pydantic models for API request and response validation. It defines the data structures used for communication between the frontend and backend APIs.

## Key Components

### Database Schema

The db_models.py module implements:

- **PlanDB**: The primary database model representing stored project plans
- UUID-based primary keys for unique identification
- JSON-encoded fields for complex data structures
- SQLModel integration for ORM functionality

### API Data Models

The plan.py module defines:

- **Phase**: Represents individual development phases within a project plan
- **PlanResponse**: The complete response structure for project plans
- **PlanRequest**: Input validation for plan generation requests

## Data Structures

### PlanDB Model
Represents the database table structure with fields for:
- id: Unique identifier (UUID)
- project_name: User-provided project name
- description: Project description
- tech_stack: JSON-encoded technology list
- recommended_tech_stack: AI-suggested technologies
- summary: AI-generated project overview
- phases: JSON-encoded project phases and tasks

### PlanResponse Model
API response structure containing:
- summary: High-level project summary
- recommended_tech_stack: List of suggested technologies
- phases: Array of Phase objects

### Phase Model
Individual phase structure with:
- name: Phase title (e.g., "Setup", "Development")
- tasks: List of actionable tasks

### PlanRequest Model
API request validation for:
- project_name: Required project name
- description: Required project description
- tech_stack: Optional technology preferences

## Data Flow and Transformation

The models facilitate data transformation between different layers:

1. **API Input**: PlanRequest validates incoming data
2. **Processing**: Data is transformed for AI processing and database storage
3. **Storage**: PlanDB handles persistence with JSON encoding for complex structures
4. **Retrieval**: Database data is deserialized and transformed into PlanResponse
5. **API Output**: PlanResponse provides structured data to clients

## Validation and Type Safety

### Pydantic Validation
- Automatic type checking and validation
- Required vs. optional field enforcement
- Data sanitization and formatting
- Runtime error prevention

### Database Constraints
- Primary key uniqueness
- Data type enforcement
- Relationship integrity (when applicable)

## Serialization Handling

The models manage complex data serialization:

- **JSON Encoding**: Complex objects (phases, tech stacks) are stored as JSON strings
- **Deserialization**: JSON data is parsed back into structured objects for API responses
- **Type Consistency**: Ensures data integrity across storage and retrieval operations

## Integration Points

### Database Layer
Models integrate with SQLModel for:
- Table creation and schema management
- Query operations and data retrieval
- Session management and transactions

### API Layer
Models provide validation for:
- Request parsing and validation
- Response formatting and serialization
- OpenAPI documentation generation

### Service Layer
Models support data transformation in:
- AI service input/output handling
- Business logic operations
- Data persistence workflows

## Extensibility

The model structure supports:
- Addition of new fields to existing models
- Creation of new model classes for expanded functionality
- Modification of validation rules
- Extension of data relationships

## Testing and Validation

Models are validated through:
- Pydantic runtime validation
- Database schema testing
- API endpoint testing with mock data
- Serialization/deserialization testing

## Best Practices

The models follow data modeling best practices:
- Clear separation of concerns between database and API models
- Consistent naming conventions
- Comprehensive field documentation
- Type hints for better IDE support and validation

This organization ensures data integrity, type safety, and maintainable code structure throughout the application.