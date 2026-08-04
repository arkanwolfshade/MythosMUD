# commands status rationale

> 81 nodes

## Key Concepts

- **test_status_commands.py** (31 connections) — `server/tests/unit/commands/test_status_commands.py`
- **handle_status_command()** (17 connections) — `server/commands/status_commands.py`
- **status_commands.py** (16 connections) — `server/commands/status_commands.py`
- **test_status_commands_helpers.py** (13 connections) — `server/tests/unit/commands/test_status_commands_helpers.py`
- **_add_additional_stats_lines()** (12 connections) — `server/commands/status_commands.py`
- **_build_base_status_lines()** (11 connections) — `server/commands/status_commands.py`
- **_add_profession_lines()** (11 connections) — `server/commands/status_commands.py`
- **handle_whoami_command()** (11 connections) — `server/commands/status_commands.py`
- **_get_profession_info()** (10 connections) — `server/commands/status_commands.py`
- **_get_combat_status()** (9 connections) — `server/commands/status_commands.py`
- **Any** (7 connections)
- **test_get_profession_info_error_handling()** (4 connections) — `server/tests/unit/commands/test_status_commands.py`
- **test_handle_status_command_error_handling()** (4 connections) — `server/tests/unit/commands/test_status_commands.py`
- **test_get_profession_info_no_profession_id()** (3 connections) — `server/tests/unit/commands/test_status_commands.py`
- **test_get_profession_info_player_dict_no_profession_id()** (3 connections) — `server/tests/unit/commands/test_status_commands.py`
- **test_get_profession_info_with_profession()** (3 connections) — `server/tests/unit/commands/test_status_commands.py`
- **test_get_profession_info_profession_not_found()** (3 connections) — `server/tests/unit/commands/test_status_commands.py`
- **test_get_combat_status_no_combat_service()** (3 connections) — `server/tests/unit/commands/test_status_commands.py`
- **test_get_combat_status_no_app()** (3 connections) — `server/tests/unit/commands/test_status_commands.py`
- **test_get_combat_status_player_in_combat()** (3 connections) — `server/tests/unit/commands/test_status_commands.py`
- **test_get_combat_status_player_not_in_combat()** (3 connections) — `server/tests/unit/commands/test_status_commands.py`
- **test_build_base_status_lines()** (3 connections) — `server/tests/unit/commands/test_status_commands.py`
- **test_build_base_status_lines_in_combat()** (3 connections) — `server/tests/unit/commands/test_status_commands.py`
- **test_add_profession_lines_with_profession()** (3 connections) — `server/tests/unit/commands/test_status_commands.py`
- **test_add_profession_lines_no_name()** (3 connections) — `server/tests/unit/commands/test_status_commands.py`
- *... and 56 more nodes in this community*

## Relationships

- [commands npc admin](commands_npc_admin.md) (3 shared connections)
- [commands who rationale](commands_who_rationale.md) (3 shared connections)
- [commands whoami utility](commands_whoami_utility.md) (3 shared connections)
- [NPC Combat](NPC_Combat.md) (2 shared connections)
- [websocket helpers realtime](websocket_helpers_realtime.md) (2 shared connections)
- [commands whisper command](commands_whisper_command.md) (1 shared connections)
- [Loot Generation](Loot_Generation.md) (1 shared connections)
- [connection realtime manager](connection_realtime_manager.md) (1 shared connections)

## Source Files

- `server/commands/status_commands.py`
- `server/tests/unit/commands/test_status_commands.py`
- `server/tests/unit/commands/test_status_commands_helpers.py`

## Audit Trail

- EXTRACTED: 274 (98%)
- INFERRED: 6 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*