# NATS Retry Handler

> 53 nodes · cohesion 0.06

## Key Concepts

- **NATSRetryHandler** (41 connections) — `server/realtime/nats_retry_handler.py`
- **test_nats_retry_handler.py** (32 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **RetryableMessage** (13 connections) — `server/realtime/nats_retry_handler.py`
- **test_retry_async_calls_function()** (4 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **test_retry_async_increments_attempt()** (4 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **test_retry_async_waits_for_backoff()** (4 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **test_retry_async_zero_delay()** (4 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **test_should_retry_at_max()** (4 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **test_should_retry_over_max()** (4 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **test_should_retry_under_max()** (4 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **test_calculate_backoff_base()** (3 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **test_calculate_backoff_capped()** (3 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **test_calculate_backoff_exponential()** (3 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **test_calculate_backoff_non_negative()** (3 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **test_get_config()** (3 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **test_nats_retry_handler_init()** (3 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **test_nats_retry_handler_init_defaults()** (3 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **test_retry_with_backoff_all_retries_fail()** (3 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **test_retry_with_backoff_different_errors()** (3 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **test_retry_with_backoff_no_sleep_after_last_attempt()** (3 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **test_retry_with_backoff_preserves_exception_type()** (3 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **test_retry_with_backoff_success_after_retries()** (3 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **test_retry_with_backoff_success_first_attempt()** (3 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **test_retryable_message_init()** (3 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **test_update_config_invalid_field()** (3 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- *... and 28 more nodes in this community*

## Relationships

- [[Realtime Nats Retry]] (14 shared connections)
- [[NPC Admin API]] (3 shared connections)
- [[NATS Chat Broadcasting]] (3 shared connections)
- [[Services Rate Limiter]] (2 shared connections)
- [[Circuit Breaker Core]] (1 shared connections)
- [[NATS Message Handler Tests]] (1 shared connections)

## Source Files

- `server/realtime/nats_retry_handler.py`
- `server/tests/unit/realtime/test_nats_retry_handler.py`

## Audit Trail

- EXTRACTED: 189 (98%)
- INFERRED: 3 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
