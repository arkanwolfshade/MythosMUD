# WebSocket Handler Tests

> 40 nodes · cohesion 0.07

## Key Concepts

- **test_websocket_handler_app_state_connection.py** (21 connections) — `server/tests/unit/realtime/test_websocket_handler_app_state_connection.py`
- **resolve_and_setup_app_state_services()** (19 connections) — `server/realtime/websocket_handler_app_state.py`
- **Test _resolve_and_setup_app_state_services resolves services.** (7 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_cleanup_connection_mute_cleanup_error()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_app_state_connection.py`
- **test_handle_websocket_connection_connect_failure()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_app_state_connection.py`
- **test_handle_websocket_connection_initial_setup_error()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_app_state_connection.py`
- **test_handle_websocket_connection_initial_state_exit()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_app_state_connection.py`
- **test_handle_websocket_connection_shutdown_rejected()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_app_state_connection.py`
- **test_handle_websocket_connection_with_room_and_death()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_app_state_connection.py`
- **test_resolve_and_setup_app_state_services_container_no_services()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_app_state_connection.py`
- **test_resolve_and_setup_app_state_services_missing_services()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_app_state_connection.py`
- **test_resolve_and_setup_app_state_services_no_app_state()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_app_state_connection.py`
- **test_resolve_and_setup_app_state_services_no_container_attribute()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_app_state_connection.py`
- **test_resolve_and_setup_app_state_services_only_player_service()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_app_state_connection.py`
- **test_resolve_and_setup_app_state_services_only_user_manager()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_app_state_connection.py`
- **test_resolve_and_setup_app_state_services_player_service_already_set()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_app_state_connection.py`
- **test_resolve_and_setup_app_state_services_player_service_no_hasattr()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_app_state_connection.py`
- **test_resolve_and_setup_app_state_services_services_already_set()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_app_state_connection.py`
- **test_resolve_and_setup_app_state_services_user_manager_already_set()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_app_state_connection.py`
- **test_resolve_and_setup_app_state_services_user_manager_no_hasattr()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_app_state_connection.py`
- **test_cleanup_connection()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **_mirror_service_to_app_state()** (3 connections) — `server/realtime/websocket_handler_app_state.py`
- **_services_from_container()** (3 connections) — `server/realtime/websocket_handler_app_state.py`
- **Test _resolve_and_setup_app_state_services when services already set.** (2 connections) — `server/tests/unit/realtime/test_websocket_handler_app_state_connection.py`
- **Test _resolve_and_setup_app_state_services when only player_service is available** (2 connections) — `server/tests/unit/realtime/test_websocket_handler_app_state_connection.py`
- *... and 15 more nodes in this community*

## Relationships

- [[Realtime WebSocket Auth]] (6 shared connections)
- [[NPC Admin API]] (3 shared connections)
- [[Help and WebSocket Core]] (2 shared connections)
- [[WebSocket Command Handler]] (2 shared connections)
- [[Database Manager Tests]] (1 shared connections)
- [[WebSocket Message Validation]] (1 shared connections)

## Source Files

- `server/realtime/websocket_handler_app_state.py`
- `server/tests/unit/realtime/test_websocket_handler_app_state_connection.py`
- `server/tests/unit/realtime/test_websocket_handler_core.py`

## Audit Trail

- EXTRACTED: 126 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
