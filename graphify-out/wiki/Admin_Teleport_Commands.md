# Admin Teleport Commands

> 122 nodes

## Key Concepts

- **command_handler_unified.py** (52 connections) — `server/command_handler_unified.py`
- **TestHelperFunctions** (33 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **_check_grace_period_block()** (24 connections) — `server/command_handler_unified.py`
- **_prepare_command_for_processing()** (21 connections) — `server/command_handler_unified.py`
- **process_command_unified()** (19 connections) — `server/command_handler_unified.py`
- **_process_alias_expansion()** (19 connections) — `server/command_handler_unified.py`
- **_handle_special_command_routing()** (18 connections) — `server/command_handler_unified.py`
- **_check_casting_state()** (18 connections) — `server/command_handler_unified.py`
- **_check_all_command_blocks()** (17 connections) — `server/command_handler_unified.py`
- **_validate_command_basics()** (16 connections) — `server/command_handler_unified.py`
- **Any** (14 connections)
- **_ensure_alias_storage()** (13 connections) — `server/command_handler_unified.py`
- **test_command_handler_unified_helpers.py** (13 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **CommandExecutionRequest** (11 connections)
- **_check_rate_limit()** (10 connections) — `server/command_handler_unified.py`
- **handle_command()** (10 connections) — `server/command_handler_unified.py`
- **test_command_handler_unified.py** (10 connections) — `server/tests/unit/commands/test_command_handler_unified.py`
- **process_command()** (9 connections) — `server/command_handler_unified.py`
- **_get_grace_check_context()** (8 connections) — `server/command_handler_unified.py`
- **test_grace_period_blocking.py** (8 connections) — `server/tests/unit/command_handler_unified/test_grace_period_blocking.py`
- **test_command_aliases.py** (8 connections) — `server/tests/unit/commands/test_command_aliases.py`
- **_get_casting_block_result()** (7 connections) — `server/command_handler_unified.py`
- **check_alias_safety()** (6 connections) — `server/command_handler/alias_expansion.py`
- **validate_expanded_command()** (6 connections) — `server/command_handler/alias_expansion.py`
- **get_help_content()** (6 connections) — `server/command_handler_unified.py`
- *... and 97 more nodes in this community*

## Relationships

- [Container Open Events](Container_Open_Events.md) (22 shared connections)
- [Catatonia Check Logic](Catatonia_Check_Logic.md) (16 shared connections)
- [Room Exploration API](Room_Exploration_API.md) (15 shared connections)
- [Persistence Container Extended](Persistence_Container_Extended.md) (8 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (6 shared connections)
- [FastAPI Auth Integration](FastAPI_Auth_Integration.md) (6 shared connections)
- [Load E 2 E Analysis](Load_E_2_E_Analysis.md) (6 shared connections)
- [Cursor Skills Frontend](Cursor_Skills_Frontend.md) (5 shared connections)
- [Game Quest Service](Game_Quest_Service.md) (5 shared connections)
- [Combat Services Messaging](Combat_Services_Messaging.md) (5 shared connections)
- [Npc Behavior Engine](Npc_Behavior_Engine.md) (4 shared connections)
- [Uvicorn Code Review](Uvicorn_Code_Review.md) (4 shared connections)

## Source Files

- `server/command_handler/alias_expansion.py`
- `server/command_handler_unified.py`
- `server/tests/unit/command_handler_unified/test_grace_period_blocking.py`
- `server/tests/unit/commands/test_command_aliases.py`
- `server/tests/unit/commands/test_command_handler_unified.py`
- `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- `server/tests/unit/commands/test_command_preparation.py`

## Audit Trail

- EXTRACTED: 539 (98%)
- INFERRED: 10 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*