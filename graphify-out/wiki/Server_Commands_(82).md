# Server Commands (82)

> 6 nodes

## Key Concepts

- **.get_player_and_room()** (6 connections) — `server/commands/combat_handler.py`
- **AppWithState** (5 connections)
- **._get_persistence_from_app()** (5 connections) — `server/commands/combat_handler.py`
- **Get player data and room, returning error dict if any step fails. Public API.** (1 connections) — `server/commands/combat_handler.py`
- **Resolve persistence from app (container preferred, then app.state). Returns None** (1 connections) — `server/commands/combat_handler.py`
- **Get player data and room, returning error dict if any step fails.** (1 connections) — `server/commands/combat_handler.py`

## Relationships

- [Server Infrastructure (4)](Server_Infrastructure_%284%29.md) (2 shared connections)
- [Server Commands (8)](Server_Commands_%288%29.md) (2 shared connections)
- [Server Commands (15)](Server_Commands_%2815%29.md) (1 shared connections)
- [Server Commands](Server_Commands.md) (1 shared connections)
- [Server Utils (6)](Server_Utils_%286%29.md) (1 shared connections)

## Source Files

- `server/commands/combat_handler.py`

## Audit Trail

- EXTRACTED: 16 (84%)
- INFERRED: 3 (16%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*