# command_handler_unified.py

> 232 nodes

## Key Concepts

- **command_handler_unified.py** (55 connections) — `server/command_handler_unified.py`
- **TestHelperFunctions** (33 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **_check_grace_period_block()** (24 connections) — `server/command_handler_unified.py`
- **_prepare_command_for_processing()** (21 connections) — `server/command_handler_unified.py`
- **asyncio** (21 connections)
- **_check_casting_state()** (19 connections) — `server/command_handler_unified.py`
- **_process_alias_expansion()** (19 connections) — `server/command_handler_unified.py`
- **process_command_unified()** (19 connections) — `server/command_handler_unified.py`
- **_check_all_command_blocks()** (17 connections) — `server/command_handler_unified.py`
- **_handle_special_command_routing()** (17 connections) — `server/command_handler_unified.py`
- **_validate_command_basics()** (16 connections) — `server/command_handler_unified.py`
- **get_help_content()** (15 connections) — `server/help/help_content.py`
- **command_handler/__init__.py** (14 connections) — `server/command_handler/__init__.py`
- **test_command_handler_unified_helpers.py** (14 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **_ensure_alias_storage()** (13 connections) — `server/command_handler_unified.py`
- **Any** (13 connections)
- **TestCommandNormalization** (12 connections) — `server/tests/unit/commands/test_command_input.py`
- **normalize_command()** (12 connections) — `server/command_handler/command_input.py`
- **test_command_handler_unified.py** (12 connections) — `server/tests/unit/commands/test_command_handler_unified.py`
- **handle_command()** (11 connections) — `server/command_handler_unified.py`
- **clean_command_input()** (10 connections) — `server/command_handler/command_input.py`
- **_check_rate_limit()** (10 connections) — `server/command_handler_unified.py`
- **CommandExecutionRequest** (9 connections)
- **test_grace_period_blocking.py** (9 connections) — `server/tests/unit/command_handler_unified/test_grace_period_blocking.py`
- **test_command_aliases.py** (9 connections) — `server/tests/unit/commands/test_command_aliases.py`
- *... and 207 more nodes in this community*

## Relationships

- [catatonia_check.py](catatonia_check.py.md) (26 shared connections)
- [AliasStorage](AliasStorage.md) (17 shared connections)
- [get_logger](get_logger.md) (17 shared connections)
- [asyncio](asyncio.md) (9 shared connections)
- [test_alias_expansion.py](test_alias_expansion.py.md) (9 shared connections)
- [test_command_validator.py](test_command_validator.py.md) (7 shared connections)
- [_is_predefined_emote](_is_predefined_emote.md) (6 shared connections)
- [pytest.md](pytest.md.md) (6 shared connections)
- [WebSocketRequestContext](WebSocketRequestContext.md) (5 shared connections)
- [disconnect_grace_period.py](disconnect_grace_period.py.md) (3 shared connections)
- [test_websocket_handler_core.py](test_websocket_handler_core.py.md) (3 shared connections)
- [websocket_handler_commands.py](websocket_handler_commands.py.md) (2 shared connections)

## Source Files

- `server/command_handler/__init__.py`
- `server/command_handler/command_input.py`
- `server/command_handler_unified.py`
- `server/help/__init__.py`
- `server/help/help_content.py`
- `server/tests/unit/command_handler_unified/test_grace_period_blocking.py`
- `server/tests/unit/commands/test_command_aliases.py`
- `server/tests/unit/commands/test_command_handler_unified.py`
- `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- `server/tests/unit/commands/test_command_input.py`
- `server/tests/unit/commands/test_command_preparation.py`
- `server/tests/unit/commands/test_command_validation.py`
- `server/tests/unit/realtime/test_websocket_handler_help.py`

## Audit Trail

- EXTRACTED: 495 (98%)
- INFERRED: 10 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*