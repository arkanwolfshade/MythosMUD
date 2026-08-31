# test_connection_error_methods.py

> 27 nodes

## Key Concepts

- **test_connection_error_methods.py** (15 connections) — `server/tests/unit/realtime/test_connection_error_methods.py`
- **delegate_error_handler()** (12 connections) — `server/realtime/connection_delegates.py`
- **connection_error_methods.py** (11 connections) — `server/realtime/connection_error_methods.py`
- **detect_and_handle_error_state_impl()** (10 connections) — `server/realtime/connection_error_methods.py`
- **handle_authentication_error_impl()** (9 connections) — `server/realtime/connection_error_methods.py`
- **handle_security_violation_impl()** (9 connections) — `server/realtime/connection_error_methods.py`
- **handle_websocket_error_impl()** (9 connections) — `server/realtime/connection_error_methods.py`
- **recover_from_error_impl()** (9 connections) — `server/realtime/connection_error_methods.py`
- **UUID** (6 connections)
- **asyncio** (6 connections)
- **Any** (5 connections)
- **test_detect_and_handle_error_state_impl_delegates()** (3 connections) — `server/tests/unit/realtime/test_connection_error_methods.py`
- **test_error_impl_returns_default_when_handler_missing()** (3 connections) — `server/tests/unit/realtime/test_connection_error_methods.py`
- **test_handle_authentication_error_impl_delegates()** (3 connections) — `server/tests/unit/realtime/test_connection_error_methods.py`
- **test_handle_security_violation_impl_delegates()** (3 connections) — `server/tests/unit/realtime/test_connection_error_methods.py`
- **test_handle_websocket_error_impl_delegates()** (3 connections) — `server/tests/unit/realtime/test_connection_error_methods.py`
- **test_recover_from_error_impl_delegates()** (3 connections) — `server/tests/unit/realtime/test_connection_error_methods.py`
- **manager()** (2 connections) — `server/tests/unit/realtime/test_connection_error_methods.py`
- **fixture** (1 connections)
- **Generic delegate for error handler methods. Args: error_handler: Error handler…** (1 connections) — `server/realtime/connection_delegates.py`
- **Error-handling method implementations for ConnectionManager. Thin wrappers that…** (1 connections) — `server/realtime/connection_error_methods.py`
- **Detect when a client is in an error state and handle it appropriately.** (1 connections) — `server/realtime/connection_error_methods.py`
- **Handle WebSocket-specific errors.** (1 connections) — `server/realtime/connection_error_methods.py`
- **Handle authentication-related errors.** (1 connections) — `server/realtime/connection_error_methods.py`
- **Handle security violations.** (1 connections) — `server/realtime/connection_error_methods.py`
- *... and 2 more nodes in this community*

## Relationships

- [test_connection_delegates.py](test_connection_delegates.py.md) (6 shared connections)
- [get_logger](get_logger.md) (6 shared connections)
- [ConnectionManager](ConnectionManager.md) (5 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/realtime/connection_delegates.py`
- `server/realtime/connection_error_methods.py`
- `server/tests/unit/realtime/test_connection_error_methods.py`

## Audit Trail

- EXTRACTED: 74 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*