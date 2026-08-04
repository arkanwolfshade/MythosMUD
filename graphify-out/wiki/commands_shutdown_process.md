# commands shutdown process

> 2 nodes

## Key Concepts

- **test_delete_player_persistence_fails()** (3 connections) — `server/tests/unit/game/test_player_service_mutations.py`
- **Test delete_player() when persistence.delete_player fails.** (1 connections) — `server/tests/unit/game/test_player_service_mutations.py`

## Relationships

- [Database Config](Database_Config.md) (1 shared connections)
- [room realtime subscription](room_realtime_subscription.md) (1 shared connections)

## Source Files

- `server/tests/unit/game/test_player_service_mutations.py`

## Audit Trail

- EXTRACTED: 3 (75%)
- INFERRED: 1 (25%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*