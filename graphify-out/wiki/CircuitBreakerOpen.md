# CircuitBreakerOpen

> 7 nodes

## Key Concepts

- **CircuitBreakerOpen** (12 connections) — `server/realtime/circuit_breaker.py`
- **test_call_rejects_when_open()** (6 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_circuit_breaker_open_exception()** (3 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **Exception** (1 connections)
- **Exception raised when circuit breaker is open. Indicates the protected service…** (1 connections) — `server/realtime/circuit_breaker.py`
- **Test CircuitBreakerOpen exception.** (1 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **Test call() raises CircuitBreakerOpen when circuit is OPEN.** (1 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`

## Relationships

- [test_circuit_breaker.py](test_circuit_breaker.py.md) (3 shared connections)
- [test_nats_message_handler.py](test_nats_message_handler.py.md) (3 shared connections)
- [CircuitState](CircuitState.md) (2 shared connections)
- [.call](call.md) (1 shared connections)
- [get_logger](get_logger.md) (1 shared connections)
- [DeadLetterQueue](DeadLetterQueue.md) (1 shared connections)
- [asyncio](asyncio.md) (1 shared connections)
- [CircuitBreaker](CircuitBreaker.md) (1 shared connections)

## Source Files

- `server/realtime/circuit_breaker.py`
- `server/tests/unit/realtime/test_circuit_breaker.py`

## Audit Trail

- EXTRACTED: 12 (63%)
- INFERRED: 7 (37%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*