# Archive Fixture Optimization

> 2 nodes · cohesion 1.00

## Key Concepts

- **test_on_player_entered_room_moves_followers()** (3 connections) — `server/tests/unit/game/test_follow_service.py`
- **When followed player moves, followers are moved same from_room -> to_room.** (1 connections) — `server/tests/unit/game/test_follow_service.py`

## Relationships

- [Distributed Event Bus](Distributed_Event_Bus.md) (1 shared connections)
- [NPC Combat Integration](NPC_Combat_Integration.md) (1 shared connections)

## Source Files

- `server/tests/unit/game/test_follow_service.py`

## Audit Trail

- EXTRACTED: 4 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*