# AI Services Module

## Overview

The `ai_services.py` module encapsulates the business logic for AI-powered project planning in the AI Project Planner Agent backend. It provides a service layer that interfaces with Azure OpenAI to generate structured project plans based on user requirements, handling prompt engineering, API communication, and response processing.

## Architecture

The module implements a service-oriented design:

- Clean separation of AI logic from API endpoints
- Centralized AI configuration and error handling
- Modular prompt construction and response parsing
- Integration with application configuration

## AIPlanner Class

### Class Definition
```python
class AIPlanner:
    # AI service implementation
```

### Initialization

#### Constructor
```python
def __init__(self):
    # Azure OpenAI client setup
```

#### Client Configuration
- **AzureOpenAI Client**: Initialized with application settings
- **API Key**: Retrieved from secure configuration
- **Endpoint**: Azure OpenAI service URL
- **API Version**: Specified version for compatibility
- **Deployment Name**: Model deployment identifier

### Core Methods

#### generate_plan Method

**Signature**:
```python
def generate_plan(
    self,
    project_name: str,
    description: str,
    tech_stack: list[str] = None
) -> dict
```

**Parameters**:
- `project_name` (str): Name of the project
- `description` (str): Detailed project description
- `tech_stack` (list[str], optional): Preferred technologies

**Returns**: Dictionary containing 'summary' and 'phases'

**Process Flow**:
1. **Input Validation**: Handle optional tech_stack parameter
2. **Prompt Construction**: Build AI prompt with project details
3. **API Call**: Send request to Azure OpenAI
4. **Response Processing**: Parse and validate AI response
5. **Error Handling**: Fallback for API failures

#### _parse_ai_response Method

**Purpose**: Safely parse AI-generated JSON responses

**Signature**:
```python
def _parse_ai_response(self, ai_output: str) -> dict
```

**Parameters**:
- `ai_output` (str): Raw JSON string from AI

**Returns**: Structured dictionary with 'summary' and 'phases'

**Error Handling**:
- JSON parsing with fallback
- Validation of required fields
- Logging of parsing failures

## Prompt Engineering

### Dynamic Prompt Construction
The service builds context-aware prompts:

#### Technology Stack Context
- **With Technologies**: "Strictly use the following technologies: [list]"
- **Without Technologies**: "Infer the most appropriate, minimal, and lightweight technologies"

#### Base Prompt Structure
```
You are an expert software architect.

Generate a high-level software project plan based on the user's requirements.
[Project details and constraints]
[Response format specifications]
```

#### Response Format Specification
Requests structured JSON output:
```json
{
  "summary": "Architectural overview",
  "phases": [
    {
      "name": "Phase Name",
      "tasks": ["Task 1", "Task 2"]
    }
  ]
}
```

## Azure OpenAI Integration

### API Communication
- **Client Library**: Uses OpenAI Python SDK for Azure
- **Authentication**: API key-based authentication
- **Model Selection**: Configurable deployment name
- **Request Format**: Structured chat completion requests

### Error Handling
- **API Exceptions**: Network and authentication errors
- **Rate Limiting**: Built-in retry logic (SDK level)
- **Invalid Responses**: Graceful fallback responses
- **Logging**: Comprehensive error logging

## Response Processing

### JSON Parsing
- **Safe Parsing**: json.loads with exception handling
- **Field Extraction**: Extract summary and phases
- **Validation**: Ensure required structure exists
- **Fallback**: Default response for parsing failures

### Data Structure
Expected AI response format:
- **summary**: String containing project overview
- **phases**: Array of phase objects with name and tasks

## Configuration Integration

### Settings Dependency
Relies on core configuration for:
- Azure OpenAI endpoint and credentials
- Model deployment and API version
- Environment-specific settings

### Environment Awareness
Adapts behavior based on:
- Development vs production settings
- Debug mode for enhanced logging
- Test environment mocking

## Error Handling and Resilience

### Service Failures
Implements multiple layers of error handling:
- **API Call Failures**: Network timeouts, authentication issues
- **Response Parsing**: Malformed JSON, missing fields
- **Service Unavailability**: Fallback responses
- **Logging**: Detailed error information for debugging

### Fallback Mechanisms
- **Default Response**: Provides basic structure when AI fails
- **Error Messages**: User-friendly error communication
- **Graceful Degradation**: Maintains application functionality

## Performance Considerations

### API Optimization
- **Efficient Prompts**: Concise, focused prompt construction
- **Response Size**: Balanced detail without excessive length
- **Caching Potential**: Designed for future response caching

### Resource Management
- **Client Reuse**: Single client instance for multiple requests
- **Connection Pooling**: Azure SDK handles connection management
- **Timeout Configuration**: Appropriate request timeouts

## Security Considerations

### Credential Management
- **Secure Storage**: API keys from environment variables
- **No Hard-coding**: Credentials never in source code
- **Access Control**: Limited to authorized service calls

### Data Protection
- **Input Sanitization**: User input validation
- **Output Validation**: AI response structure checking
- **Logging Security**: No sensitive data in logs

## Testing Support

### Mock Implementation
Supports testing through mock services:
- **MockAIPlanner**: Provides predictable test responses
- **Dependency Injection**: Easy service replacement in tests
- **Isolated Testing**: No external API calls during testing

### Test Data
Mock responses simulate real AI output:
```python
{
    "summary": "Mock summary",
    "phases": [
        {"name": "Mock phase 1", "tasks": ["Task A", "Task B"]},
        {"name": "Mock phase 2", "tasks": ["Task C"]}
    ]
}
```

## Integration Points

### API Layer
Consumed by `planner.py` endpoints:
- Plan generation requests
- Response formatting for API output
- Error handling and user feedback

### Configuration Layer
Depends on `config.py` for:
- Azure OpenAI settings
- Environment configuration
- Service credentials

### Database Layer
Indirect integration through API layer:
- Generated plans stored via database models
- Retrieval of existing plans

## Monitoring and Logging

### Operational Logging
- **Request Logging**: AI service calls and parameters
- **Response Logging**: Success/failure status
- **Error Logging**: Detailed failure information
- **Performance Metrics**: Response times and success rates

### Debug Support
Enhanced logging in debug mode:
- Full prompt and response logging
- Detailed error stack traces
- API call timing information

## Extensibility

### Model Support
Designed for multiple AI models:
- **GPT Variants**: Different model capabilities
- **Custom Deployments**: Organization-specific models
- **Fallback Models**: Alternative AI services

### Feature Expansion
Supports future enhancements:
- **Advanced Prompting**: Few-shot learning, chain-of-thought
- **Response Caching**: Reduce API calls for similar requests
- **Batch Processing**: Multiple plan generation
- **Model Fine-tuning**: Custom training data

## Best Practices

The service follows AI integration best practices:
- **Prompt Engineering**: Clear, structured prompts
- **Error Resilience**: Comprehensive failure handling
- **Security**: Secure credential management
- **Testing**: Mockable design for reliable testing
- **Monitoring**: Detailed logging and metrics

## Maintenance

### API Updates
- **SDK Updates**: OpenAI library version management
- **API Changes**: Azure OpenAI API evolution
- **Model Updates**: New model deployment support

### Prompt Optimization
- **Continuous Improvement**: Prompt refinement based on results
- **A/B Testing**: Different prompt strategies
- **User Feedback**: Incorporation of success metrics

### Cost Management
- **Usage Monitoring**: API call volume tracking
- **Optimization**: Prompt efficiency improvements
- **Caching Strategies**: Reduce redundant requests

This module provides a robust and maintainable AI service layer, enabling sophisticated project planning capabilities while ensuring reliability, security, and performance.