---
name: mythosmud-logging-standards
description: Use MythosMUD logging: get_logger from server.logging.enhanced_logging_config, structured key=value args, no f-strings or context= parameter. Use when adding or editing Python logging, or when the user mentions logs or logging.
---

# MythosMUD Logging Standards

## Import

Always use the project logger:

```python
from server.logging.enhanced_logging_config import get_logger
logger = get_logger(__name__)
```

**Never** use `import logging` or `logging.getLogger()`.

## Structured Logging

Pass data as **keyword arguments** (key=value). Do not use f-strings or the deprecated `context=` parameter.

**Correct:**

```python
logger.info("User action completed", user_id=user.id, action="login", success=True)
logger.error("Request failed", path=request.url.path, status_code=500)
```

**Wrong:**

```python
logger.info(f"User {user_id} performed {action}")  # No f-strings
logger.info("message", context={"key": "value"})  # No context= parameter
```

## Optional Helpers

- **Request context:** `bind_request_context(correlation_id=id, user_id=uid)` when handling requests.
- **Performance:** `with measure_performance("operation"):` for timing blocks.

Import these from `server.logging.enhanced_logging_config` when needed.

## Summary

| Do | Do not |
|----|--------|
| `get_logger(__name__)` | `logging.getLogger()` |
| `logger.info("msg", key=value)` | `logger.info(f"msg {x}")` |
| Key-value args | `context={"key": "value"}` |

## Reference

- Full rules: [CLAUDE.md](../../CLAUDE.md) "LOGGING STANDARDS" and "Example Patterns"
