# Player Command Developer Guide

> 14 nodes · cohesion 0.14

## Key Concepts

- **RetryConfig** (10 connections) — `server/realtime/nats_retry_handler.py`
- **.get_config()** (3 connections) — `server/realtime/nats_retry_handler.py`
- **.__init__()** (3 connections) — `server/realtime/nats_retry_handler.py`
- **test_retry_config_calculate_delay_base()** (3 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **test_retry_config_calculate_delay_capped()** (3 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **test_retry_config_defaults()** (3 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **.calculate_delay()** (2 connections) — `server/realtime/nats_retry_handler.py`
- **Get current retry configuration.          Returns:             Current RetryConf** (1 connections) — `server/realtime/nats_retry_handler.py`
- **Configuration for retry behavior.      Defines retry parameters for handling tra** (1 connections) — `server/realtime/nats_retry_handler.py`
- **Calculate delay for a given attempt number.          Uses exponential backoff ca** (1 connections) — `server/realtime/nats_retry_handler.py`
- **Initialize retry handler.          Args:             max_retries: Maximum number** (1 connections) — `server/realtime/nats_retry_handler.py`
- **Test RetryConfig.calculate_delay() with base delay.** (1 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **Test RetryConfig.calculate_delay() respects max_delay.** (1 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **Test RetryConfig default values.** (1 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`

## Relationships

- [NATS Retry Handler](NATS_Retry_Handler.md) (7 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (1 shared connections)

## Source Files

- `server/realtime/nats_retry_handler.py`
- `server/tests/unit/realtime/test_nats_retry_handler.py`

## Audit Trail

- EXTRACTED: 33 (97%)
- INFERRED: 1 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*