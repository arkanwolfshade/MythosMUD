# Enhanced Logging System Guide

## Overview

The MythosMUD server uses an enhanced structured logging system built on
`structlog` with MDC (Mapped Diagnostic Context), correlation IDs, security
sanitization, and performance optimizations. This system provides comprehensive
observability for debugging, monitoring, and audit purposes.

## Quick Start

### Basic Usage

```python
from server.logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)

# Structured logging with key-value pairs
logger.info("User action completed", user_id=user.id, action="login", success=True)
logger.error("Operation failed", operation="user_creation", error=str(e), retry_count=3)
```

### Request Context Binding

```python
from server.logging.enhanced_logging_config import bind_request_context

# Bind context for request tracing
bind_request_context(
    correlation_id="req-123",
    user_id="user-456",
    session_id="session-789"
)
# All subsequent logs automatically include this context
```

## Architecture

### Core Components

1. **Enhanced Logging Config** (`enhanced_logging_config.py`)
   - MDC implementation with `structlog.contextvars`
   - Security sanitization processor
   - Correlation ID management
   - Performance monitoring integration

2. **Custom Processors**
   - `sanitize_sensitive_data`: Automatically redacts passwords, tokens, secrets
   - `add_correlation_id`: Ensures all logs have correlation IDs
   - `add_request_context`: Adds request metadata
   - `enhance_player_ids`: Converts GUIDs to human-readable format

3. **Custom Formatters**
   - `PlayerGuidFormatter`: Converts player GUIDs to `<name>: <GUID>` format
   - Enhanced readability for debugging

### Log Categories

The system automatically routes logs to subsystem-specific files. Each
subsystem has its own log file for better organization and debugging:

**Core Subsystems:**
- **server.log**: Core server operations, uvicorn lifecycle
- **persistence.log**: Database operations, SQL queries, persistence layer
- **authentication.log**: Authentication, authorization, user management
- **inventory.log**: Inventory management, containers, equipment
- **npc.log**: NPC services, NPC instances, NPC lifecycle
- **game.log**: Game mechanics, movement, room services, world loading
- **api.log**: API endpoints, REST operations
- **middleware.log**: Middleware operations, request processing
- **monitoring.log**: Performance metrics, monitoring, system health
- **time.log**: Time services, game ticks, scheduling
- **caching.log**: Cache operations, cache management
- **communications.log**: Real-time messaging, chat, WebSocket, SSE
- **commands.log**: Player commands, command processing
- **events.log**: Event bus, event publishing, event subscriptions
- **infrastructure.log**: NATS broker, message broker, infrastructure components
- **validators.log**: Input validation, command validation, security validation
- **combat.log**: Combat system, combat events, combat services
- **magic.log**: Magic system, spellcasting, spell effects, MP management
- **access.log**: Access control, permissions, API access
- **security.log**: Security events, audit trails, security violations

**Aggregator Logs:**
- **warnings.log**: ALL WARNING level logs from ALL subsystems (dual logging)
- **errors.log**: ALL ERROR and CRITICAL level logs from ALL subsystems (dual
  logging)
- **console.log**: Console output, general logging

### Dual Logging Behavior

The system implements dual logging for warnings and errors:

- **Warnings**: All WARNING level logs appear in BOTH their subsystem log file AND `warnings.log`
- **Errors**: All ERROR and CRITICAL level logs appear in BOTH their subsystem log file AND `errors.log`

This enables:
- **Subsystem-specific debugging**: Find all logs for a specific subsystem in
  its dedicated file
- **Centralized monitoring**: Quickly scan all warnings or errors across the
  entire system
- **Better observability**: No need to search multiple files to find all
  warnings or errors

Example:
```python
# In persistence subsystem
logger.warning("Database connection slow", query_time=1.5)
# This appears in: persistence.log AND warnings.log

logger.error("Database connection failed", error=str(e))
# This appears in: persistence.log AND errors.log
```

## F-String Logging Anti-Pattern

**CRITICAL**: The most common and destructive anti-pattern is f-string
logging. This MUST be eliminated:

```python
# ❌ WRONG - Destroys structured logging benefits
logger.info(f"Starting combat between {attacker} and {target}")
logger.error(f"Failed to process: {error}")
logger.debug(f"Message data: {message_data}")

# ✅ CORRECT - Structured logging enables aggregation and analysis
logger.info("Starting combat", attacker=attacker, target=target,
            room_id=room_id)
logger.error("Failed to process", error=str(error), operation="combat_start")
logger.debug("NATS message received", message_data=message_data,
             message_type=type(message_data))
```

**Why f-strings are forbidden:**
- **Breaks log aggregation**: Cannot search by specific fields
- **Prevents alerting**: Cannot create alerts based on structured data
- **Reduces performance**: String formatting is slower than structured data
- **Loses context**: Cannot correlate events across different log entries
- **Makes debugging harder**: Cannot filter or analyze logs effectively

## Best Practices

### ✅ CORRECT Usage Patterns

```python
# ✅ Structured logging with key-value pairs
logger.info("User action completed", user_id=user.id, action="login",
            success=True)

# ✅ Error logging with context
logger.error("Operation failed", operation="user_creation", error=str(e),
             retry_count=3)

# ✅ Performance logging
with measure_performance("database_query", user_id=user.id):
    result = database.query("SELECT * FROM players")

# ✅ Request context binding
bind_request_context(correlation_id=req_id, user_id=user.id,
                     session_id=session.id)
```

### ❌ FORBIDDEN Anti-Patterns

```python
# ❌ WRONG - F-string logging destroys structured logging
logger.info(f"User {user_id} performed {action}")
logger.error(f"Failed to process: {error}")
logger.debug(f"Message data: {message_data}")

# ❌ WRONG - Deprecated context parameter
logger.info("message", context={"key": "value"})

# ❌ WRONG - Unstructured messages
logger.info("Error occurred")

# ❌ WRONG - String formatting breaks structured logging
logger.info(f"Starting combat between {attacker} and {target}")
logger.error(f"Failed to process: {error}")
logger.debug(f"Message data: {message_data}")

# ❌ WRONG - Logging sensitive data
logger.info("Login attempt", username=user, password=password)
```

### Why F-Strings Are Forbidden

F-string logging destroys structured logging benefits:

- **Breaks log aggregation**: Cannot search by specific fields
- **Prevents alerting**: Cannot create alerts based on structured data
- **Reduces performance**: String formatting is slower than structured data
- **Loses context**: Cannot correlate events across different log entries
- **Makes debugging harder**: Cannot filter or analyze logs effectively

## Security Features

### Automatic Data Sanitization

The system automatically redacts sensitive information:

```python
# These fields are automatically sanitized:
# password, token, secret, key, credential, auth, jwt, api_key,
# private_key, session_token, access_token, refresh_token, bearer, authorization

logger.info("User login", username=user, password="secret123")  # password will be [REDACTED]
```

### Security Best Practices

1. **Never log sensitive data** - The sanitization helps, but avoid logging passwords, tokens, etc.
2. **Use appropriate log levels** - DEBUG for development, INFO for normal operations, ERROR for failures
3. **Include context** - Always provide enough context for debugging
4. **Use correlation IDs** - Bind request context for tracing

## Performance Features

### Async Logging

The system supports asynchronous logging for high-throughput scenarios:

```python
# Async logging is automatically enabled in production
logger.info("High-volume operation", operation="batch_processing", count=1000)
```

### Performance Monitoring

```python
from server.monitoring.performance_monitor import measure_performance

with measure_performance("database_query", user_id=user.id):
    result = database.query("SELECT * FROM players")
```

## Testing

### Unit Testing Logging

```python
import pytest
from unittest.mock import patch
from server.logging.enhanced_logging_config import get_logger

def test_logging_output():
    logger = get_logger("test.module")

    with patch('server.logging.enhanced_logging_config.structlog') as mock_structlog:
        logger.info("Test message", key="value")
        mock_structlog.get_logger.assert_called_with("test.module")
```

### Integration Testing

```python
def test_correlation_id_propagation():
    from server.logging.enhanced_logging_config import bind_request_context, get_current_context

    bind_request_context(correlation_id="test-123", user_id="user-456")
    context = get_current_context()

    assert context["correlation_id"] == "test-123"
    assert context["user_id"] == "user-456"
```

## Troubleshooting

### Common Issues

1. **Import Errors**: Always use `from server.logging.enhanced_logging_config import get_logger`
2. **Missing Context**: Bind request context with `bind_request_context()`
3. **Performance Issues**: Check if async logging is enabled
4. **Missing Logs**: Verify log level configuration

### Debug Mode

Enable debug logging for development:

```python
# In your environment configuration
LOGGING_LEVEL = "DEBUG"
```

### Log Rotation

Logs are automatically rotated based on size and time:

- **Size-based**: 10MB default, configurable
- **Time-based**: Daily rotation
- **Retention**: 5 backup files by default

## Migration Guide

### From Standard Logging

```python
# OLD - Standard Python logging
import logging
logger = logging.getLogger(__name__)
logger.info(f"User {user_id} performed {action}")

# NEW - Enhanced structured logging
from server.logging.enhanced_logging_config import get_logger
logger = get_logger(__name__)
logger.info("User action", user_id=user_id, action=action)
```

### From Deprecated Context Parameter

```python
# OLD - Deprecated context parameter
logger.info("message", context={"key": "value"})

# NEW - Direct key-value pairs
logger.info("message", key="value")
```

## Configuration

### Environment Variables

```bash
# Logging configuration
LOGGING_LEVEL=INFO
LOGGING_ENVIRONMENT=local
LOGGING_BASE=logs
LOGGING_ENABLE_ASYNC=true
```

### YAML Configuration

```yaml
logging:
  level: INFO
  environment: local
  log_base: logs
  enable_async: true
  rotation:
    max_size: 10MB
    backup_count: 5
```

## Monitoring and Alerting

### Log Aggregation

Logs are structured for easy aggregation with tools like:

- **ELK Stack** (Elasticsearch, Logstash, Kibana)
- **Splunk**
- **Grafana Loki**
- **CloudWatch Logs**

### Alerting Examples

```json
// Alert on high error rates
{
  "query": "level:ERROR",
  "threshold": "> 10 errors per minute",
  "action": "notify_ops_team"
}

// Alert on security violations
{
  "query": "security_violation:true",
  "threshold": "> 0",
  "action": "immediate_alert"
}
```

## API Reference

### Core Functions

- `get_logger(name)`: Get enhanced logger instance
- `bind_request_context(**kwargs)`: Bind request context
- `clear_request_context()`: Clear current context
- `get_current_context()`: Get current context
- `log_with_context(logger, level, message, **kwargs)`: Log with context

### Processors

- `sanitize_sensitive_data`: Security sanitization
- `add_correlation_id`: Correlation ID management
- `add_request_context`: Request context enhancement
- `enhance_player_ids`: Player GUID formatting

### Formatters

- `PlayerGuidFormatter`: Player GUID to name conversion

## Contributing

When adding new logging:

1. **Use structured logging** - Key-value pairs, not f-strings
2. **Include context** - User ID, operation, relevant metadata
3. **Choose appropriate level** - DEBUG, INFO, WARNING, ERROR, CRITICAL
4. **Test logging** - Verify output in development
5. **Document new patterns** - Update this guide

## References

- [Structlog Documentation](https://www.structlog.org/)
- [Python Logging Best Practices](https://docs.python.org/3/howto/logging.html)
- [Observability Patterns](https://microservices.io/patterns/observability/)
- [Security Logging Guidelines](https://owasp.org/www-project-logging-security-cheat-sheet/)

---

*As noted in the Pnakotic Manuscripts, proper documentation of our eldritch systems is essential for maintaining their stability. This enhanced logging system provides the foundation for comprehensive system monitoring and debugging, ensuring the continued observability of the MythosMUD server.*
