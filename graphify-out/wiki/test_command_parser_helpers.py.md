# test_command_parser_helpers.py

> 59 nodes · cohesion 0.06

## Key Concepts

- **test_combat_handler.py** (39 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **_handler_with_persistence()** (22 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **asyncio** (14 connections)
- **_as_app_with_state()** (9 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **test_get_player_and_room_no_current_room()** (7 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **test_get_player_and_room_success()** (7 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **test_get_player_and_room_unknown_player()** (7 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **test_get_player_and_room_unknown_room()** (7 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **test_resolve_combat_target_accepts_live_phantom()** (6 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **test_resolve_combat_target_rejects_dead_npc()** (6 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **test_resolve_combat_target_rejects_dissipated_phantom()** (6 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **test_resolve_combat_target_rejects_non_npc()** (6 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **_AppStatePersistence** (5 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **_AppWithPersistence** (5 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **test_get_player_and_room_no_persistence_on_app()** (5 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **test_resolve_combat_target_failure_message()** (5 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **test_combat_command_handler_extras_optional()** (4 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **test_handle_flee_command_delegates()** (4 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **test_handle_taunt_command_delegates()** (4 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **test_validate_combat_action()** (4 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **test_validate_combat_action_empty_name()** (4 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **_CmdType** (3 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **mock_persistence()** (3 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **test_combat_command_handler_requires_async_persistence()** (3 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **test_extract_combat_command_data_enum_value()** (3 connections) — `server/tests/unit/commands/test_combat_handler.py`
- *... and 34 more nodes in this community*

## Relationships

- [NPCCombatLucidity](NPCCombatLucidity.md) (6 shared connections)
- [RoomService](RoomService.md) (5 shared connections)
- [PlayerPositionService](PlayerPositionService.md) (4 shared connections)
- [test_help_docs.py](test_help_docs.py.md) (4 shared connections)
- [command_parser.py](command_parser.py.md) (2 shared connections)
- [InventorySchemaValidationError](InventorySchemaValidationError.md) (2 shared connections)

## Source Files

- `server/tests/unit/commands/test_combat_handler.py`

## Audit Trail

- EXTRACTED: 118 (92%)
- INFERRED: 10 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*