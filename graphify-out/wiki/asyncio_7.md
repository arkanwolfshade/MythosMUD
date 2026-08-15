# asyncio

> 13 nodes

## Key Concepts

- **asyncio** (8 connections)
- **test_call_closes_from_half_open_on_success()** (5 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_call_failure_closed_state()** (5 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_call_opens_circuit_after_threshold()** (5 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_call_reopens_from_half_open_on_failure()** (5 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_call_transitions_to_half_open_after_timeout()** (5 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_call_success_closed_state()** (4 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **Test call() closes circuit from HALF_OPEN after success threshold.** (1 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **Test call() reopens circuit from HALF_OPEN on failure.** (1 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **Test call() executes successfully in CLOSED state.** (1 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **Test call() handles failure in CLOSED state.** (1 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **Test call() opens circuit after failure threshold.** (1 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **Test call() transitions to HALF_OPEN after timeout.** (1 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`

## Relationships

- [test_circuit_breaker.py](test_circuit_breaker.py.md) (7 shared connections)
- [CircuitBreaker](CircuitBreaker.md) (6 shared connections)
- [CircuitState](CircuitState.md) (5 shared connections)
- [CircuitBreakerOpen](CircuitBreakerOpen.md) (1 shared connections)

## Source Files

- `server/tests/unit/realtime/test_circuit_breaker.py`

## Audit Trail

- EXTRACTED: 20 (65%)
- INFERRED: 11 (35%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*