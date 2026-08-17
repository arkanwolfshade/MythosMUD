# NPCDied

> 62 nodes

## Key Concepts

- **NPCDied** (29 connections) — `server/events/event_types.py`
- **NPCLifecycleState** (24 connections) — `server/npc/lifecycle_types.py`
- **lifecycle_death.py** (24 connections) — `server/npc/lifecycle_death.py`
- **despawn_npc_impl()** (20 connections) — `server/npc/lifecycle_despawn.py`
- **test_lifecycle_despawn.py** (19 connections) — `server/tests/unit/npc/test_lifecycle_despawn.py`
- **NPCLifecycleRecord** (16 connections) — `server/npc/lifecycle_types.py`
- **test_lifecycle_death.py** (16 connections) — `server/tests/unit/npc/test_lifecycle_death.py`
- **NPCLifecycleEvent** (13 connections) — `server/npc/lifecycle_types.py`
- **_LifecycleManagerForDeath** (12 connections) — `server/npc/lifecycle_death.py`
- **handle_npc_died_impl()** (11 connections) — `server/npc/lifecycle_death.py`
- **_mark_despawned_and_queue_respawn()** (10 connections) — `server/npc/lifecycle_death.py`
- **_make_manager()** (10 connections) — `server/tests/unit/npc/test_lifecycle_despawn.py`
- **_remove_active_npc_and_notify()** (8 connections) — `server/npc/lifecycle_death.py`
- **test_handle_npc_died_impl_full_path()** (6 connections) — `server/tests/unit/npc/test_lifecycle_death.py`
- **test_mark_despawned_logs_failure()** (6 connections) — `server/tests/unit/npc/test_lifecycle_death.py`
- **_remove_npc_from_room_on_despawn()** (5 connections) — `server/npc/lifecycle_despawn.py`
- **.add_event()** (5 connections) — `server/npc/lifecycle_types.py`
- **_manager_stub()** (5 connections) — `server/tests/unit/npc/test_lifecycle_death.py`
- **test_despawn_exception_sets_error_state()** (5 connections) — `server/tests/unit/npc/test_lifecycle_despawn.py`
- **test_despawn_success_with_persistence_and_room()** (5 connections) — `server/tests/unit/npc/test_lifecycle_despawn.py`
- **._handle_npc_died()** (4 connections) — `server/npc/lifecycle_manager.py`
- **.change_state()** (4 connections) — `server/npc/lifecycle_types.py`
- **_record()** (4 connections) — `server/tests/unit/npc/test_lifecycle_death.py`
- **test_handle_npc_died_impl_no_record()** (4 connections) — `server/tests/unit/npc/test_lifecycle_death.py`
- **test_remove_active_npc_skips_when_not_active()** (4 connections) — `server/tests/unit/npc/test_lifecycle_death.py`
- *... and 37 more nodes in this community*

## Relationships

- [ApplicationContainer](ApplicationContainer.md) (18 shared connections)
- [ConnectionManager](ConnectionManager.md) (12 shared connections)
- [NPCLifecycleManager](NPCLifecycleManager.md) (11 shared connections)
- [test_quest_events.py](test_quest_events.py.md) (6 shared connections)
- [test_lifecycle_periodic.py](test_lifecycle_periodic.py.md) (5 shared connections)
- [test_lifecycle_manager.py](test_lifecycle_manager.py.md) (4 shared connections)
- [NPCBase](NPCBase.md) (3 shared connections)
- [npc_base.py](npc_base.py.md) (3 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (3 shared connections)
- [EventBus](EventBus.md) (2 shared connections)
- [NPCDefinition](NPCDefinition.md) (2 shared connections)
- [build_event](build_event.md) (2 shared connections)

## Source Files

- `server/events/event_types.py`
- `server/npc/lifecycle_death.py`
- `server/npc/lifecycle_despawn.py`
- `server/npc/lifecycle_manager.py`
- `server/npc/lifecycle_types.py`
- `server/tests/unit/npc/test_lifecycle_death.py`
- `server/tests/unit/npc/test_lifecycle_despawn.py`

## Audit Trail

- EXTRACTED: 163 (80%)
- INFERRED: 42 (20%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*