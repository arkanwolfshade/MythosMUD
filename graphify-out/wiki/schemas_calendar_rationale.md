# schemas calendar rationale

> 10 nodes

## Key Concepts

- **handle_aliases_command()** (11 connections) — `server/commands/alias_commands.py`
- **test_handle_aliases_command_no_storage()** (3 connections) — `server/tests/unit/commands/test_alias_commands.py`
- **test_handle_aliases_command_no_aliases()** (3 connections) — `server/tests/unit/commands/test_alias_commands.py`
- **test_handle_aliases_command_with_aliases()** (3 connections) — `server/tests/unit/commands/test_alias_commands.py`
- **test_handle_aliases_command_error()** (3 connections) — `server/tests/unit/commands/test_alias_commands.py`
- **Handle the aliases command for listing all aliases.      Args:         command_d** (1 connections) — `server/commands/alias_commands.py`
- **Test handle_aliases_command when alias storage is not available.** (1 connections) — `server/tests/unit/commands/test_alias_commands.py`
- **Test handle_aliases_command when player has no aliases.** (1 connections) — `server/tests/unit/commands/test_alias_commands.py`
- **Test handle_aliases_command listing aliases.** (1 connections) — `server/tests/unit/commands/test_alias_commands.py`
- **Test handle_aliases_command when listing fails.** (1 connections) — `server/tests/unit/commands/test_alias_commands.py`

## Relationships

- [scripts worktree ops](scripts_worktree_ops.md) (5 shared connections)
- [commands admin mute](commands_admin_mute.md) (3 shared connections)
- [realtime circuit breaker](realtime_circuit_breaker.md) (1 shared connections)
- [commands alias rationale](commands_alias_rationale.md) (1 shared connections)

## Source Files

- `server/commands/alias_commands.py`
- `server/tests/unit/commands/test_alias_commands.py`

## Audit Trail

- EXTRACTED: 28 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*