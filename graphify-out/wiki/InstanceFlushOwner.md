# InstanceFlushOwner

> 5 nodes

## Key Concepts

- **InstanceFlushOwner** (9 connections) — `server/realtime/player_disconnect_handlers.py`
- **.instance_flush_service()** (2 connections) — `server/realtime/player_disconnect_handlers.py`
- **Protocol** (1 connections)
- **The ConnectionManager's instance flusher, as departure cleanup reads it.** (1 connections) — `server/realtime/player_disconnect_handlers.py`
- **Set by the game bundle; None in tests and early startup.** (1 connections) — `server/realtime/player_disconnect_handlers.py`

## Relationships

- [get_logger](get_logger.md) (2 shared connections)
- [player_presence_tracker.py](player_presence_tracker.py.md) (2 shared connections)
- [test_player_disconnect_handlers.py](test_player_disconnect_handlers.py.md) (1 shared connections)
- [start_grace_period](start_grace_period.md) (1 shared connections)

## Source Files

- `server/realtime/player_disconnect_handlers.py`

## Audit Trail

- EXTRACTED: 8 (80%)
- INFERRED: 2 (20%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*