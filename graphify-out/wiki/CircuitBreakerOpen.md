# CircuitBreakerOpen

> 24 nodes

## Key Concepts

- **CircuitBreakerOpen** (11 connections) — `server/realtime/circuit_breaker.py`
- **.call()** (9 connections) — `server/realtime/circuit_breaker.py`
- **._transition_to()** (6 connections) — `server/realtime/circuit_breaker.py`
- **.get_stats()** (4 connections) — `server/realtime/circuit_breaker.py`
- **._on_failure()** (4 connections) — `server/realtime/circuit_breaker.py`
- **._on_success()** (4 connections) — `server/realtime/circuit_breaker.py`
- **._time_until_retry()** (4 connections) — `server/realtime/circuit_breaker.py`
- **test_handle_nats_message_circuit_breaker_open()** (4 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_handle_nats_message_unknown_message_id_defaults()** (4 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **._should_attempt_reset()** (3 connections) — `server/realtime/circuit_breaker.py`
- **test_circuit_breaker_open_exception()** (3 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **Any** (2 connections)
- **Exception** (1 connections)
- **Handle successful function call. Updates state based on current circuit state:…** (1 connections) — `server/realtime/circuit_breaker.py`
- **Handle failed function call. Updates state based on failure count: - Increments…** (1 connections) — `server/realtime/circuit_breaker.py`
- **Check if enough time has passed to attempt circuit reset. Returns: True if…** (1 connections) — `server/realtime/circuit_breaker.py`
- **Calculate seconds until circuit can attempt reset. Returns: Seconds until retry…** (1 connections) — `server/realtime/circuit_breaker.py`
- **Transition circuit to new state. Args: new_state: State to transition to AI:…** (1 connections) — `server/realtime/circuit_breaker.py`
- **Get circuit breaker statistics. Returns: Dictionary with circuit breaker…** (1 connections) — `server/realtime/circuit_breaker.py`
- **Exception raised when circuit breaker is open. Indicates the protected service…** (1 connections) — `server/realtime/circuit_breaker.py`
- **Execute function through circuit breaker. Enforces circuit breaker logic: -…** (1 connections) — `server/realtime/circuit_breaker.py`
- **Test CircuitBreakerOpen exception.** (1 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **Test _handle_nats_message() handles circuit breaker open.** (1 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **Test _handle_nats_message uses 'unknown' as default message_id when missing.** (1 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`

## Relationships

- [CircuitBreaker](CircuitBreaker.md) (11 shared connections)
- [test_nats_message_handler.py](test_nats_message_handler.py.md) (5 shared connections)
- [get_logger](get_logger.md) (1 shared connections)
- [NATSMessageHandler](NATSMessageHandler.md) (1 shared connections)

## Source Files

- `server/realtime/circuit_breaker.py`
- `server/tests/unit/realtime/test_circuit_breaker.py`
- `server/tests/unit/realtime/test_nats_message_handler.py`

## Audit Trail

- EXTRACTED: 43 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*