# server commands rest command

> 73 nodes

## Key Concepts

- **PlayerPositionService** (48 connections) — `server/services/player_position_service.py`
- **rest_command.py** (28 connections) — `server/commands/rest_command.py`
- **test_player_position_service.py** (28 connections) — `server/tests/unit/services/test_player_position_service.py`
- **cancel_rest_countdown()** (21 connections) — `server/commands/rest_command.py`
- **_start_rest_countdown()** (12 connections) — `server/commands/rest_command.py`
- **Any** (12 connections)
- **asyncio** (12 connections)
- **_execute_rest_flow()** (11 connections) — `server/commands/rest_command.py`
- **UUID** (10 connections)
- **_check_player_in_combat()** (9 connections) — `server/commands/rest_command.py`
- **_begin_seated_rest_countdown()** (8 connections) — `server/commands/rest_command.py`
- **_disconnect_player_intentionally()** (8 connections) — `server/commands/rest_command.py`
- **_resolve_rest_command_setup()** (6 connections) — `server/commands/rest_command.py`
- **_stand_after_cancelled_rest()** (6 connections) — `server/commands/rest_command.py`
- **test_change_position_database_error()** (5 connections) — `server/tests/unit/services/test_player_position_service.py`
- **test_change_position_save_error()** (5 connections) — `server/tests/unit/services/test_player_position_service.py`
- **_get_services_from_app()** (4 connections) — `server/commands/rest_command.py`
- **test_change_position_all_positions()** (4 connections) — `server/tests/unit/services/test_player_position_service.py`
- **test_change_position_already_in_position()** (4 connections) — `server/tests/unit/services/test_player_position_service.py`
- **test_change_position_get_stats_error()** (4 connections) — `server/tests/unit/services/test_player_position_service.py`
- **test_change_position_invalid_position()** (4 connections) — `server/tests/unit/services/test_player_position_service.py`
- **test_change_position_no_get_stats()** (4 connections) — `server/tests/unit/services/test_player_position_service.py`
- **test_change_position_no_persistence()** (4 connections) — `server/tests/unit/services/test_player_position_service.py`
- **test_change_position_player_not_found()** (4 connections) — `server/tests/unit/services/test_player_position_service.py`
- **test_change_position_success()** (4 connections) — `server/tests/unit/services/test_player_position_service.py`
- *... and 48 more nodes in this community*

## Relationships

- [server commands combat handler combatcommandhandler](server_commands_combat_handler_combatcommandhandler.md) (26 shared connections)
- [server services player position service](server_services_player_position_service.md) (10 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (7 shared connections)
- [server realtime disconnect grace period](server_realtime_disconnect_grace_period.md) (4 shared connections)
- [server commands position commands](server_commands_position_commands.md) (3 shared connections)
- [followtargetvalue](followtargetvalue.md) (3 shared connections)
- [server alias storage aliasstorage](server_alias_storage_aliasstorage.md) (3 shared connections)
- [server commands go command](server_commands_go_command.md) (3 shared connections)
- [server app game tick counter](server_app_game_tick_counter.md) (3 shared connections)
- [server commands rest countdown task](server_commands_rest_countdown_task.md) (3 shared connections)
- [scripts populate test npc databases](scripts_populate_test_npc_databases.md) (3 shared connections)
- [server realtime player disconnect handlers](server_realtime_player_disconnect_handlers.md) (2 shared connections)

## Source Files

- `server/commands/rest_command.py`
- `server/services/player_position_service.py`
- `server/tests/unit/services/test_player_position_service.py`

## Audit Trail

- EXTRACTED: 182 (87%)
- INFERRED: 28 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*