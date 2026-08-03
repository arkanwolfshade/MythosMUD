# retry nats handler

> 59 nodes

## Key Concepts

- **NATSRetryHandler** (42 connections) — `server/realtime/nats_retry_handler.py`
- **test_nats_retry_handler.py** (34 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **RetryableMessage** (13 connections) — `server/realtime/nats_retry_handler.py`
- **.should_retry()** (4 connections) — `server/realtime/nats_retry_handler.py`
- **test_should_retry_under_max()** (4 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **test_should_retry_at_max()** (4 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **test_should_retry_over_max()** (4 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **test_retry_async_increments_attempt()** (4 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **test_retry_async_calls_function()** (4 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **test_retry_async_waits_for_backoff()** (4 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **test_retry_async_zero_delay()** (4 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **test_nats_message_handler_init()** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
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
- **test_retry_with_backoff_no_sleep_after_last_attempt()** (3 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **test_update_config_valid_field()** (3 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- *... and 34 more nodes in this community*

## Relationships

- [commands communication support](commands_communication_support.md) (8 shared connections)
- [NATS Messaging](NATS_Messaging.md) (6 shared connections)
- [game chat moderation](game_chat_moderation.md) (6 shared connections)
- [nats message handler](nats_message_handler.md) (2 shared connections)
- [Memory Task Runtime](Memory_Task_Runtime.md) (1 shared connections)
- [realtime message filtering](realtime_message_filtering.md) (1 shared connections)
- [message nats handler](message_nats_handler.md) (1 shared connections)

## Source Files

- `server/realtime/nats_retry_handler.py`
- `server/tests/unit/realtime/test_nats_message_handler.py`
- `server/tests/unit/realtime/test_nats_retry_handler.py`

## Audit Trail

- EXTRACTED: 201 (98%)
- INFERRED: 4 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*