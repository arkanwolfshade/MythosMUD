# NPCCombatLucidity

> 73 nodes · cohesion 0.05

## Key Concepts

- **TargetResolutionResult** (38 connections) — `server/schemas/shared/target_resolution.py`
- **test_follow_commands.py** (23 connections) — `server/tests/unit/commands/test_follow_commands.py`
- **follow_commands.py** (20 connections) — `server/commands/follow_commands.py`
- **handle_follow_command()** (18 connections) — `server/commands/follow_commands.py`
- **.async_persistence()** (15 connections) — `server/commands/cleanse_command.py`
- **asyncio** (13 connections)
- **_make_container()** (12 connections) — `server/tests/unit/commands/test_follow_commands.py`
- **_make_request()** (12 connections) — `server/tests/unit/commands/test_follow_commands.py`
- **handle_following_command()** (11 connections) — `server/commands/follow_commands.py`
- **handle_unfollow_command()** (11 connections) — `server/commands/follow_commands.py`
- **test_handle_follow_same_room_npc_immediate()** (8 connections) — `server/tests/unit/commands/test_follow_commands.py`
- **test_handle_follow_same_room_player_sends_request()** (8 connections) — `server/tests/unit/commands/test_follow_commands.py`
- **test_handle_follow_self_rejected()** (8 connections) — `server/tests/unit/commands/test_follow_commands.py`
- **test_handle_follow_no_such_player_or_npc()** (7 connections) — `server/tests/unit/commands/test_follow_commands.py`
- **.resolve_combat_target()** (6 connections) — `server/commands/combat_handler.py`
- **_get_container()** (6 connections) — `server/commands/follow_commands.py`
- **_load_follow_context()** (6 connections) — `server/commands/follow_commands.py`
- **Any** (6 connections)
- **test_handle_follow_no_persistence()** (6 connections) — `server/tests/unit/commands/test_follow_commands.py`
- **test_handle_follow_no_target()** (6 connections) — `server/tests/unit/commands/test_follow_commands.py`
- **test_handle_follow_player_not_in_game()** (6 connections) — `server/tests/unit/commands/test_follow_commands.py`
- **test_handle_following_display()** (6 connections) — `server/tests/unit/commands/test_follow_commands.py`
- **test_handle_unfollow_success()** (6 connections) — `server/tests/unit/commands/test_follow_commands.py`
- **test_handle_unfollow_was_not_following()** (6 connections) — `server/tests/unit/commands/test_follow_commands.py`
- **._validate_combat_target_match()** (5 connections) — `server/commands/combat_handler.py`
- *... and 48 more nodes in this community*

## Relationships

- [command_parser.py](command_parser.py.md) (14 shared connections)
- [RoomService](RoomService.md) (14 shared connections)
- [PlayerPositionService](PlayerPositionService.md) (11 shared connections)
- [test_user_manager.py](test_user_manager.py.md) (6 shared connections)
- [test_command_parser_helpers.py](test_command_parser_helpers.py.md) (6 shared connections)
- [test_help_docs.py](test_help_docs.py.md) (4 shared connections)
- [MemoryThresholdMonitor](MemoryThresholdMonitor.md) (3 shared connections)
- [InventorySchemaValidationError](InventorySchemaValidationError.md) (3 shared connections)
- [.load_room_data](load_room_data.md) (3 shared connections)
- [test_nats_message_handler.py](test_nats_message_handler.py.md) (3 shared connections)
- [test_player_respawn_api.py](test_player_respawn_api.py.md) (2 shared connections)
- [Room](Room.md) (2 shared connections)

## Source Files

- `server/commands/cleanse_command.py`
- `server/commands/combat_handler.py`
- `server/commands/follow_commands.py`
- `server/schemas/shared/target_resolution.py`
- `server/tests/unit/commands/test_follow_commands.py`
- `server/tests/unit/schemas/test_target_resolution.py`

## Audit Trail

- EXTRACTED: 192 (88%)
- INFERRED: 25 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*