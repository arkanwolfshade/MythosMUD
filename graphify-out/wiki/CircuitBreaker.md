# CircuitBreaker

> 82 nodes

## Key Concepts

- **CircuitBreaker** (43 connections) — `server/realtime/circuit_breaker.py`
- **test_circuit_breaker.py** (32 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **.call()** (9 connections) — `server/realtime/circuit_breaker.py`
- **asyncio** (8 connections)
- **CircuitState** (6 connections) — `server/realtime/circuit_breaker.py`
- **._transition_to()** (6 connections) — `server/realtime/circuit_breaker.py`
- **.get_stats()** (4 connections) — `server/realtime/circuit_breaker.py`
- **._on_failure()** (4 connections) — `server/realtime/circuit_breaker.py`
- **._on_success()** (4 connections) — `server/realtime/circuit_breaker.py`
- **._time_until_retry()** (4 connections) — `server/realtime/circuit_breaker.py`
- **test_call_closes_from_half_open_on_success()** (4 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_call_failure_closed_state()** (4 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_call_opens_circuit_after_threshold()** (4 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_call_rejects_when_open()** (4 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_call_reopens_from_half_open_on_failure()** (4 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_call_success_closed_state()** (4 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_call_transitions_to_half_open_after_timeout()** (4 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **.get_state()** (3 connections) — `server/realtime/circuit_breaker.py`
- **.__init__()** (3 connections) — `server/realtime/circuit_breaker.py`
- **._should_attempt_reset()** (3 connections) — `server/realtime/circuit_breaker.py`
- **test_circuit_breaker_init()** (3 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_circuit_breaker_init_defaults()** (3 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_circuit_breaker_open_exception()** (3 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_get_state()** (3 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_get_stats()** (3 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- *... and 57 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (6 shared connections)
- [test_nats_message_handler.py](test_nats_message_handler.py.md) (3 shared connections)
- [MessageFilteringHelper](MessageFilteringHelper.md) (1 shared connections)
- [NATSMessageHandlerMixinBase](NATSMessageHandlerMixinBase.md) (1 shared connections)
- [PlayerEventHandlerUtils](PlayerEventHandlerUtils.md) (1 shared connections)

## Source Files

- `server/realtime/circuit_breaker.py`
- `server/tests/unit/realtime/test_circuit_breaker.py`

## Audit Trail

- EXTRACTED: 134 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*