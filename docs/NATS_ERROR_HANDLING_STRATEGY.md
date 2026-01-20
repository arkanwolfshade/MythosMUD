# NATS Error Handling Strategy

**Date**: 2026-01-13
**Purpose**: Guidelines for consistent error handling in NATS operations

## Overview

MythosMUD's NATS implementation uses a **standardized exception-based error handling strategy**. All NATS operations raise specific exception types instead of returning error codes or `None`, enabling precise error handling and better debugging.

## Exception Hierarchy

All NATS exceptions inherit from `NATSError`:

```
NATSError (base)
├── NATSConnectionError
├── NATSPublishError
├── NATSSubscribeError
├── NATSUnsubscribeError
├── NATSRequestError
└── NATSHealthCheckError
```

### Exception Types

#### `NATSError`
Base exception for all NATS-related errors. Catch this for general NATS error handling.

#### `NATSConnectionError`
Raised when connection operations fail.

**Attributes**:
- `url`: NATS server URL (if available)
- `original_error`: Underlying exception

**Example**:
```python
try:
    await nats_service.connect()
except NATSConnectionError as e:
    logger.error("Failed to connect", url=e.url, error=e.original_error)
```

#### `NATSPublishError`
Raised when message publishing fails.

**Attributes**:
- `subject`: Subject that failed to publish
- `original_error`: Underlying exception

**Example**:
```python
try:
    await nats_service.publish("chat.say.room.arkham_1", message_data)
except NATSPublishError as e:
    logger.error("Publish failed", subject=e.subject, error=e.original_error)
```

#### `NATSSubscribeError`
Raised when subscription operations fail.

**Attributes**:
- `subject`: Subject that failed to subscribe
- `original_error`: Underlying exception

**Example**:
```python
try:
    await nats_service.subscribe("chat.say.*", handler)
except NATSSubscribeError as e:
    logger.error("Subscribe failed", subject=e.subject, error=e.original_error)
```

#### `NATSUnsubscribeError`
Raised when unsubscribe operations fail.

**Attributes**:
- `subject`: Subject that failed to unsubscribe
- `original_error`: Underlying exception

**Example**:
```python
try:
    await nats_service.unsubscribe("chat.say.room.arkham_1")
except NATSUnsubscribeError as e:
    logger.error("Unsubscribe failed", subject=e.subject, error=e.original_error)
```

#### `NATSRequestError`
Raised when request/response operations fail.

**Attributes**:
- `subject`: Subject that failed
- `timeout`: Timeout value (if timeout occurred)
- `original_error`: Underlying exception

**Example**:
```python
try:
    response = await nats_service.request("service.status", {"query": "health"})
except NATSRequestError as e:
    if e.timeout:
        logger.warning("Request timed out", subject=e.subject, timeout=e.timeout)
    else:
        logger.error("Request failed", subject=e.subject, error=e.original_error)
```

#### `NATSHealthCheckError`
Raised when health check operations fail.

**Attributes**:
- `consecutive_failures`: Number of consecutive failures

## Error Handling Patterns

### Pattern 1: Let Exceptions Propagate

For operations where failure should stop execution:

```python
# Let exception propagate to caller
async def send_critical_message(message_data: dict[str, Any]) -> None:
    await nats_service.publish("critical.events", message_data)
    # If publish fails, exception propagates - caller handles it
```

### Pattern 2: Catch and Log

For operations where failure should be logged but not stop execution:

```python
async def send_optional_notification(message_data: dict[str, Any]) -> None:
    try:
        await nats_service.publish("notifications.optional", message_data)
    except NATSPublishError as e:
        logger.warning("Failed to send optional notification", error=str(e))
        # Continue execution - notification is optional
```

### Pattern 3: Catch and Retry

For operations that should be retried on failure:

```python
async def send_with_retry(message_data: dict[str, Any], max_retries: int = 3) -> bool:
    for attempt in range(max_retries):
        try:
            await nats_service.publish("important.events", message_data)
            return True
        except NATSPublishError as e:
            if attempt < max_retries - 1:
                await asyncio.sleep(2 ** attempt)  # Exponential backoff
                continue
            logger.error("Failed after retries", error=str(e), attempts=max_retries)
            return False
    return False
```

### Pattern 4: Catch Specific Exceptions

For operations requiring different handling per error type:

```python
async def handle_nats_operation() -> None:
    try:
        await nats_service.publish("events.test", {"data": "test"})
    except NATSConnectionError:
        # Connection issue - may need to reconnect
        logger.error("Connection error - may need to reconnect")
        await handle_connection_loss()
    except NATSPublishError as e:
        # Publish-specific error - log and continue
        logger.error("Publish error", subject=e.subject, error=str(e))
    except NATSError:
        # Other NATS errors - generic handling
        logger.error("NATS error occurred")
```

### Pattern 5: Catch All NATS Errors

For operations where any NATS error should be handled uniformly:

```python
async def safe_nats_operation() -> None:
    try:
        await nats_service.publish("events.test", {"data": "test"})
        await nats_service.subscribe("events.*", handler)
    except NATSError as e:
        # Handle any NATS error
        logger.error("NATS operation failed", error=str(e), error_type=type(e).__name__)
        # Add to dead letter queue or retry queue
```

## Best Practices

### 1. Always Handle Exceptions

Never let NATS exceptions propagate unhandled in production code:

```python
# ❌ Bad: Exception may crash application
async def handler():
    await nats_service.publish("events.test", data)

# ✅ Good: Exception handled
async def handler():
    try:
        await nats_service.publish("events.test", data)
    except NATSPublishError as e:
        logger.error("Publish failed", error=str(e))
```

### 2. Use Specific Exception Types

Catch specific exceptions when you need different handling:

```python
# ✅ Good: Specific handling
try:
    await nats_service.publish(subject, data)
except NATSPublishError:
    # Handle publish errors
    pass
except NATSConnectionError:
    # Handle connection errors differently
    pass
```

### 3. Preserve Exception Context

Always use `from e` when re-raising or wrapping exceptions:

```python
# ✅ Good: Preserves context
try:
    await nats_service.publish(subject, data)
except NATSPublishError as e:
    raise MyCustomError("Failed to publish") from e
```

### 4. Log with Context

Include exception attributes in logs:

```python
# ✅ Good: Rich context
try:
    await nats_service.publish(subject, data)
except NATSPublishError as e:
    logger.error(
        "Publish failed",
        subject=e.subject,
        error=str(e),
        original_error=str(e.original_error) if e.original_error else None,
    )
```

### 5. Don't Swallow Exceptions

Avoid catching exceptions without logging or handling:

```python
# ❌ Bad: Exception swallowed
try:
    await nats_service.publish(subject, data)
except NATSPublishError:
    pass  # Silent failure

# ✅ Good: Exception logged or handled
try:
    await nats_service.publish(subject, data)
except NATSPublishError as e:
    logger.warning("Publish failed, continuing", error=str(e))
```

## Error Recovery Strategies

### Connection Errors

```python
async def publish_with_reconnect(subject: str, data: dict[str, Any]) -> bool:
    try:
        await nats_service.publish(subject, data)
        return True
    except NATSConnectionError:
        # Attempt reconnection
        if await nats_service.connect():
            try:
                await nats_service.publish(subject, data)
                return True
            except NATSPublishError:
                return False
        return False
```

### Publish Errors

```python
async def publish_with_fallback(subject: str, data: dict[str, Any]) -> bool:
    try:
        await nats_service.publish(subject, data)
        return True
    except NATSPublishError as e:
        # Add to retry queue or dead letter queue
        await add_to_retry_queue(subject, data, error=str(e))
        return False
```

### Request/Response Errors

```python
async def request_with_fallback(subject: str, data: dict[str, Any]) -> dict[str, Any] | None:
    try:
        return await nats_service.request(subject, data, timeout=5.0)
    except NATSRequestError as e:
        if e.timeout:
            # Timeout - may want to retry with longer timeout
            logger.warning("Request timeout", subject=subject)
        else:
            # Other error - log and return None
            logger.error("Request failed", subject=subject, error=str(e))
        return None
```

## Integration with Error Boundaries

The NATS message handler uses error boundaries (retry handler, circuit breaker, DLQ):

```python
# In NATSMessageHandler
async def _handle_nats_message(self, message_data: dict[str, Any]):
    try:
        # Process through circuit breaker
        await self.circuit_breaker.call(self._process_message_with_retry, message_data)
    except CircuitBreakerOpen:
        # Circuit open - add to DLQ immediately
        self.dead_letter_queue.enqueue(message_data, error="circuit_open")
    except NATSError as e:
        # NATS-specific errors - add to DLQ
        self.dead_letter_queue.enqueue(message_data, error=str(e))
```

## Testing Error Handling

### Test Exception Raising

```python
async def test_publish_raises_exception():
    with pytest.raises(NATSPublishError):
        await nats_service.publish("invalid.subject", {})
```

### Test Exception Attributes

```python
async def test_publish_exception_attributes():
    with pytest.raises(NATSPublishError) as exc_info:
        await nats_service.publish("test.subject", {})

    assert exc_info.value.subject == "test.subject"
    assert exc_info.value.original_error is not None
```

## Migration Guide

### From Return-Value Pattern

**Before**:
```python
# Old pattern: Return False on error
success = await nats_service.publish(subject, data)
if not success:
    logger.error("Publish failed")
```

**After**:
```python
# New pattern: Catch exceptions
try:
    await nats_service.publish(subject, data)
except NATSPublishError as e:
    logger.error("Publish failed", subject=e.subject, error=str(e))
```

### From None Return Pattern

**Before**:
```python
# Old pattern: Return None on error
response = await nats_service.request(subject, data)
if response is None:
    logger.error("Request failed")
```

**After**:
```python
# New pattern: Catch exceptions
try:
    response = await nats_service.request(subject, data)
except NATSRequestError as e:
    logger.error("Request failed", subject=e.subject, error=str(e))
    response = None
```

## Summary

- **Always use exceptions** - Never return error codes or `None`
- **Catch specific exceptions** - Use specific types when different handling is needed
- **Preserve context** - Use `from e` when re-raising
- **Log with context** - Include exception attributes in logs
- **Handle appropriately** - Don't swallow exceptions, but don't let them crash the app
- **Use error boundaries** - Leverage retry handler, circuit breaker, and DLQ

---

**Status**: Documentation Complete
**Last Updated**: 2026-01-13
