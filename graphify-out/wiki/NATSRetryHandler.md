# NATSRetryHandler

> 87 nodes

## Key Concepts

- **NATSRetryHandler** (39 connections) — `server/realtime/nats_retry_handler.py`
- **test_nats_retry_handler.py** (34 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **RetryableMessage** (13 connections) — `server/realtime/nats_retry_handler.py`
- **asyncio** (13 connections)
- **RetryConfig** (9 connections) — `server/realtime/nats_retry_handler.py`
- **nats_retry_handler.py** (9 connections) — `server/realtime/nats_retry_handler.py`
- **.retry_async()** (5 connections) — `server/realtime/nats_retry_handler.py`
- **test_retry_async_calls_function()** (5 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **test_retry_async_increments_attempt()** (5 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **test_retry_async_waits_for_backoff()** (5 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **test_retry_async_zero_delay()** (5 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **test_should_retry_at_max()** (5 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **test_should_retry_over_max()** (5 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **test_should_retry_under_max()** (5 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **.calculate_backoff()** (4 connections) — `server/realtime/nats_retry_handler.py`
- **.retry_with_backoff()** (4 connections) — `server/realtime/nats_retry_handler.py`
- **.should_retry()** (4 connections) — `server/realtime/nats_retry_handler.py`
- **test_retry_with_backoff_all_retries_fail()** (4 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **test_retry_with_backoff_different_errors()** (4 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **test_retry_with_backoff_no_sleep_after_last_attempt()** (4 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **test_retry_with_backoff_preserves_exception_type()** (4 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **test_retry_with_backoff_success_after_retries()** (4 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **test_retry_with_backoff_success_first_attempt()** (4 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **Any** (4 connections)
- **.get_config()** (3 connections) — `server/realtime/nats_retry_handler.py`
- *... and 62 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (3 shared connections)
- [build_event](build_event.md) (2 shared connections)
- [test_nats_message_handler.py](test_nats_message_handler.py.md) (2 shared connections)
- [MessageFilteringHelper](MessageFilteringHelper.md) (1 shared connections)
- [NATSMessageHandler](NATSMessageHandler.md) (1 shared connections)

## Source Files

- `server/realtime/nats_retry_handler.py`
- `server/tests/unit/realtime/test_nats_retry_handler.py`

## Audit Trail

- EXTRACTED: 153 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*