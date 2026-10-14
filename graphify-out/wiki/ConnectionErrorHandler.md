# ConnectionErrorHandler

> 43 nodes

## Key Concepts

- **ConnectionErrorHandler** (28 connections) — `server/realtime/errors/error_handler.py`
- **test_connection_error_handler.py** (15 connections) — `server/tests/unit/realtime/test_connection_error_handler.py`
- **initialize_error_handler()** (9 connections) — `server/realtime/connection_initialization.py`
- **.detect_and_handle_error_state()** (9 connections) — `server/realtime/errors/error_handler.py`
- **UUID** (9 connections)
- **asyncio** (9 connections)
- **ConnectionErrorHandlerCallbacks** (7 connections) — `server/realtime/errors/error_handler.py`
- **Any** (7 connections)
- **.get_error_statistics()** (5 connections) — `server/realtime/errors/error_handler.py`
- **.handle_authentication_error()** (5 connections) — `server/realtime/errors/error_handler.py`
- **.handle_security_violation()** (5 connections) — `server/realtime/errors/error_handler.py`
- **.handle_websocket_error()** (5 connections) — `server/realtime/errors/error_handler.py`
- **._terminate_connections_for_error()** (5 connections) — `server/realtime/errors/error_handler.py`
- **._write_error_log_entry()** (5 connections) — `server/realtime/errors/error_handler.py`
- **.recover_from_error()** (4 connections) — `server/realtime/errors/error_handler.py`
- **handler()** (4 connections) — `server/tests/unit/realtime/test_connection_error_handler.py`
- **.__init__()** (3 connections) — `server/realtime/errors/error_handler.py`
- **test_connection_specific_error()** (3 connections) — `server/tests/unit/realtime/test_connection_error_handler.py`
- **test_disconnect_failure_records_error()** (3 connections) — `server/tests/unit/realtime/test_connection_error_handler.py`
- **test_fatal_error_force_disconnect()** (3 connections) — `server/tests/unit/realtime/test_connection_error_handler.py`
- **test_handle_authentication_error()** (3 connections) — `server/tests/unit/realtime/test_connection_error_handler.py`
- **test_handle_security_violation()** (3 connections) — `server/tests/unit/realtime/test_connection_error_handler.py`
- **test_handle_websocket_critical_error()** (3 connections) — `server/tests/unit/realtime/test_connection_error_handler.py`
- **test_non_fatal_error_keeps_connections()** (3 connections) — `server/tests/unit/realtime/test_connection_error_handler.py`
- **test_recover_connections_only()** (3 connections) — `server/tests/unit/realtime/test_connection_error_handler.py`
- *... and 18 more nodes in this community*

## Relationships

- [connection_initialization.py](connection_initialization.py.md) (7 shared connections)
- [get_logger](get_logger.md) (7 shared connections)
- [CombatService](CombatService.md) (2 shared connections)
- [connection_manager_methods.py](connection_manager_methods.py.md) (1 shared connections)

## Source Files

- `server/realtime/connection_initialization.py`
- `server/realtime/errors/__init__.py`
- `server/realtime/errors/error_handler.py`
- `server/tests/unit/realtime/test_connection_error_handler.py`

## Audit Trail

- EXTRACTED: 88 (89%)
- INFERRED: 11 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*