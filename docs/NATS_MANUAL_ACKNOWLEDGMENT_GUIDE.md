# NATS Manual Acknowledgment Guide

**Date**: 2026-01-13
**Purpose**: Guide for when to use manual vs automatic message acknowledgment in NATS

## Overview

NATS supports two acknowledgment modes for message delivery:

1. **Automatic Acknowledgment** (default): Messages are automatically acknowledged when the handler callback returns
2. **Manual Acknowledgment**: Messages must be explicitly acknowledged (`msg.ack()`) or negatively acknowledged (`msg.nak()`)

## Current Configuration

Manual acknowledgment is **disabled by default** in MythosMUD's NATS implementation. This can be enabled via configuration:

```python
# In NATSConfig
manual_ack: bool = Field(default=False, description="Enable manual message acknowledgment (ack/nak)")
```

## When to Use Manual Acknowledgment

### Use Manual Ack For:

1. **Critical Messages** - Messages that must not be lost if processing fails
   - Player state updates
   - Financial transactions
   - Persistent game state changes
   - Admin commands

2. **Long-Running Processing** - Messages that take significant time to process
   - Complex calculations
   - Database operations that may fail
   - External API calls

3. **At-Least-Once Delivery** - When you need guaranteed delivery semantics
   - Messages that can be safely reprocessed (idempotent operations)
   - Messages where duplicates are acceptable

4. **Error Recovery** - When you want to retry failed messages
   - Use `msg.nak()` to requeue messages for retry
   - Allows for custom retry logic

### Use Automatic Ack For:

1. **High-Throughput Messages** - Messages that are processed quickly
   - Chat messages
   - Real-time events
   - Non-critical notifications

2. **Fire-and-Forget Operations** - Messages where loss is acceptable
   - Metrics/telemetry
   - Logging events
   - Best-effort notifications

3. **Simple Handlers** - Handlers that rarely fail
   - Simple data transformations
   - Cache updates
   - Stateless operations

## Implementation Details

### Enabling Manual Acknowledgment

```python
# In configuration
nats_config = NATSConfig(
    manual_ack=True,  # Enable manual acknowledgment
    # ... other config
)

# Or via environment variable
NATS_MANUAL_ACK=true
```

### How It Works

When `manual_ack=True`:

1. **Message Handler**: The handler receives the raw NATS message object
2. **Processing**: Your handler processes the message
3. **Acknowledgment**: You must call `msg.ack()` after successful processing
4. **Negative Acknowledgment**: Call `msg.nak()` if processing fails (requeues message)

**Example**:

```python
async def message_handler(msg: Any) -> None:
    try:
        message_data = await decode_message(msg)
        await process_critical_operation(message_data)
        # Explicitly acknowledge after successful processing
        await msg.ack()
    except Exception as e:
        # Negatively acknowledge to requeue for retry
        await msg.nak()
        logger.error("Failed to process message", error=str(e))
```

### Automatic Acknowledgment (Default)

When `manual_ack=False` (default):

1. **Message Handler**: Handler receives decoded message data (dict)
2. **Processing**: Your handler processes the message
3. **Automatic Ack**: NATS automatically acknowledges when handler returns successfully
4. **No Retry**: Failed messages are not automatically requeued

**Example**:

```python
async def message_handler(message_data: dict[str, Any]) -> None:
    # Process message - automatically acknowledged on return
    await process_message(message_data)
    # No need to call ack() - handled automatically
```

## Performance Considerations

### Manual Acknowledgment

- **Pros**:
  - Better reliability for critical messages
  - Allows retry logic via `nak()`
  - Prevents message loss on handler failures

- **Cons**:
  - Slightly higher overhead (explicit ack calls)
  - Requires careful error handling (must ack or nak)
  - Risk of message loss if handler crashes before ack

### Automatic Acknowledgment

- **Pros**:
  - Lower overhead
  - Simpler handler code
  - Better for high-throughput scenarios

- **Cons**:
  - Messages may be lost if handler fails after processing
  - No built-in retry mechanism
  - Less control over message lifecycle

## Best Practices

### 1. Use Manual Ack for Critical Paths

```python
# Critical: Player state update
async def handle_player_state_update(msg: Any) -> None:
    try:
        state = await decode_state(msg)
        await persist_player_state(state)
        await msg.ack()  # Only ack after persistence succeeds
    except Exception:
        await msg.nak()  # Requeue for retry
```

### 2. Use Automatic Ack for Non-Critical Messages

```python
# Non-critical: Chat message
async def handle_chat_message(message_data: dict[str, Any]) -> None:
    await broadcast_to_clients(message_data)
    # Automatically acknowledged on return
```

### 3. Handle Errors Properly

```python
# Always ack or nak in manual mode
async def handle_with_manual_ack(msg: Any) -> None:
    try:
        await process_message(msg)
        await msg.ack()
    except RecoverableError:
        await msg.nak()  # Retry
    except FatalError:
        await msg.ack()  # Don't retry fatal errors
        logger.error("Fatal error, message acknowledged to prevent retry loop")
```

### 4. Consider Idempotency

When using manual ack with retries, ensure handlers are idempotent:

```python
async def handle_idempotent_operation(msg: Any) -> None:
    message_id = extract_message_id(msg)

    # Check if already processed
    if await is_already_processed(message_id):
        await msg.ack()  # Already done, just ack
        return

    # Process and mark as processed
    await process_operation(msg)
    await mark_as_processed(message_id)
    await msg.ack()
```

## Configuration Recommendations

### Production (High Reliability)

```python
NATS_MANUAL_ACK=true  # Enable for critical messages
```

### Development/Testing

```python
NATS_MANUAL_ACK=false  # Simpler for development
```

### Mixed Mode (Future Enhancement)

Consider implementing per-subject acknowledgment configuration:

```python
# Subscribe with manual ack for critical subjects
await nats_service.subscribe("critical.*", handler, manual_ack=True)

# Subscribe with auto ack for non-critical subjects
await nats_service.subscribe("chat.*", handler, manual_ack=False)
```

## Migration Path

If you want to enable manual ack for existing handlers:

1. **Update Handlers**: Change signature from `(message_data: dict)` to `(msg: Any)`
2. **Add Ack Calls**: Add `await msg.ack()` after successful processing
3. **Add Nak Calls**: Add `await msg.nak()` for retryable failures
4. **Test Thoroughly**: Ensure no messages are lost or duplicated
5. **Monitor**: Watch for acknowledgment failures in metrics

## Monitoring

When manual ack is enabled, monitor:

- **Acknowledgment Failures**: Messages that fail to ack/nak
- **Retry Rates**: Frequency of `nak()` calls
- **Message Loss**: Messages that timeout without ack
- **Processing Time**: Time between message receipt and ack

## Conclusion

- **Default (Auto Ack)**: Best for most use cases - simple, fast, good for high-throughput
- **Manual Ack**: Use for critical messages requiring guaranteed delivery
- **Decision Factor**: Consider message criticality, processing time, and error recovery needs

For MythosMUD's current implementation, automatic acknowledgment is appropriate for most chat and event messages. Consider enabling manual ack for:
- Player state persistence
- Financial transactions
- Admin commands
- Critical game state changes

---

**Status**: Documentation Complete
**Last Updated**: 2026-01-13
