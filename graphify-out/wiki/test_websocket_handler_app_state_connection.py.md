# test_websocket_handler_app_state_connection.py

> 50 nodes

## Key Concepts

- **test_websocket_handler_app_state_connection.py** (25 connections) — `server/tests/unit/realtime/test_websocket_handler_app_state_connection.py`
- **handle_websocket_connection()** (21 connections) — `server/realtime/websocket_handler.py`
- **resolve_and_setup_app_state_services()** (19 connections) — `server/realtime/websocket_handler_app_state.py`
- **asyncio** (8 connections)
- **load_player_mute_data()** (7 connections) — `server/realtime/websocket_helpers.py`
- **test_handle_websocket_connection_connect_failure()** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_app_state_connection.py`
- **test_handle_websocket_connection_initial_setup_error()** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_app_state_connection.py`
- **test_handle_websocket_connection_initial_state_exit()** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_app_state_connection.py`
- **test_handle_websocket_connection_shutdown_rejected()** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_app_state_connection.py`
- **test_handle_websocket_connection_with_room_and_death()** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_app_state_connection.py`
- **_mirror_service_to_app_state()** (3 connections) — `server/realtime/websocket_handler_app_state.py`
- **_services_from_container()** (3 connections) — `server/realtime/websocket_handler_app_state.py`
- **test_cleanup_connection_mute_cleanup_error()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_app_state_connection.py`
- **test_handle_websocket_message_loop()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_app_state_connection.py`
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
- *... and 25 more nodes in this community*

## Relationships

- [test_websocket_handler_coverage_gaps.py](test_websocket_handler_coverage_gaps.py.md) (6 shared connections)
- [websocket_handler.py](websocket_handler.py.md) (5 shared connections)
- [get_logger](get_logger.md) (4 shared connections)
- [real_time.py](real_time.py.md) (3 shared connections)
- [check_shutdown_and_reject](check_shutdown_and_reject.md) (3 shared connections)
- [websocket_handler_commands.py](websocket_handler_commands.py.md) (2 shared connections)
- [test_websocket_helpers.py](test_websocket_helpers.py.md) (2 shared connections)
- [test_websocket_handler_core.py](test_websocket_handler_core.py.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/realtime/websocket_handler.py`
- `server/realtime/websocket_handler_app_state.py`
- `server/realtime/websocket_helpers.py`
- `server/tests/unit/realtime/test_websocket_handler_app_state_connection.py`

## Audit Trail

- EXTRACTED: 98 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*