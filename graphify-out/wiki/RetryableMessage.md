# RetryableMessage

> 15 nodes

## Key Concepts

- **RetryableMessage** (13 connections) — `server/realtime/nats_retry_handler.py`
- **test_retry_async_waits_for_backoff()** (5 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **test_retry_async_zero_delay()** (5 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **test_should_retry_at_max()** (5 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **test_should_retry_over_max()** (5 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **.should_retry()** (4 connections) — `server/realtime/nats_retry_handler.py`
- **test_retryable_message_init()** (3 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **Exception** (1 connections)
- **Determine if a message should be retried. Args: message: Message that failed…** (1 connections) — `server/realtime/nats_retry_handler.py`
- **Message that can be retried with tracking metadata. Stores message data along…** (1 connections) — `server/realtime/nats_retry_handler.py`
- **Test should_retry() returns False when at max retries.** (1 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **Test should_retry() returns False when over max retries.** (1 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **Test retry_async() requests backoff delay (sleep called with positive delay).** (1 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **Test retry_async() handles zero delay.** (1 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **Test RetryableMessage initialization.** (1 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`

## Relationships

- [test_nats_retry_handler.py](test_nats_retry_handler.py.md) (6 shared connections)
- [NATSRetryHandler](NATSRetryHandler.md) (6 shared connections)
- [asyncio](asyncio.md) (5 shared connections)
- [get_logger](get_logger.md) (1 shared connections)
- [test_retry_async_calls_function](test_retry_async_calls_function.md) (1 shared connections)
- [test_retry_async_increments_attempt](test_retry_async_increments_attempt.md) (1 shared connections)

## Source Files

- `server/realtime/nats_retry_handler.py`
- `server/tests/unit/realtime/test_nats_retry_handler.py`

## Audit Trail

- EXTRACTED: 22 (65%)
- INFERRED: 12 (35%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*