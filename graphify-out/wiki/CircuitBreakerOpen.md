# CircuitBreakerOpen

> 11 nodes

## Key Concepts

- **CircuitBreakerOpen** (12 connections) — `server/realtime/circuit_breaker.py`
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

- [Circuit Breaker Core](Circuit_Breaker_Core.md) (3 shared connections)
- [SQLAlchemy Model Base](SQLAlchemy_Model_Base.md) (3 shared connections)
- [Commands Rest Countdown](Commands_Rest_Countdown.md) (1 shared connections)
- [Investigations Sessions Session](Investigations_Sessions_Session.md) (1 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (1 shared connections)
- [NATS Chat Broadcasting](NATS_Chat_Broadcasting.md) (1 shared connections)
- [Performance Optimization Summary](Performance_Optimization_Summary.md) (1 shared connections)

## Source Files

- `server/realtime/circuit_breaker.py`
- `server/tests/unit/realtime/test_circuit_breaker.py`
- `server/tests/unit/realtime/test_nats_message_handler.py`

## Audit Trail

- EXTRACTED: 28 (90%)
- INFERRED: 3 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*