# Status Command Handlers

> 83 nodes

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
- *... and 58 more nodes in this community*

## Relationships

- [Client Event Store](Client_Event_Store.md) (3 shared connections)
- [Player Schema Converter](Player_Schema_Converter.md) (3 shared connections)
- [Chat NATS Publisher](Chat_NATS_Publisher.md) (3 shared connections)
- [Combat UUID Display Bug](Combat_UUID_Display_Bug.md) (3 shared connections)
- [Logger Client Add To](Logger_Client_Add_To.md) (3 shared connections)
- [Auth Token Utilities](Auth_Token_Utilities.md) (2 shared connections)
- [Container Repository CRUD](Container_Repository_CRUD.md) (1 shared connections)

## Source Files

- `server/commands/status_commands.py`
- `server/tests/unit/commands/test_status_commands.py`
- `server/tests/unit/commands/test_status_commands_helpers.py`

## Audit Trail

- EXTRACTED: 286 (97%)
- INFERRED: 8 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*