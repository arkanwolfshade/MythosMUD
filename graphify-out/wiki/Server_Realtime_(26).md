# Server Realtime (26)

> 62 nodes

## Key Concepts

- **NATSRetryHandler** (38 connections) — `server/realtime/nats_retry_handler.py`
- **test_nats_retry_handler.py** (34 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **RetryableMessage** (13 connections) — `server/realtime/nats_retry_handler.py`
- **nats_retry_handler.py** (9 connections) — `server/realtime/nats_retry_handler.py`
- **.retry_async()** (5 connections) — `server/realtime/nats_retry_handler.py`
- **.should_retry()** (4 connections) — `server/realtime/nats_retry_handler.py`
- **test_should_retry_under_max()** (4 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **test_should_retry_at_max()** (4 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **test_should_retry_over_max()** (4 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **test_retry_async_increments_attempt()** (4 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **test_retry_async_calls_function()** (4 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **test_retry_async_waits_for_backoff()** (4 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **test_retry_async_zero_delay()** (4 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **test_get_config()** (4 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **test_retryable_message_init()** (3 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **test_nats_retry_handler_init()** (3 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **test_nats_retry_handler_init_defaults()** (3 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **test_calculate_backoff_base()** (3 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **test_calculate_backoff_exponential()** (3 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **test_calculate_backoff_capped()** (3 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **test_calculate_backoff_non_negative()** (3 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **test_get_retry_stats()** (3 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **test_retry_with_backoff_success_first_attempt()** (3 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **test_retry_with_backoff_success_after_retries()** (3 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **test_retry_with_backoff_all_retries_fail()** (3 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- *... and 37 more nodes in this community*

## Relationships

- [Server Realtime (91)](Server_Realtime_%2891%29.md) (8 shared connections)
- [Server Realtime (108)](Server_Realtime_%28108%29.md) (6 shared connections)
- [Server Realtime](Server_Realtime.md) (4 shared connections)
- [Server Commands](Server_Commands.md) (3 shared connections)
- [Server Realtime (11)](Server_Realtime_%2811%29.md) (1 shared connections)

## Source Files

- `server/realtime/nats_retry_handler.py`
- `server/tests/unit/realtime/test_nats_retry_handler.py`

## Audit Trail

- EXTRACTED: 216 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*