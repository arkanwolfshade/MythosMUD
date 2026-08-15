# test_circuit_breaker.py

> 20 nodes

## Key Concepts

- **test_circuit_breaker.py** (32 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_on_failure_resets_success_count()** (4 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_should_attempt_reset_returns_false_when_not_open()** (4 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_should_attempt_reset_returns_true_after_timeout()** (4 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_time_until_retry_returns_zero_after_timeout()** (4 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_circuit_breaker_init_defaults()** (3 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_get_stats()** (3 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_get_stats_with_failure_time()** (3 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_on_failure_increments_failure_count()** (3 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_on_success_resets_failure_count_closed()** (3 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **Unit tests for circuit breaker. Tests the CircuitBreaker class and…** (1 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **Test _on_success() resets failure count in CLOSED state.** (1 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **Test _on_failure() increments failure count.** (1 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **Test _on_failure() resets success count.** (1 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **Test _should_attempt_reset() returns True after timeout.** (1 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **Test _should_attempt_reset() returns False when not OPEN.** (1 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **Test _time_until_retry() returns 0 after timeout.** (1 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **Test get_stats() returns comprehensive statistics.** (1 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **Test get_stats() includes failure time when set.** (1 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **Test CircuitBreaker initialization with defaults.** (1 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`

## Relationships

- [CircuitBreaker](CircuitBreaker.md) (13 shared connections)
- [CircuitState](CircuitState.md) (10 shared connections)
- [asyncio](asyncio.md) (7 shared connections)
- [CircuitBreakerOpen](CircuitBreakerOpen.md) (3 shared connections)
- [test_circuit_breaker_init](test_circuit_breaker_init.md) (1 shared connections)
- [test_reset](test_reset.md) (1 shared connections)

## Source Files

- `server/tests/unit/realtime/test_circuit_breaker.py`

## Audit Trail

- EXTRACTED: 41 (76%)
- INFERRED: 13 (24%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*