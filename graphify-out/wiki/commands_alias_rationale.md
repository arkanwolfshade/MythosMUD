# commands alias rationale

> 17 nodes

## Key Concepts

- **handle_alias_command()** (24 connections) — `server/commands/alias_commands.py`
- **_extract_alias_params()** (4 connections) — `server/commands/alias_commands.py`
- **Any** (4 connections)
- **test_handle_alias_command_no_storage()** (3 connections) — `server/tests/unit/commands/test_alias_commands.py`
- **test_handle_alias_command_view_nonexistent()** (3 connections) — `server/tests/unit/commands/test_alias_commands.py`
- **test_handle_alias_command_create_from_args()** (3 connections) — `server/tests/unit/commands/test_alias_commands.py`
- **test_handle_alias_command_create_from_structured_data()** (3 connections) — `server/tests/unit/commands/test_alias_commands.py`
- **test_handle_alias_command_create_error()** (3 connections) — `server/tests/unit/commands/test_alias_commands.py`
- **test_handle_alias_command_invalid_command_empty()** (3 connections) — `server/tests/unit/commands/test_alias_commands.py`
- **Extract alias_name and command from command_data. Returns (alias_name, command).** (1 connections) — `server/commands/alias_commands.py`
- **Handle the alias command for creating and viewing aliases.      Args:         co** (1 connections) — `server/commands/alias_commands.py`
- **Test handle_alias_command when alias storage is not available.** (1 connections) — `server/tests/unit/commands/test_alias_commands.py`
- **Test handle_alias_command viewing nonexistent alias.** (1 connections) — `server/tests/unit/commands/test_alias_commands.py`
- **Test handle_alias_command creating alias from args.** (1 connections) — `server/tests/unit/commands/test_alias_commands.py`
- **Test handle_alias_command creating alias from structured data.** (1 connections) — `server/tests/unit/commands/test_alias_commands.py`
- **Test handle_alias_command when creation fails.** (1 connections) — `server/tests/unit/commands/test_alias_commands.py`
- **Test handle_alias_command with empty command.** (1 connections) — `server/tests/unit/commands/test_alias_commands.py`

## Relationships

- [scripts worktree ops](scripts_worktree_ops.md) (11 shared connections)
- [realtime circuit breaker](realtime_circuit_breaker.md) (4 shared connections)
- [commands admin mute](commands_admin_mute.md) (3 shared connections)
- [schemas calendar rationale](schemas_calendar_rationale.md) (1 shared connections)
- [emote game service](emote_game_service.md) (1 shared connections)
- [combat services messaging](combat_services_messaging.md) (1 shared connections)
- [schemas player requests](schemas_player_requests.md) (1 shared connections)
- [headers middleware security](headers_middleware_security.md) (1 shared connections)
- [ascii map renderer](ascii_map_renderer.md) (1 shared connections)

## Source Files

- `server/commands/alias_commands.py`
- `server/tests/unit/commands/test_alias_commands.py`

## Audit Trail

- EXTRACTED: 58 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*