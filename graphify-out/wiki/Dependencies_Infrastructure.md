# Dependencies Infrastructure

> 2 nodes · cohesion 1.00

## Key Concepts

- **test_get_players_batch_with_players()** (3 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_cache.py`
- **Test get_players_batch with actual players (UUID conversion).** (1 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_cache.py`

## Relationships

- [Event Bus Serialization](Event_Bus_Serialization.md) (1 shared connections)
- [Cursor Plans Postgresql](Cursor_Plans_Postgresql.md) (1 shared connections)

## Source Files

- `server/tests/unit/infrastructure/test_async_persistence_room_cache.py`

## Audit Trail

- EXTRACTED: 3 (75%)
- INFERRED: 1 (25%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*