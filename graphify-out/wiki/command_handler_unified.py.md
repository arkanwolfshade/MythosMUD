# command_handler_unified.py

> 105 nodes

## Key Concepts

- **command_handler_unified.py** (55 connections) — `server/command_handler_unified.py`
- **_prepare_command_for_processing()** (20 connections) — `server/command_handler_unified.py`
- **process_command_unified()** (19 connections) — `server/command_handler_unified.py`
- **_handle_special_command_routing()** (17 connections) — `server/command_handler_unified.py`
- **_process_alias_expansion()** (17 connections) — `server/command_handler_unified.py`
- **_validate_command_basics()** (15 connections) — `server/command_handler_unified.py`
- **get_help_content()** (15 connections) — `server/help/help_content.py`
- **_ensure_alias_storage()** (13 connections) — `server/command_handler_unified.py`
- **handle_command()** (13 connections) — `server/command_handler_unified.py`
- **test_command_handler_unified.py** (13 connections) — `server/tests/unit/commands/test_command_handler_unified.py`
- **test_command_handler_unified_helpers.py** (11 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **CommandRequest** (9 connections) — `server/command_handler_unified.py`
- **_check_rate_limit()** (9 connections) — `server/command_handler_unified.py`
- **_run_expanded_alias()** (9 connections) — `server/command_handler_unified.py`
- **test_command_aliases.py** (8 connections) — `server/tests/unit/commands/test_command_aliases.py`
- **TestPrepareCommandForProcessing** (7 connections) — `server/tests/unit/commands/test_command_preparation.py`
- **process_command()** (7 connections) — `server/command_handler_unified.py`
- **asyncio** (7 connections)
- **TestHandleCommand** (6 connections) — `server/tests/unit/commands/test_command_handler_unified.py`
- **TestProcessCommandUnified** (6 connections) — `server/tests/unit/commands/test_command_handler_unified.py`
- **get_help_content()** (6 connections) — `server/command_handler_unified.py`
- **CommandExecutionRequest** (6 connections)
- **test_websocket_handler_help.py** (6 connections) — `server/tests/unit/realtime/test_websocket_handler_help.py`
- **TestEnsureAliasStorage** (5 connections) — `server/tests/unit/commands/test_command_aliases.py`
- **TestLegacyFunctions** (5 connections) — `server/tests/unit/commands/test_command_handler_unified.py`
- *... and 80 more nodes in this community*

## Relationships

- [TestHelperFunctions](TestHelperFunctions.md) (23 shared connections)
- [catatonia_check.py](catatonia_check.py.md) (9 shared connections)
- [AliasStorage](AliasStorage.md) (9 shared connections)
- [asyncio](asyncio.md) (9 shared connections)
- [command_input.py](command_input.py.md) (7 shared connections)
- [get_logger](get_logger.md) (7 shared connections)
- [alias_expansion.py](alias_expansion.py.md) (6 shared connections)
- [User](User.md) (5 shared connections)
- [test_command_validator.py](test_command_validator.py.md) (4 shared connections)
- [TestValidateCommandBasics](TestValidateCommandBasics.md) (4 shared connections)
- [SecureBaseModel](SecureBaseModel.md) (3 shared connections)
- [Alias](Alias.md) (3 shared connections)

## Source Files

- `server/command_handler_unified.py`
- `server/help/__init__.py`
- `server/help/help_content.py`
- `server/tests/unit/commands/test_command_aliases.py`
- `server/tests/unit/commands/test_command_handler_unified.py`
- `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- `server/tests/unit/commands/test_command_preparation.py`
- `server/tests/unit/realtime/test_websocket_handler_core.py`
- `server/tests/unit/realtime/test_websocket_handler_help.py`

## Audit Trail

- EXTRACTED: 273 (96%)
- INFERRED: 11 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*