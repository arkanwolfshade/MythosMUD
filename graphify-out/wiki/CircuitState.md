# CircuitState

> 15 nodes

## Key Concepts

- **CircuitState** (25 connections) — `server/realtime/circuit_breaker.py`
- **circuit_breaker.py** (12 connections) — `server/realtime/circuit_breaker.py`
- **test_get_state()** (4 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_on_failure_opens_circuit_at_threshold()** (4 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_on_success_increments_success_count_half_open()** (4 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_should_attempt_reset_returns_false_before_timeout()** (4 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **.get_state()** (3 connections) — `server/realtime/circuit_breaker.py`
- **Enum** (2 connections)
- **Circuit breaker pattern for NATS message processing. Implements three-state…** (1 connections) — `server/realtime/circuit_breaker.py`
- **Circuit breaker states. - CLOSED: Normal operation, requests pass through -…** (1 connections) — `server/realtime/circuit_breaker.py`
- **Get current circuit state. Returns: Current CircuitState AI: For monitoring and…** (1 connections) — `server/realtime/circuit_breaker.py`
- **Test _on_success() increments success count in HALF_OPEN state.** (1 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **Test _on_failure() opens circuit at threshold.** (1 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **Test _should_attempt_reset() returns False before timeout.** (1 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **Test get_state() returns current state.** (1 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`

## Relationships

- [test_circuit_breaker.py](test_circuit_breaker.py.md) (10 shared connections)
- [CircuitBreaker](CircuitBreaker.md) (9 shared connections)
- [asyncio](asyncio.md) (5 shared connections)
- [get_logger](get_logger.md) (5 shared connections)
- [CircuitBreakerOpen](CircuitBreakerOpen.md) (2 shared connections)
- [.call](call.md) (1 shared connections)
- [test_circuit_breaker_init](test_circuit_breaker_init.md) (1 shared connections)
- [test_reset](test_reset.md) (1 shared connections)
- [test_nats_message_handler.py](test_nats_message_handler.py.md) (1 shared connections)

## Source Files

- `server/realtime/circuit_breaker.py`
- `server/tests/unit/realtime/test_circuit_breaker.py`

## Audit Trail

- EXTRACTED: 27 (54%)
- INFERRED: 23 (46%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*