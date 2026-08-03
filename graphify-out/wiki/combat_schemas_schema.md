# combat schemas schema

> 43 nodes

## Key Concepts

- **test_websocket_handler_coverage_gaps.py** (24 connections) — `server/tests/unit/realtime/test_websocket_handler_coverage_gaps.py`
- **handle_chat_message()** (18 connections) — `server/realtime/websocket_handler.py`
- **UUID** (3 connections)
- **test_handle_chat_message()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_handle_websocket_connection_full_flow()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_coverage_gaps.py`
- **test_process_websocket_command_resolve_connection_manager_from_app()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_coverage_gaps.py`
- **test_handle_chat_message_resolve_connection_manager_from_app()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_coverage_gaps.py`
- **test_handle_chat_message_exception_handling()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_coverage_gaps.py`
- **test_handle_chat_message_runtime_error_handling()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_coverage_gaps.py`
- **test_handle_websocket_connection_no_connection_manager()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_coverage_gaps.py`
- **test_handle_websocket_connection_connect_failed()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_coverage_gaps.py`
- **test_handle_websocket_connection_setup_fails()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_coverage_gaps.py`
- **test_handle_websocket_connection_welcome_fails()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_coverage_gaps.py`
- **test_handle_chat_message_no_player()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- **test_message_loop_should_raise_exception()** (2 connections) — `server/tests/unit/realtime/test_websocket_handler_coverage_gaps.py`
- **test_process_exception_in_message_loop()** (2 connections) — `server/tests/unit/realtime/test_websocket_handler_coverage_gaps.py`
- **test_setup_initial_connection_state_should_exit()** (2 connections) — `server/tests/unit/realtime/test_websocket_handler_coverage_gaps.py`
- **test_setup_initial_connection_state_with_room()** (2 connections) — `server/tests/unit/realtime/test_websocket_handler_coverage_gaps.py`
- **test_setup_initial_connection_state_websocket_disconnect()** (2 connections) — `server/tests/unit/realtime/test_websocket_handler_coverage_gaps.py`
- **test_send_welcome_event_already_disconnected()** (2 connections) — `server/tests/unit/realtime/test_websocket_handler_coverage_gaps.py`
- **test_send_welcome_event_close_message_sent()** (2 connections) — `server/tests/unit/realtime/test_websocket_handler_coverage_gaps.py`
- **test_send_welcome_event_cannot_call_error()** (2 connections) — `server/tests/unit/realtime/test_websocket_handler_coverage_gaps.py`
- **Handle a chat message from a player.      Args:         websocket: The WebSocket** (1 connections) — `server/realtime/websocket_handler.py`
- **Test handle_chat_message handles chat message.** (1 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **Unit tests to fill coverage gaps in websocket_handler.py.  These tests target sp** (1 connections) — `server/tests/unit/realtime/test_websocket_handler_coverage_gaps.py`
- *... and 18 more nodes in this community*

## Relationships

- [combat commands handler](combat_commands_handler.md) (7 shared connections)
- [websocket validation realtime](websocket_validation_realtime.md) (6 shared connections)
- [websocket realtime handler](websocket_realtime_handler.md) (3 shared connections)
- [room look commands](room_look_commands.md) (3 shared connections)
- [combat services messaging](combat_services_messaging.md) (2 shared connections)
- [websocket handler realtime](websocket_handler_realtime.md) (2 shared connections)
- [Error Handling Core](Error_Handling_Core.md) (1 shared connections)
- [command inventory factories](command_inventory_factories.md) (1 shared connections)

## Source Files

- `server/realtime/websocket_handler.py`
- `server/tests/unit/realtime/test_websocket_handler_core.py`
- `server/tests/unit/realtime/test_websocket_handler_coverage_gaps.py`
- `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`

## Audit Trail

- EXTRACTED: 114 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*