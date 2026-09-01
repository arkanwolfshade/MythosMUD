# alias_expansion.py

> 21 nodes

## Key Concepts

- **alias_expansion.py** (17 connections) — `server/command_handler/alias_expansion.py`
- **test_alias_expansion.py** (14 connections) — `server/tests/unit/commands/test_alias_expansion.py`
- **handle_expanded_command()** (11 connections) — `server/command_handler/alias_expansion.py`
- **check_alias_safety()** (10 connections) — `server/command_handler/alias_expansion.py`
- **validate_expanded_command()** (10 connections) — `server/command_handler/alias_expansion.py`
- **asyncio** (5 connections)
- **test_check_alias_safety_cycle_detected()** (3 connections) — `server/tests/unit/commands/test_alias_expansion.py`
- **test_check_alias_safety_depth_too_deep()** (3 connections) — `server/tests/unit/commands/test_alias_expansion.py`
- **test_check_alias_safety_ok()** (3 connections) — `server/tests/unit/commands/test_alias_expansion.py`
- **test_handle_expanded_command_delegates()** (3 connections) — `server/tests/unit/commands/test_alias_expansion.py`
- **test_handle_expanded_command_depth_limit()** (3 connections) — `server/tests/unit/commands/test_alias_expansion.py`
- **test_validate_expanded_command_invalid_content()** (2 connections) — `server/tests/unit/commands/test_alias_expansion.py`
- **test_validate_expanded_command_ok()** (2 connections) — `server/tests/unit/commands/test_alias_expansion.py`
- **test_validate_expanded_command_too_long()** (2 connections) — `server/tests/unit/commands/test_alias_expansion.py`
- **Any** (1 connections)
- **CommandExecutionRequest** (1 connections)
- **Alias Expansion Logic for MythosMUD. This module handles alias resolution,…** (1 connections) — `server/command_handler/alias_expansion.py`
- **Handle command processing with alias expansion and loop detection. This…** (1 connections) — `server/command_handler/alias_expansion.py`
- **Check if an alias is safe to expand. Builds an alias dependency graph and…** (1 connections) — `server/command_handler/alias_expansion.py`
- **Validate an expanded command for length and content. Args: expanded_command:…** (1 connections) — `server/command_handler/alias_expansion.py`
- **Unit tests for alias_expansion module.** (1 connections) — `server/tests/unit/commands/test_alias_expansion.py`

## Relationships

- [command_handler_unified.py](command_handler_unified.py.md) (6 shared connections)
- [command_input.py](command_input.py.md) (4 shared connections)
- [test_command_validator.py](test_command_validator.py.md) (3 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [AliasGraph](AliasGraph.md) (2 shared connections)
- [test_command_processing.py](test_command_processing.py.md) (2 shared connections)
- [AliasStorage](AliasStorage.md) (1 shared connections)
- [audit_logger.py](audit_logger.py.md) (1 shared connections)
- [WebSocketRequestContext](WebSocketRequestContext.md) (1 shared connections)
- [alias_storage.py](alias_storage.py.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/command_handler/alias_expansion.py`
- `server/tests/unit/commands/test_alias_expansion.py`

## Audit Trail

- EXTRACTED: 60 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*