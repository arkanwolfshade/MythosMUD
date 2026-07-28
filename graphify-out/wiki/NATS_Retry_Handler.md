# NATS Retry Handler

> 61 nodes · cohesion 0.05

## Key Concepts

- **NATSRetryHandler** (40 connections) — `server/realtime/nats_retry_handler.py`
- **test_nats_retry_handler.py** (34 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **RetryableMessage** (13 connections) — `server/realtime/nats_retry_handler.py`
- **.should_retry()** (4 connections) — `server/realtime/nats_retry_handler.py`
- **test_get_config()** (4 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **test_retry_async_calls_function()** (4 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **test_retry_async_increments_attempt()** (4 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **test_retry_async_waits_for_backoff()** (4 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **test_retry_async_zero_delay()** (4 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **test_should_retry_at_max()** (4 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **test_should_retry_over_max()** (4 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **test_should_retry_under_max()** (4 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **test_nats_message_handler_init()** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_calculate_backoff_base()** (3 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **test_calculate_backoff_capped()** (3 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **test_calculate_backoff_exponential()** (3 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **test_calculate_backoff_non_negative()** (3 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **test_get_retry_stats()** (3 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **test_nats_retry_handler_init()** (3 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **test_nats_retry_handler_init_defaults()** (3 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **test_retry_with_backoff_all_retries_fail()** (3 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **test_retry_with_backoff_different_errors()** (3 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **test_retry_with_backoff_no_sleep_after_last_attempt()** (3 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **test_retry_with_backoff_preserves_exception_type()** (3 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **test_retry_with_backoff_success_after_retries()** (3 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- *... and 36 more nodes in this community*

## Relationships

- [Player Command Developer Guide](Player_Command_Developer_Guide.md) (7 shared connections)
- [E 2 E Di Migration](E_2_E_Di_Migration.md) (6 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (4 shared connections)
- [Base Command Models](Base_Command_Models.md) (2 shared connections)
- [Connection Disconnection Cleanup](Connection_Disconnection_Cleanup.md) (1 shared connections)
- [NATS Chat Broadcasting](NATS_Chat_Broadcasting.md) (1 shared connections)
- [Character Creation E2E](Character_Creation_E2E.md) (1 shared connections)

## Source Files

- `server/realtime/nats_retry_handler.py`
- `server/tests/unit/realtime/test_nats_message_handler.py`
- `server/tests/unit/realtime/test_nats_retry_handler.py`

## Audit Trail

- EXTRACTED: 204 (98%)
- INFERRED: 4 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*