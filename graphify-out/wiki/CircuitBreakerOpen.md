# CircuitBreakerOpen

> 9 nodes

## Key Concepts

- **CircuitBreakerOpen** (12 connections) — `server/realtime/circuit_breaker.py`
- **test_handle_nats_message_circuit_breaker_open()** (4 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_handle_nats_message_unknown_message_id_defaults()** (4 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_circuit_breaker_open_exception()** (3 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **Exception** (1 connections)
- **Exception raised when circuit breaker is open. Indicates the protected service…** (1 connections) — `server/realtime/circuit_breaker.py`
- **Test CircuitBreakerOpen exception.** (1 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **Test _handle_nats_message() handles circuit breaker open.** (1 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **Test _handle_nats_message uses 'unknown' as default message_id when missing.** (1 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`

## Relationships

- [test_nats_message_handler.py](test_nats_message_handler.py.md) (5 shared connections)
- [CircuitBreaker](CircuitBreaker.md) (4 shared connections)
- [ConnectionManager](ConnectionManager.md) (2 shared connections)
- [.call](call.md) (1 shared connections)

## Source Files

- `server/realtime/circuit_breaker.py`
- `server/tests/unit/realtime/test_circuit_breaker.py`
- `server/tests/unit/realtime/test_nats_message_handler.py`

## Audit Trail

- EXTRACTED: 15 (75%)
- INFERRED: 5 (25%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*