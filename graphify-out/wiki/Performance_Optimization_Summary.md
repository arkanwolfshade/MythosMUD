# Performance Optimization Summary

> 19 nodes

## Key Concepts

- **CircuitBreaker** (41 connections) — `server/realtime/circuit_breaker.py`
- **.__init__()** (3 connections) — `server/realtime/circuit_breaker.py`
- **test_call_opens_circuit_after_threshold()** (3 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_call_closes_from_half_open_on_success()** (3 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_on_success_increments_success_count_half_open()** (3 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_should_attempt_reset_returns_false_before_timeout()** (3 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_get_state()** (3 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_get_stats()** (3 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **.reset()** (2 connections) — `server/realtime/circuit_breaker.py`
- **timedelta** (1 connections)
- **Circuit breaker for NATS message processing.      Implements Martin Fowler's cir** (1 connections) — `server/realtime/circuit_breaker.py`
- **Initialize circuit breaker.          Args:             failure_threshold: Number** (1 connections) — `server/realtime/circuit_breaker.py`
- **Manually reset circuit breaker to CLOSED state.          Clears all counters and** (1 connections) — `server/realtime/circuit_breaker.py`
- **Test call() opens circuit after failure threshold.** (1 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **Test call() closes circuit from HALF_OPEN after success threshold.** (1 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **Test _on_success() increments success count in HALF_OPEN state.** (1 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **Test _should_attempt_reset() returns False before timeout.** (1 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **Test get_state() returns current state.** (1 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **Test get_stats() returns comprehensive statistics.** (1 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`

## Relationships

- [Circuit Breaker Core](Circuit_Breaker_Core.md) (16 shared connections)
- [Investigations Sessions Session](Investigations_Sessions_Session.md) (7 shared connections)
- [Commands Rest Countdown](Commands_Rest_Countdown.md) (2 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (1 shared connections)
- [NATS Chat Broadcasting](NATS_Chat_Broadcasting.md) (1 shared connections)
- [Chat Message Filtering](Chat_Message_Filtering.md) (1 shared connections)
- [test_call_failure_closed_state](test_call_failure_closed_state.md) (1 shared connections)
- [CircuitBreakerOpen](CircuitBreakerOpen.md) (1 shared connections)
- [test_call_transitions_to_half_open_after_timeout](test_call_transitions_to_half_open_after_timeout.md) (1 shared connections)
- [test_get_stats_with_failure_time](test_get_stats_with_failure_time.md) (1 shared connections)
- [test_on_failure_opens_circuit_at_threshold](test_on_failure_opens_circuit_at_threshold.md) (1 shared connections)
- [test_on_failure_resets_success_count](test_on_failure_resets_success_count.md) (1 shared connections)

## Source Files

- `server/realtime/circuit_breaker.py`
- `server/tests/unit/realtime/test_circuit_breaker.py`

## Audit Trail

- EXTRACTED: 73 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*