# Status Command Handlers

> 86 nodes · cohesion 0.04

## Key Concepts

- **test_status_commands.py** (30 connections) — `server/tests/unit/commands/test_status_commands.py`
- **handle_status_command()** (17 connections) — `server/commands/status_commands.py`
- **status_commands.py** (14 connections) — `server/commands/status_commands.py`
- **_add_additional_stats_lines()** (12 connections) — `server/commands/status_commands.py`
- **test_status_commands_helpers.py** (12 connections) — `server/tests/unit/commands/test_status_commands_helpers.py`
- **_add_profession_lines()** (11 connections) — `server/commands/status_commands.py`
- **_build_base_status_lines()** (11 connections) — `server/commands/status_commands.py`
- **handle_whoami_command()** (11 connections) — `server/commands/status_commands.py`
- **_get_profession_info()** (10 connections) — `server/commands/status_commands.py`
- **_get_combat_status()** (9 connections) — `server/commands/status_commands.py`
- **Any** (7 connections) — `server/commands/status_commands.py`
- **test_get_profession_info_error_handling()** (4 connections) — `server/tests/unit/commands/test_status_commands.py`
- **test_utility_commands_whoami.py** (4 connections) — `server/tests/unit/commands/test_utility_commands_whoami.py`
- **test_add_additional_stats_lines()** (3 connections) — `server/tests/unit/commands/test_status_commands_helpers.py`
- **test_add_additional_stats_lines_empty()** (3 connections) — `server/tests/unit/commands/test_status_commands_helpers.py`
- **test_add_additional_stats_lines_zero_values()** (3 connections) — `server/tests/unit/commands/test_status_commands_helpers.py`
- **test_add_profession_lines()** (3 connections) — `server/tests/unit/commands/test_status_commands_helpers.py`
- **test_add_profession_lines_no_profession()** (3 connections) — `server/tests/unit/commands/test_status_commands_helpers.py`
- **test_build_base_status_lines()** (3 connections) — `server/tests/unit/commands/test_status_commands_helpers.py`
- **test_build_base_status_lines_in_combat()** (3 connections) — `server/tests/unit/commands/test_status_commands_helpers.py`
- **test_build_base_status_lines_sitting()** (3 connections) — `server/tests/unit/commands/test_status_commands_helpers.py`
- **test_add_additional_stats_lines_missing_stats()** (3 connections) — `server/tests/unit/commands/test_status_commands.py`
- **test_add_additional_stats_lines_with_stats()** (3 connections) — `server/tests/unit/commands/test_status_commands.py`
- **test_add_additional_stats_lines_zero_stats()** (3 connections) — `server/tests/unit/commands/test_status_commands.py`
- **test_add_profession_lines_no_name()** (3 connections) — `server/tests/unit/commands/test_status_commands.py`
- *... and 61 more nodes in this community*

## Relationships

- [[Alias Expansion Logic]] (6 shared connections)
- [[Services Service Room]] (3 shared connections)
- [[NPC Admin API]] (2 shared connections)
- [[Command Helper Utilities]] (1 shared connections)
- [[Ground and Rescue Commands]] (1 shared connections)

## Source Files

- `server/commands/status_commands.py`
- `server/tests/unit/commands/test_status_commands.py`
- `server/tests/unit/commands/test_status_commands_helpers.py`
- `server/tests/unit/commands/test_utility_commands_whoami.py`

## Audit Trail

- EXTRACTED: 281 (97%)
- INFERRED: 8 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
