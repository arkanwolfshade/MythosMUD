# command_handler_unified.py

> 77 nodes

## Key Concepts

- **command_handler_unified.py** (55 connections) — `server/command_handler_unified.py`
- **_prepare_command_for_processing()** (21 connections) — `server/command_handler_unified.py`
- **_check_casting_state()** (19 connections) — `server/command_handler_unified.py`
- **_process_alias_expansion()** (19 connections) — `server/command_handler_unified.py`
- **process_command_unified()** (19 connections) — `server/command_handler_unified.py`
- **_check_all_command_blocks()** (17 connections) — `server/command_handler_unified.py`
- **_handle_special_command_routing()** (17 connections) — `server/command_handler_unified.py`
- **_validate_command_basics()** (16 connections) — `server/command_handler_unified.py`
- **command_request_app_state()** (15 connections) — `server/command_handler/command_execution_request.py`
- **test_command_handler_unified_helpers.py** (14 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **_ensure_alias_storage()** (13 connections) — `server/command_handler_unified.py`
- **Any** (13 connections)
- **test_command_handler_unified.py** (12 connections) — `server/tests/unit/commands/test_command_handler_unified.py`
- **_check_rate_limit()** (10 connections) — `server/command_handler_unified.py`
- **CommandExecutionRequest** (9 connections)
- **test_command_aliases.py** (9 connections) — `server/tests/unit/commands/test_command_aliases.py`
- **process_command()** (8 connections) — `server/command_handler_unified.py`
- **TestPrepareCommandForProcessing** (7 connections) — `server/tests/unit/commands/test_command_preparation.py`
- **TestValidateCommandBasics** (6 connections) — `server/tests/unit/commands/test_command_validation.py`
- **_get_casting_block_result()** (6 connections) — `server/command_handler_unified.py`
- **get_help_content()** (6 connections) — `server/command_handler_unified.py`
- **TestEnsureAliasStorage** (5 connections) — `server/tests/unit/commands/test_command_aliases.py`
- **TestLegacyFunctions** (5 connections) — `server/tests/unit/commands/test_command_handler_unified.py`
- **test_command_preparation.py** (4 connections) — `server/tests/unit/commands/test_command_preparation.py`
- **test_command_request_app_state_missing_app_or_state_returns_none()** (3 connections) — `server/tests/unit/command_handler/test_command_execution_request.py`
- *... and 52 more nodes in this community*

## Relationships

- [TestHelperFunctions](TestHelperFunctions.md) (31 shared connections)
- [test_command_validation.py](test_command_validation.py.md) (17 shared connections)
- [handle_command](handle_command.md) (14 shared connections)
- [_check_grace_period_block](_check_grace_period_block.md) (11 shared connections)
- [get_logger](get_logger.md) (11 shared connections)
- [asyncio](asyncio.md) (9 shared connections)
- [AliasStorage](AliasStorage.md) (8 shared connections)
- [AliasGraph](AliasGraph.md) (7 shared connections)
- [normalize_command](normalize_command.md) (6 shared connections)
- [command_service.py](command_service.py.md) (4 shared connections)
- [WebSocketRequestContext](WebSocketRequestContext.md) (3 shared connections)
- [test_command_validator.py](test_command_validator.py.md) (3 shared connections)

## Source Files

- `server/command_handler/command_execution_request.py`
- `server/command_handler_unified.py`
- `server/tests/unit/command_handler/test_command_execution_request.py`
- `server/tests/unit/commands/test_command_aliases.py`
- `server/tests/unit/commands/test_command_handler_unified.py`
- `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- `server/tests/unit/commands/test_command_preparation.py`
- `server/tests/unit/commands/test_command_validation.py`

## Audit Trail

- EXTRACTED: 268 (96%)
- INFERRED: 10 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*