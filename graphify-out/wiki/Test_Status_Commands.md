# Test Status Commands

> 84 nodes

## Key Concepts

- **test_status_commands.py** (32 connections) — `server/tests/unit/commands/test_status_commands.py`
- **status_commands.py** (18 connections) — `server/commands/status_commands.py`
- **asyncio** (14 connections)
- **handle_status_command()** (13 connections) — `server/commands/status_commands.py`
- **test_status_commands_helpers.py** (13 connections) — `server/tests/unit/commands/test_status_commands_helpers.py`
- **_add_additional_stats_lines()** (12 connections) — `server/commands/status_commands.py`
- **_add_profession_lines()** (11 connections) — `server/commands/status_commands.py`
- **_build_base_status_lines()** (11 connections) — `server/commands/status_commands.py`
- **handle_whoami_command()** (11 connections) — `server/commands/status_commands.py`
- **_get_profession_info()** (10 connections) — `server/commands/status_commands.py`
- **_build_status_result()** (9 connections) — `server/commands/status_commands.py`
- **_get_combat_status()** (9 connections) — `server/commands/status_commands.py`
- **Any** (9 connections)
- **test_get_profession_info_error_handling()** (5 connections) — `server/tests/unit/commands/test_status_commands.py`
- **test_handle_status_command_error_handling()** (5 connections) — `server/tests/unit/commands/test_status_commands.py`
- **test_get_combat_status_no_app()** (4 connections) — `server/tests/unit/commands/test_status_commands.py`
- **test_get_combat_status_no_combat_service()** (4 connections) — `server/tests/unit/commands/test_status_commands.py`
- **test_get_combat_status_player_in_combat()** (4 connections) — `server/tests/unit/commands/test_status_commands.py`
- **test_get_combat_status_player_not_in_combat()** (4 connections) — `server/tests/unit/commands/test_status_commands.py`
- **test_get_profession_info_no_profession_id()** (4 connections) — `server/tests/unit/commands/test_status_commands.py`
- **test_get_profession_info_player_dict_no_profession_id()** (4 connections) — `server/tests/unit/commands/test_status_commands.py`
- **test_get_profession_info_profession_not_found()** (4 connections) — `server/tests/unit/commands/test_status_commands.py`
- **test_get_profession_info_with_profession()** (4 connections) — `server/tests/unit/commands/test_status_commands.py`
- **test_handle_status_command_no_persistence()** (4 connections) — `server/tests/unit/commands/test_status_commands.py`
- **test_handle_status_command_player_not_found()** (4 connections) — `server/tests/unit/commands/test_status_commands.py`
- *... and 59 more nodes in this community*

## Relationships

- [Test Who Commands](Test_Who_Commands.md) (3 shared connections)
- [Test Npc Admin Commands](Test_Npc_Admin_Commands.md) (3 shared connections)
- [Test Utility Commands Whoami](Test_Utility_Commands_Whoami.md) (3 shared connections)
- [Test Combat Persistence Handler Persistence](Test_Combat_Persistence_Handler_Persistence.md) (2 shared connections)
- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (2 shared connections)
- [Test Rescue Commands](Test_Rescue_Commands.md) (1 shared connections)
- [Alias Storage](Alias_Storage.md) (1 shared connections)
- [Test Command Parser](Test_Command_Parser.md) (1 shared connections)
- [Container Exception Handling](Container_Exception_Handling.md) (1 shared connections)

## Source Files

- `server/commands/status_commands.py`
- `server/tests/unit/commands/test_status_commands.py`
- `server/tests/unit/commands/test_status_commands_helpers.py`

## Audit Trail

- EXTRACTED: 163 (96%)
- INFERRED: 6 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*