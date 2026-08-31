# test_circuit_breaker.py

> 18 nodes

## Key Concepts

- **test_circuit_breaker.py** (33 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_on_failure_opens_circuit_at_threshold()** (4 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_on_failure_resets_success_count()** (4 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_on_success_increments_success_count_half_open()** (4 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_should_attempt_reset_returns_false_before_timeout()** (4 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_time_until_retry_returns_zero_when_not_open()** (4 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_circuit_breaker_init_defaults()** (3 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_circuit_breaker_open_exception()** (3 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_on_failure_increments_failure_count()** (3 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **Unit tests for circuit breaker. Tests the CircuitBreaker class and…** (1 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **Test _on_success() increments success count in HALF_OPEN state.** (1 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **Test _on_failure() increments failure count.** (1 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **Test _on_failure() opens circuit at threshold.** (1 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **Test _on_failure() resets success count.** (1 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **Test _should_attempt_reset() returns False before timeout.** (1 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **Test _time_until_retry() returns 0 when not OPEN.** (1 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **Test CircuitBreaker initialization with defaults.** (1 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **Test CircuitBreakerOpen exception.** (1 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`

## Relationships

- [CircuitBreaker](CircuitBreaker.md) (13 shared connections)
- [CircuitState](CircuitState.md) (11 shared connections)
- [asyncio](asyncio.md) (8 shared connections)
- [format_message_content](format_message_content.md) (2 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)
- [get_logger](get_logger.md) (1 shared connections)
- [test_circuit_breaker_init](test_circuit_breaker_init.md) (1 shared connections)

## Source Files

- `server/tests/unit/realtime/test_circuit_breaker.py`

## Audit Trail

- EXTRACTED: 49 (91%)
- INFERRED: 5 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*