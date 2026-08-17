# server commands combat handler combatcommandhandler

> 6 nodes

## Key Concepts

- **.get_player_and_room()** (6 connections) — `server/commands/combat_handler.py`
- **._get_persistence_from_app()** (5 connections) — `server/commands/combat_handler.py`
- **AppWithState** (3 connections)
- **Get player data and room, returning error dict if any step fails. Public API.** (1 connections) — `server/commands/combat_handler.py`
- **Resolve persistence from app (container preferred, then app.state). Returns…** (1 connections) — `server/commands/combat_handler.py`
- **Get player data and room, returning error dict if any step fails.** (1 connections) — `server/commands/combat_handler.py`

## Relationships

- [server commands combat handler combatcommandhandler](server_commands_combat_handler_combatcommandhandler.md) (3 shared connections)
- [server async persistence asyncpersistencelayer](server_async_persistence_asyncpersistencelayer.md) (1 shared connections)
- [server commands admin commands](server_commands_admin_commands.md) (1 shared connections)

## Source Files

- `server/commands/combat_handler.py`

## Audit Trail

- EXTRACTED: 10 (91%)
- INFERRED: 1 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*