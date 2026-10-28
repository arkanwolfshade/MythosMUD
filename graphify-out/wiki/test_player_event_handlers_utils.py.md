# test_player_event_handlers_utils.py

> 95 nodes · cohesion 0.04

## Key Concepts

- **test_status_commands.py** (31 connections) — `server/tests/unit/commands/test_status_commands.py`
- **status_commands.py** (20 connections) — `server/commands/status_commands.py`
- **utility_commands.py** (20 connections) — `server/commands/utility_commands.py`
- **handle_status_command()** (15 connections) — `server/commands/status_commands.py`
- **asyncio** (14 connections)
- **test_status_commands_helpers.py** (13 connections) — `server/tests/unit/commands/test_status_commands_helpers.py`
- **_add_additional_stats_lines()** (12 connections) — `server/commands/status_commands.py`
- **handle_whoami_command()** (12 connections) — `server/commands/status_commands.py`
- **_add_profession_lines()** (11 connections) — `server/commands/status_commands.py`
- **_build_base_status_lines()** (11 connections) — `server/commands/status_commands.py`
- **_build_status_result()** (10 connections) — `server/commands/status_commands.py`
- **_get_profession_info()** (10 connections) — `server/commands/status_commands.py`
- **_get_combat_status()** (9 connections) — `server/commands/status_commands.py`
- **Any** (9 connections)
- **test_get_profession_info_error_handling()** (5 connections) — `server/tests/unit/commands/test_status_commands.py`
- **test_handle_status_command_error_handling()** (5 connections) — `server/tests/unit/commands/test_status_commands.py`
- **test_utility_commands_whoami.py** (5 connections) — `server/tests/unit/commands/test_utility_commands_whoami.py`
- **test_get_combat_status_no_app()** (4 connections) — `server/tests/unit/commands/test_status_commands.py`
- **test_get_combat_status_no_combat_service()** (4 connections) — `server/tests/unit/commands/test_status_commands.py`
- **test_get_combat_status_player_in_combat()** (4 connections) — `server/tests/unit/commands/test_status_commands.py`
- **test_get_combat_status_player_not_in_combat()** (4 connections) — `server/tests/unit/commands/test_status_commands.py`
- **test_get_profession_info_no_profession_id()** (4 connections) — `server/tests/unit/commands/test_status_commands.py`
- **test_get_profession_info_player_dict_no_profession_id()** (4 connections) — `server/tests/unit/commands/test_status_commands.py`
- **test_get_profession_info_profession_not_found()** (4 connections) — `server/tests/unit/commands/test_status_commands.py`
- **test_get_profession_info_with_profession()** (4 connections) — `server/tests/unit/commands/test_status_commands.py`
- *... and 70 more nodes in this community*

## Relationships

- [command_parser.py](command_parser.py.md) (13 shared connections)
- [get_cached_player](get_cached_player.md) (3 shared connections)
- [Room](Room.md) (2 shared connections)
- [test_python_version_pin.py](test_python_version_pin.py.md) (2 shared connections)
- [test_players_procedures.py](test_players_procedures.py.md) (2 shared connections)
- [security.ts](security.ts.md) (2 shared connections)
- [CommandFactory](CommandFactory.md) (1 shared connections)
- [.load_room_data](load_room_data.md) (1 shared connections)
- [ConnectionErrorHandler](ConnectionErrorHandler.md) (1 shared connections)
- [audit_suppressions.py](audit_suppressions.py.md) (1 shared connections)
- [NpcDisposition](NpcDisposition.md) (1 shared connections)
- [RoomRepository](RoomRepository.md) (1 shared connections)

## Source Files

- `server/commands/status_commands.py`
- `server/commands/utility_commands.py`
- `server/tests/unit/commands/test_status_commands.py`
- `server/tests/unit/commands/test_status_commands_helpers.py`
- `server/tests/unit/commands/test_utility_commands_whoami.py`

## Audit Trail

- EXTRACTED: 193 (96%)
- INFERRED: 8 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*