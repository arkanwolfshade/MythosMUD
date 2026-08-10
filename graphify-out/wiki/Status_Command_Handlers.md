# Status Command Handlers

> 79 nodes

## Key Concepts

- **test_status_commands.py** (31 connections) — `server/tests/unit/commands/test_status_commands.py`
- **status_commands.py** (18 connections) — `server/commands/status_commands.py`
- **handle_status_command()** (14 connections) — `server/commands/status_commands.py`
- **test_status_commands_helpers.py** (13 connections) — `server/tests/unit/commands/test_status_commands_helpers.py`
- **_add_additional_stats_lines()** (12 connections) — `server/commands/status_commands.py`
- **_build_base_status_lines()** (11 connections) — `server/commands/status_commands.py`
- **_add_profession_lines()** (11 connections) — `server/commands/status_commands.py`
- **_get_profession_info()** (10 connections) — `server/commands/status_commands.py`
- **Any** (9 connections)
- **_get_combat_status()** (9 connections) — `server/commands/status_commands.py`
- **_build_status_result()** (9 connections) — `server/commands/status_commands.py`
- **test_get_profession_info_error_handling()** (4 connections) — `server/tests/unit/commands/test_status_commands.py`
- **test_handle_status_command_error_handling()** (4 connections) — `server/tests/unit/commands/test_status_commands.py`
- **_get_status_persistence()** (3 connections) — `server/commands/status_commands.py`
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
- *... and 54 more nodes in this community*

## Relationships

- [Client Event Store](Client_Event_Store.md) (6 shared connections)
- [Logger Client Add To](Logger_Client_Add_To.md) (5 shared connections)
- [Game Service Bundle](Game_Service_Bundle.md) (2 shared connections)
- [Commands System Help](Commands_System_Help.md) (2 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (2 shared connections)

## Source Files

- `server/commands/status_commands.py`
- `server/tests/unit/commands/test_status_commands.py`
- `server/tests/unit/commands/test_status_commands_helpers.py`

## Audit Trail

- EXTRACTED: 273 (99%)
- INFERRED: 4 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*