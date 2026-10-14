# CorpseLifecycleService

> 30 nodes

## Key Concepts

- **CorpseLifecycleService** (71 connections) — `server/services/corpse_lifecycle_service.py`
- **.cleanup_decayed_corpse()** (8 connections) — `server/services/corpse_lifecycle_service.py`
- **._persist_corpse()** (8 connections) — `server/services/corpse_lifecycle_service.py`
- **.get_decayed_corpses_in_room()** (6 connections) — `server/services/corpse_lifecycle_service.py`
- **._register_corpse_on_room()** (6 connections) — `server/services/corpse_lifecycle_service.py`
- **.can_access_corpse()** (5 connections) — `server/services/corpse_lifecycle_service.py`
- **.get_all_decayed_corpses()** (5 connections) — `server/services/corpse_lifecycle_service.py`
- **.cleanup_all_decayed_corpses()** (4 connections) — `server/services/corpse_lifecycle_service.py`
- **.cleanup_decayed_corpses_in_room()** (4 connections) — `server/services/corpse_lifecycle_service.py`
- **._emit_corpse_created()** (4 connections) — `server/services/corpse_lifecycle_service.py`
- **.is_corpse_decayed()** (4 connections) — `server/services/corpse_lifecycle_service.py`
- **._live_room()** (4 connections) — `server/services/corpse_lifecycle_service.py`
- **._unregister_corpse_from_room()** (4 connections) — `server/services/corpse_lifecycle_service.py`
- **._grace_period_allows_others()** (3 connections) — `server/services/corpse_lifecycle_service.py`
- **test_corpse_lifecycle_service_init_no_persistence()** (3 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_live_room_returns_none_when_persistence_has_no_sync_lookup()** (3 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **Service for managing corpse container lifecycle. Handles creation on death,…** (1 connections) — `server/services/corpse_lifecycle_service.py`
- **Add the corpse to the in-memory Room so room_state carries it (#711). The…** (1 connections) — `server/services/corpse_lifecycle_service.py`
- **Drop a decayed corpse from the in-memory Room (mirror of…** (1 connections) — `server/services/corpse_lifecycle_service.py`
- **In-memory Room for room_id, or None when persistence exposes no sync lookup.** (1 connections) — `server/services/corpse_lifecycle_service.py`
- **Best-effort container.created broadcast so room occupants see the fresh corpse.…** (1 connections) — `server/services/corpse_lifecycle_service.py`
- **True if player may access corpse (owner/admin always; others after grace).** (1 connections) — `server/services/corpse_lifecycle_service.py`
- **Check if a corpse container has decayed. Args: corpse: Corpse container to…** (1 connections) — `server/services/corpse_lifecycle_service.py`
- **Get all decayed corpse containers in a room. Args: room_id: Room ID to check…** (1 connections) — `server/services/corpse_lifecycle_service.py`
- **Delete a decayed corpse container (items discarded with the container).** (1 connections) — `server/services/corpse_lifecycle_service.py`
- *... and 5 more nodes in this community*

## Relationships

- [ContainerComponent](ContainerComponent.md) (27 shared connections)
- [test_corpse_lifecycle_decay.py](test_corpse_lifecycle_decay.py.md) (19 shared connections)
- [UUID](UUID.md) (9 shared connections)
- [_get_enum_value](_get_enum_value.md) (7 shared connections)
- [CombatService](CombatService.md) (3 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [game_tick_processing.py](game_tick_processing.py.md) (2 shared connections)
- [game_tick_death.py](game_tick_death.py.md) (2 shared connections)
- [corpse_service](corpse_service.md) (2 shared connections)
- [_RecordingRoom](_RecordingRoom.md) (1 shared connections)
- [test_container_websocket_events.py](test_container_websocket_events.py.md) (1 shared connections)

## Source Files

- `server/services/corpse_lifecycle_service.py`
- `server/tests/unit/services/test_corpse_lifecycle_service.py`

## Audit Trail

- EXTRACTED: 89 (77%)
- INFERRED: 27 (23%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*