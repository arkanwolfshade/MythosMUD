# command_handler_unified.py

> 296 nodes

## Key Concepts

- **command_handler_unified.py** (53 connections) — `server/command_handler_unified.py`
- **TestHelperFunctions** (33 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **_check_grace_period_block()** (24 connections) — `server/command_handler_unified.py`
- **_prepare_command_for_processing()** (21 connections) — `server/command_handler_unified.py`
- **asyncio** (21 connections)
- **_check_casting_state()** (19 connections) — `server/command_handler_unified.py`
- **_process_alias_expansion()** (19 connections) — `server/command_handler_unified.py`
- **process_command_unified()** (19 connections) — `server/command_handler_unified.py`
- **_check_all_command_blocks()** (17 connections) — `server/command_handler_unified.py`
- **_handle_special_command_routing()** (17 connections) — `server/command_handler_unified.py`
- **command_validator.py** (17 connections) — `server/validators/command_validator.py`
- **_validate_command_basics()** (16 connections) — `server/command_handler_unified.py`
- **command_input.py** (15 connections) — `server/command_handler/command_input.py`
- **command_request_app_state()** (14 connections) — `server/command_handler/command_execution_request.py`
- **command_handler/__init__.py** (14 connections) — `server/command_handler/__init__.py`
- **process_command_with_validation()** (13 connections) — `server/command_handler/processing.py`
- **_ensure_alias_storage()** (13 connections) — `server/command_handler_unified.py`
- **Any** (13 connections)
- **test_alias_expansion.py** (13 connections) — `server/tests/unit/commands/test_alias_expansion.py`
- **test_command_handler_unified_helpers.py** (13 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **TestCommandNormalization** (12 connections) — `server/tests/unit/commands/test_command_input.py`
- **normalize_command()** (12 connections) — `server/command_handler/command_input.py`
- **handle_expanded_command()** (11 connections) — `server/command_handler/alias_expansion.py`
- **handle_command()** (11 connections) — `server/command_handler_unified.py`
- **check_alias_safety()** (10 connections) — `server/command_handler/alias_expansion.py`
- *... and 271 more nodes in this community*

## Relationships

- [catatonia_check.py](catatonia_check.py.md) (27 shared connections)
- [get_logger](get_logger.md) (23 shared connections)
- [AliasStorage](AliasStorage.md) (14 shared connections)
- [test_command_validator.py](test_command_validator.py.md) (13 shared connections)
- [test_command_processing.py](test_command_processing.py.md) (5 shared connections)
- [test_security_validator.py](test_security_validator.py.md) (3 shared connections)
- [get_config](get_config.md) (3 shared connections)
- [EmoteService](EmoteService.md) (2 shared connections)
- [test_rest_and_grace_period.py](test_rest_and_grace_period.py.md) (2 shared connections)
- [get_username_from_user](get_username_from_user.md) (2 shared connections)
- [websocket_handler_commands.py](websocket_handler_commands.py.md) (2 shared connections)
- [AliasGraph](AliasGraph.md) (1 shared connections)

## Source Files

- `server/command_handler/__init__.py`
- `server/command_handler/alias_expansion.py`
- `server/command_handler/command_execution_request.py`
- `server/command_handler/command_input.py`
- `server/command_handler/processing.py`
- `server/command_handler_unified.py`
- `server/tests/unit/command_handler/test_command_execution_request.py`
- `server/tests/unit/command_handler_unified/test_grace_period_blocking.py`
- `server/tests/unit/commands/test_alias_expansion.py`
- `server/tests/unit/commands/test_command_aliases.py`
- `server/tests/unit/commands/test_command_handler_unified.py`
- `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- `server/tests/unit/commands/test_command_input.py`
- `server/tests/unit/commands/test_command_preparation.py`
- `server/tests/unit/commands/test_command_validation.py`
- `server/validators/command_validator.py`

## Audit Trail

- EXTRACTED: 609 (98%)
- INFERRED: 13 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*