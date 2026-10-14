# _DyingPlayer

> 16 nodes

## Key Concepts

- **_DyingPlayer** (7 connections) — `server/services/corpse_lifecycle_service.py`
- **_RoomContainers** (5 connections) — `server/services/corpse_lifecycle_service.py`
- **Protocol** (5 connections)
- **_SyncRoomLookup** (4 connections) — `server/services/corpse_lifecycle_service.py`
- **.get_equipped_items()** (2 connections) — `server/services/corpse_lifecycle_service.py`
- **.add_container()** (2 connections) — `server/services/corpse_lifecycle_service.py`
- **.remove_container()** (2 connections) — `server/services/corpse_lifecycle_service.py`
- **.get_room_by_id()** (2 connections) — `server/services/corpse_lifecycle_service.py`
- **.get_inventory()** (1 connections) — `server/services/corpse_lifecycle_service.py`
- **The in-memory Room's container registry (server/models/room.py::Room). An…** (1 connections) — `server/services/corpse_lifecycle_service.py`
- **Register a runtime-created container so room_state carries it.** (1 connections) — `server/services/corpse_lifecycle_service.py`
- **Drop a container from the room.** (1 connections) — `server/services/corpse_lifecycle_service.py`
- **The synchronous room lookup _live_room needs from a persistence layer.** (1 connections) — `server/services/corpse_lifecycle_service.py`
- **Return the in-memory Room for room_id (may be an awaitable on async-only…** (1 connections) — `server/services/corpse_lifecycle_service.py`
- **The slice of Player that moving a dead player's gear onto a corpse reads (#917).** (1 connections) — `server/services/corpse_lifecycle_service.py`
- **Equipped stacks keyed by slot.** (1 connections) — `server/services/corpse_lifecycle_service.py`

## Relationships

- [UUID](UUID.md) (3 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [CombatService](CombatService.md) (1 shared connections)

## Source Files

- `server/services/corpse_lifecycle_service.py`

## Audit Trail

- EXTRACTED: 22 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*