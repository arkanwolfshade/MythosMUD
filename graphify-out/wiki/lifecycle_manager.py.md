# lifecycle_manager.py

> 95 nodes

## Key Concepts

- **lifecycle_manager.py** (49 connections) — `server/npc/lifecycle_manager.py`
- **NPCLeftRoom** (45 connections) — `server/events/event_types.py`
- **NPCDied** (32 connections) — `server/events/event_types.py`
- **test_lifecycle_manager.py** (27 connections) — `server/tests/unit/npc/test_lifecycle_manager.py`
- **lifecycle_death.py** (24 connections) — `server/npc/lifecycle_death.py`
- **test_lifecycle_despawn.py** (19 connections) — `server/tests/unit/npc/test_lifecycle_despawn.py`
- **NPCLifecycleRecord** (18 connections) — `server/npc/lifecycle_types.py`
- **despawn_npc_impl()** (18 connections) — `server/npc/lifecycle_despawn.py`
- **_make_manager()** (18 connections) — `server/tests/unit/npc/test_lifecycle_manager.py`
- **NPCLifecycleState** (17 connections) — `server/npc/lifecycle_types.py`
- **_LifecycleManagerForDeath** (16 connections) — `server/npc/lifecycle_death.py`
- **_SpawningServiceProtocol** (16 connections) — `server/npc/lifecycle_manager.py`
- **_SpawnTrackedNPC** (16 connections) — `server/npc/lifecycle_manager.py`
- **lifecycle_despawn.py** (16 connections) — `server/npc/lifecycle_despawn.py`
- **lifecycle_types.py** (16 connections) — `server/npc/lifecycle_types.py`
- **test_lifecycle_death.py** (16 connections) — `server/tests/unit/npc/test_lifecycle_death.py`
- **NPCLifecycleEvent** (12 connections) — `server/npc/lifecycle_types.py`
- **handle_npc_died_impl()** (11 connections) — `server/npc/lifecycle_death.py`
- **_make_manager()** (10 connections) — `server/tests/unit/npc/test_lifecycle_despawn.py`
- **_mark_despawned_and_queue_respawn()** (8 connections) — `server/npc/lifecycle_death.py`
- **_remove_active_npc_and_notify()** (8 connections) — `server/npc/lifecycle_death.py`
- **_resolve_despawn_room_id()** (6 connections) — `server/npc/lifecycle_despawn.py`
- **_remove_npc_from_room_on_despawn()** (5 connections) — `server/npc/lifecycle_despawn.py`
- **.add_event()** (5 connections) — `server/npc/lifecycle_types.py`
- **_manager_stub()** (5 connections) — `server/tests/unit/npc/test_lifecycle_death.py`
- *... and 70 more nodes in this community*

## Relationships

- [event_types.py](event_types.py.md) (29 shared connections)
- [EventBus](EventBus.md) (28 shared connections)
- [NPCLifecycleManager](NPCLifecycleManager.md) (26 shared connections)
- [get_logger](get_logger.md) (12 shared connections)
- [test_npc_event_handlers.py](test_npc_event_handlers.py.md) (9 shared connections)
- [.__post_init__](__post_init__.md) (8 shared connections)
- [population_control.py](population_control.py.md) (8 shared connections)
- [test_lifecycle_periodic.py](test_lifecycle_periodic.py.md) (8 shared connections)
- [test_quest_events.py](test_quest_events.py.md) (4 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (3 shared connections)
- [NPCThreadManager](NPCThreadManager.md) (3 shared connections)
- [connection_manager.py](connection_manager.py.md) (3 shared connections)

## Source Files

- `server/events/event_types.py`
- `server/npc/lifecycle_death.py`
- `server/npc/lifecycle_despawn.py`
- `server/npc/lifecycle_manager.py`
- `server/npc/lifecycle_types.py`
- `server/npc/spawning_service.py`
- `server/tests/unit/npc/test_lifecycle_death.py`
- `server/tests/unit/npc/test_lifecycle_despawn.py`
- `server/tests/unit/npc/test_lifecycle_manager.py`

## Audit Trail

- EXTRACTED: 324 (89%)
- INFERRED: 42 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*