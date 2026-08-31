# UUID

> 5 nodes

## Key Concepts

- **UUID** (8 connections)
- **._publish_player_dp_correction_event()** (5 connections) — `server/services/combat_hp_sync.py`
- **._persist_player_dp_background()** (3 connections) — `server/services/combat_hp_sync.py`
- **Publish a correction event when database persistence fails.** (1 connections) — `server/services/combat_hp_sync.py`
- **Persist player DP to database in background (fire-and-forget). This method runs…** (1 connections) — `server/services/combat_hp_sync.py`

## Relationships

- [NATSError](NATSError.md) (7 shared connections)
- [EventBus](EventBus.md) (1 shared connections)
- [PlayerEnteredRoom](PlayerEnteredRoom.md) (1 shared connections)
- [event_types.py](event_types.py.md) (1 shared connections)

## Source Files

- `server/services/combat_hp_sync.py`

## Audit Trail

- EXTRACTED: 14 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*