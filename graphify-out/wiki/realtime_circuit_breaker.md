# realtime circuit breaker

> 8 nodes

## Key Concepts

- **alias_commands.py** (15 connections) — `server/commands/alias_commands.py`
- **_create_alias()** (5 connections) — `server/commands/alias_commands.py`
- **_view_alias()** (4 connections) — `server/commands/alias_commands.py`
- **_validate_alias_params()** (3 connections) — `server/commands/alias_commands.py`
- **Alias management commands for MythosMUD.  This module contains handlers for alia** (1 connections) — `server/commands/alias_commands.py`
- **View an existing alias. Returns result dict.** (1 connections) — `server/commands/alias_commands.py`
- **Validate alias name and command. Returns error dict if invalid, None if valid.** (1 connections) — `server/commands/alias_commands.py`
- **Create or update an alias. Returns result dict.** (1 connections) — `server/commands/alias_commands.py`

## Relationships

- [commands admin mute](commands_admin_mute.md) (6 shared connections)
- [commands alias rationale](commands_alias_rationale.md) (4 shared connections)
- [command inventory factories](command_inventory_factories.md) (2 shared connections)
- [schemas calendar rationale](schemas_calendar_rationale.md) (1 shared connections)
- [emote game service](emote_game_service.md) (1 shared connections)
- [scripts worktree ops](scripts_worktree_ops.md) (1 shared connections)

## Source Files

- `server/commands/alias_commands.py`

## Audit Trail

- EXTRACTED: 31 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*