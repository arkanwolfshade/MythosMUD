# server realtime connection delegates delegate

> 27 nodes

## Key Concepts

- **delegate_error_handler()** (18 connections) — `server/realtime/connection_delegates.py`
- **test_connection_error_methods.py** (15 connections) — `server/tests/unit/realtime/test_connection_error_methods.py`
- **connection_error_methods.py** (11 connections) — `server/realtime/connection_error_methods.py`
- **detect_and_handle_error_state_impl()** (8 connections) — `server/realtime/connection_error_methods.py`
- **handle_authentication_error_impl()** (7 connections) — `server/realtime/connection_error_methods.py`
- **handle_security_violation_impl()** (7 connections) — `server/realtime/connection_error_methods.py`
- **handle_websocket_error_impl()** (7 connections) — `server/realtime/connection_error_methods.py`
- **recover_from_error_impl()** (7 connections) — `server/realtime/connection_error_methods.py`
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

- [server realtime connection delegates delegate](server_realtime_connection_delegates_delegate.md) (6 shared connections)
- [server realtime connection delegates](server_realtime_connection_delegates.md) (3 shared connections)
- [server realtime connection delegates cleanup](server_realtime_connection_delegates_cleanup.md) (3 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (1 shared connections)
- [characterinfo](characterinfo.md) (1 shared connections)

## Source Files

- `server/realtime/connection_delegates.py`
- `server/realtime/connection_error_methods.py`
- `server/tests/unit/realtime/test_connection_error_methods.py`

## Audit Trail

- EXTRACTED: 70 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*