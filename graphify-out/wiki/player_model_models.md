# player model models

> 58 nodes

## Key Concepts

- **command_handler_unified.py** (52 connections) — `server/command_handler_unified.py`
- **_check_grace_period_block()** (24 connections) — `server/command_handler_unified.py`
- **_prepare_command_for_processing()** (21 connections) — `server/command_handler_unified.py`
- **process_command_unified()** (19 connections) — `server/command_handler_unified.py`
- **_check_casting_state()** (19 connections) — `server/command_handler_unified.py`
- **_process_alias_expansion()** (19 connections) — `server/command_handler_unified.py`
- **_handle_special_command_routing()** (18 connections) — `server/command_handler_unified.py`
- **_check_all_command_blocks()** (17 connections) — `server/command_handler_unified.py`
- **_validate_command_basics()** (16 connections) — `server/command_handler_unified.py`
- **command_request_app_state()** (14 connections) — `server/command_handler/command_execution_request.py`
- **Any** (14 connections)
- **_ensure_alias_storage()** (13 connections) — `server/command_handler_unified.py`
- **test_command_handler_unified_helpers.py** (13 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **CommandExecutionRequest** (11 connections)
- **should_treat_as_emote()** (10 connections) — `server/command_handler/command_input.py`
- **_check_rate_limit()** (10 connections) — `server/command_handler_unified.py`
- **handle_command()** (10 connections) — `server/command_handler_unified.py`
- **test_command_handler_unified.py** (10 connections) — `server/tests/unit/commands/test_command_handler_unified.py`
- **command_execution_request.py** (9 connections) — `server/command_handler/command_execution_request.py`
- **process_command()** (9 connections) — `server/command_handler_unified.py`
- **_get_grace_check_context()** (8 connections) — `server/command_handler_unified.py`
- **test_command_execution_request.py** (8 connections) — `server/tests/unit/command_handler/test_command_execution_request.py`
- **test_command_aliases.py** (8 connections) — `server/tests/unit/commands/test_command_aliases.py`
- **_get_casting_block_result()** (7 connections) — `server/command_handler_unified.py`
- **get_help_content()** (6 connections) — `server/command_handler_unified.py`
- *... and 33 more nodes in this community*

## Relationships

- [command commands handler](command_commands_handler.md) (31 shared connections)
- [auth dependencies rationale](auth_dependencies_rationale.md) (15 shared connections)
- [command validation commands](command_validation_commands.md) (13 shared connections)
- [alias storage rationale](alias_storage_rationale.md) (13 shared connections)
- [player left room](player_left_room.md) (7 shared connections)
- [connection realtime name](connection_realtime_name.md) (6 shared connections)
- [commands command validation](commands_command_validation.md) (6 shared connections)
- [commands recovery lucidity](commands_recovery_lucidity.md) (5 shared connections)
- [startup services npc](startup_services_npc.md) (5 shared connections)
- [combat npc services](combat_npc_services.md) (5 shared connections)
- [error websocket handler](error_websocket_handler.md) (5 shared connections)
- [Error Conversion](Error_Conversion.md) (4 shared connections)

## Source Files

- `server/command_handler/command_execution_request.py`
- `server/command_handler/command_input.py`
- `server/command_handler_unified.py`
- `server/tests/unit/command_handler/test_command_execution_request.py`
- `server/tests/unit/commands/test_command_aliases.py`
- `server/tests/unit/commands/test_command_handler_unified.py`
- `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- `server/tests/unit/commands/test_command_preparation.py`

## Audit Trail

- EXTRACTED: 401 (98%)
- INFERRED: 10 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*