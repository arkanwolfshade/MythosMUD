# WebSocket Command Handler

> 66 nodes · cohesion 0.05

## Key Concepts

- **websocket_handler_commands.py** (31 connections) — `server/realtime/websocket_handler_commands.py`
- **handle_game_command()** (29 connections) — `server/realtime/websocket_handler_commands.py`
- **test_websocket_handler_commands.py** (27 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- **resolve_websocket_connection_manager()** (9 connections) — `server/realtime/websocket_handler_commands.py`
- **validate_player_and_persistence()** (9 connections) — `server/realtime/websocket_handler_commands.py`
- **_websocket_unified_command_result()** (9 connections) — `server/realtime/websocket_handler_commands.py`
- **_attach_room_state_to_result()** (8 connections) — `server/realtime/websocket_handler_commands.py`
- **parse_game_command_tokens()** (8 connections) — `server/realtime/websocket_handler_commands.py`
- **is_client_disconnected_exception()** (6 connections) — `server/realtime/websocket_helpers.py`
- **test_process_websocket_command_attaches_room_state()** (5 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- **test_process_websocket_command_room_state_get_room_fails_softly()** (5 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- **_resolve_get_room_state_callable()** (5 connections) — `server/realtime/websocket_handler_commands.py`
- **_cm_with_player_and_app()** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- **test_process_websocket_command_room_changed_no_player_handler_skips_room_state()** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- **_broadcast_command_room_if_needed()** (4 connections) — `server/realtime/websocket_handler_commands.py`
- **_send_invalid_command_empty()** (4 connections) — `server/realtime/websocket_handler_commands.py`
- **Path** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- **test_handle_game_command_broadcasts_when_result_requests()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- **test_handle_game_command()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_handle_game_command_empty_command()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_handle_game_command_single_word_no_args()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_handle_game_command_whitespace_only()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_handle_game_command_with_provided_args()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_handle_game_command_broadcast_no_current_room_id()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- **test_handle_game_command_broadcast_no_player()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- *... and 41 more nodes in this community*

## Relationships

- [[Help and WebSocket Core]] (14 shared connections)
- [[WebSocket Handler Helpers]] (5 shared connections)
- [[NPC Admin API]] (5 shared connections)
- [[WebSocket Message Validation]] (5 shared connections)
- [[Pydantic Error Handlers]] (4 shared connections)
- [[Combat Player Broadcasts]] (4 shared connections)
- [[Room Occupant Events]] (3 shared connections)
- [[WebSocket Coverage Gaps]] (3 shared connections)
- [[Alias Expansion Logic]] (2 shared connections)
- [[Unified Command Handler]] (2 shared connections)
- [[Standardized Error Responses]] (2 shared connections)
- [[WebSocket Request Context]] (2 shared connections)

## Source Files

- `server/realtime/websocket_handler_commands.py`
- `server/realtime/websocket_helpers.py`
- `server/tests/unit/realtime/test_websocket_handler_commands.py`
- `server/tests/unit/realtime/test_websocket_handler_core.py`
- `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`

## Audit Trail

- EXTRACTED: 235 (91%)
- INFERRED: 24 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
