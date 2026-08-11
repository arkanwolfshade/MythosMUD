# Admin Teleport Commands

> 277 nodes

## Key Concepts

- **command_handler_unified.py** (52 connections) — `server/command_handler_unified.py`
- **TestHelperFunctions** (33 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **_check_grace_period_block()** (24 connections) — `server/command_handler_unified.py`
- **player_service()** (23 connections) — `docs/examples/logging/fastapi_integration.py`
- **_prepare_command_for_processing()** (21 connections) — `server/command_handler_unified.py`
- **process_command_unified()** (19 connections) — `server/command_handler_unified.py`
- **_process_alias_expansion()** (19 connections) — `server/command_handler_unified.py`
- **_handle_special_command_routing()** (18 connections) — `server/command_handler_unified.py`
- **_check_casting_state()** (18 connections) — `server/command_handler_unified.py`
- **_check_all_command_blocks()** (17 connections) — `server/command_handler_unified.py`
- **command_validator.py** (17 connections) — `server/validators/command_validator.py`
- **alias_expansion.py** (16 connections) — `server/command_handler/alias_expansion.py`
- **_validate_command_basics()** (16 connections) — `server/command_handler_unified.py`
- **command_request_app_state()** (14 connections) — `server/command_handler/command_execution_request.py`
- **command_input.py** (14 connections) — `server/command_handler/command_input.py`
- **Any** (14 connections)
- **get_help_content()** (14 connections) — `server/help/help_content.py`
- **CommandValidator** (14 connections) — `server/validators/command_validator.py`
- **__init__.py** (13 connections) — `server/command_handler/__init__.py`
- **_ensure_alias_storage()** (13 connections) — `server/command_handler_unified.py`
- **test_command_handler_unified_helpers.py** (13 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **normalize_command()** (12 connections) — `server/command_handler/command_input.py`
- **TestCommandNormalization** (12 connections) — `server/tests/unit/commands/test_command_input.py`
- **CommandRequest** (11 connections) — `server/command_handler_unified.py`
- **CommandExecutionRequest** (11 connections)
- *... and 252 more nodes in this community*

## Relationships

- [Client Event Store](Client_Event_Store.md) (20 shared connections)
- [Catatonia Check Logic](Catatonia_Check_Logic.md) (18 shared connections)
- [Persistence Container Extended](Persistence_Container_Extended.md) (17 shared connections)
- [Player Schema Converter](Player_Schema_Converter.md) (16 shared connections)
- [Async Audit Cursor](Async_Audit_Cursor.md) (11 shared connections)
- [WebSocket Auth Integration](WebSocket_Auth_Integration.md) (7 shared connections)
- [Character Info Panel Fix](Character_Info_Panel_Fix.md) (6 shared connections)
- [Game Tick Processing](Game_Tick_Processing.md) (5 shared connections)
- [Cursor Skills Frontend](Cursor_Skills_Frontend.md) (5 shared connections)
- [Game Quest Service](Game_Quest_Service.md) (5 shared connections)
- [Npc Behavior Engine](Npc_Behavior_Engine.md) (4 shared connections)
- [Game Magic Spell](Game_Magic_Spell.md) (4 shared connections)

## Source Files

- `docs/examples/logging/fastapi_integration.py`
- `server/command_handler/__init__.py`
- `server/command_handler/alias_expansion.py`
- `server/command_handler/command_execution_request.py`
- `server/command_handler/command_input.py`
- `server/command_handler_unified.py`
- `server/help/__init__.py`
- `server/help/help_content.py`
- `server/realtime/request_context.py`
- `server/tests/unit/command_handler/test_command_execution_request.py`
- `server/tests/unit/command_handler_unified/test_grace_period_blocking.py`
- `server/tests/unit/commands/test_command_aliases.py`
- `server/tests/unit/commands/test_command_handler_unified.py`
- `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- `server/tests/unit/commands/test_command_input.py`
- `server/tests/unit/commands/test_command_preparation.py`
- `server/tests/unit/realtime/test_websocket_handler_help.py`
- `server/validators/command_validator.py`

## Audit Trail

- EXTRACTED: 1029 (96%)
- INFERRED: 38 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*