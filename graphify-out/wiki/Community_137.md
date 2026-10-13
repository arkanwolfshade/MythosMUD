# Community 137

> 87 nodes

## Key Concepts

- **CircuitBreaker** (40 connections) — `server/realtime/circuit_breaker.py`
- **test_circuit_breaker.py** (32 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **CircuitState** (25 connections) — `server/realtime/circuit_breaker.py`
- **circuit_breaker.py** (12 connections) — `server/realtime/circuit_breaker.py`
- **CircuitBreakerOpen** (10 connections) — `server/realtime/circuit_breaker.py`
- **.call()** (10 connections) — `server/realtime/circuit_breaker.py`
- **asyncio** (8 connections)
- **._transition_to()** (6 connections) — `server/realtime/circuit_breaker.py`
- **test_call_rejects_when_open()** (6 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_call_closes_from_half_open_on_success()** (5 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_call_failure_closed_state()** (5 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_call_opens_circuit_after_threshold()** (5 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_call_reopens_from_half_open_on_failure()** (5 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_call_transitions_to_half_open_after_timeout()** (5 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **.get_stats()** (4 connections) — `server/realtime/circuit_breaker.py`
- **._on_failure()** (4 connections) — `server/realtime/circuit_breaker.py`
- **._on_success()** (4 connections) — `server/realtime/circuit_breaker.py`
- **._time_until_retry()** (4 connections) — `server/realtime/circuit_breaker.py`
- **test_call_success_closed_state()** (4 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_circuit_breaker_init()** (4 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_get_state()** (4 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_on_failure_opens_circuit_at_threshold()** (4 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_on_failure_resets_success_count()** (4 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_on_success_increments_success_count_half_open()** (4 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_reset()** (4 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- *... and 62 more nodes in this community*

## Relationships

- [Community 58](Community_58.md) (4 shared connections)
- [Community 47](Community_47.md) (3 shared connections)
- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (2 shared connections)
- [Community 1169](Community_1169.md) (1 shared connections)
- [Community 233](Community_233.md) (1 shared connections)
- [Community 41](Community_41.md) (1 shared connections)

## Source Files

- `server/realtime/circuit_breaker.py`
- `server/tests/unit/realtime/test_circuit_breaker.py`

## Audit Trail

- EXTRACTED: 136 (81%)
- INFERRED: 31 (19%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*