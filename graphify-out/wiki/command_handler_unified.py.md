# command_handler_unified.py

> 347 nodes

## Key Concepts

- **command_handler_unified.py** (55 connections) — `server/command_handler_unified.py`
- **TestHelperFunctions** (33 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **WebSocketRequestContext** (26 connections) — `server/realtime/request_context.py`
- **_check_grace_period_block()** (24 connections) — `server/command_handler_unified.py`
- **_prepare_command_for_processing()** (21 connections) — `server/command_handler_unified.py`
- **asyncio** (21 connections)
- **_check_casting_state()** (19 connections) — `server/command_handler_unified.py`
- **_process_alias_expansion()** (19 connections) — `server/command_handler_unified.py`
- **process_command_unified()** (19 connections) — `server/command_handler_unified.py`
- **command_request_app_state()** (17 connections) — `server/command_handler/command_execution_request.py`
- **_check_all_command_blocks()** (17 connections) — `server/command_handler_unified.py`
- **_handle_special_command_routing()** (17 connections) — `server/command_handler_unified.py`
- **_validate_command_basics()** (16 connections) — `server/command_handler_unified.py`
- **test_request_context.py** (16 connections) — `server/tests/unit/realtime/test_request_context.py`
- **get_help_content()** (15 connections) — `server/help/help_content.py`
- **command_input.py** (15 connections) — `server/command_handler/command_input.py`
- **test_command_handler_unified_helpers.py** (14 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **_ensure_alias_storage()** (13 connections) — `server/command_handler_unified.py`
- **Any** (13 connections)
- **TestCommandNormalization** (12 connections) — `server/tests/unit/commands/test_command_input.py`
- **normalize_command()** (12 connections) — `server/command_handler/command_input.py`
- **help_content.py** (12 connections) — `server/help/help_content.py`
- **test_command_handler_unified.py** (12 connections) — `server/tests/unit/commands/test_command_handler_unified.py`
- **_is_predefined_emote()** (11 connections) — `server/command_handler/command_input.py`
- **should_treat_as_emote()** (11 connections) — `server/command_handler/command_input.py`
- *... and 322 more nodes in this community*

## Relationships

- [catatonia_check.py](catatonia_check.py.md) (26 shared connections)
- [AliasStorage](AliasStorage.md) (16 shared connections)
- [processing.py](processing.py.md) (15 shared connections)
- [get_logger](get_logger.md) (14 shared connections)
- [.state](state.md) (4 shared connections)
- [test_command_validator.py](test_command_validator.py.md) (4 shared connections)
- [test_websocket_handler_core.py](test_websocket_handler_core.py.md) (4 shared connections)
- [pytest.md](pytest.md.md) (4 shared connections)
- [get_config](get_config.md) (3 shared connections)
- [get_username_from_user](get_username_from_user.md) (3 shared connections)
- [look_command.py](look_command.py.md) (3 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (3 shared connections)

## Source Files

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
- `server/tests/unit/commands/test_command_validation.py`
- `server/tests/unit/realtime/test_request_context.py`
- `server/tests/unit/realtime/test_websocket_handler_help.py`

## Audit Trail

- EXTRACTED: 678 (98%)
- INFERRED: 16 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*