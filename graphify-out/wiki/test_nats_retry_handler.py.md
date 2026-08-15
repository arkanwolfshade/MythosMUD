# test_nats_retry_handler.py

> 22 nodes

## Key Concepts

- **test_nats_retry_handler.py** (34 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **test_calculate_backoff_base()** (3 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **test_calculate_backoff_capped()** (3 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **test_calculate_backoff_exponential()** (3 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **test_calculate_backoff_non_negative()** (3 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **test_get_retry_stats()** (3 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **test_nats_retry_handler_init()** (3 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **test_nats_retry_handler_init_defaults()** (3 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **test_update_config_invalid_field()** (3 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **test_update_config_multiple_fields()** (3 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **test_update_config_valid_field()** (3 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **Unit tests for NATS retry handler. Tests the NATSRetryHandler class and related…** (1 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **Test get_retry_stats() returns correct statistics.** (1 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **Test update_config() updates valid field.** (1 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **Test update_config() updates multiple fields.** (1 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **Test update_config() ignores invalid field.** (1 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **Test NATSRetryHandler initialization.** (1 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **Test NATSRetryHandler default values.** (1 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **Test calculate_backoff() with base attempt.** (1 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **Test calculate_backoff() with exponential growth.** (1 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **Test calculate_backoff() respects max_delay.** (1 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **Test calculate_backoff() never returns negative.** (1 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`

## Relationships

- [NATSRetryHandler](NATSRetryHandler.md) (11 shared connections)
- [asyncio](asyncio.md) (7 shared connections)
- [RetryableMessage](RetryableMessage.md) (6 shared connections)
- [RetryConfig](RetryConfig.md) (5 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [test_retry_async_increments_attempt](test_retry_async_increments_attempt.md) (1 shared connections)
- [test_retry_async_calls_function](test_retry_async_calls_function.md) (1 shared connections)

## Source Files

- `server/tests/unit/realtime/test_nats_retry_handler.py`

## Audit Trail

- EXTRACTED: 44 (81%)
- INFERRED: 10 (19%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*