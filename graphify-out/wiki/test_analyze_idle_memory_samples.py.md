# test_analyze_idle_memory_samples.py

> 19 nodes · cohesion 0.11

## Key Concepts

- **_DeathPersistence** (6 connections) — `server/services/corpse_lifecycle_service.py`
- **Protocol** (5 connections)
- **_RoomContainers** (5 connections) — `server/services/corpse_lifecycle_service.py`
- **_SyncRoomLookup** (4 connections) — `server/services/corpse_lifecycle_service.py`
- **.clear_player_inventory()** (3 connections) — `server/services/corpse_lifecycle_service.py`
- **.delete_container()** (3 connections) — `server/services/corpse_lifecycle_service.py`
- **.get_containers_by_entity_id()** (3 connections) — `server/services/corpse_lifecycle_service.py`
- **.add_container()** (2 connections) — `server/services/corpse_lifecycle_service.py`
- **.remove_container()** (2 connections) — `server/services/corpse_lifecycle_service.py`
- **.get_room_by_id()** (2 connections) — `server/services/corpse_lifecycle_service.py`
- **The in-memory Room's container registry (server/models/room.py::Room). An…** (1 connections) — `server/services/corpse_lifecycle_service.py`
- **Register a runtime-created container so room_state carries it.** (1 connections) — `server/services/corpse_lifecycle_service.py`
- **Drop a container from the room.** (1 connections) — `server/services/corpse_lifecycle_service.py`
- **The synchronous room lookup _live_room needs from a persistence layer.** (1 connections) — `server/services/corpse_lifecycle_service.py`
- **Return the in-memory Room for room_id (may be an awaitable on async-only…** (1 connections) — `server/services/corpse_lifecycle_service.py`
- **The persistence calls moving a dead player's gear onto a corpse makes (#917).** (1 connections) — `server/services/corpse_lifecycle_service.py`
- **Containers owned by an entity (a player's worn-container rows).** (1 connections) — `server/services/corpse_lifecycle_service.py`
- **Delete a container row.** (1 connections) — `server/services/corpse_lifecycle_service.py`
- **Empty only the player's carried and equipped items (never stats: no race with…** (1 connections) — `server/services/corpse_lifecycle_service.py`

## Relationships

- [ApplicationContainer](ApplicationContainer.md) (4 shared connections)
- [connection_manager_methods.py](connection_manager_methods.py.md) (3 shared connections)
- [test_npc_combat_integration_join.py](test_npc_combat_integration_join.py.md) (1 shared connections)

## Source Files

- `server/services/corpse_lifecycle_service.py`

## Audit Trail

- EXTRACTED: 26 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*