# websocket handler realtime

> 35 nodes

## Key Concepts

- **test_websocket_handler_commands.py** (28 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- **resolve_websocket_connection_manager()** (11 connections) — `server/realtime/websocket_handler_commands.py`
- **validate_player_and_persistence()** (9 connections) — `server/realtime/websocket_handler_commands.py`
- **parse_game_command_tokens()** (8 connections) — `server/realtime/websocket_handler_commands.py`
- **_attach_room_state_to_result()** (8 connections) — `server/realtime/websocket_handler_commands.py`
- **_resolve_get_room_state_callable()** (6 connections) — `server/realtime/websocket_handler_commands.py`
- **test_process_websocket_command_attaches_room_state()** (5 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- **test_process_websocket_command_room_state_get_room_fails_softly()** (5 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- **_cm_with_player_and_app()** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- **Path** (4 connections)
- **test_process_websocket_command_room_changed_no_player_handler_skips_room_state()** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- **_invoke_get_room_state_event()** (3 connections) — `server/realtime/websocket_handler_commands.py`
- **test_handle_game_command_broadcasts_when_result_requests()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- **test_attach_room_state_to_result_adds_room_state_when_available()** (2 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- **test_attach_room_state_to_result_noop_when_room_not_changed()** (2 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- **test_parse_game_command_tokens_splits_string()** (2 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- **test_parse_game_command_tokens_empty_returns_none()** (2 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- **test_parse_game_command_tokens_explicit_args()** (2 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- **test_parse_game_command_tokens_single_word_no_args()** (2 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- **test_resolve_websocket_connection_manager_uses_passed()** (2 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- **test_resolve_get_room_state_callable_requires_player_handler_with_method()** (2 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- **test_resolve_websocket_connection_manager_fallback_app_state()** (2 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- **test_validate_player_and_persistence_not_found()** (2 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- **test_validate_player_and_persistence_missing_room_attr()** (2 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- **test_validate_player_and_persistence_no_persistence()** (2 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- *... and 10 more nodes in this community*

## Relationships

- [room look commands](room_look_commands.md) (9 shared connections)
- [models npc rationale](models_npc_rationale.md) (8 shared connections)
- [realtime player connection](realtime_player_connection.md) (5 shared connections)
- [command utility models](command_utility_models.md) (2 shared connections)
- [NATS Messaging](NATS_Messaging.md) (1 shared connections)

## Source Files

- `server/realtime/websocket_handler_commands.py`
- `server/tests/unit/realtime/test_websocket_handler_commands.py`

## Audit Trail

- EXTRACTED: 130 (98%)
- INFERRED: 3 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*