# Command Request App State

> 100 nodes · cohesion 0.04

## Key Concepts

- **command_handler_unified.py** (52 connections) — `server/command_handler_unified.py`
- **TestHelperFunctions** (33 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **_prepare_command_for_processing()** (21 connections) — `server/command_handler_unified.py`
- **_process_alias_expansion()** (19 connections) — `server/command_handler_unified.py`
- **process_command_unified()** (19 connections) — `server/command_handler_unified.py`
- **_check_casting_state()** (18 connections) — `server/command_handler_unified.py`
- **_handle_special_command_routing()** (18 connections) — `server/command_handler_unified.py`
- **_check_all_command_blocks()** (17 connections) — `server/command_handler_unified.py`
- **_validate_command_basics()** (16 connections) — `server/command_handler_unified.py`
- **command_request_app_state()** (14 connections) — `server/command_handler/command_execution_request.py`
- **Any** (14 connections)
- **_ensure_alias_storage()** (13 connections) — `server/command_handler_unified.py`
- **test_command_handler_unified_helpers.py** (13 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **CommandExecutionRequest** (11 connections)
- **_check_rate_limit()** (10 connections) — `server/command_handler_unified.py`
- **handle_command()** (10 connections) — `server/command_handler_unified.py`
- **test_command_handler_unified.py** (10 connections) — `server/tests/unit/commands/test_command_handler_unified.py`
- **process_command()** (9 connections) — `server/command_handler_unified.py`
- **_get_grace_check_context()** (8 connections) — `server/command_handler_unified.py`
- **test_command_aliases.py** (8 connections) — `server/tests/unit/commands/test_command_aliases.py`
- **_get_casting_block_result()** (7 connections) — `server/command_handler_unified.py`
- **check_alias_safety()** (6 connections) — `server/command_handler/alias_expansion.py`
- **validate_expanded_command()** (6 connections) — `server/command_handler/alias_expansion.py`
- **get_help_content()** (6 connections) — `server/command_handler_unified.py`
- **.test_ensure_alias_storage_provided()** (4 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- *... and 75 more nodes in this community*

## Relationships

- [Admin Set Lucidity Command](Admin_Set_Lucidity_Command.md) (16 shared connections)
- [Unified Command Handler](Unified_Command_Handler.md) (15 shared connections)
- [Catatonia Check Logic](Catatonia_Check_Logic.md) (14 shared connections)
- [Stats Planning Archive](Stats_Planning_Archive.md) (12 shared connections)
- [Command Field Validators](Command_Field_Validators.md) (7 shared connections)
- [WebSocket Request Context](WebSocket_Request_Context.md) (6 shared connections)
- [Combat Attack Service](Combat_Attack_Service.md) (6 shared connections)
- [Cursor Plans Best](Cursor_Plans_Best.md) (6 shared connections)
- [Realtime Npc Event](Realtime_Npc_Event.md) (5 shared connections)
- [Cursor Plans Pydantic](Cursor_Plans_Pydantic.md) (5 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (4 shared connections)
- [Services Inventory Mutation](Services_Inventory_Mutation.md) (4 shared connections)

## Source Files

- `server/command_handler/alias_expansion.py`
- `server/command_handler/command_execution_request.py`
- `server/command_handler_unified.py`
- `server/tests/unit/commands/test_command_aliases.py`
- `server/tests/unit/commands/test_command_handler_unified.py`
- `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- `server/tests/unit/commands/test_command_preparation.py`

## Audit Trail

- EXTRACTED: 480 (98%)
- INFERRED: 11 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*