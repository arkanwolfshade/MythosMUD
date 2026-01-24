# Structured Error Logging Specification

## Overview

This specification defines the comprehensive error logging system for MythosMUD, ensuring that all Python code raising errors is properly integrated with our StructLog system and directed to the correct logfiles. As noted in the Pnakotic Manuscripts, proper categorization of anomalous events is essential for maintaining the delicate balance between order and chaos in our digital realm.

## Current State Analysis

### Existing Infrastructure

Our current system has several components in place:

1. **StructLog Configuration** (`server/logging_config.py`)

   - Comprehensive logging setup with categorized log files
   - Automatic error logging in `MythosMUDError` base class
   - Proper log rotation and file management

2. **Error Hierarchy** (`server/exceptions.py`)

   - `MythosMUDError` base class with automatic logging
   - Structured error context with metadata
   - Proper error categorization

3. **Error Handlers** (`server/error_handlers.py`)

   - FastAPI exception handlers with logging
   - Error response standardization
   - Graceful degradation support

### Identified Gaps

Through analysis of the codebase, several areas require attention:

1. **Direct Exception Raising**: Many locations raise exceptions without proper logging
2. **HTTPException Usage**: FastAPI HTTPExceptions bypass our logging system
3. **Third-party Exceptions**: External library exceptions not properly captured
4. **Test Code**: Test exceptions not following production patterns

## Technical Specifications

### 1. Error Logging Categories

Our logging system categorizes errors into specific log files:

```python
log_categories = {
    "server": ["server", "uvicorn"],
    "persistence": ["persistence", "PersistenceLayer", "aiosqlite"],
    "authentication": ["auth"],
    "world": ["world"],
    "communications": ["realtime", "communications"],
    "commands": ["commands"],
    "errors": ["errors"],  # Global error capture
    "access": ["access", "server.app.factory"],
}
```

### 2. Required Error Logging Patterns

#### Pattern 1: MythosMUDError Usage (Preferred)

```python
from server.exceptions import MythosMUDError, create_error_context
from server.logging_config import get_logger

logger = get_logger(__name__)

# Automatic logging via base class

raise AuthenticationError(
    "Invalid credentials provided",
    context=create_error_context(
        user_id=user_id,
        request_id=request_id,
        metadata={"ip_address": client_ip}
    ),
    details={"attempt_count": 3},
    user_friendly="Login failed. Please check your credentials."
)
```

#### Pattern 2: Wrapped Exception Logging

```python
from server.exceptions import handle_exception, create_error_context
from server.logging_config import get_logger

logger = get_logger(__name__)

try:
    # Some operation that might fail

    result = risky_operation()
except Exception as e:
    # Convert and log the exception

    context = create_error_context(
        user_id=user_id,
        command="risky_operation",
        metadata={"operation_type": "database_query"}
    )
    mythos_error = handle_exception(e, context)
    raise mythos_error
```

#### Pattern 3: HTTPException with Logging

```python
from fastapi import HTTPException
from server.logging_config import get_logger

logger = get_logger(__name__)

# Log before raising HTTPException

logger.warning(
    "Authentication failed",
    user_id=user_id,
    reason="invalid_token",
    ip_address=client_ip,
    status_code=401
)
raise HTTPException(status_code=401, detail="Invalid or missing token")
```

### 3. Error Context Requirements

All errors must include appropriate context:

```python
@dataclass
class ErrorContext:
    user_id: str | None = None
    room_id: str | None = None
    command: str | None = None
    session_id: str | None = None
    request_id: str | None = None
    timestamp: datetime = field(default_factory=lambda: datetime.now(UTC))
    metadata: dict[str, Any] = field(default_factory=dict)
```

### 4. Logging Levels and Usage

**ERROR**: System errors, exceptions, failures

**WARNING**: Recoverable issues, deprecated usage, rate limiting

**INFO**: Normal operations, successful authentications
- **DEBUG**: Detailed diagnostic information

## Implementation Tasks

### Phase 1: Core Infrastructure Enhancement

#### Task 1.1: Enhanced Exception Wrapper

[ ] Create `log_and_raise` utility function

- [ ] Implement automatic context detection
- [ ] Add support for HTTPException logging

#### Task 1.2: HTTPException Integration

[ ] Create custom HTTPException subclass with logging

- [ ] Update FastAPI handlers to use logged exceptions
- [ ] Implement automatic context extraction

#### Task 1.3: Third-party Exception Handling

[ ] Create wrapper for common third-party exceptions

- [ ] Implement automatic exception conversion
- [ ] Add proper error categorization

### Phase 2: Codebase Integration

#### Task 2.1: API Layer Updates

[ ] Update `server/api/real_time.py` error handling

- [ ] Update `server/api/players.py` error handling
- [ ] Update `server/api/rooms.py` error handling
- [ ] Update `server/api/monitoring.py` error handling

#### Task 2.2: Authentication Layer Updates

[ ] Update `server/auth/argon2_utils.py` error handling

- [ ] Update `server/auth/endpoints.py` error handling
- [ ] Update `server/auth/dependencies.py` error handling
- [ ] Update `server/auth/invites.py` error handling

#### Task 2.3: Game Logic Updates

[ ] Update `server/game/player_service.py` error handling

- [ ] Update `server/game/movement_service.py` error handling
- [ ] Update `server/game/emote_service.py` error handling

#### Task 2.4: Utility Layer Updates

[ ] Update `server/utils/command_parser.py` error handling

- [ ] Update `server/utils/rate_limiter.py` error handling
- [ ] Update `server/security_utils.py` error handling

#### Task 2.5: Persistence Layer Updates

[ ] Update `server/persistence.py` error handling

- [ ] Update `server/database.py` error handling
- [ ] Update `server/world_loader.py` error handling

### Phase 3: Testing and Validation

#### Task 3.1: Test Coverage

[ ] Create tests for new error logging utilities

- [ ] Update existing tests to verify logging behavior
- [ ] Add integration tests for error flow

#### Task 3.2: Log Analysis

[ ] Create log analysis tools

- [ ] Implement error pattern detection
- [ ] Add monitoring for error rates

#### Task 3.3: Documentation

[ ] Update developer documentation

- [ ] Create error handling guidelines
- [ ] Add troubleshooting guides

## Security Considerations

### COPPA Compliance

No personal information in error logs

- Sanitized error messages for user-facing content
- Secure log file storage and access controls

### Data Protection

Sensitive data exclusion from logs

- Proper log retention policies
- Secure log transmission and storage

## Performance Considerations

### Logging Overhead

Minimal performance impact on error paths

- Efficient context serialization
- Proper log level filtering

### Storage Management

Automatic log rotation

- Configurable retention policies
- Efficient log file organization

## Monitoring and Alerting

### Error Metrics

Error rate tracking by category

- Response time impact measurement
- User experience degradation detection

### Alerting Thresholds

Critical error rate thresholds

- Performance degradation alerts
- Security incident detection

## Implementation Guidelines

### Code Review Checklist

[ ] All exceptions include proper logging

- [ ] Error context is complete and relevant
- [ ] Log levels are appropriate
- [ ] No sensitive data in logs
- [ ] Proper error categorization

### Testing Requirements

[ ] Unit tests for error logging

- [ ] Integration tests for error flow
- [ ] Performance tests for logging overhead
- [ ] Security tests for data protection

## Success Criteria

### Functional Requirements

All Python exceptions are properly logged

- Error context is complete and structured
- Log files are properly categorized
- Error responses are user-friendly

### Non-Functional Requirements

Logging overhead < 5ms per error

- 100% error coverage in production code
- Zero sensitive data leakage
- Comprehensive test coverage (>90%)

## Future Enhancements

### Advanced Features

Machine learning error pattern detection

- Automated error resolution suggestions
- Real-time error dashboard
- Predictive error analysis

### Integration Opportunities

External monitoring system integration

- Error reporting to development teams
- Automated incident response
- Performance optimization recommendations

---

*As the restricted archives of Miskatonic University teach us, the proper documentation of anomalous events is not merely an academic exercise, but a critical component of maintaining the delicate balance between order and chaos in our digital realm. This specification ensures that every error, every exception, and every anomaly is properly catalogued for posterity and analysis.*
