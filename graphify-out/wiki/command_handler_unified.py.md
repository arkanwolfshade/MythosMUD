# command_handler_unified.py

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

- [AliasStorage](AliasStorage.md) (16 shared connections)
- [CommandRequest](CommandRequest.md) (15 shared connections)
- [catatonia_check.py](catatonia_check.py.md) (14 shared connections)
- [_check_grace_period_block](_check_grace_period_block.md) (12 shared connections)
- [TestHandleSpecialCommandRouting](TestHandleSpecialCommandRouting.md) (9 shared connections)
- [test_command_validator.py](test_command_validator.py.md) (7 shared connections)
- [WebSocketRequestContext](WebSocketRequestContext.md) (6 shared connections)
- [command_input.py](command_input.py.md) (6 shared connections)
- [TestPrepareCommandForProcessing](TestPrepareCommandForProcessing.md) (6 shared connections)
- [TestProcessAliasExpansion](TestProcessAliasExpansion.md) (5 shared connections)
- [get_logger](get_logger.md) (4 shared connections)
- [TestCheckAllCommandBlocks](TestCheckAllCommandBlocks.md) (4 shared connections)

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