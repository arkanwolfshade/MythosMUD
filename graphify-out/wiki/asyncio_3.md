# asyncio

> 15 nodes

## Key Concepts

- **asyncio** (13 connections)
- **test_should_retry_under_max()** (5 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **test_retry_with_backoff_all_retries_fail()** (4 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **test_retry_with_backoff_different_errors()** (4 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **test_retry_with_backoff_no_sleep_after_last_attempt()** (4 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **test_retry_with_backoff_preserves_exception_type()** (4 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **test_retry_with_backoff_success_after_retries()** (4 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **test_retry_with_backoff_success_first_attempt()** (4 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **Test should_retry() returns True when under max retries.** (1 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **Test retry_with_backoff() succeeds on first attempt.** (1 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **Test retry_with_backoff() succeeds after retries.** (1 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **Test retry_with_backoff() returns False when all retries fail.** (1 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **Test retry_with_backoff() doesn't sleep after last attempt.** (1 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **Test retry_with_backoff() preserves exception type.** (1 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **Test retry_with_backoff() handles different error types.** (1 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`

## Relationships

- [test_nats_retry_handler.py](test_nats_retry_handler.py.md) (7 shared connections)
- [NATSRetryHandler](NATSRetryHandler.md) (7 shared connections)
- [RetryableMessage](RetryableMessage.md) (5 shared connections)
- [test_retry_async_calls_function](test_retry_async_calls_function.md) (1 shared connections)
- [test_retry_async_increments_attempt](test_retry_async_increments_attempt.md) (1 shared connections)

## Source Files

- `server/tests/unit/realtime/test_nats_retry_handler.py`

## Audit Trail

- EXTRACTED: 27 (77%)
- INFERRED: 8 (23%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*