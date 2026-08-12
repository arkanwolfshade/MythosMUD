# CircuitBreakerOpen

> 16 nodes

## Key Concepts

- **CircuitBreakerOpen** (11 connections) — `server/realtime/circuit_breaker.py`
- **circuit_breaker.py** (10 connections) — `server/realtime/circuit_breaker.py`
- **CircuitState** (6 connections) — `server/realtime/circuit_breaker.py`
- **test_handle_nats_message_circuit_breaker_open()** (4 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_handle_nats_message_unknown_message_id_defaults()** (4 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **.get_state()** (3 connections) — `server/realtime/circuit_breaker.py`
- **test_circuit_breaker_open_exception()** (3 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **Enum** (2 connections)
- **Exception** (1 connections)
- **Circuit breaker pattern for NATS message processing. Implements three-state…** (1 connections) — `server/realtime/circuit_breaker.py`
- **Circuit breaker states. - CLOSED: Normal operation, requests pass through -…** (1 connections) — `server/realtime/circuit_breaker.py`
- **Get current circuit state. Returns: Current CircuitState AI: For monitoring and…** (1 connections) — `server/realtime/circuit_breaker.py`
- **Exception raised when circuit breaker is open. Indicates the protected service…** (1 connections) — `server/realtime/circuit_breaker.py`
- **Test CircuitBreakerOpen exception.** (1 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **Test _handle_nats_message() handles circuit breaker open.** (1 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **Test _handle_nats_message uses 'unknown' as default message_id when missing.** (1 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`

## Relationships

- [CircuitBreaker](CircuitBreaker.md) (6 shared connections)
- [test_nats_message_handler.py](test_nats_message_handler.py.md) (6 shared connections)
- [.call](call.md) (2 shared connections)
- [build_event](build_event.md) (2 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [NATSMessageHandler](NATSMessageHandler.md) (1 shared connections)

## Source Files

- `server/realtime/circuit_breaker.py`
- `server/tests/unit/realtime/test_circuit_breaker.py`
- `server/tests/unit/realtime/test_nats_message_handler.py`

## Audit Trail

- EXTRACTED: 50 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*