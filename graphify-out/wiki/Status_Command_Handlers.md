# Status Command Handlers

> 91 nodes

## Key Concepts

- **test_status_commands.py** (31 connections) — `server/tests/unit/commands/test_status_commands.py`
- **status_commands.py** (18 connections) — `server/commands/status_commands.py`
- **handle_status_command()** (14 connections) — `server/commands/status_commands.py`
- **test_status_commands_helpers.py** (13 connections) — `server/tests/unit/commands/test_status_commands_helpers.py`
- **_add_additional_stats_lines()** (12 connections) — `server/commands/status_commands.py`
- **handle_whoami_command()** (12 connections) — `server/commands/status_commands.py`
- **_build_base_status_lines()** (11 connections) — `server/commands/status_commands.py`
- **_add_profession_lines()** (11 connections) — `server/commands/status_commands.py`
- **_get_profession_info()** (10 connections) — `server/commands/status_commands.py`
- **Any** (9 connections)
- **_get_combat_status()** (9 connections) — `server/commands/status_commands.py`
- **_build_status_result()** (9 connections) — `server/commands/status_commands.py`
- **test_utility_commands_whoami.py** (5 connections) — `server/tests/unit/commands/test_utility_commands_whoami.py`
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
- *... and 66 more nodes in this community*

## Relationships

- [Container Open Events](Container_Open_Events.md) (8 shared connections)
- [Async Persistence Types](Async_Persistence_Types.md) (4 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (2 shared connections)
- [Playwright E2E Specs](Playwright_E2E_Specs.md) (2 shared connections)

## Source Files

- `server/commands/status_commands.py`
- `server/tests/unit/commands/test_status_commands.py`
- `server/tests/unit/commands/test_status_commands_helpers.py`
- `server/tests/unit/commands/test_utility_commands_whoami.py`

## Audit Trail

- EXTRACTED: 301 (96%)
- INFERRED: 11 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*