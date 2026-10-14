# NPCLifecycleManager

> 161 nodes

## Key Concepts

- **NPCLifecycleManager** (71 connections) — `server/npc/lifecycle_manager.py`
- **lifecycle_manager.py** (49 connections) — `server/npc/lifecycle_manager.py`
- **NPCDied** (29 connections) — `server/events/event_types.py`
- **test_lifecycle_manager.py** (29 connections) — `server/tests/unit/npc/test_lifecycle_manager.py`
- **NPCLifecycleState** (24 connections) — `server/npc/lifecycle_types.py`
- **lifecycle_death.py** (24 connections) — `server/npc/lifecycle_death.py`
- **despawn_npc_impl()** (22 connections) — `server/npc/lifecycle_despawn.py`
- **test_lifecycle_despawn.py** (21 connections) — `server/tests/unit/npc/test_lifecycle_despawn.py`
- **_make_manager()** (19 connections) — `server/tests/unit/npc/test_lifecycle_manager.py`
- **NPCLifecycleRecord** (16 connections) — `server/npc/lifecycle_types.py`
- **lifecycle_despawn.py** (16 connections) — `server/npc/lifecycle_despawn.py`
- **lifecycle_types.py** (16 connections) — `server/npc/lifecycle_types.py`
- **test_lifecycle_death.py** (16 connections) — `server/tests/unit/npc/test_lifecycle_death.py`
- **RoomOccupantsRefreshRequested** (14 connections) — `server/events/event_types.py`
- **NPCLifecycleEvent** (13 connections) — `server/npc/lifecycle_types.py`
- **_LifecycleManagerForDeath** (12 connections) — `server/npc/lifecycle_death.py`
- **._spawn_npc_impl()** (12 connections) — `server/npc/lifecycle_manager.py`
- **_make_manager()** (12 connections) — `server/tests/unit/npc/test_lifecycle_despawn.py`
- **handle_npc_died_impl()** (11 connections) — `server/npc/lifecycle_death.py`
- **_mark_despawned_and_queue_respawn()** (10 connections) — `server/npc/lifecycle_death.py`
- **_remove_active_npc_and_notify()** (8 connections) — `server/npc/lifecycle_death.py`
- **.__init__()** (8 connections) — `server/npc/lifecycle_manager.py`
- **_resolve_despawn_room_id()** (6 connections) — `server/npc/lifecycle_despawn.py`
- **._finalize_spawn_record()** (6 connections) — `server/npc/lifecycle_manager.py`
- **._notify_room_and_threads()** (6 connections) — `server/npc/lifecycle_manager.py`
- *... and 136 more nodes in this community*

## Relationships

- [EventBus](EventBus.md) (68 shared connections)
- [get_logger](get_logger.md) (16 shared connections)
- [test_lifecycle_periodic.py](test_lifecycle_periodic.py.md) (13 shared connections)
- [NPCPopulationController](NPCPopulationController.md) (11 shared connections)
- [PlayerEnteredRoom](PlayerEnteredRoom.md) (6 shared connections)
- [test_lifespan_event_subscriptions.py](test_lifespan_event_subscriptions.py.md) (5 shared connections)
- [PlayerCombatService](PlayerCombatService.md) (5 shared connections)
- [test_npc_utils.py](test_npc_utils.py.md) (5 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (4 shared connections)
- [lifespan_startup.py](lifespan_startup.py.md) (3 shared connections)
- [test_lifecycle_respawn.py](test_lifecycle_respawn.py.md) (3 shared connections)
- [NPCThreadManager](NPCThreadManager.md) (3 shared connections)

## Source Files

- `server/events/event_types.py`
- `server/models/room.py`
- `server/npc/lifecycle_death.py`
- `server/npc/lifecycle_despawn.py`
- `server/npc/lifecycle_manager.py`
- `server/npc/lifecycle_types.py`
- `server/tests/unit/npc/test_lifecycle_death.py`
- `server/tests/unit/npc/test_lifecycle_despawn.py`
- `server/tests/unit/npc/test_lifecycle_manager.py`

## Audit Trail

- EXTRACTED: 418 (89%)
- INFERRED: 52 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*