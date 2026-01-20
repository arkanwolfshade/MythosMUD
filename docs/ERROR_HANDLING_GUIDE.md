# Error Handling Guide for MythosMUD

*As documented in the restricted archives of Miskatonic University, proper error handling is not merely a technical
exercise, but a critical component of maintaining the delicate balance between order and chaos in our digital realm.*

## Overview

This guide provides comprehensive instructions for implementing proper error handling throughout the MythosMUD codebase.
Our structured error logging system ensures that every anomaly, every exception, and every error is properly catalogued
for posterity and analysis.

## Core Principles

### 1. **Enhanced Structured Logging First**

All errors must be logged with the enhanced structured logging system before being raised or returned. This ensures
complete traceability and analysis capabilities.

**Required Import:**

```python
from server.logging.enhanced_logging_config import get_logger
logger = get_logger(__name__)
```

**Forbidden Patterns:**

```python
# ❌ WRONG - Will cause failures

import logging
logger = logging.getLogger(__name__)

# ❌ WRONG - Deprecated context parameter

logger.error("Error occurred", context={"key": "value"})
```

### 2. **Context is King**

Every error must include sufficient context to understand:

- What operation was being performed
- Who was performing it (if applicable)
- When it occurred
- What data was involved
- Why it failed

### 3. **User-Friendly Messages**

Errors exposed to users must be clear, actionable, and free of technical jargon or sensitive information.

### 4. **Security by Design**

Never log sensitive data such as passwords, tokens, or personal information. Our error logging system automatically
filters such data.

## Error Types and Usage

### MythosMUDError (Base Class)

The foundation of our error hierarchy. All custom errors should inherit from this class.

```python
from server.exceptions import MythosMUDError, ErrorContext
from server.logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)

# Basic usage with enhanced logging

try:
    result = database.save_player(player_data)
except Exception as e:
    logger.error(
        "Database connection failed",
        operation="player_save",
        user_id="player123",
        room_id="arkham_001",
        error_code="DB_CONN_TIMEOUT",
        error=str(e)
    )
    raise MythosMUDError(
        message="Database connection failed",
        context=ErrorContext(
            operation="player_save",
            user_id="player123",
            metadata={"room_id": "arkham_001"}
        ),
        details={"error_code": "DB_CONN_TIMEOUT"},
    user_friendly="Unable to save your progress. Please try again."
)
```

### ValidationError

Use for input validation failures and business rule violations.

```python
from server.exceptions import ValidationError
from server.utils.error_logging import log_and_raise, create_error_context

# In a service method

def create_player(name: str, room_id: str) -> Player:
    if not name or len(name.strip()) < 2:
        context = create_error_context(
            operation="create_player",
            metadata={"player_name": name, "room_id": room_id}
        )
        log_and_raise(
            ValidationError,
            "Player name must be at least 2 characters",
            context=context,
            details={"provided_name": name, "min_length": 2},
            user_friendly="Player names must be at least 2 characters long"
        )

    # Check for existing player

    if player_exists(name):
        context = create_error_context(
            operation="create_player",
            metadata={"player_name": name}
        )
        log_and_raise(
            ValidationError,
            "Player name already exists",
            context=context,
            details={"player_name": name},
            user_friendly="A player with this name already exists"
        )

    # Continue with player creation...

```

### DatabaseError

Use for database-related failures.

```python
from server.exceptions import DatabaseError
from server.utils.error_logging import log_and_raise

def save_player_data(player: Player) -> None:
    try:
        # Database operation

        db.save(player)
    except sqlite3.Error as e:
        context = create_error_context(
            operation="save_player_data",
            user_id=str(player.id),
            metadata={"player_name": player.name}
        )
        log_and_raise(
            DatabaseError,
            "Failed to save player data to database",
            context=context,
            details={"sqlite_error": str(e), "player_id": str(player.id)},
            user_friendly="Unable to save your progress. Please try again."
        )
```

### LoggedHTTPException

Use for API endpoint errors that need to be returned as HTTP responses.

```python
from server.exceptions import LoggedHTTPException
from server.utils.error_logging import create_context_from_request

@app.post("/api/players")
async def create_player(
    name: str,
    current_user: User = Depends(get_current_user),
    request: Request = None
):
    try:
        return player_service.create_player(name, starting_room_id)
    except ValidationError as e:
        context = create_context_from_request(request)
        if current_user:
            context.user_id = str(current_user.id)
        context.metadata["player_name"] = name
        context.metadata["starting_room_id"] = starting_room_id

        raise LoggedHTTPException(
            status_code=400,
            detail="Invalid input provided",
            context=context
        ) from None
```

## Error Context Best Practices

### Creating Error Context

Always provide meaningful context when creating errors:

```python
from server.utils.error_logging import create_error_context

# Good: Comprehensive context

context = create_error_context(
    operation="process_movement_command",
    user_id=str(player.id),
    request_id=request_id,
    metadata={
        "command": "go",
        "direction": "north",
        "current_room": player.current_room_id,
        "target_room": target_room_id
    }
)

# Bad: Minimal context

context = create_error_context(operation="move")
```

### Metadata Guidelines

Include relevant metadata that will help with debugging:

```python
# For player operations

metadata = {
    "player_id": str(player.id),
    "player_name": player.name,
    "current_room": player.current_room_id,
    "action": "movement"
}

# For API operations

metadata = {
    "endpoint": "/api/players",
    "method": "POST",
    "user_agent": request.headers.get("user-agent"),
    "ip_address": request.client.host
}

# For database operations

metadata = {
    "table": "players",
    "operation": "INSERT",
    "record_id": str(record.id)
}
```

## Logging Patterns

### Using log_and_raise

The `log_and_raise` utility is the preferred way to log and raise errors:

```python
from server.utils.error_logging import log_and_raise

# Simple error

log_and_raise(
    ValidationError,
    "Invalid input provided",
    details={"field": "email", "value": email}
)

# Error with context

log_and_raise(
    DatabaseError,
    "Failed to retrieve player data",
    context=context,
    details={"player_id": player_id, "query": query},
    user_friendly="Unable to load player data. Please try again."
)
```

### Direct Exception Creation

For cases where you need more control:

```python
from server.exceptions import ValidationError, ErrorContext

error = ValidationError(
    message="Player name contains invalid characters",
    context=ErrorContext(
        operation="validate_player_name",
        metadata={"player_name": name, "invalid_chars": invalid_chars}
    ),
    details={"name": name, "allowed_pattern": r"^[a-zA-Z0-9_]+$"},
    user_friendly="Player names can only contain letters, numbers, and underscores"
)
raise error
```

## Common Patterns

### Input Validation

```python
def validate_player_name(name: str) -> None:
    """Validate player name according to game rules."""
    if not name:
        log_and_raise(
            ValidationError,
            "Player name cannot be empty",
            details={"provided_name": name},
            user_friendly="Please enter a player name"
        )

    if len(name) < 2:
        log_and_raise(
            ValidationError,
            "Player name too short",
            details={"provided_name": name, "min_length": 2},
            user_friendly="Player names must be at least 2 characters long"
        )

    if len(name) > 20:
        log_and_raise(
            ValidationError,
            "Player name too long",
            details={"provided_name": name, "max_length": 20},
            user_friendly="Player names cannot exceed 20 characters"
        )

    if not re.match(r"^[a-zA-Z0-9_]+$", name):
        log_and_raise(
            ValidationError,
            "Player name contains invalid characters",
            details={"provided_name": name, "allowed_pattern": r"^[a-zA-Z0-9_]+$"},
            user_friendly="Player names can only contain letters, numbers, and underscores"
        )
```

### Database Operations

```python
def get_player_by_id(player_id: str) -> Player:
    """Retrieve player by ID with proper error handling."""
    try:
        player = db.query(Player).filter(Player.id == player_id).first()
        if not player:
            context = create_error_context(
                operation="get_player_by_id",
                metadata={"player_id": player_id}
            )
            log_and_raise(
                ValidationError,
                "Player not found",
                context=context,
                details={"player_id": player_id},
                user_friendly="Player not found"
            )
        return player
    except sqlite3.Error as e:
        context = create_error_context(
            operation="get_player_by_id",
            metadata={"player_id": player_id}
        )
        log_and_raise(
            DatabaseError,
            "Database error while retrieving player",
            context=context,
            details={"player_id": player_id, "sqlite_error": str(e)},
            user_friendly="Unable to retrieve player data. Please try again."
        )
```

### API Endpoint Error Handling

```python
@app.post("/api/players/{player_id}/move")
async def move_player(
    player_id: str,
    direction: str,
    current_user: User = Depends(get_current_user),
    request: Request = None
):
    """Move player in specified direction."""
    try:
        result = movement_service.move_player(player_id, direction)
        return {"success": True, "result": result}
    except ValidationError as e:
        # ValidationError is already logged by the service

        context = create_context_from_request(request)
        context.user_id = str(current_user.id)
        context.metadata.update({
            "player_id": player_id,
            "direction": direction
        })

        raise LoggedHTTPException(
            status_code=400,
            detail=str(e),
            context=context
        ) from None
    except DatabaseError as e:
        # DatabaseError is already logged by the service

        context = create_context_from_request(request)
        context.user_id = str(current_user.id)
        context.metadata.update({
            "player_id": player_id,
            "direction": direction
        })

        raise LoggedHTTPException(
            status_code=500,
            detail="Internal server error",
            context=context
        ) from None
```

## Testing Error Handling

### Unit Tests

```python
import pytest
from server.exceptions import ValidationError
from server.utils.error_logging import log_and_raise

def test_validate_player_name_empty():
    """Test validation of empty player name."""
    with pytest.raises(ValidationError) as exc_info:
        validate_player_name("")

    error = exc_info.value
    assert "empty" in error.message.lower()
    assert "Please enter a player name" == error.user_friendly

def test_validate_player_name_too_short():
    """Test validation of short player name."""
    with pytest.raises(ValidationError) as exc_info:
        validate_player_name("a")

    error = exc_info.value
    assert "too short" in error.message.lower()
    assert "at least 2 characters" in error.user_friendly
```

### Integration Tests

```python
def test_create_player_duplicate_name():
    """Test creating player with duplicate name."""
    # Create first player

    player1 = player_service.create_player("TestPlayer", "arkham_001")

    # Try to create second player with same name

    with pytest.raises(ValidationError) as exc_info:
        player_service.create_player("TestPlayer", "arkham_001")

    error = exc_info.value
    assert "already exists" in error.message.lower()
    assert "A player with this name already exists" == error.user_friendly
```

## Error Analysis and Monitoring

### Using Log Analysis Tools

Our log analysis tools help identify patterns and trends in errors:

```bash
# Generate comprehensive error report

python scripts/analyze_error_logs.py --log-dir logs/development --report

# Analyze error patterns

python scripts/analyze_error_logs.py --log-dir logs/development --patterns

# Monitor errors in real-time

python scripts/error_monitoring.py --log-dir logs/development --monitor --interval 30
```

### Common Error Categories

Our system automatically categorizes errors:

**Database**: SQL errors, connection failures, query timeouts

**Network**: WebSocket issues, connection timeouts, network failures

**Authentication**: Login failures, token validation, authorization errors

**Validation**: Input validation, business rule violations

**File System**: File access errors, permission issues

- **Game Logic**: Player actions, room interactions, command processing
- **System**: Memory issues, resource exhaustion, system errors

## Anti-Patterns to Avoid

### ❌ Don't Do This

```python
# Bad: Generic error without context

try:
    player = get_player(player_id)
except Exception as e:
    logger.error(f"Error: {e}")
    raise

# Bad: Exposing internal details to users

try:
    result = complex_operation()
except Exception as e:
    return {"error": f"Database error: {e}"}

# Bad: Not logging errors

def risky_operation():
    try:
        return dangerous_call()
    except Exception:
        return None  # Silent failure
```

### ✅ Do This Instead

```python
# Good: Structured error with context

try:
    player = get_player(player_id)
except Exception as e:
    context = create_error_context(
        operation="get_player",
        metadata={"player_id": player_id}
    )
    log_and_raise(
        DatabaseError,
        "Failed to retrieve player",
        context=context,
        details={"player_id": player_id, "original_error": str(e)},
        user_friendly="Unable to load player data. Please try again."
    )

# Good: User-friendly error messages

try:
    result = complex_operation()
except Exception as e:
    context = create_error_context(operation="complex_operation")
    log_and_raise(
        DatabaseError,
        "Complex operation failed",
        context=context,
        details={"error": str(e)},
        user_friendly="Operation failed. Please try again."
    )

# Good: Proper error logging

def risky_operation():
    try:
        return dangerous_call()
    except Exception as e:
        context = create_error_context(operation="risky_operation")
        log_and_raise(
            SystemError,
            "Risky operation failed",
            context=context,
            details={"error": str(e)},
            user_friendly="Operation unavailable. Please try again later."
        )
```

## Security Considerations

### Sensitive Data Protection

Our error logging system automatically filters sensitive data, but you should still be mindful:

```python
# Good: No sensitive data in context

context = create_error_context(
    operation="authenticate_user",
    metadata={
        "username": username,  # OK - not sensitive
        "login_attempt": True
    }
)

# Bad: Sensitive data in context

context = create_error_context(
    operation="authenticate_user",
    metadata={
        "password": password,  # BAD - sensitive!
        "token": auth_token    # BAD - sensitive!
    }
)
```

### Error Message Sanitization

```python
# Good: Sanitized error message

log_and_raise(
    ValidationError,
    "Invalid input provided",
    details={"field": "email", "error_type": "format"},
    user_friendly="Please enter a valid email address"
)

# Bad: Exposing internal details

log_and_raise(
    ValidationError,
    f"Regex pattern {pattern} failed to match {input_value}",
    user_friendly="Invalid input"
)
```

## Performance Considerations

### Error Logging Overhead

Our error logging system is designed for minimal performance impact:

- Logging operations are asynchronous where possible
- Context creation is optimized for common use cases
- Error analysis tools are separate from runtime operations

### Best Practices

```python
# Good: Create context once and reuse

def process_multiple_operations(operations):
    base_context = create_error_context(operation="batch_processing")

    for op in operations:
        try:
            process_operation(op)
        except Exception as e:
            # Reuse base context with operation-specific metadata

            op_context = base_context.copy()
            op_context.metadata["operation"] = op.name
            log_and_raise(
                ProcessingError,
                f"Failed to process operation {op.name}",
                context=op_context,
                details={"operation": op.name, "error": str(e)}
            )

# Bad: Creating new context for each operation

def process_multiple_operations(operations):
    for op in operations:
        try:
            process_operation(op)
        except Exception as e:
            # Inefficient: new context for each error

            context = create_error_context(
                operation="batch_processing",
                metadata={"operation": op.name}
            )
            log_and_raise(ProcessingError, f"Failed: {e}", context=context)
```

## Troubleshooting

### Common Issues

1. **Missing Context**: Always provide meaningful context
2. **Generic Error Messages**: Be specific about what failed
3. **Sensitive Data Leakage**: Never log passwords or tokens
4. **Silent Failures**: Always log errors before handling them
5. **Poor User Messages**: Make error messages actionable

### Debugging Tips

1. Use the log analysis tools to identify error patterns
2. Check error categories to understand failure types
3. Look at error timelines to identify trends
4. Use the monitoring tools for real-time error tracking

## Enhanced Logging Best Practices for Error Handling

### **CRITICAL: Enhanced Logging Requirements for Error Handling**

All error handling MUST use the enhanced logging system for proper observability and debugging.

#### **Required Import Pattern**

```python
# ✅ CORRECT - Enhanced logging import (MANDATORY)

from server.logging.enhanced_logging_config import get_logger, bind_request_context
logger = get_logger(__name__)
```

#### **Forbidden Patterns**

```python
# ❌ FORBIDDEN - Will cause import failures and system crashes

import logging
logger = logging.getLogger(__name__)

# ❌ FORBIDDEN - Deprecated context parameter (causes TypeError)

logger.error("Error occurred", context={"key": "value"})

# ❌ FORBIDDEN - String formatting breaks structured logging

logger.error(f"Error in {operation} for user {user_id}")
```

#### **Correct Error Logging Patterns**

```python
# ✅ CORRECT - Error logging with enhanced context

logger.error("Database operation failed",
             operation="player_save",
             user_id=user.id,
             room_id=room.id,
             error_code="DB_CONN_TIMEOUT",
             error=str(e),
             retry_count=3)

# ✅ CORRECT - Request context binding for error tracking

bind_request_context(correlation_id=req_id, user_id=user.id, session_id=session.id)
logger.error("Authentication failed",
             user_id=user.id,
             auth_method="password",
             error_code="AUTH_INVALID_CREDENTIALS")

# ✅ CORRECT - Performance logging with error context

with measure_performance("database_query", user_id=user.id):
    try:
        result = database.query("SELECT * FROM players")
    except Exception as e:
        logger.error("Database query failed",
                     query="SELECT * FROM players",
                     user_id=user.id,
                     error=str(e))
        raise
```

#### **Error Logging Best Practices**

**Structured Logging**: Always use key-value pairs for log data

**Error Context**: Include operation, user_id, and error details

**Correlation IDs**: Use request context binding for error tracking

**Performance Tracking**: Log performance metrics with error context

**Security**: Never log sensitive data (automatic sanitization helps)

#### **Error Logging Validation**

```python
# ✅ CORRECT - Validate error logging behavior

def test_error_logging():
    """Test that errors are logged correctly."""
    with patch.object(enhanced_logging, 'get_logger') as mock_logger:
        # Setup mock logger

        mock_logger.return_value.error = MagicMock()

        # Trigger error

        with pytest.raises(ValidationError):
            validate_player_name("")

        # Verify error logging occurred

        mock_logger.return_value.error.assert_called_with(
            "Validation failed",
            operation="validate_player_name",
            user_id=user.id,
            error_code="VALIDATION_ERROR"
        )
```

#### **Documentation References**

**Complete Guide**: [LOGGING_BEST_PRACTICES.md](LOGGING_BEST_PRACTICES.md)

**Quick Reference**: [LOGGING_QUICK_REFERENCE.md](LOGGING_QUICK_REFERENCE.md)

**Error Handling Examples**: [docs/examples/logging/](examples/logging/)

## Conclusion

Proper error handling is essential for maintaining a robust and reliable system. By following these guidelines and using
our structured error logging system, you ensure that:

- All errors are properly logged and analyzed
- Users receive clear, actionable error messages
- Developers have sufficient context for debugging
- System security is maintained
- Performance impact is minimized

Remember: *As the Pnakotic Manuscripts teach us, the proper cataloguing of anomalies is not merely an academic exercise,
but a fundamental requirement for understanding the deeper patterns that govern our digital realm.*

---

*This guide is maintained by the Department of Occult Studies, Miskatonic University. For questions or clarifications,
consult the restricted archives or contact the system administrators.*
