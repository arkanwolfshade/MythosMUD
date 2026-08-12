# Room Exploration API

> 59 nodes

## Key Concepts

- **command_handler_unified.py** (52 connections) — `server/command_handler_unified.py`
- **_check_grace_period_block()** (24 connections) — `server/command_handler_unified.py`
- **process_command_unified()** (19 connections) — `server/command_handler_unified.py`
- **_process_alias_expansion()** (19 connections) — `server/command_handler_unified.py`
- **_handle_special_command_routing()** (18 connections) — `server/command_handler_unified.py`
- **_check_casting_state()** (18 connections) — `server/command_handler_unified.py`
- **_check_all_command_blocks()** (17 connections) — `server/command_handler_unified.py`
- **command_request_app_state()** (14 connections) — `server/command_handler/command_execution_request.py`
- **Any** (14 connections)
- **_ensure_alias_storage()** (13 connections) — `server/command_handler_unified.py`
- **test_command_handler_unified_helpers.py** (13 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **CommandRequest** (11 connections) — `server/command_handler_unified.py`
- **CommandExecutionRequest** (11 connections)
- **handle_command()** (10 connections) — `server/command_handler_unified.py`
- **test_command_handler_unified.py** (10 connections) — `server/tests/unit/commands/test_command_handler_unified.py`
- **process_command()** (9 connections) — `server/command_handler_unified.py`
- **_get_grace_check_context()** (8 connections) — `server/command_handler_unified.py`
- **test_command_aliases.py** (8 connections) — `server/tests/unit/commands/test_command_aliases.py`
- **_get_casting_block_result()** (7 connections) — `server/command_handler_unified.py`
- **TestProcessCommandUnified** (7 connections) — `server/tests/unit/commands/test_command_handler_unified.py`
- **check_alias_safety()** (6 connections) — `server/command_handler/alias_expansion.py`
- **validate_expanded_command()** (6 connections) — `server/command_handler/alias_expansion.py`
- **TestHandleCommand** (5 connections) — `server/tests/unit/commands/test_command_handler_unified.py`
- **.test_handle_command_unauthorized()** (4 connections) — `server/tests/unit/commands/test_command_handler_unified.py`
- **.test_handle_command_success()** (4 connections) — `server/tests/unit/commands/test_command_handler_unified.py`
- *... and 34 more nodes in this community*

## Relationships

- [Admin Teleport Commands](Admin_Teleport_Commands.md) (21 shared connections)
- [Player Schema Converter](Player_Schema_Converter.md) (15 shared connections)
- [Catatonia Check Logic](Catatonia_Check_Logic.md) (9 shared connections)
- [FastAPI Auth Integration](FastAPI_Auth_Integration.md) (8 shared connections)
- [Persistence Container Extended](Persistence_Container_Extended.md) (7 shared connections)
- [Load E 2 E Analysis](Load_E_2_E_Analysis.md) (6 shared connections)
- [E 2 E Testing Approach](E_2_E_Testing_Approach.md) (6 shared connections)
- [Investigations Sessions Session](Investigations_Sessions_Session.md) (5 shared connections)
- [Client Event Store](Client_Event_Store.md) (5 shared connections)
- [Cursor Skills Frontend](Cursor_Skills_Frontend.md) (5 shared connections)
- [Game Quest Service](Game_Quest_Service.md) (5 shared connections)
- [Combat Services Messaging](Combat_Services_Messaging.md) (5 shared connections)

## Source Files

- `server/command_handler/alias_expansion.py`
- `server/command_handler/command_execution_request.py`
- `server/command_handler_unified.py`
- `server/tests/unit/commands/test_command_aliases.py`
- `server/tests/unit/commands/test_command_handler_unified.py`
- `server/tests/unit/commands/test_command_handler_unified_helpers.py`

## Audit Trail

- EXTRACTED: 357 (96%)
- INFERRED: 15 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*