# chat logger services

> 34 nodes

## Key Concepts

- **test_websocket_handler_core.py** (42 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_handle_generic_exception()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_handle_generic_exception_should_break()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_handle_chat_message()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_send_error_response()** (2 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_handle_json_decode_error()** (2 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_handle_runtime_error()** (2 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_handle_message_loop_exception_json_decode()** (2 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_handle_message_loop_exception_disconnect()** (2 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_process_message()** (2 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_process_message_rate_limit_exceeded()** (2 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_validate_player_and_persistence_success()** (2 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_validate_player_and_persistence_not_found()** (2 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_validate_player_and_persistence_no_persistence()** (2 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_cleanup_connection()** (2 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_resolve_and_setup_app_state_services()** (2 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_resolve_and_setup_app_state_services_no_container()** (2 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **Unit tests for core websocket handler functions.  Tests core WebSocket handler f** (1 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **Test _send_error_response sends error response.** (1 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **Test _handle_json_decode_error sends error response.** (1 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **Test _handle_runtime_error handles runtime error.** (1 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **Test _handle_generic_exception handles generic exception.** (1 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **Test _handle_generic_exception returns True when send_error_response fails.** (1 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **Test _handle_message_loop_exception handles JSON decode error.** (1 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **Test _handle_message_loop_exception handles WebSocket disconnect.** (1 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- *... and 9 more nodes in this community*

## Relationships

- [alias storage rationale](alias_storage_rationale.md) (11 shared connections)
- [persistence container item](persistence_container_item.md) (6 shared connections)
- [handler realtime nats](handler_realtime_nats.md) (3 shared connections)
- [logging examples fastapi](logging_examples_fastapi.md) (3 shared connections)
- [persistence combat services](persistence_combat_services.md) (3 shared connections)
- [Error Handling Core](Error_Handling_Core.md) (1 shared connections)
- [occupant formatter realtime](occupant_formatter_realtime.md) (1 shared connections)

## Source Files

- `server/tests/unit/realtime/test_websocket_handler_core.py`

## Audit Trail

- EXTRACTED: 92 (98%)
- INFERRED: 2 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*