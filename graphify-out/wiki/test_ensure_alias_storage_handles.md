# .test ensure alias storage handles

> 16 nodes

## Key Concepts

- **_ensure_alias_storage()** (13 connections) — `server/command_handler_unified.py`
- **TestEnsureAliasStorage** (5 connections) — `server/tests/unit/commands/test_command_aliases.py`
- **.test_ensure_alias_storage_provided()** (4 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **.test_ensure_alias_storage_returns_existing()** (3 connections) — `server/tests/unit/commands/test_command_aliases.py`
- **.test_ensure_alias_storage_initializes_new()** (3 connections) — `server/tests/unit/commands/test_command_aliases.py`
- **.test_ensure_alias_storage_handles_error()** (3 connections) — `server/tests/unit/commands/test_command_aliases.py`
- **.test_ensure_alias_storage_creates_new()** (3 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **.test_ensure_alias_storage_handles_error()** (3 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **Ensure alias storage is initialized.** (1 connections) — `server/command_handler_unified.py`
- **Test _ensure_alias_storage function.** (1 connections) — `server/tests/unit/commands/test_command_aliases.py`
- **Test _ensure_alias_storage returns existing storage if provided.** (1 connections) — `server/tests/unit/commands/test_command_aliases.py`
- **Test _ensure_alias_storage initializes new storage when None.** (1 connections) — `server/tests/unit/commands/test_command_aliases.py`
- **Test _ensure_alias_storage returns None on initialization error.** (1 connections) — `server/tests/unit/commands/test_command_aliases.py`
- **Test _ensure_alias_storage returns provided storage.** (1 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **Test _ensure_alias_storage creates new storage when None.** (1 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **Test _ensure_alias_storage returns None on error.** (1 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`

## Relationships

- [check alias safety()](check_alias_safety%28%29.md) (7 shared connections)
- [Any](Any.md) (2 shared connections)
- [Test prepare command for processing](Test_prepare_command_for_processing.md) (1 shared connections)
- [initialize nats and combat services()](initialize_nats_and_combat_services%28%29.md) (1 shared connections)

## Source Files

- `server/command_handler_unified.py`
- `server/tests/unit/commands/test_command_aliases.py`
- `server/tests/unit/commands/test_command_handler_unified_helpers.py`

## Audit Trail

- EXTRACTED: 44 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*