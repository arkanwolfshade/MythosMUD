# test_room_subscription_manager_drops.py

> 52 nodes · cohesion 0.09

## Key Concepts

- **test_websocket_handler_commands.py** (41 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- **handle_game_command()** (32 connections) — `server/realtime/websocket_handler_commands.py`
- **process_websocket_command()** (20 connections) — `server/realtime/websocket_handler_commands.py`
- **asyncio** (18 connections)
- **Path** (11 connections)
- **resolve_websocket_connection_manager()** (10 connections) — `server/realtime/websocket_handler_commands.py`
- **_run_game_command_with_unified_result()** (10 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- **validate_player_and_persistence()** (9 connections) — `server/realtime/websocket_handler_commands.py`
- **_attach_room_state_to_result()** (8 connections) — `server/realtime/websocket_handler_commands.py`
- **parse_game_command_tokens()** (8 connections) — `server/realtime/websocket_handler_commands.py`
- **_player_cm()** (7 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- **test_command_response_keeps_system_error_from_command_error()** (7 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- **_resolve_get_room_state_callable()** (6 connections) — `server/realtime/websocket_handler_commands.py`
- **test_command_response_carries_the_handlers_segments_untouched()** (6 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- **test_command_response_defaults_to_command_output_category()** (6 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- **test_command_response_keeps_a_handler_supplied_category()** (6 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- **test_process_websocket_command_attaches_room_state()** (6 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- **test_process_websocket_command_room_state_get_room_fails_softly()** (6 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- **test_room_broadcast_defaults_to_command_output_category()** (6 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- **test_room_broadcast_uses_broadcast_category_override()** (6 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- **test_process_websocket_command_room_changed_no_player_handler_skips_room_state()** (5 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- **_cm_with_player_and_app()** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- **test_handle_game_command_broadcasts_when_result_requests()** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- **test_process_websocket_command_player_not_found_is_system_error()** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- **test_validate_player_and_persistence_missing_room_attr()** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- *... and 27 more nodes in this community*

## Relationships

- [look_container.py](look_container.py.md) (22 shared connections)
- [NATSService](NATSService.md) (12 shared connections)
- [Alias](Alias.md) (7 shared connections)
- [resolve_weapon_attack_from_equipped](resolve_weapon_attack_from_equipped.md) (4 shared connections)
- [test_corpse_lifecycle_decay.py](test_corpse_lifecycle_decay.py.md) (4 shared connections)
- [command_parser.py](command_parser.py.md) (3 shared connections)
- [.publish_with_pool](publish_with_pool.md) (2 shared connections)
- [test_game.py](test_game.py.md) (1 shared connections)
- [EventBus](EventBus.md) (1 shared connections)
- [test_command_admin.py](test_command_admin.py.md) (1 shared connections)
- [._bind_event_type](_bind_event_type.md) (1 shared connections)
- [security.ts](security.ts.md) (1 shared connections)

## Source Files

- `server/realtime/websocket_handler_commands.py`
- `server/tests/unit/realtime/test_websocket_handler_commands.py`

## Audit Trail

- EXTRACTED: 148 (83%)
- INFERRED: 31 (17%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*