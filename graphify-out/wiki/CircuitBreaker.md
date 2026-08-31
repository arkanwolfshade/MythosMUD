# CircuitBreaker

> 17 nodes

## Key Concepts

- **CircuitBreaker** (43 connections) — `server/realtime/circuit_breaker.py`
- **test_should_attempt_reset_returns_true_after_timeout()** (4 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_transition_to_updates_state()** (4 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **.__init__()** (3 connections) — `server/realtime/circuit_breaker.py`
- **test_get_stats()** (3 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_get_stats_with_failure_time()** (3 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_on_success_resets_failure_count_closed()** (3 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **.reset()** (2 connections) — `server/realtime/circuit_breaker.py`
- **timedelta** (1 connections)
- **Manually reset circuit breaker to CLOSED state. Clears all counters and timers.…** (1 connections) — `server/realtime/circuit_breaker.py`
- **Circuit breaker for NATS message processing. Implements Martin Fowler's circuit…** (1 connections) — `server/realtime/circuit_breaker.py`
- **Initialize circuit breaker. Args: failure_threshold: Number of failures before…** (1 connections) — `server/realtime/circuit_breaker.py`
- **Test _on_success() resets failure count in CLOSED state.** (1 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **Test _should_attempt_reset() returns True after timeout.** (1 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **Test _transition_to() updates state.** (1 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **Test get_stats() returns comprehensive statistics.** (1 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **Test get_stats() includes failure time when set.** (1 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`

## Relationships

- [test_circuit_breaker.py](test_circuit_breaker.py.md) (13 shared connections)
- [CircuitState](CircuitState.md) (8 shared connections)
- [.call](call.md) (7 shared connections)
- [asyncio](asyncio.md) (7 shared connections)
- [get_logger](get_logger.md) (4 shared connections)
- [GameStateProvider](GameStateProvider.md) (2 shared connections)
- [test_circuit_breaker_init](test_circuit_breaker_init.md) (1 shared connections)

## Source Files

- `server/realtime/circuit_breaker.py`
- `server/tests/unit/realtime/test_circuit_breaker.py`

## Audit Trail

- EXTRACTED: 47 (81%)
- INFERRED: 11 (19%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*