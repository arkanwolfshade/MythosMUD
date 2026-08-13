# CircuitBreaker

> 16 nodes

## Key Concepts

- **CircuitBreaker** (41 connections) — `server/realtime/circuit_breaker.py`
- **test_on_success_resets_failure_count_closed()** (3 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_reset()** (3 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_should_attempt_reset_returns_false_before_timeout()** (3 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_should_attempt_reset_returns_false_when_not_open()** (3 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_time_until_retry_returns_remaining_time()** (3 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_time_until_retry_returns_zero_when_not_open()** (3 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **.reset()** (2 connections) — `server/realtime/circuit_breaker.py`
- **Manually reset circuit breaker to CLOSED state. Clears all counters and timers.…** (1 connections) — `server/realtime/circuit_breaker.py`
- **Circuit breaker for NATS message processing. Implements Martin Fowler's circuit…** (1 connections) — `server/realtime/circuit_breaker.py`
- **Test _on_success() resets failure count in CLOSED state.** (1 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **Test _should_attempt_reset() returns False before timeout.** (1 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **Test _should_attempt_reset() returns False when not OPEN.** (1 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **Test _time_until_retry() returns 0 when not OPEN.** (1 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **Test _time_until_retry() returns remaining time.** (1 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **Test reset() manually resets circuit breaker.** (1 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`

## Relationships

- [test_circuit_breaker.py](test_circuit_breaker.py.md) (15 shared connections)
- [asyncio](asyncio.md) (7 shared connections)
- [.call](call.md) (7 shared connections)
- [circuit_breaker.py](circuit_breaker.py.md) (2 shared connections)
- [MessageFilteringHelper](MessageFilteringHelper.md) (1 shared connections)
- [test_get_stats_with_failure_time](test_get_stats_with_failure_time.md) (1 shared connections)
- [test_on_success_increments_success_count_half_open](test_on_success_increments_success_count_half_open.md) (1 shared connections)
- [test_should_attempt_reset_returns_true_after_timeout](test_should_attempt_reset_returns_true_after_timeout.md) (1 shared connections)
- [test_transition_to_updates_state](test_transition_to_updates_state.md) (1 shared connections)
- [build_event](build_event.md) (1 shared connections)
- [.__init__](__init__.md) (1 shared connections)
- [NATSMessageHandler](NATSMessageHandler.md) (1 shared connections)

## Source Files

- `server/realtime/circuit_breaker.py`
- `server/tests/unit/realtime/test_circuit_breaker.py`

## Audit Trail

- EXTRACTED: 53 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*