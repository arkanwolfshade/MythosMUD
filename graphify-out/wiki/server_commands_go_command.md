# server commands go command

> 80 nodes

## Key Concepts

- **test_go_command.py** (33 connections) — `server/tests/unit/commands/test_go_command.py`
- **go_command.py** (30 connections) — `server/commands/go_command.py`
- **handle_go_command()** (20 connections) — `server/commands/go_command.py`
- **asyncio** (15 connections)
- **_setup_go_command()** (13 connections) — `server/commands/go_command.py`
- **Any** (12 connections)
- **_execute_movement()** (10 connections) — `server/commands/go_command.py`
- **_validate_exit()** (10 connections) — `server/commands/go_command.py`
- **_validate_player_posture()** (10 connections) — `server/commands/go_command.py`
- **_cancel_rest_if_moving()** (7 connections) — `server/commands/go_command.py`
- **_movement_combat_and_event_bus_from_go_app()** (6 connections) — `server/commands/go_command.py`
- **_movement_service_for_go_command()** (6 connections) — `server/commands/go_command.py`
- **_canonical_room_id_for_go()** (4 connections) — `server/commands/go_command.py`
- **_connection_manager_from_go_app()** (4 connections) — `server/commands/go_command.py`
- **_resolve_async_persistence_from_go_app()** (4 connections) — `server/commands/go_command.py`
- **_resolved_direction_for_go_command()** (4 connections) — `server/commands/go_command.py`
- **test_execute_movement_error_handling()** (4 connections) — `server/tests/unit/commands/test_go_command.py`
- **test_execute_movement_failure()** (4 connections) — `server/tests/unit/commands/test_go_command.py`
- **test_execute_movement_fallback_service()** (4 connections) — `server/tests/unit/commands/test_go_command.py`
- **test_execute_movement_success()** (4 connections) — `server/tests/unit/commands/test_go_command.py`
- **test_handle_go_command_invalid_posture()** (4 connections) — `server/tests/unit/commands/test_go_command.py`
- **test_handle_go_command_no_direction()** (4 connections) — `server/tests/unit/commands/test_go_command.py`
- **test_handle_go_command_no_exit()** (4 connections) — `server/tests/unit/commands/test_go_command.py`
- **test_handle_go_command_rest_interrupt_still_moves()** (4 connections) — `server/tests/unit/commands/test_go_command.py`
- **test_handle_go_command_setup_failure()** (4 connections) — `server/tests/unit/commands/test_go_command.py`
- *... and 55 more nodes in this community*

## Relationships

- [claude rules asyncio](claude_rules_asyncio.md) (5 shared connections)
- [server commands rest command](server_commands_rest_command.md) (3 shared connections)
- [server game dialogue dialogue service](server_game_dialogue_dialogue_service.md) (3 shared connections)
- [server commands combat handler combatcommandhandler](server_commands_combat_handler_combatcommandhandler.md) (2 shared connections)
- [server commands exploration commands](server_commands_exploration_commands.md) (2 shared connections)
- [server alias storage aliasstorage](server_alias_storage_aliasstorage.md) (2 shared connections)
- [server commands admin commands](server_commands_admin_commands.md) (2 shared connections)
- [server game movement service movementservice](server_game_movement_service_movementservice.md) (2 shared connections)
- [server game magic spell targeting](server_game_magic_spell_targeting.md) (1 shared connections)
- [eventbus](eventbus.md) (1 shared connections)
- [attributeerror](attributeerror.md) (1 shared connections)
- [scripts populate test npc databases](scripts_populate_test_npc_databases.md) (1 shared connections)

## Source Files

- `server/commands/go_command.py`
- `server/tests/unit/commands/test_go_command.py`

## Audit Trail

- EXTRACTED: 168 (97%)
- INFERRED: 5 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*