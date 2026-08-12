# CircuitBreaker

> 67 nodes

## Key Concepts

- **CircuitBreaker** (41 connections) — `server/realtime/circuit_breaker.py`
- **test_circuit_breaker.py** (32 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **circuit_breaker.py** (10 connections) — `server/realtime/circuit_breaker.py`
- **asyncio** (8 connections)
- **CircuitState** (6 connections) — `server/realtime/circuit_breaker.py`
- **test_call_closes_from_half_open_on_success()** (4 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_call_failure_closed_state()** (4 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_call_opens_circuit_after_threshold()** (4 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_call_rejects_when_open()** (4 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_call_reopens_from_half_open_on_failure()** (4 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_call_success_closed_state()** (4 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_call_transitions_to_half_open_after_timeout()** (4 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **.get_state()** (3 connections) — `server/realtime/circuit_breaker.py`
- **.__init__()** (3 connections) — `server/realtime/circuit_breaker.py`
- **test_circuit_breaker_init()** (3 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_circuit_breaker_init_defaults()** (3 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_get_state()** (3 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_get_stats()** (3 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_get_stats_with_failure_time()** (3 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_on_failure_increments_failure_count()** (3 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_on_failure_opens_circuit_at_threshold()** (3 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_on_failure_resets_success_count()** (3 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_on_success_increments_success_count_half_open()** (3 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_on_success_resets_failure_count_closed()** (3 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_reset()** (3 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- *... and 42 more nodes in this community*

## Relationships

- [CircuitBreakerOpen](CircuitBreakerOpen.md) (11 shared connections)
- [get_logger](get_logger.md) (4 shared connections)
- [EventHandler](EventHandler.md) (1 shared connections)
- [NATSMessageHandler](NATSMessageHandler.md) (1 shared connections)
- [test_nats_message_handler.py](test_nats_message_handler.py.md) (1 shared connections)

## Source Files

- `server/realtime/circuit_breaker.py`
- `server/tests/unit/realtime/test_circuit_breaker.py`

## Audit Trail

- EXTRACTED: 221 (100%)
- INFERRED: 1 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*