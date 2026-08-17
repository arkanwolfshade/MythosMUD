# server realtime nats retry handler

> 86 nodes

## Key Concepts

- **NATSRetryHandler** (42 connections) — `server/realtime/nats_retry_handler.py`
- **test_nats_retry_handler.py** (35 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **RetryableMessage** (13 connections) — `server/realtime/nats_retry_handler.py`
- **asyncio** (13 connections)
- **RetryConfig** (10 connections) — `server/realtime/nats_retry_handler.py`
- **nats_retry_handler.py** (10 connections) — `server/realtime/nats_retry_handler.py`
- **.retry_async()** (5 connections) — `server/realtime/nats_retry_handler.py`
- **test_retry_async_calls_function()** (5 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **test_retry_async_increments_attempt()** (5 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **test_retry_async_waits_for_backoff()** (5 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **test_retry_async_zero_delay()** (5 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **test_should_retry_at_max()** (5 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **test_should_retry_over_max()** (5 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **test_should_retry_under_max()** (5 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **.calculate_backoff()** (4 connections) — `server/realtime/nats_retry_handler.py`
- **.should_retry()** (4 connections) — `server/realtime/nats_retry_handler.py`
- **test_get_config()** (4 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **test_retry_with_backoff_all_retries_fail()** (4 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **test_retry_with_backoff_different_errors()** (4 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **test_retry_with_backoff_no_sleep_after_last_attempt()** (4 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **test_retry_with_backoff_preserves_exception_type()** (4 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **test_retry_with_backoff_success_after_retries()** (4 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **test_retry_with_backoff_success_first_attempt()** (4 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **.get_config()** (3 connections) — `server/realtime/nats_retry_handler.py`
- **.get_retry_stats()** (3 connections) — `server/realtime/nats_retry_handler.py`
- *... and 61 more nodes in this community*

## Relationships

- [server realtime event handlers](server_realtime_event_handlers.md) (7 shared connections)
- [server tests unit realtime test](server_tests_unit_realtime_test.md) (3 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (3 shared connections)
- [characterinfo](characterinfo.md) (1 shared connections)

## Source Files

- `server/realtime/nats_retry_handler.py`
- `server/tests/unit/realtime/test_nats_retry_handler.py`

## Audit Trail

- EXTRACTED: 120 (75%)
- INFERRED: 39 (25%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*