# Enhanced Logging Quick Reference

## One-page cheat sheet for MythosMUD enhanced logging patterns

## 🚨 CRITICAL: DO NOT USE

```python
# ❌ FORBIDDEN - Will cause failures

import logging
logger = logging.getLogger(__name__)

# ❌ FORBIDDEN - Deprecated context parameter

logger.info("message", context={"key": "value"})

# ❌ FORBIDDEN - String formatting

logger.info(f"User {user_id} performed {action}")

# ❌ FORBIDDEN - Logging sensitive data

logger.info("Login", username=user, password=password)
```

## ✅ MANDATORY: ALWAYS USE

```python
# ✅ REQUIRED - Enhanced logging import

from server.structured_logging.enhanced_logging_config import get_logger
logger = get_logger(__name__)

# ✅ REQUIRED - Structured logging

logger.info("User action completed", user_id=user.id, action="login", success=True)

# ✅ REQUIRED - Error logging with context

logger.error("Operation failed", operation="user_creation", error=str(e), retry_count=3)

# ✅ REQUIRED - Performance logging

with measure_performance("database_query", user_id=user.id):
    result = database.query("SELECT * FROM players")

# ✅ REQUIRED - Request context binding

bind_request_context(correlation_id=req_id, user_id=user.id, session_id=session.id)
```

## Log Levels

| Level      | Usage                             | Example                                                                                  |
| ---------- | --------------------------------- | ---------------------------------------------------------------------------------------- |
| `DEBUG`    | Detailed diagnostic info          | `logger.debug("Processing item", item_id=item.id, batch_size=len(items))`                |
| `INFO`     | General system operation          | `logger.info("User logged in", user_id=user.id, login_method="password")`                |
| `WARNING`  | Potentially harmful situations    | `logger.warning("High memory usage", memory_percent=85.5, threshold=80.0)`               |
| `ERROR`    | Error events (recoverable)        | `logger.error("Database connection failed", retry_count=3, error=str(e))`                |
| `CRITICAL` | Very severe errors (system abort) | `logger.critical("Memory allocation failed", requested_bytes=size, available=available)` |

## Common Patterns

### User Actions

```python
logger.info("User action performed", user_id=user.id, action="move", direction="north", room_id=room.id)
```

### API Requests

```python
logger.info("API request", method=request.method, path=request.url.path, user_id=user.id, status_code=200)
```

### Database Operations

```python
logger.debug("Database query executed", query=query, duration_ms=duration*1000, rows_affected=count)
```

### Errors with Context

```python
logger.error("Operation failed", operation="user_creation", user_id=user.id, error=str(e), retry_count=retry_count)
```

### Performance Monitoring

```python
with measure_performance("player_movement", user_id=user.id, direction=direction):
    movement_service.move_player(player, direction)
```

## Context Binding

### Request Context

```python
bind_request_context(
    correlation_id=str(uuid.uuid4()),
    user_id=current_user.id,
    session_id=session.id,
    request_id=str(request.url)
)
```

### Clear Context

```python
clear_request_context()
```

## Security Features

**Automatic Sanitization**: Sensitive data automatically redacted

**MDC Support**: Context automatically included in all logs

**Correlation IDs**: Request tracing across services

**Performance Monitoring**: Built-in metrics collection

## Quick Fixes

| Problem                                        | Fix                                                                 |
| ---------------------------------------------- | ------------------------------------------------------------------- |
| `ImportError: cannot import name 'get_logger'` | Use `from server.logging.enhanced_logging_config import get_logger` |
| `TypeError: context parameter`                 | Remove `context=` and use direct key-value pairs                    |
| Logs not appearing                             | Check log levels and configuration                                  |
| Sensitive data in logs                         | Enhanced logging automatically sanitizes                            |

## Validation Checklist

[ ] Uses enhanced logging import

- [ ] No `import logging` statements
- [ ] No `context={"key": "value"}` parameters
- [ ] No string formatting in log messages
- [ ] All logs use structured key-value pairs
- [ ] Appropriate log levels used
- [ ] Error logs include sufficient context

---

### For complete documentation, see [ENHANCED_LOGGING_GUIDE.md](ENHANCED_LOGGING_GUIDE.md)
