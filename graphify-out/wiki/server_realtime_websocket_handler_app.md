# server realtime websocket handler app

> 87 nodes

## Key Concepts

- **test_websocket_handler_coverage_gaps.py** (26 connections) — `server/tests/unit/realtime/test_websocket_handler_coverage_gaps.py`
- **test_websocket_handler_app_state_connection.py** (25 connections) — `server/tests/unit/realtime/test_websocket_handler_app_state_connection.py`
- **handle_websocket_connection()** (21 connections) — `server/realtime/websocket_handler.py`
- **asyncio** (20 connections)
- **resolve_and_setup_app_state_services()** (19 connections) — `server/realtime/websocket_handler_app_state.py`
- **websocket_handler_app_state.py** (11 connections) — `server/realtime/websocket_handler_app_state.py`
- **asyncio** (8 connections)
- **Test _resolve_and_setup_app_state_services when container has no services.** (6 connections) — `server/tests/unit/realtime/test_websocket_handler_app_state_connection.py`
- **test_handle_websocket_connection_connect_failure()** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_app_state_connection.py`
- **test_handle_websocket_connection_initial_setup_error()** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_app_state_connection.py`
- **test_handle_websocket_connection_initial_state_exit()** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_app_state_connection.py`
- **test_handle_websocket_connection_shutdown_rejected()** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_app_state_connection.py`
- **test_handle_websocket_connection_with_room_and_death()** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_app_state_connection.py`
- **test_handle_chat_message_exception_handling()** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_coverage_gaps.py`
- **test_handle_chat_message_resolve_connection_manager_from_app()** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_coverage_gaps.py`
- **test_handle_chat_message_runtime_error_handling()** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_coverage_gaps.py`
- **test_handle_game_command_exception_handling()** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_coverage_gaps.py`
- **test_handle_game_command_resolve_connection_manager_from_app()** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_coverage_gaps.py`
- **test_handle_game_command_runtime_error_handling()** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_coverage_gaps.py`
- **test_handle_websocket_connection_connect_failed()** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_coverage_gaps.py`
- **test_handle_websocket_connection_full_flow()** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_coverage_gaps.py`
- **test_handle_websocket_connection_no_connection_manager()** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_coverage_gaps.py`
- **test_handle_websocket_connection_setup_fails()** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_coverage_gaps.py`
- **test_handle_websocket_connection_welcome_fails()** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_coverage_gaps.py`
- **test_process_websocket_command_resolve_connection_manager_from_app()** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_coverage_gaps.py`
- *... and 62 more nodes in this community*

## Relationships

- [server realtime envelope build event](server_realtime_envelope_build_event.md) (11 shared connections)
- [server realtime websocket handler](server_realtime_websocket_handler.md) (7 shared connections)
- [server api real time](server_api_real_time.md) (3 shared connections)
- [server commands container helpers inventory](server_commands_container_helpers_inventory.md) (2 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (2 shared connections)
- [server command handler command execution](server_command_handler_command_execution.md) (2 shared connections)
- [characterinfo](characterinfo.md) (2 shared connections)
- [claude rules fastapi](claude_rules_fastapi.md) (1 shared connections)

## Source Files

- `server/realtime/websocket_handler.py`
- `server/realtime/websocket_handler_app_state.py`
- `server/tests/unit/realtime/test_websocket_handler_app_state_connection.py`
- `server/tests/unit/realtime/test_websocket_handler_coverage_gaps.py`

## Audit Trail

- EXTRACTED: 167 (97%)
- INFERRED: 5 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*