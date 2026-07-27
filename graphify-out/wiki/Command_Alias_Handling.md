# Command Alias Handling

> 47 nodes · cohesion 0.06

## Key Concepts

- **TestHelperFunctions** (33 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **_process_alias_expansion()** (19 connections) — `server/command_handler_unified.py`
- **_ensure_alias_storage()** (14 connections) — `server/command_handler_unified.py`
- **test_command_handler_unified_helpers.py** (13 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **test_command_aliases.py** (8 connections) — `server/tests/unit/commands/test_command_aliases.py`
- **TestProcessAliasExpansion** (6 connections) — `server/tests/unit/commands/test_command_aliases.py`
- **TestEnsureAliasStorage** (5 connections) — `server/tests/unit/commands/test_command_aliases.py`
- **Test _process_alias_expansion returns error for invalid expanded command.** (4 connections) — `server/tests/unit/commands/test_command_aliases.py`
- **.test_ensure_alias_storage_handles_error()** (3 connections) — `server/tests/unit/commands/test_command_aliases.py`
- **.test_ensure_alias_storage_initializes_new()** (3 connections) — `server/tests/unit/commands/test_command_aliases.py`
- **.test_ensure_alias_storage_returns_existing()** (3 connections) — `server/tests/unit/commands/test_command_aliases.py`
- **.test_process_alias_expansion_invalid_expanded()** (3 connections) — `server/tests/unit/commands/test_command_aliases.py`
- **.test_process_alias_expansion_no_alias()** (3 connections) — `server/tests/unit/commands/test_command_aliases.py`
- **.test_process_alias_expansion_no_alias_storage()** (3 connections) — `server/tests/unit/commands/test_command_aliases.py`
- **.test_process_alias_expansion_unsafe_alias()** (3 connections) — `server/tests/unit/commands/test_command_aliases.py`
- **.test_check_rate_limit_allowed()** (3 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **.test_check_rate_limit_blocked()** (3 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **.test_ensure_alias_storage_creates_new()** (3 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **.test_ensure_alias_storage_handles_error()** (3 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **.test_ensure_alias_storage_provided()** (3 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **.test_prepare_command_for_processing_empty_after_cleaning()** (3 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **.test_prepare_command_for_processing_rate_limited()** (3 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **.test_prepare_command_for_processing_success()** (3 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **.test_prepare_command_for_processing_validation_failed()** (3 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **.test_process_alias_expansion_invalid_expanded()** (3 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- *... and 22 more nodes in this community*

## Relationships

- [[Unified Command Handler]] (16 shared connections)
- [[Alias Expansion Logic]] (9 shared connections)
- [[Command Commands Validation]] (9 shared connections)
- [[Grace Period Blocking Tests]] (6 shared connections)
- [[Command Request App State]] (6 shared connections)
- [[Commands Command Handler]] (2 shared connections)
- [[NPC Admin API]] (1 shared connections)

## Source Files

- `server/command_handler_unified.py`
- `server/tests/unit/commands/test_command_aliases.py`
- `server/tests/unit/commands/test_command_handler_unified_helpers.py`

## Audit Trail

- EXTRACTED: 184 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
