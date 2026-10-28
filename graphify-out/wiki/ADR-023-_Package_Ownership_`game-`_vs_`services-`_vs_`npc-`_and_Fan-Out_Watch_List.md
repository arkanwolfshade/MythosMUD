# ADR-023: Package Ownership (`game/` vs `services/` vs `npc/`) and Fan-Out Watch List

> 63 nodes · cohesion 0.06

## Key Concepts

- **NPCLeftRoom** (46 connections) — `server/events/event_types.py`
- **test_lifecycle_manager.py** (29 connections) — `server/tests/unit/npc/test_lifecycle_manager.py`
- **despawn_npc_impl()** (22 connections) — `server/npc/lifecycle_despawn.py`
- **test_lifecycle_despawn.py** (21 connections) — `server/tests/unit/npc/test_lifecycle_despawn.py`
- **_make_manager()** (19 connections) — `server/tests/unit/npc/test_lifecycle_manager.py`
- **lifecycle_despawn.py** (16 connections) — `server/npc/lifecycle_despawn.py`
- **lifecycle_types.py** (16 connections) — `server/npc/lifecycle_types.py`
- **NPCLifecycleEvent** (13 connections) — `server/npc/lifecycle_types.py`
- **_make_manager()** (12 connections) — `server/tests/unit/npc/test_lifecycle_despawn.py`
- **_resolve_despawn_room_id()** (6 connections) — `server/npc/lifecycle_despawn.py`
- **_remove_npc_from_room_on_despawn()** (5 connections) — `server/npc/lifecycle_despawn.py`
- **test_despawn_exception_sets_error_state()** (5 connections) — `server/tests/unit/npc/test_lifecycle_despawn.py`
- **test_despawn_success_with_persistence_and_room()** (5 connections) — `server/tests/unit/npc/test_lifecycle_despawn.py`
- **._publish_movement_events()** (4 connections) — `server/npc/movement_integration.py`
- **test_despawn_publishes_event_when_room_missing()** (4 connections) — `server/tests/unit/npc/test_lifecycle_despawn.py`
- **test_despawn_stops_npc_thread_worker()** (4 connections) — `server/tests/unit/npc/test_lifecycle_despawn.py`
- **test_despawn_stops_npc_thread_worker_even_without_active_instance()** (4 connections) — `server/tests/unit/npc/test_lifecycle_despawn.py`
- **test_handle_npc_entered_room_transitions_spawning()** (4 connections) — `server/tests/unit/npc/test_lifecycle_manager.py`
- **test_queue_npc_thread_stop_schedules_stop_on_thread_manager()** (4 connections) — `server/tests/unit/npc/test_lifecycle_manager.py`
- **Any** (3 connections)
- **.despawn_npc()** (3 connections) — `server/npc/lifecycle_manager.py`
- **._handle_npc_left_room()** (3 connections) — `server/npc/lifecycle_manager.py`
- **._handle_npc_left_room()** (3 connections) — `server/npc/population_control.py`
- **._handle_npc_left_room()** (3 connections) — `server/npc/spawning_service.py`
- **test_despawn_prefers_current_room_over_room_id()** (3 connections) — `server/tests/unit/npc/test_lifecycle_despawn.py`
- *... and 38 more nodes in this community*

## Relationships

- [CombatInstance](CombatInstance.md) (19 shared connections)
- [SpellEffectType](SpellEffectType.md) (10 shared connections)
- [SpellLearningService](SpellLearningService.md) (8 shared connections)
- [BaseEvent](BaseEvent.md) (7 shared connections)
- [look_container.py](look_container.py.md) (7 shared connections)
- [Room](Room.md) (6 shared connections)
- [test_npc_combat_integration_service_player_attacks.py](test_npc_combat_integration_service_player_attacks.py.md) (6 shared connections)
- [RoomLoader](RoomLoader.md) (5 shared connections)
- [test_rescue_service.py](test_rescue_service.py.md) (5 shared connections)
- [get_username_from_user](get_username_from_user.md) (3 shared connections)
- [aggro_threat.py](aggro_threat.py.md) (2 shared connections)
- [._bind_event_type](_bind_event_type.md) (2 shared connections)

## Source Files

- `server/events/event_types.py`
- `server/npc/lifecycle_despawn.py`
- `server/npc/lifecycle_manager.py`
- `server/npc/lifecycle_types.py`
- `server/npc/movement_integration.py`
- `server/npc/population_control.py`
- `server/npc/spawning_service.py`
- `server/tests/unit/npc/test_lifecycle_despawn.py`
- `server/tests/unit/npc/test_lifecycle_manager.py`

## Audit Trail

- EXTRACTED: 184 (90%)
- INFERRED: 21 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*