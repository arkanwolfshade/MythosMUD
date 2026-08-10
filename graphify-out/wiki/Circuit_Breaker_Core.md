# Circuit Breaker Core

> 20 nodes

## Key Concepts

- **test_circuit_breaker.py** (31 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_circuit_breaker_init()** (3 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_circuit_breaker_init_defaults()** (3 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_call_success_closed_state()** (3 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_call_reopens_from_half_open_on_failure()** (3 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_on_success_resets_failure_count_closed()** (3 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_on_failure_increments_failure_count()** (3 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_should_attempt_reset_returns_false_when_not_open()** (3 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_time_until_retry_returns_remaining_time()** (3 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_reset()** (3 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **Unit tests for circuit breaker.  Tests the CircuitBreaker class and CircuitBreak** (1 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **Test CircuitBreaker initialization.** (1 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **Test CircuitBreaker initialization with defaults.** (1 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **Test call() executes successfully in CLOSED state.** (1 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **Test call() reopens circuit from HALF_OPEN on failure.** (1 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **Test _on_success() resets failure count in CLOSED state.** (1 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **Test _on_failure() increments failure count.** (1 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **Test _should_attempt_reset() returns False when not OPEN.** (1 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **Test _time_until_retry() returns remaining time.** (1 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **Test reset() manually resets circuit breaker.** (1 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`

## Relationships

- [Performance Optimization Summary](Performance_Optimization_Summary.md) (16 shared connections)
- [CircuitBreakerOpen](CircuitBreakerOpen.md) (3 shared connections)
- [Commands Rest Countdown](Commands_Rest_Countdown.md) (2 shared connections)
- [test_call_failure_closed_state](test_call_failure_closed_state.md) (1 shared connections)
- [test_call_transitions_to_half_open_after_timeout](test_call_transitions_to_half_open_after_timeout.md) (1 shared connections)
- [test_get_stats_with_failure_time](test_get_stats_with_failure_time.md) (1 shared connections)
- [test_on_failure_opens_circuit_at_threshold](test_on_failure_opens_circuit_at_threshold.md) (1 shared connections)
- [test_on_failure_resets_success_count](test_on_failure_resets_success_count.md) (1 shared connections)
- [test_should_attempt_reset_returns_true_after_timeout](test_should_attempt_reset_returns_true_after_timeout.md) (1 shared connections)
- [test_time_until_retry_returns_zero_after_timeout](test_time_until_retry_returns_zero_after_timeout.md) (1 shared connections)
- [test_time_until_retry_returns_zero_when_not_open](test_time_until_retry_returns_zero_when_not_open.md) (1 shared connections)
- [test_transition_to_updates_state](test_transition_to_updates_state.md) (1 shared connections)

## Source Files

- `server/tests/unit/realtime/test_circuit_breaker.py`

## Audit Trail

- EXTRACTED: 68 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*