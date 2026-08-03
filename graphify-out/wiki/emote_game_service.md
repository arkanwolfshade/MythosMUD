# emote game service

> 12 nodes

## Key Concepts

- **handle_unalias_command()** (12 connections) — `server/commands/alias_commands.py`
- **test_handle_unalias_command_no_storage()** (3 connections) — `server/tests/unit/commands/test_alias_commands.py`
- **test_handle_unalias_command_no_args()** (3 connections) — `server/tests/unit/commands/test_alias_commands.py`
- **test_handle_unalias_command_alias_not_found()** (3 connections) — `server/tests/unit/commands/test_alias_commands.py`
- **test_handle_unalias_command_success()** (3 connections) — `server/tests/unit/commands/test_alias_commands.py`
- **test_handle_unalias_command_error()** (3 connections) — `server/tests/unit/commands/test_alias_commands.py`
- **Handle the unalias command for removing aliases.      Args:         command_data** (1 connections) — `server/commands/alias_commands.py`
- **Test handle_unalias_command when alias storage is not available.** (1 connections) — `server/tests/unit/commands/test_alias_commands.py`
- **Test handle_unalias_command with no arguments.** (1 connections) — `server/tests/unit/commands/test_alias_commands.py`
- **Test handle_unalias_command when alias doesn't exist.** (1 connections) — `server/tests/unit/commands/test_alias_commands.py`
- **Test handle_unalias_command successful removal.** (1 connections) — `server/tests/unit/commands/test_alias_commands.py`
- **Test handle_unalias_command when removal fails.** (1 connections) — `server/tests/unit/commands/test_alias_commands.py`

## Relationships

- [scripts worktree ops](scripts_worktree_ops.md) (6 shared connections)
- [commands admin mute](commands_admin_mute.md) (3 shared connections)
- [realtime circuit breaker](realtime_circuit_breaker.md) (1 shared connections)
- [commands alias rationale](commands_alias_rationale.md) (1 shared connections)

## Source Files

- `server/commands/alias_commands.py`
- `server/tests/unit/commands/test_alias_commands.py`

## Audit Trail

- EXTRACTED: 33 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*