# command commands aliases

> 278 nodes

## Key Concepts

- **websocket_handler.py** (64 connections) — `server/realtime/websocket_handler.py`
- **test_websocket_handler_core.py** (42 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_websocket_handler_validation_errors.py** (39 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- **websocket_handler_commands.py** (32 connections) — `server/realtime/websocket_handler_commands.py`
- **handle_game_command()** (29 connections) — `server/realtime/websocket_handler_commands.py`
- **test_websocket_handler_commands.py** (28 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- **test_websocket_handler_coverage_gaps.py** (24 connections) — `server/tests/unit/realtime/test_websocket_handler_coverage_gaps.py`
- **test_websocket_handler_app_state_connection.py** (23 connections) — `server/tests/unit/realtime/test_websocket_handler_app_state_connection.py`
- **handle_websocket_connection()** (21 connections) — `server/realtime/websocket_handler.py`
- **resolve_and_setup_app_state_services()** (20 connections) — `server/realtime/websocket_handler_app_state.py`
- **process_websocket_command()** (19 connections) — `server/realtime/websocket_handler_commands.py`
- **handle_chat_message()** (18 connections) — `server/realtime/websocket_handler.py`
- **send_system_message()** (13 connections) — `server/realtime/websocket_handler.py`
- **resolve_websocket_connection_manager()** (11 connections) — `server/realtime/websocket_handler_commands.py`
- **handle_websocket_message()** (10 connections) — `server/realtime/websocket_handler.py`
- **_websocket_unified_command_result()** (10 connections) — `server/realtime/websocket_handler_commands.py`
- **create_websocket_request_context()** (9 connections) — `server/realtime/request_context.py`
- **validate_player_and_persistence()** (9 connections) — `server/realtime/websocket_handler_commands.py`
- **parse_game_command_tokens()** (8 connections) — `server/realtime/websocket_handler_commands.py`
- **_attach_room_state_to_result()** (8 connections) — `server/realtime/websocket_handler_commands.py`
- **test_websocket_handler_system_message.py** (8 connections) — `server/tests/unit/realtime/test_websocket_handler_system_message.py`
- **_resolve_get_room_state_callable()** (6 connections) — `server/realtime/websocket_handler_commands.py`
- **test_process_websocket_command_attaches_room_state()** (5 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- **test_process_websocket_command_room_state_get_room_fails_softly()** (5 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- **WebSocket** (4 connections)
- *... and 253 more nodes in this community*

## Relationships

- [handler realtime nats](handler_realtime_nats.md) (18 shared connections)
- [Error Conversion](Error_Conversion.md) (12 shared connections)
- [occupant formatter realtime](occupant_formatter_realtime.md) (10 shared connections)
- [combat services messaging](combat_services_messaging.md) (9 shared connections)
- [realtime message validator](realtime_message_validator.md) (8 shared connections)
- [room websocket updates](room_websocket_updates.md) (7 shared connections)
- [request context realtime](request_context_realtime.md) (5 shared connections)
- [nats services metrics](nats_services_metrics.md) (4 shared connections)
- [database config helpers](database_config_helpers.md) (4 shared connections)
- [realtime websocket initial](realtime_websocket_initial.md) (4 shared connections)
- [shutdown admin command](shutdown_admin_command.md) (3 shared connections)
- [professions endpoints all](professions_endpoints_all.md) (3 shared connections)

## Source Files

- `server/realtime/request_context.py`
- `server/realtime/websocket_handler.py`
- `server/realtime/websocket_handler_app_state.py`
- `server/realtime/websocket_handler_commands.py`
- `server/tests/unit/realtime/test_websocket_handler_app_state_connection.py`
- `server/tests/unit/realtime/test_websocket_handler_commands.py`
- `server/tests/unit/realtime/test_websocket_handler_core.py`
- `server/tests/unit/realtime/test_websocket_handler_coverage_gaps.py`
- `server/tests/unit/realtime/test_websocket_handler_system_message.py`
- `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`

## Audit Trail

- EXTRACTED: 868 (95%)
- INFERRED: 49 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*