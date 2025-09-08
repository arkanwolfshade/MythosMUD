# Logging Best Practices for MythosMUD

*As documented in the restricted archives of Miskatonic University, proper logging is the foundation upon which all system observability and debugging capabilities rest. Without comprehensive logging, we are blind to the inner workings of our digital realm.*

## Overview

This document outlines the best practices for logging throughout the MythosMUD codebase. Our structured logging system provides comprehensive observability while maintaining security and performance.

## Core Logging Principles

### 1. **Structured Logging**
All log entries must be structured with consistent fields and formats. This enables automated analysis and monitoring.

### 2. **Context is Everything**
Every log entry should include sufficient context to understand what was happening when the event occurred.

### 3. **Security First**
Never log sensitive information such as passwords, tokens, or personal data.

### 4. **Performance Aware**
Logging should not significantly impact system performance.

### 5. **Actionable Information**
Log entries should provide information that can be acted upon by developers or operators.

## Log Levels and Usage

### DEBUG
Use for detailed diagnostic information that is typically only of interest when diagnosing problems.

```python
import structlog

logger = structlog.get_logger(__name__)

# Good: Detailed debugging information
logger.debug(
    "Processing player movement",
    player_id=player.id,
    current_room=player.current_room_id,
    direction=direction,
    target_room=target_room_id,
    movement_type="normal"
)

# Bad: Too verbose for production
logger.debug(f"Variable x = {x}, y = {y}, z = {z}")  # Too detailed
```

### INFO
Use for general information about system operation.

```python
# Good: Important system events
logger.info(
    "Player connected",
    player_id=player.id,
    player_name=player.name,
    connection_type="websocket",
    ip_address=request.client.host
)

logger.info(
    "Server startup completed",
    startup_time=startup_duration,
    components_loaded=len(loaded_components),
    database_connected=True
)

# Bad: Too frequent or not meaningful
logger.info(f"Processing request {request_id}")  # Too frequent
```

### WARNING
Use for potentially harmful situations or unexpected conditions that don't prevent the system from functioning.

```python
# Good: Warning about potential issues
logger.warning(
    "High memory usage detected",
    memory_usage_percent=85.5,
    threshold=80.0,
    component="database_connection_pool"
)

logger.warning(
    "Player movement rate limit approaching",
    player_id=player.id,
    movements_per_minute=45,
    limit=50
)

# Bad: Using warning for normal conditions
logger.warning("Player moved to room X")  # This is normal operation
```

### ERROR
Use for error events that might still allow the application to continue running.

```python
# Good: Error conditions that are handled
logger.error(
    "Database connection failed, retrying",
    database_url=db_url,
    retry_count=retry_count,
    max_retries=max_retries,
    error=str(e)
)

logger.error(
    "Failed to send message to player",
    player_id=player.id,
    message_type="system_notification",
    error=str(e),
    retry_scheduled=True
)

# Bad: Using error for handled exceptions
logger.error("Caught expected exception")  # If it's expected, use info or debug
```

### CRITICAL
Use for very severe error events that will presumably lead the application to abort.

```python
# Good: Critical system failures
logger.critical(
    "Database connection pool exhausted",
    active_connections=pool_size,
    max_connections=max_pool_size,
    pending_requests=queue_size
)

logger.critical(
    "Memory allocation failed",
    requested_bytes=requested_size,
    available_memory=available_memory,
    system_memory=total_memory
)

# Bad: Using critical for recoverable errors
logger.critical("Failed to load player preferences")  # This is recoverable
```

## Structured Logging Patterns

### Basic Logging

```python
import structlog

logger = structlog.get_logger(__name__)

# Good: Structured logging with context
logger.info(
    "Player action completed",
    player_id=player.id,
    action="move",
    direction="north",
    from_room=player.current_room_id,
    to_room=new_room_id,
    duration_ms=movement_duration
)

# Bad: String formatting
logger.info(f"Player {player.id} moved from {old_room} to {new_room}")
```

### Error Logging with Context

```python
# Good: Comprehensive error context
try:
    result = risky_operation()
except Exception as e:
    logger.error(
        "Operation failed",
        operation="player_save",
        player_id=player.id,
        error_type=type(e).__name__,
        error_message=str(e),
        retry_count=retry_count,
        will_retry=True
    )
    raise

# Bad: Minimal error information
try:
    result = risky_operation()
except Exception as e:
    logger.error(f"Error: {e}")
    raise
```

### Performance Logging

```python
import time
from contextlib import contextmanager

@contextmanager
def log_performance(operation_name: str, **context):
    """Context manager for logging operation performance."""
    start_time = time.time()
    logger.info(f"{operation_name} started", **context)

    try:
        yield
    except Exception as e:
        duration = time.time() - start_time
        logger.error(
            f"{operation_name} failed",
            duration_ms=duration * 1000,
            error=str(e),
            **context
        )
        raise
    else:
        duration = time.time() - start_time
        logger.info(
            f"{operation_name} completed",
            duration_ms=duration * 1000,
            **context
        )

# Usage
with log_performance("player_movement", player_id=player.id, direction="north"):
    movement_service.move_player(player, "north")
```

## Context Management

### Request Context

```python
from server.utils.error_logging import create_context_from_request

@app.middleware("http")
async def add_request_context(request: Request, call_next):
    """Add request context to all log entries."""
    # Create request context
    context = create_context_from_request(request)

    # Add to structlog context
    structlog.contextvars.clear_contextvars()
    structlog.contextvars.bind_contextvars(
        request_id=context.request_id,
        user_id=context.user_id,
        ip_address=context.ip_address,
        user_agent=context.user_agent
    )

    try:
        response = await call_next(request)
        return response
    finally:
        structlog.contextvars.clear_contextvars()
```

### User Context

```python
def log_user_action(action: str, **kwargs):
    """Log user action with consistent context."""
    logger.info(
        f"User action: {action}",
        action=action,
        user_id=current_user.id if current_user else None,
        timestamp=datetime.now().isoformat(),
        **kwargs
    )

# Usage
log_user_action("player_created", player_name=name, starting_room=room_id)
log_user_action("movement", direction=direction, room_id=room_id)
```

### System Context

```python
def log_system_event(event: str, **kwargs):
    """Log system event with consistent context."""
    logger.info(
        f"System event: {event}",
        event=event,
        component=kwargs.get("component", "unknown"),
        timestamp=datetime.now().isoformat(),
        **kwargs
    )

# Usage
log_system_event("database_connected", component="database", connection_count=5)
log_system_event("cache_cleared", component="cache", entries_cleared=1000)
```

## Security Considerations

### Sensitive Data Protection

```python
# Good: Logging without sensitive data
logger.info(
    "User authentication attempt",
    username=username,  # OK - username is not sensitive
    ip_address=request.client.host,
    user_agent=request.headers.get("user-agent"),
    success=False
)

# Bad: Logging sensitive data
logger.info(
    "User authentication attempt",
    username=username,
    password=password,  # BAD - password is sensitive!
    token=auth_token    # BAD - token is sensitive!
)
```

### Data Sanitization

```python
def sanitize_for_logging(data: dict) -> dict:
    """Remove sensitive fields from data before logging."""
    sensitive_fields = {
        "password", "token", "secret", "key", "auth", "credential",
        "ssn", "social_security", "credit_card", "cvv"
    }

    sanitized = {}
    for key, value in data.items():
        if any(sensitive in key.lower() for sensitive in sensitive_fields):
            sanitized[key] = "[REDACTED]"
        else:
            sanitized[key] = value

    return sanitized

# Usage
user_data = {"username": "john", "password": "secret123", "email": "john@example.com"}
logger.info("User data processed", **sanitize_for_logging(user_data))
# Logs: {"username": "john", "password": "[REDACTED]", "email": "john@example.com"}
```

## Performance Logging

### Database Query Logging

```python
def log_database_query(query: str, params: dict, duration: float, rows_affected: int):
    """Log database query with performance metrics."""
    logger.debug(
        "Database query executed",
        query=query,
        params=sanitize_for_logging(params),
        duration_ms=duration * 1000,
        rows_affected=rows_affected,
        query_type=query.split()[0].upper()  # SELECT, INSERT, etc.
    )

# Usage in database operations
start_time = time.time()
result = db.execute(query, params)
duration = time.time() - start_time
log_database_query(query, params, duration, result.rowcount)
```

### API Request Logging

```python
@app.middleware("http")
async def log_api_requests(request: Request, call_next):
    """Log API requests with performance metrics."""
    start_time = time.time()

    # Log request
    logger.info(
        "API request started",
        method=request.method,
        url=str(request.url),
        path=request.url.path,
        query_params=dict(request.query_params),
        client_ip=request.client.host,
        user_agent=request.headers.get("user-agent")
    )

    response = await call_next(request)
    duration = time.time() - start_time

    # Log response
    logger.info(
        "API request completed",
        method=request.method,
        url=str(request.url),
        status_code=response.status_code,
        duration_ms=duration * 1000,
        response_size=response.headers.get("content-length", 0)
    )

    return response
```

## Log Analysis and Monitoring

### Using Our Log Analysis Tools

```bash
# Generate comprehensive error report
python scripts/analyze_error_logs.py --log-dir logs/development --report

# Monitor errors in real-time
python scripts/error_monitoring.py --log-dir logs/development --monitor --interval 30

# Analyze error patterns
python scripts/analyze_error_logs.py --log-dir logs/development --patterns
```

### Custom Log Analysis

```python
import structlog
from pathlib import Path
import json

def analyze_log_file(log_file: Path) -> dict:
    """Analyze a log file for patterns and statistics."""
    stats = {
        "total_entries": 0,
        "by_level": {},
        "by_component": {},
        "error_patterns": {},
        "performance_metrics": []
    }

    with open(log_file, 'r') as f:
        for line in f:
            try:
                # Parse structured log entry
                entry = json.loads(line)
                stats["total_entries"] += 1

                # Count by level
                level = entry.get("level", "unknown")
                stats["by_level"][level] = stats["by_level"].get(level, 0) + 1

                # Count by component
                component = entry.get("component", "unknown")
                stats["by_component"][component] = stats["by_component"].get(component, 0) + 1

                # Track error patterns
                if level in ["ERROR", "CRITICAL"]:
                    error_msg = entry.get("event", "")
                    stats["error_patterns"][error_msg] = stats["error_patterns"].get(error_msg, 0) + 1

                # Track performance metrics
                if "duration_ms" in entry:
                    stats["performance_metrics"].append({
                        "operation": entry.get("event", ""),
                        "duration_ms": entry["duration_ms"],
                        "timestamp": entry.get("timestamp", "")
                    })

            except json.JSONDecodeError:
                # Skip malformed log entries
                continue

    return stats
```

## Common Anti-Patterns

### ❌ Don't Do This

```python
# Bad: String formatting in logs
logger.info(f"User {user_id} performed action {action}")

# Bad: Logging sensitive data
logger.info("User login", username=username, password=password)

# Bad: Too verbose logging
logger.debug(f"Variable x = {x}, y = {y}, z = {z}, a = {a}, b = {b}")

# Bad: Inconsistent log levels
logger.error("Normal operation completed")  # Should be info
logger.info("Critical system failure")      # Should be critical

# Bad: No context in logs
logger.error("Error occurred")

# Bad: Logging in tight loops
for i in range(10000):
    logger.debug(f"Processing item {i}")  # Too frequent
```

### ✅ Do This Instead

```python
# Good: Structured logging
logger.info("User action performed", user_id=user_id, action=action)

# Good: Sanitized data
logger.info("User login", username=username, success=True)

# Good: Appropriate detail level
logger.debug("Processing batch", batch_size=len(items), batch_id=batch_id)

# Good: Correct log levels
logger.info("Operation completed successfully")
logger.critical("System failure detected")

# Good: Rich context
logger.error(
    "Operation failed",
    operation="user_creation",
    user_id=user_id,
    error_type=type(e).__name__,
    error_message=str(e),
    retry_count=retry_count
)

# Good: Batched logging
logger.info("Batch processing completed", items_processed=len(items), batch_id=batch_id)
```

## Testing Logging

### Unit Tests for Logging

```python
import pytest
from unittest.mock import patch
import structlog

def test_user_action_logging():
    """Test that user actions are properly logged."""
    with patch.object(structlog.get_logger(), 'info') as mock_logger:
        log_user_action("test_action", user_id="123", extra_data="test")

        mock_logger.assert_called_once_with(
            "User action: test_action",
            action="test_action",
            user_id="123",
            extra_data="test",
            timestamp=pytest.approx(datetime.now().isoformat(), rel=1)
        )

def test_error_logging_with_context():
    """Test that errors are logged with proper context."""
    with patch.object(structlog.get_logger(), 'error') as mock_logger:
        try:
            raise ValueError("Test error")
        except Exception as e:
            logger.error(
                "Test operation failed",
                operation="test",
                error_type=type(e).__name__,
                error_message=str(e)
            )

        mock_logger.assert_called_once()
        call_args = mock_logger.call_args[1]
        assert call_args["operation"] == "test"
        assert call_args["error_type"] == "ValueError"
        assert call_args["error_message"] == "Test error"
```

### Integration Tests

```python
def test_api_request_logging():
    """Test that API requests are properly logged."""
    with patch.object(structlog.get_logger(), 'info') as mock_logger:
        response = client.get("/api/players")

        # Check that request was logged
        assert mock_logger.call_count >= 2  # Request start and completion

        # Check request logging
        request_call = mock_logger.call_args_list[0]
        assert "API request started" in request_call[0][0]
        assert request_call[1]["method"] == "GET"
        assert request_call[1]["path"] == "/api/players"

        # Check response logging
        response_call = mock_logger.call_args_list[1]
        assert "API request completed" in response_call[0][0]
        assert response_call[1]["status_code"] == 200
        assert "duration_ms" in response_call[1]
```

## Log Rotation and Management

### Configuration

```python
# In logging configuration
LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "structured": {
            "()": structlog.stdlib.ProcessorFormatter,
            "processor": structlog.dev.ConsoleRenderer(colors=False),
        },
    },
    "handlers": {
        "file": {
            "class": "logging.handlers.RotatingFileHandler",
            "filename": "logs/mythosmud.log",
            "maxBytes": 10485760,  # 10MB
            "backupCount": 5,
            "formatter": "structured",
        },
        "error_file": {
            "class": "logging.handlers.RotatingFileHandler",
            "filename": "logs/errors.log",
            "maxBytes": 10485760,  # 10MB
            "backupCount": 5,
            "formatter": "structured",
            "level": "ERROR",
        },
    },
    "loggers": {
        "": {
            "handlers": ["file", "error_file"],
            "level": "INFO",
            "propagate": False,
        },
    },
}
```

### Log Cleanup

```python
import os
from pathlib import Path
from datetime import datetime, timedelta

def cleanup_old_logs(log_dir: Path, days_to_keep: int = 30):
    """Remove log files older than specified days."""
    cutoff_date = datetime.now() - timedelta(days=days_to_keep)

    for log_file in log_dir.glob("*.log*"):
        if log_file.stat().st_mtime < cutoff_date.timestamp():
            logger.info("Removing old log file", file_path=str(log_file))
            log_file.unlink()

# Usage
cleanup_old_logs(Path("logs"), days_to_keep=30)
```

## Conclusion

Proper logging is essential for maintaining a robust and observable system. By following these best practices:

- Use structured logging with consistent context
- Choose appropriate log levels
- Protect sensitive information
- Monitor performance impact
- Test logging behavior
- Manage log files properly

You ensure that your system is observable, debuggable, and maintainable. Remember: *As the restricted archives teach us, the proper documentation of system behavior is not merely a technical requirement, but a fundamental aspect of understanding the deeper patterns that govern our digital realm.*

---

*This guide is maintained by the Department of Occult Studies, Miskatonic University. For questions or clarifications, consult the restricted archives or contact the system administrators.*
