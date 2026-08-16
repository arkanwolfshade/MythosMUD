# NPCDied

> 50 nodes

## Key Concepts

- **NPCDied** (29 connections) — `server/events/event_types.py`
- **test_lifecycle_manager.py** (27 connections) — `server/tests/unit/npc/test_lifecycle_manager.py`
- **lifecycle_death.py** (24 connections) — `server/npc/lifecycle_death.py`
- **_make_manager()** (18 connections) — `server/tests/unit/npc/test_lifecycle_manager.py`
- **NPCLifecycleRecord** (16 connections) — `server/npc/lifecycle_types.py`
- **lifecycle_types.py** (16 connections) — `server/npc/lifecycle_types.py`
- **test_lifecycle_death.py** (16 connections) — `server/tests/unit/npc/test_lifecycle_death.py`
- **_LifecycleManagerForDeath** (12 connections) — `server/npc/lifecycle_death.py`
- **handle_npc_died_impl()** (11 connections) — `server/npc/lifecycle_death.py`
- **_mark_despawned_and_queue_respawn()** (10 connections) — `server/npc/lifecycle_death.py`
- **_remove_active_npc_and_notify()** (8 connections) — `server/npc/lifecycle_death.py`
- **test_handle_npc_died_impl_full_path()** (6 connections) — `server/tests/unit/npc/test_lifecycle_death.py`
- **test_mark_despawned_logs_failure()** (6 connections) — `server/tests/unit/npc/test_lifecycle_death.py`
- **_manager_stub()** (5 connections) — `server/tests/unit/npc/test_lifecycle_death.py`
- **._handle_npc_died()** (4 connections) — `server/npc/lifecycle_manager.py`
- **_record()** (4 connections) — `server/tests/unit/npc/test_lifecycle_death.py`
- **test_handle_npc_died_impl_no_record()** (4 connections) — `server/tests/unit/npc/test_lifecycle_death.py`
- **test_remove_active_npc_skips_when_not_active()** (4 connections) — `server/tests/unit/npc/test_lifecycle_death.py`
- **test_handle_npc_entered_room_transitions_spawning()** (4 connections) — `server/tests/unit/npc/test_lifecycle_manager.py`
- **.get_npc_lifecycle_record()** (3 connections) — `server/npc/lifecycle_manager.py`
- **.__init__()** (3 connections) — `server/npc/lifecycle_types.py`
- **test_handle_npc_died_delegates()** (3 connections) — `server/tests/unit/npc/test_lifecycle_manager.py`
- **test_handle_npc_left_room_adds_event()** (3 connections) — `server/tests/unit/npc/test_lifecycle_manager.py`
- **test_apply_schedule_state()** (2 connections) — `server/tests/unit/npc/test_lifecycle_manager.py`
- **test_can_spawn_admin_bypass()** (2 connections) — `server/tests/unit/npc/test_lifecycle_manager.py`
- *... and 25 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (37 shared connections)
- [get_npc_instance_service](get_npc_instance_service.md) (10 shared connections)
- [test_lifecycle_periodic.py](test_lifecycle_periodic.py.md) (9 shared connections)
- [despawn_npc_impl](despawn_npc_impl.md) (5 shared connections)
- [NPCBase](NPCBase.md) (3 shared connections)
- [.__post_init__](__post_init__.md) (3 shared connections)
- [.add_event](add_event.md) (3 shared connections)
- [NATSRetryHandler](NATSRetryHandler.md) (2 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (2 shared connections)
- [NPCDefinition](NPCDefinition.md) (2 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (1 shared connections)

## Source Files

- `server/events/event_types.py`
- `server/npc/lifecycle_death.py`
- `server/npc/lifecycle_manager.py`
- `server/npc/lifecycle_types.py`
- `server/tests/unit/npc/test_lifecycle_death.py`
- `server/tests/unit/npc/test_lifecycle_manager.py`

## Audit Trail

- EXTRACTED: 145 (82%)
- INFERRED: 31 (18%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*