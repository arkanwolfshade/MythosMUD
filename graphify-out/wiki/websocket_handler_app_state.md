# websocket handler app state

> 96 nodes

## Key Concepts

- **test_websocket_handler_coverage_gaps.py** (24 connections) — `server/tests/unit/realtime/test_websocket_handler_coverage_gaps.py`
- **test_websocket_handler_app_state_connection.py** (23 connections) — `server/tests/unit/realtime/test_websocket_handler_app_state_connection.py`
- **handle_websocket_connection()** (21 connections) — `server/realtime/websocket_handler.py`
- **resolve_and_setup_app_state_services()** (20 connections) — `server/realtime/websocket_handler_app_state.py`
- **handle_chat_message()** (18 connections) — `server/realtime/websocket_handler.py`
- **websocket_handler_app_state.py** (11 connections) — `server/realtime/websocket_handler_app_state.py`
- **load_player_mute_data()** (7 connections) — `server/realtime/websocket_helpers.py`
- **Test _resolve_and_setup_app_state_services when app_state is None.** (5 connections) — `server/tests/unit/realtime/test_websocket_handler_app_state_connection.py`
- **WebSocket** (4 connections)
- **_services_from_container()** (4 connections) — `server/realtime/websocket_handler_app_state.py`
- **UUID** (3 connections)
- **_mirror_service_to_app_state()** (3 connections) — `server/realtime/websocket_handler_app_state.py`
- **test_resolve_and_setup_app_state_services_services_already_set()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_app_state_connection.py`
- **test_resolve_and_setup_app_state_services_missing_services()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_app_state_connection.py`
- **test_resolve_and_setup_app_state_services_no_app_state()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_app_state_connection.py`
- **test_resolve_and_setup_app_state_services_container_no_services()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_app_state_connection.py`
- **test_resolve_and_setup_app_state_services_no_container_attribute()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_app_state_connection.py`
- **test_resolve_and_setup_app_state_services_only_player_service()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_app_state_connection.py`
- **test_resolve_and_setup_app_state_services_only_user_manager()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_app_state_connection.py`
- **test_resolve_and_setup_app_state_services_player_service_already_set()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_app_state_connection.py`
- **test_resolve_and_setup_app_state_services_user_manager_already_set()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_app_state_connection.py`
- **test_resolve_and_setup_app_state_services_player_service_no_hasattr()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_app_state_connection.py`
- **test_resolve_and_setup_app_state_services_user_manager_no_hasattr()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_app_state_connection.py`
- **test_handle_websocket_connection_shutdown_rejected()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_app_state_connection.py`
- **test_handle_websocket_connection_connect_failure()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_app_state_connection.py`
- *... and 71 more nodes in this community*

## Relationships

- [websocket handler commands](websocket_handler_commands.md) (11 shared connections)
- [. init ()](_init_%28%29.md) (9 shared connections)
- [.model dump()](model_dump%28%29.md) (4 shared connections)
- [Send a system message to](Send_a_system_message_to.md) (4 shared connections)
- [real time](real_time.md) (3 shared connections)
- [message handlers](message_handlers.md) (2 shared connections)
- [command execution request](command_execution_request.md) (2 shared connections)
- [main()](main%28%29.md) (2 shared connections)
- [Any](Any.md) (2 shared connections)
- [UUID](UUID.md) (1 shared connections)
- [.get room by id()](get_room_by_id%28%29.md) (1 shared connections)

## Source Files

- `server/realtime/websocket_handler.py`
- `server/realtime/websocket_handler_app_state.py`
- `server/realtime/websocket_helpers.py`
- `server/tests/unit/realtime/test_websocket_handler_app_state_connection.py`
- `server/tests/unit/realtime/test_websocket_handler_core.py`
- `server/tests/unit/realtime/test_websocket_handler_coverage_gaps.py`
- `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`

## Audit Trail

- EXTRACTED: 295 (98%)
- INFERRED: 6 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*