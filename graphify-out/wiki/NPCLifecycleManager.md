# NPCLifecycleManager

> 161 nodes

## Key Concepts

- **NPCLifecycleManager** (71 connections) — `server/npc/lifecycle_manager.py`
- **lifecycle_manager.py** (49 connections) — `server/npc/lifecycle_manager.py`
- **NPCLeftRoom** (43 connections) — `server/events/event_types.py`
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
- **_resolve_despawn_room_id()** (6 connections) — `server/npc/lifecycle_despawn.py`
- **._finalize_spawn_record()** (6 connections) — `server/npc/lifecycle_manager.py`
- **._notify_room_and_threads()** (6 connections) — `server/npc/lifecycle_manager.py`
- *... and 136 more nodes in this community*

## Relationships

- [NPCDefinition](NPCDefinition.md) (39 shared connections)
- [event_types.py](event_types.py.md) (20 shared connections)
- [NPCPopulationController](NPCPopulationController.md) (16 shared connections)
- [test_lifecycle_periodic.py](test_lifecycle_periodic.py.md) (13 shared connections)
- [EventBus](EventBus.md) (11 shared connections)
- [get_logger](get_logger.md) (10 shared connections)
- [event_handler.py](event_handler.py.md) (6 shared connections)
- [test_npc_event_handlers.py](test_npc_event_handlers.py.md) (6 shared connections)
- [FollowService](FollowService.md) (6 shared connections)
- [test_lifespan_event_subscriptions.py](test_lifespan_event_subscriptions.py.md) (5 shared connections)
- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (5 shared connections)
- [test_npc_utils.py](test_npc_utils.py.md) (5 shared connections)

## Source Files

- `server/events/event_types.py`
- `server/npc/lifecycle_death.py`
- `server/npc/lifecycle_despawn.py`
- `server/npc/lifecycle_manager.py`
- `server/npc/lifecycle_types.py`
- `server/npc/movement_integration.py`
- `server/npc/spawning_service.py`
- `server/tests/unit/npc/test_lifecycle_death.py`
- `server/tests/unit/npc/test_lifecycle_despawn.py`
- `server/tests/unit/npc/test_lifecycle_manager.py`

## Audit Trail

- EXTRACTED: 439 (88%)
- INFERRED: 59 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*