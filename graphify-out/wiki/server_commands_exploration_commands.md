# server commands exploration commands

> 92 nodes

## Key Concepts

- **test_go_command.py** (33 connections) — `server/tests/unit/commands/test_go_command.py`
- **go_command.py** (30 connections) — `server/commands/go_command.py`
- **handle_go_command()** (20 connections) — `server/commands/go_command.py`
- **asyncio** (15 connections)
- **_setup_go_command()** (13 connections) — `server/commands/go_command.py`
- **Any** (12 connections)
- **exploration_commands.py** (11 connections) — `server/commands/exploration_commands.py`
- **_execute_movement()** (10 connections) — `server/commands/go_command.py`
- **_validate_exit()** (10 connections) — `server/commands/go_command.py`
- **_validate_player_posture()** (10 connections) — `server/commands/go_command.py`
- **handle_explore_command()** (9 connections) — `server/commands/exploration_commands.py`
- **_cancel_rest_if_moving()** (7 connections) — `server/commands/go_command.py`
- **_movement_combat_and_event_bus_from_go_app()** (6 connections) — `server/commands/go_command.py`
- **_movement_service_for_go_command()** (6 connections) — `server/commands/go_command.py`
- **test_exploration_commands.py** (6 connections) — `server/tests/unit/commands/test_exploration_commands.py`
- **_canonical_room_id_for_go()** (4 connections) — `server/commands/go_command.py`
- **_connection_manager_from_go_app()** (4 connections) — `server/commands/go_command.py`
- **_resolve_async_persistence_from_go_app()** (4 connections) — `server/commands/go_command.py`
- **_resolved_direction_for_go_command()** (4 connections) — `server/commands/go_command.py`
- **test_handle_explore_command()** (4 connections) — `server/tests/unit/commands/test_exploration_commands.py`
- **test_handle_explore_command_no_persistence()** (4 connections) — `server/tests/unit/commands/test_exploration_commands.py`
- **test_execute_movement_error_handling()** (4 connections) — `server/tests/unit/commands/test_go_command.py`
- **test_execute_movement_failure()** (4 connections) — `server/tests/unit/commands/test_go_command.py`
- **test_execute_movement_fallback_service()** (4 connections) — `server/tests/unit/commands/test_go_command.py`
- **test_execute_movement_success()** (4 connections) — `server/tests/unit/commands/test_go_command.py`
- *... and 67 more nodes in this community*

## Relationships

- [server commands combat handler combatcommandhandler](server_commands_combat_handler_combatcommandhandler.md) (5 shared connections)
- [server alias storage aliasstorage](server_alias_storage_aliasstorage.md) (4 shared connections)
- [server commands admin commands](server_commands_admin_commands.md) (4 shared connections)
- [server commands talk command](server_commands_talk_command.md) (3 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (3 shared connections)
- [server game magic spell effects](server_game_magic_spell_effects.md) (2 shared connections)
- [server commands look command](server_commands_look_command.md) (2 shared connections)
- [aliaspayload](aliaspayload.md) (2 shared connections)
- [claude rules sqlalchemy](claude_rules_sqlalchemy.md) (2 shared connections)
- [claude rules pytest](claude_rules_pytest.md) (2 shared connections)
- [server commands look helpers lookrequest](server_commands_look_helpers_lookrequest.md) (1 shared connections)
- [server commands rescue commands](server_commands_rescue_commands.md) (1 shared connections)

## Source Files

- `server/commands/exploration_commands.py`
- `server/commands/go_command.py`
- `server/tests/unit/commands/test_exploration_commands.py`
- `server/tests/unit/commands/test_go_command.py`

## Audit Trail

- EXTRACTED: 191 (96%)
- INFERRED: 7 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*