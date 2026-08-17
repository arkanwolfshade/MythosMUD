# server commands combat handler combatcommandhandler

> 68 nodes

## Key Concepts

- **test_rest_command.py** (41 connections) — `server/tests/unit/commands/test_rest_command.py`
- **asyncio** (22 connections)
- **handle_rest_command()** (21 connections) — `server/commands/rest_command.py`
- **is_player_resting()** (17 connections) — `server/commands/rest_command.py`
- **_check_rest_location()** (9 connections) — `server/commands/rest_command.py`
- **.check_and_interrupt_rest()** (7 connections) — `server/commands/combat_handler.py`
- **fixture** (5 connections)
- **mock_persistence()** (4 connections) — `server/tests/unit/commands/test_rest_command.py`
- **test_cancel_rest_countdown_cancels_task()** (4 connections) — `server/tests/unit/commands/test_rest_command.py`
- **test_cancel_rest_countdown_not_resting()** (4 connections) — `server/tests/unit/commands/test_rest_command.py`
- **test_cancel_rest_countdown_restores_standing()** (4 connections) — `server/tests/unit/commands/test_rest_command.py`
- **test_check_player_in_combat_false()** (4 connections) — `server/tests/unit/commands/test_rest_command.py`
- **test_check_player_in_combat_no_service()** (4 connections) — `server/tests/unit/commands/test_rest_command.py`
- **test_check_player_in_combat_true()** (4 connections) — `server/tests/unit/commands/test_rest_command.py`
- **test_check_rest_location_false()** (4 connections) — `server/tests/unit/commands/test_rest_command.py`
- **test_check_rest_location_no_persistence()** (4 connections) — `server/tests/unit/commands/test_rest_command.py`
- **test_check_rest_location_no_room()** (4 connections) — `server/tests/unit/commands/test_rest_command.py`
- **test_check_rest_location_true()** (4 connections) — `server/tests/unit/commands/test_rest_command.py`
- **test_disconnect_player_intentionally()** (4 connections) — `server/tests/unit/commands/test_rest_command.py`
- **test_handle_rest_command_already_resting()** (4 connections) — `server/tests/unit/commands/test_rest_command.py`
- **test_handle_rest_command_in_combat()** (4 connections) — `server/tests/unit/commands/test_rest_command.py`
- **test_handle_rest_command_no_app()** (4 connections) — `server/tests/unit/commands/test_rest_command.py`
- **test_handle_rest_command_no_connection_manager()** (4 connections) — `server/tests/unit/commands/test_rest_command.py`
- **test_handle_rest_command_no_persistence()** (4 connections) — `server/tests/unit/commands/test_rest_command.py`
- **test_handle_rest_command_player_not_found()** (4 connections) — `server/tests/unit/commands/test_rest_command.py`
- *... and 43 more nodes in this community*

## Relationships

- [server commands rest command](server_commands_rest_command.md) (26 shared connections)
- [server realtime disconnect grace period](server_realtime_disconnect_grace_period.md) (5 shared connections)
- [server commands combat handler combatcommandhandler](server_commands_combat_handler_combatcommandhandler.md) (3 shared connections)
- [server commands admin commands](server_commands_admin_commands.md) (2 shared connections)
- [server commands go command](server_commands_go_command.md) (2 shared connections)
- [server realtime player disconnect handlers](server_realtime_player_disconnect_handlers.md) (2 shared connections)
- [server app game tick counter](server_app_game_tick_counter.md) (2 shared connections)
- [server tests unit commands test](server_tests_unit_commands_test.md) (2 shared connections)
- [server alias storage aliasstorage](server_alias_storage_aliasstorage.md) (1 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (1 shared connections)
- [characterinfo](characterinfo.md) (1 shared connections)

## Source Files

- `server/commands/combat_handler.py`
- `server/commands/rest_command.py`
- `server/tests/unit/commands/test_rest_command.py`

## Audit Trail

- EXTRACTED: 154 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*