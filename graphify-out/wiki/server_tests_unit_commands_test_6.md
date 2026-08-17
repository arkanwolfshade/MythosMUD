# server tests unit commands test

> 55 nodes

## Key Concepts

- **test_combat_handler.py** (38 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **_handler_with_persistence()** (20 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **asyncio** (12 connections)
- **_as_app_with_state()** (9 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **test_get_player_and_room_no_current_room()** (7 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **test_get_player_and_room_success()** (7 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **test_get_player_and_room_unknown_player()** (7 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **test_get_player_and_room_unknown_room()** (7 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **test_resolve_combat_target_rejects_dead_npc()** (6 connections) — `server/tests/unit/commands/test_combat_handler.py`
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
- **test_extract_combat_command_data_string_type()** (3 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **test_room_forbids_combat_false_no_attrs()** (3 connections) — `server/tests/unit/commands/test_combat_handler.py`
- *... and 30 more nodes in this community*

## Relationships

- [server commands combat app protocols](server_commands_combat_app_protocols.md) (5 shared connections)
- [server commands combat handler combatcommandhandler](server_commands_combat_handler_combatcommandhandler.md) (4 shared connections)
- [server schemas shared target metadata](server_schemas_shared_target_metadata.md) (4 shared connections)
- [server commands combat taunt rationale](server_commands_combat_taunt_rationale.md) (3 shared connections)
- [server commands combat](server_commands_combat.md) (2 shared connections)
- [characterinfo](characterinfo.md) (1 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (1 shared connections)

## Source Files

- `server/tests/unit/commands/test_combat_handler.py`

## Audit Trail

- EXTRACTED: 107 (91%)
- INFERRED: 10 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*