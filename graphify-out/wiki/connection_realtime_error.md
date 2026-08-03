# connection realtime error

> 20 nodes

## Key Concepts

- **delegate_error_handler()** (12 connections) — `server/realtime/connection_delegates.py`
- **connection_error_methods.py** (10 connections) — `server/realtime/connection_error_methods.py`
- **detect_and_handle_error_state_impl()** (7 connections) — `server/realtime/connection_error_methods.py`
- **handle_websocket_error_impl()** (7 connections) — `server/realtime/connection_error_methods.py`
- **handle_authentication_error_impl()** (7 connections) — `server/realtime/connection_error_methods.py`
- **handle_security_violation_impl()** (7 connections) — `server/realtime/connection_error_methods.py`
- **recover_from_error_impl()** (7 connections) — `server/realtime/connection_error_methods.py`
- **UUID** (6 connections)
- **Any** (5 connections)
- **test_delegate_error_handler_success()** (3 connections) — `server/tests/unit/realtime/test_connection_delegates.py`
- **test_delegate_error_handler_none()** (3 connections) — `server/tests/unit/realtime/test_connection_delegates.py`
- **Generic delegate for error handler methods.      Args:         error_handler: Er** (1 connections) — `server/realtime/connection_delegates.py`
- **Error-handling method implementations for ConnectionManager.  Thin wrappers that** (1 connections) — `server/realtime/connection_error_methods.py`
- **Detect when a client is in an error state and handle it appropriately.** (1 connections) — `server/realtime/connection_error_methods.py`
- **Handle WebSocket-specific errors.** (1 connections) — `server/realtime/connection_error_methods.py`
- **Handle authentication-related errors.** (1 connections) — `server/realtime/connection_error_methods.py`
- **Handle security violations.** (1 connections) — `server/realtime/connection_error_methods.py`
- **Attempt to recover from an error state for a player.** (1 connections) — `server/realtime/connection_error_methods.py`
- **Test delegate_error_handler() successfully delegates to handler.** (1 connections) — `server/tests/unit/realtime/test_connection_delegates.py`
- **Test delegate_error_handler() returns default when handler is None.** (1 connections) — `server/tests/unit/realtime/test_connection_delegates.py`

## Relationships

- [Room Broadcast](Room_Broadcast.md) (11 shared connections)
- [connection realtime delegates](connection_realtime_delegates.md) (6 shared connections)

## Source Files

- `server/realtime/connection_delegates.py`
- `server/realtime/connection_error_methods.py`
- `server/tests/unit/realtime/test_connection_delegates.py`

## Audit Trail

- EXTRACTED: 83 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*