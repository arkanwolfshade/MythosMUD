# circuit_breaker.py

> 7 nodes

## Key Concepts

- **circuit_breaker.py** (10 connections) — `server/realtime/circuit_breaker.py`
- **CircuitState** (6 connections) — `server/realtime/circuit_breaker.py`
- **.get_state()** (3 connections) — `server/realtime/circuit_breaker.py`
- **Enum** (2 connections)
- **Circuit breaker pattern for NATS message processing. Implements three-state…** (1 connections) — `server/realtime/circuit_breaker.py`
- **Circuit breaker states. - CLOSED: Normal operation, requests pass through -…** (1 connections) — `server/realtime/circuit_breaker.py`
- **Get current circuit state. Returns: Current CircuitState AI: For monitoring and…** (1 connections) — `server/realtime/circuit_breaker.py`

## Relationships

- [test_circuit_breaker.py](test_circuit_breaker.py.md) (2 shared connections)
- [CircuitBreaker](CircuitBreaker.md) (2 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [test_nats_message_handler.py](test_nats_message_handler.py.md) (2 shared connections)
- [.call](call.md) (1 shared connections)
- [build_event](build_event.md) (1 shared connections)

## Source Files

- `server/realtime/circuit_breaker.py`

## Audit Trail

- EXTRACTED: 17 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*