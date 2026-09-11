# test_connection_error_methods.py

> 31 nodes

## Key Concepts

- **test_connection_error_methods.py** (14 connections) — `server/tests/unit/realtime/test_connection_error_methods.py`
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
- **.detect_and_handle_error_state()** (4 connections) — `server/realtime/connection_manager.py`
- **.handle_security_violation()** (4 connections) — `server/realtime/connection_manager.py`
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
- *... and 6 more nodes in this community*

## Relationships

- [connection_manager.py](connection_manager.py.md) (12 shared connections)
- [UUID](UUID.md) (5 shared connections)
- [ConnectionManager](ConnectionManager.md) (2 shared connections)

## Source Files

- `server/realtime/connection_delegates.py`
- `server/realtime/connection_error_methods.py`
- `server/realtime/connection_manager.py`
- `server/tests/unit/realtime/test_connection_error_methods.py`

## Audit Trail

- EXTRACTED: 79 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*