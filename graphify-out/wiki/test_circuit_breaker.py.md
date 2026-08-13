# test_circuit_breaker.py

> 20 nodes

## Key Concepts

- **test_circuit_breaker.py** (32 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_circuit_breaker_init()** (3 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_circuit_breaker_init_defaults()** (3 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_circuit_breaker_open_exception()** (3 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_get_state()** (3 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_get_stats()** (3 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_on_failure_increments_failure_count()** (3 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_on_failure_opens_circuit_at_threshold()** (3 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_on_failure_resets_success_count()** (3 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_time_until_retry_returns_zero_after_timeout()** (3 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **Unit tests for circuit breaker. Tests the CircuitBreaker class and…** (1 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **Test _on_failure() increments failure count.** (1 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **Test _on_failure() opens circuit at threshold.** (1 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **Test CircuitBreaker initialization.** (1 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **Test _on_failure() resets success count.** (1 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **Test _time_until_retry() returns 0 after timeout.** (1 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **Test get_state() returns current state.** (1 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **Test get_stats() returns comprehensive statistics.** (1 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **Test CircuitBreaker initialization with defaults.** (1 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **Test CircuitBreakerOpen exception.** (1 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`

## Relationships

- [CircuitBreaker](CircuitBreaker.md) (15 shared connections)
- [asyncio](asyncio.md) (8 shared connections)
- [test_nats_message_handler.py](test_nats_message_handler.py.md) (2 shared connections)
- [circuit_breaker.py](circuit_breaker.py.md) (2 shared connections)
- [test_on_success_increments_success_count_half_open](test_on_success_increments_success_count_half_open.md) (1 shared connections)
- [test_should_attempt_reset_returns_true_after_timeout](test_should_attempt_reset_returns_true_after_timeout.md) (1 shared connections)
- [test_transition_to_updates_state](test_transition_to_updates_state.md) (1 shared connections)
- [test_get_stats_with_failure_time](test_get_stats_with_failure_time.md) (1 shared connections)

## Source Files

- `server/tests/unit/realtime/test_circuit_breaker.py`

## Audit Trail

- EXTRACTED: 50 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*