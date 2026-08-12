# .get_player_and_room

> 6 nodes

## Key Concepts

- **.get_player_and_room()** (6 connections) — `server/commands/combat_handler.py`
- **._get_persistence_from_app()** (5 connections) — `server/commands/combat_handler.py`
- **AppWithState** (3 connections)
- **Get player data and room, returning error dict if any step fails. Public API.** (1 connections) — `server/commands/combat_handler.py`
- **Resolve persistence from app (container preferred, then app.state). Returns…** (1 connections) — `server/commands/combat_handler.py`
- **Get player data and room, returning error dict if any step fails.** (1 connections) — `server/commands/combat_handler.py`

## Relationships

- [CombatCommandHandler](CombatCommandHandler.md) (2 shared connections)
- [get_logger](get_logger.md) (1 shared connections)
- [get_username_from_user](get_username_from_user.md) (1 shared connections)
- [test_rest_command.py](test_rest_command.py.md) (1 shared connections)

## Source Files

- `server/commands/combat_handler.py`

## Audit Trail

- EXTRACTED: 16 (94%)
- INFERRED: 1 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*