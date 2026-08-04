# config rationale config()

> 11 nodes

## Key Concepts

- **CircuitBreakerOpen** (14 connections) — `server/realtime/circuit_breaker.py`
- **test_call_rejects_when_open()** (4 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_circuit_breaker_open_exception()** (3 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **test_handle_nats_message_circuit_breaker_open()** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_handle_nats_message_unknown_message_id_defaults()** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **Exception** (1 connections)
- **Exception raised when circuit breaker is open.      Indicates the protected serv** (1 connections) — `server/realtime/circuit_breaker.py`
- **Test call() raises CircuitBreakerOpen when circuit is OPEN.** (1 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **Test CircuitBreakerOpen exception.** (1 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **Test _handle_nats_message() handles circuit breaker open.** (1 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **Test _handle_nats_message uses 'unknown' as default message_id when missing.** (1 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`

## Relationships

- [websocket handler realtime](websocket_handler_realtime.md) (5 shared connections)
- [container persistence rationale](container_persistence_rationale.md) (3 shared connections)
- [nats message handler](nats_message_handler.md) (3 shared connections)
- [conftest mock rationale](conftest_mock_rationale.md) (1 shared connections)
- [NPC Combat](NPC_Combat.md) (1 shared connections)

## Source Files

- `server/realtime/circuit_breaker.py`
- `server/tests/unit/realtime/test_circuit_breaker.py`
- `server/tests/unit/realtime/test_nats_message_handler.py`

## Audit Trail

- EXTRACTED: 28 (85%)
- INFERRED: 5 (15%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*