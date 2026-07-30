# Test process exit rows logs

> 6 nodes

## Key Concepts

- **.get_player_and_room()** (6 connections) — `server/commands/combat_handler.py`
- **AppWithState** (5 connections)
- **._get_persistence_from_app()** (5 connections) — `server/commands/combat_handler.py`
- **Get player data and room, returning error dict if any step fails. Public API.** (1 connections) — `server/commands/combat_handler.py`
- **Resolve persistence from app (container preferred, then app.state). Returns None** (1 connections) — `server/commands/combat_handler.py`
- **Get player data and room, returning error dict if any step fails.** (1 connections) — `server/commands/combat_handler.py`

## Relationships

- [chat nats publisher](chat_nats_publisher.md) (2 shared connections)
- [CombatService](CombatService.md) (2 shared connections)
- [Any](Any.md) (1 shared connections)
- [PlayerPositionService](PlayerPositionService.md) (1 shared connections)
- [Player Position Service](Player_Position_Service.md) (1 shared connections)

## Source Files

- `server/commands/combat_handler.py`

## Audit Trail

- EXTRACTED: 16 (84%)
- INFERRED: 3 (16%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*