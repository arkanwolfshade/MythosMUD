# CircuitBreaker

> 13 nodes

## Key Concepts

- **CircuitBreaker** (43 connections) — `server/realtime/circuit_breaker.py`
- **test_time_until_retry_returns_remaining_time()** (4 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_time_until_retry_returns_zero_when_not_open()** (4 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_transition_to_updates_state()** (4 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **.__init__()** (3 connections) — `server/realtime/circuit_breaker.py`
- **.reset()** (2 connections) — `server/realtime/circuit_breaker.py`
- **timedelta** (1 connections)
- **Manually reset circuit breaker to CLOSED state. Clears all counters and timers.…** (1 connections) — `server/realtime/circuit_breaker.py`
- **Circuit breaker for NATS message processing. Implements Martin Fowler's circuit…** (1 connections) — `server/realtime/circuit_breaker.py`
- **Initialize circuit breaker. Args: failure_threshold: Number of failures before…** (1 connections) — `server/realtime/circuit_breaker.py`
- **Test _time_until_retry() returns 0 when not OPEN.** (1 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **Test _time_until_retry() returns remaining time.** (1 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **Test _transition_to() updates state.** (1 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`

## Relationships

- [test_circuit_breaker.py](test_circuit_breaker.py.md) (13 shared connections)
- [CircuitState](CircuitState.md) (9 shared connections)
- [.call](call.md) (7 shared connections)
- [asyncio](asyncio.md) (6 shared connections)
- [NATSRetryHandler](NATSRetryHandler.md) (2 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [test_circuit_breaker_init](test_circuit_breaker_init.md) (1 shared connections)
- [test_reset](test_reset.md) (1 shared connections)
- [PlayerEventHandlerUtils](PlayerEventHandlerUtils.md) (1 shared connections)
- [CircuitBreakerOpen](CircuitBreakerOpen.md) (1 shared connections)

## Source Files

- `server/realtime/circuit_breaker.py`
- `server/tests/unit/realtime/test_circuit_breaker.py`

## Audit Trail

- EXTRACTED: 25 (45%)
- INFERRED: 30 (55%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*