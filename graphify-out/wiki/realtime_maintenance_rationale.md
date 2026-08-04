# realtime maintenance rationale

> 2 nodes

## Key Concepts

- **test_remove_player_invalid_params()** (3 connections) — `server/tests/unit/game/test_movement_service.py`
- **Test remove_player_from_room validates empty player_id.** (1 connections) — `server/tests/unit/game/test_movement_service.py`

## Relationships

- [Loot Generation](Loot_Generation.md) (1 shared connections)
- [movement service game](movement_service_game.md) (1 shared connections)

## Source Files

- `server/tests/unit/game/test_movement_service.py`

## Audit Trail

- EXTRACTED: 3 (75%)
- INFERRED: 1 (25%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*