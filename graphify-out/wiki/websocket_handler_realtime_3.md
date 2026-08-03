# websocket handler realtime

> 120 nodes

## Key Concepts

- **test_websocket_handler_core.py** (42 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **websocket_handler_commands.py** (32 connections) — `server/realtime/websocket_handler_commands.py`
- **handle_game_command()** (29 connections) — `server/realtime/websocket_handler_commands.py`
- **test_websocket_handler_commands.py** (28 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- **process_websocket_command()** (19 connections) — `server/realtime/websocket_handler_commands.py`
- **resolve_websocket_connection_manager()** (11 connections) — `server/realtime/websocket_handler_commands.py`
- **handle_websocket_message()** (10 connections) — `server/realtime/websocket_handler.py`
- **_websocket_unified_command_result()** (10 connections) — `server/realtime/websocket_handler_commands.py`
- **validate_player_and_persistence()** (9 connections) — `server/realtime/websocket_handler_commands.py`
- **parse_game_command_tokens()** (8 connections) — `server/realtime/websocket_handler_commands.py`
- **_attach_room_state_to_result()** (8 connections) — `server/realtime/websocket_handler_commands.py`
- **_resolve_get_room_state_callable()** (6 connections) — `server/realtime/websocket_handler_commands.py`
- **is_client_disconnected_exception()** (6 connections) — `server/realtime/websocket_helpers.py`
- **event_handler()** (6 connections) — `server/tests/unit/realtime/test_event_handler.py`
- **test_process_websocket_command_attaches_room_state()** (5 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- **test_process_websocket_command_room_state_get_room_fails_softly()** (5 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- **WebSocket** (4 connections)
- **_send_invalid_command_empty()** (4 connections) — `server/realtime/websocket_handler_commands.py`
- **_broadcast_command_room_if_needed()** (4 connections) — `server/realtime/websocket_handler_commands.py`
- **_cm_with_player_and_app()** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- **Path** (4 connections)
- **test_process_websocket_command_room_changed_no_player_handler_skips_room_state()** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- **_invoke_get_room_state_event()** (3 connections) — `server/realtime/websocket_handler_commands.py`
- **test_handle_game_command_broadcasts_when_result_requests()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- **test_handle_generic_exception()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- *... and 95 more nodes in this community*

## Relationships

- [websocket handler realtime](websocket_handler_realtime.md) (12 shared connections)
- [websocket validation realtime](websocket_validation_realtime.md) (11 shared connections)
- [Error Handling Core](Error_Handling_Core.md) (11 shared connections)
- [websocket realtime handler](websocket_realtime_handler.md) (8 shared connections)
- [commands alias rationale](commands_alias_rationale.md) (6 shared connections)
- [combat services messaging](combat_services_messaging.md) (4 shared connections)
- [NATS Messaging](NATS_Messaging.md) (3 shared connections)
- [realtime game state](realtime_game_state.md) (3 shared connections)
- [command handler unified](command_handler_unified.md) (2 shared connections)
- [Item Instances](Item_Instances.md) (2 shared connections)
- [Room Broadcast](Room_Broadcast.md) (2 shared connections)
- [request context realtime](request_context_realtime.md) (2 shared connections)

## Source Files

- `server/realtime/websocket_handler.py`
- `server/realtime/websocket_handler_commands.py`
- `server/realtime/websocket_helpers.py`
- `server/tests/unit/realtime/test_event_handler.py`
- `server/tests/unit/realtime/test_websocket_handler_commands.py`
- `server/tests/unit/realtime/test_websocket_handler_core.py`

## Audit Trail

- EXTRACTED: 382 (90%)
- INFERRED: 42 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*