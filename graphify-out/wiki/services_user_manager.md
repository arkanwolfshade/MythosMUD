# services user manager

> 6 nodes

## Key Concepts

- **.get_player_and_room()** (6 connections) — `server/commands/combat_handler.py`
- **AppWithState** (5 connections)
- **._get_persistence_from_app()** (5 connections) — `server/commands/combat_handler.py`
- **Get player data and room, returning error dict if any step fails. Public API.** (1 connections) — `server/commands/combat_handler.py`
- **Resolve persistence from app (container preferred, then app.state). Returns None** (1 connections) — `server/commands/combat_handler.py`
- **Get player data and room, returning error dict if any step fails.** (1 connections) — `server/commands/combat_handler.py`

## Relationships

- [player event handlers](player_event_handlers.md) (2 shared connections)
- [NPC Services Bootstrap](NPC_Services_Bootstrap.md) (2 shared connections)
- [alias storage rationale](alias_storage_rationale.md) (1 shared connections)
- [rest grace period](rest_grace_period.md) (1 shared connections)
- [connection realtime manager](connection_realtime_manager.md) (1 shared connections)

## Source Files

- `server/commands/combat_handler.py`

## Audit Trail

- EXTRACTED: 16 (84%)
- INFERRED: 3 (16%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*