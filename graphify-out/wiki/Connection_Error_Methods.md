# Connection Error Methods

> 35 nodes

## Key Concepts

- **test_connection_error_methods.py** (15 connections) — `server/tests/unit/realtime/test_connection_error_methods.py`
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
- **.handle_authentication_error()** (4 connections) — `server/realtime/connection_manager.py`
- **.handle_security_violation()** (4 connections) — `server/realtime/connection_manager.py`
- **.handle_websocket_error()** (4 connections) — `server/realtime/connection_manager.py`
- **.recover_from_error()** (4 connections) — `server/realtime/connection_manager.py`
- **test_detect_and_handle_error_state_impl_delegates()** (3 connections) — `server/tests/unit/realtime/test_connection_error_methods.py`
- **test_error_impl_returns_default_when_handler_missing()** (3 connections) — `server/tests/unit/realtime/test_connection_error_methods.py`
- **test_handle_authentication_error_impl_delegates()** (3 connections) — `server/tests/unit/realtime/test_connection_error_methods.py`
- **test_handle_security_violation_impl_delegates()** (3 connections) — `server/tests/unit/realtime/test_connection_error_methods.py`
- **test_handle_websocket_error_impl_delegates()** (3 connections) — `server/tests/unit/realtime/test_connection_error_methods.py`
- **test_recover_from_error_impl_delegates()** (3 connections) — `server/tests/unit/realtime/test_connection_error_methods.py`
- **manager()** (2 connections) — `server/tests/unit/realtime/test_connection_error_methods.py`
- **fixture** (1 connections)
- **Error-handling method implementations for ConnectionManager. Thin wrappers that…** (1 connections) — `server/realtime/connection_error_methods.py`
- **Detect when a client is in an error state and handle it appropriately.** (1 connections) — `server/realtime/connection_error_methods.py`
- *... and 10 more nodes in this community*

## Relationships

- [Connection Manager](Connection_Manager.md) (10 shared connections)
- [Test Connection Delegates](Test_Connection_Delegates.md) (7 shared connections)
- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (6 shared connections)
- [Container Exception Handling](Container_Exception_Handling.md) (1 shared connections)

## Source Files

- `server/realtime/connection_error_methods.py`
- `server/realtime/connection_manager.py`
- `server/tests/unit/realtime/test_connection_error_methods.py`

## Audit Trail

- EXTRACTED: 83 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*