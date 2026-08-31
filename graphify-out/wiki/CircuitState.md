# CircuitState

> 15 nodes

## Key Concepts

- **CircuitState** (25 connections) — `server/realtime/circuit_breaker.py`
- **test_get_state()** (4 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_reset()** (4 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_should_attempt_reset_returns_false_when_not_open()** (4 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_time_until_retry_returns_remaining_time()** (4 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_time_until_retry_returns_zero_after_timeout()** (4 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **.get_state()** (3 connections) — `server/realtime/circuit_breaker.py`
- **Enum** (2 connections)
- **Circuit breaker states. - CLOSED: Normal operation, requests pass through -…** (1 connections) — `server/realtime/circuit_breaker.py`
- **Get current circuit state. Returns: Current CircuitState AI: For monitoring and…** (1 connections) — `server/realtime/circuit_breaker.py`
- **Test _should_attempt_reset() returns False when not OPEN.** (1 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **Test _time_until_retry() returns remaining time.** (1 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **Test _time_until_retry() returns 0 after timeout.** (1 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **Test get_state() returns current state.** (1 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **Test reset() manually resets circuit breaker.** (1 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`

## Relationships

- [test_circuit_breaker.py](test_circuit_breaker.py.md) (11 shared connections)
- [CircuitBreaker](CircuitBreaker.md) (8 shared connections)
- [asyncio](asyncio.md) (6 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [.call](call.md) (1 shared connections)
- [test_circuit_breaker_init](test_circuit_breaker_init.md) (1 shared connections)

## Source Files

- `server/realtime/circuit_breaker.py`
- `server/tests/unit/realtime/test_circuit_breaker.py`

## Audit Trail

- EXTRACTED: 24 (56%)
- INFERRED: 19 (44%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*