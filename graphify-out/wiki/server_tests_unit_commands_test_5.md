# server tests unit commands test

> 13 nodes

## Key Concepts

- **asyncio** (7 connections)
- **TestProcessAliasExpansion** (6 connections) — `server/tests/unit/commands/test_command_aliases.py`
- **.test_handle_special_command_routing_alias_command_no_storage()** (4 connections) — `server/tests/unit/commands/test_command_aliases.py`
- **.test_process_alias_expansion_invalid_expanded()** (4 connections) — `server/tests/unit/commands/test_command_aliases.py`
- **.test_process_alias_expansion_no_alias()** (4 connections) — `server/tests/unit/commands/test_command_aliases.py`
- **.test_process_alias_expansion_no_alias_storage()** (4 connections) — `server/tests/unit/commands/test_command_aliases.py`
- **.test_process_alias_expansion_unsafe_alias()** (4 connections) — `server/tests/unit/commands/test_command_aliases.py`
- **Test _handle_special_command_routing returns error when alias storage…** (1 connections) — `server/tests/unit/commands/test_command_aliases.py`
- **Test _process_alias_expansion function.** (1 connections) — `server/tests/unit/commands/test_command_aliases.py`
- **Test _process_alias_expansion returns None when no alias storage.** (1 connections) — `server/tests/unit/commands/test_command_aliases.py`
- **Test _process_alias_expansion returns None when alias not found.** (1 connections) — `server/tests/unit/commands/test_command_aliases.py`
- **Test _process_alias_expansion returns error for unsafe alias.** (1 connections) — `server/tests/unit/commands/test_command_aliases.py`
- **Test _process_alias_expansion returns error for invalid expanded command.** (1 connections) — `server/tests/unit/commands/test_command_aliases.py`

## Relationships

- [server command handler command execution](server_command_handler_command_execution.md) (5 shared connections)
- [server command handler unified check](server_command_handler_unified_check.md) (4 shared connections)

## Source Files

- `server/tests/unit/commands/test_command_aliases.py`

## Audit Trail

- EXTRACTED: 24 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*