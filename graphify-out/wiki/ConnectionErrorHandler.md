# ConnectionErrorHandler

> 35 nodes

## Key Concepts

- **ConnectionErrorHandler** (24 connections) — `server/realtime/errors/error_handler.py`
- **test_connection_error_handler.py** (14 connections) — `server/tests/unit/realtime/test_connection_error_handler.py`
- **asyncio** (9 connections)
- **.detect_and_handle_error_state()** (8 connections) — `server/realtime/errors/error_handler.py`
- **UUID** (8 connections)
- **Any** (7 connections)
- **.get_error_statistics()** (5 connections) — `server/realtime/errors/error_handler.py`
- **.handle_authentication_error()** (5 connections) — `server/realtime/errors/error_handler.py`
- **.handle_security_violation()** (5 connections) — `server/realtime/errors/error_handler.py`
- **.handle_websocket_error()** (5 connections) — `server/realtime/errors/error_handler.py`
- **.__init__()** (4 connections) — `server/realtime/errors/error_handler.py`
- **.recover_from_error()** (4 connections) — `server/realtime/errors/error_handler.py`
- **handler()** (3 connections) — `server/tests/unit/realtime/test_connection_error_handler.py`
- **test_connection_specific_error()** (3 connections) — `server/tests/unit/realtime/test_connection_error_handler.py`
- **test_disconnect_failure_records_error()** (3 connections) — `server/tests/unit/realtime/test_connection_error_handler.py`
- **test_fatal_error_force_disconnect()** (3 connections) — `server/tests/unit/realtime/test_connection_error_handler.py`
- **test_handle_authentication_error()** (3 connections) — `server/tests/unit/realtime/test_connection_error_handler.py`
- **test_handle_security_violation()** (3 connections) — `server/tests/unit/realtime/test_connection_error_handler.py`
- **test_handle_websocket_critical_error()** (3 connections) — `server/tests/unit/realtime/test_connection_error_handler.py`
- **test_non_fatal_error_keeps_connections()** (3 connections) — `server/tests/unit/realtime/test_connection_error_handler.py`
- **test_recover_connections_only()** (3 connections) — `server/tests/unit/realtime/test_connection_error_handler.py`
- **test_recover_from_error_full()** (3 connections) — `server/tests/unit/realtime/test_connection_error_handler.py`
- **errors/__init__.py** (3 connections) — `server/realtime/errors/__init__.py`
- **test_get_error_statistics()** (2 connections) — `server/tests/unit/realtime/test_connection_error_handler.py`
- **fixture** (1 connections)
- *... and 10 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (5 shared connections)
- [get_config](get_config.md) (2 shared connections)
- [HealthMonitor](HealthMonitor.md) (1 shared connections)

## Source Files

- `server/realtime/errors/__init__.py`
- `server/realtime/errors/error_handler.py`
- `server/tests/unit/realtime/test_connection_error_handler.py`

## Audit Trail

- EXTRACTED: 65 (86%)
- INFERRED: 11 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*