# Vim Editor Guidelines

> 84 nodes

## Key Concepts

- **NATSRetryHandler** (40 connections) — `server/realtime/nats_retry_handler.py`
- **test_nats_retry_handler.py** (34 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **RetryableMessage** (13 connections) — `server/realtime/nats_retry_handler.py`
- **RetryConfig** (10 connections) — `server/realtime/nats_retry_handler.py`
- **.retry_async()** (5 connections) — `server/realtime/nats_retry_handler.py`
- **.calculate_backoff()** (4 connections) — `server/realtime/nats_retry_handler.py`
- **.should_retry()** (4 connections) — `server/realtime/nats_retry_handler.py`
- **Any** (4 connections)
- **.retry_with_backoff()** (4 connections) — `server/realtime/nats_retry_handler.py`
- **test_should_retry_under_max()** (4 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **test_should_retry_at_max()** (4 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **test_should_retry_over_max()** (4 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **test_retry_async_increments_attempt()** (4 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **test_retry_async_calls_function()** (4 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **test_retry_async_waits_for_backoff()** (4 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **test_retry_async_zero_delay()** (4 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **test_get_config()** (4 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **.__init__()** (3 connections) — `server/realtime/nats_retry_handler.py`
- **.get_retry_stats()** (3 connections) — `server/realtime/nats_retry_handler.py`
- **.get_config()** (3 connections) — `server/realtime/nats_retry_handler.py`
- **.update_config()** (3 connections) — `server/realtime/nats_retry_handler.py`
- **test_retry_config_calculate_delay_base()** (3 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **test_retry_config_calculate_delay_capped()** (3 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **test_retry_config_defaults()** (3 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **test_retryable_message_init()** (3 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- *... and 59 more nodes in this community*

## Relationships

- [Client Event Store](Client_Event_Store.md) (5 shared connections)
- [NATS Chat Broadcasting](NATS_Chat_Broadcasting.md) (1 shared connections)
- [Test Optimization Insights](Test_Optimization_Insights.md) (1 shared connections)
- [SQLAlchemy Model Base](SQLAlchemy_Model_Base.md) (1 shared connections)
- [Lucidity Utc Now](Lucidity_Utc_Now.md) (1 shared connections)
- [Communication Command Flows](Communication_Command_Flows.md) (1 shared connections)

## Source Files

- `server/realtime/nats_retry_handler.py`
- `server/tests/unit/realtime/test_nats_retry_handler.py`

## Audit Trail

- EXTRACTED: 262 (98%)
- INFERRED: 4 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*