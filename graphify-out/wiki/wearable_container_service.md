# wearable container service

> 56 nodes

## Key Concepts

- **test_lifecycle_manager.py** (27 connections) — `server/tests/unit/npc/test_lifecycle_manager.py`
- **test_lifecycle_despawn.py** (19 connections) — `server/tests/unit/npc/test_lifecycle_despawn.py`
- **despawn_npc_impl()** (18 connections) — `server/npc/lifecycle_despawn.py`
- **_make_manager()** (18 connections) — `server/tests/unit/npc/test_lifecycle_manager.py`
- **NPCLifecycleState** (17 connections) — `server/npc/lifecycle_types.py`
- **lifecycle_despawn.py** (16 connections) — `server/npc/lifecycle_despawn.py`
- **lifecycle_types.py** (16 connections) — `server/npc/lifecycle_types.py`
- **NPCLifecycleEvent** (12 connections) — `server/npc/lifecycle_types.py`
- **_make_manager()** (10 connections) — `server/tests/unit/npc/test_lifecycle_despawn.py`
- **_resolve_despawn_room_id()** (6 connections) — `server/npc/lifecycle_despawn.py`
- **_remove_npc_from_room_on_despawn()** (5 connections) — `server/npc/lifecycle_despawn.py`
- **.add_event()** (5 connections) — `server/npc/lifecycle_types.py`
- **.change_state()** (4 connections) — `server/npc/lifecycle_types.py`
- **test_despawn_publishes_event_when_room_missing()** (4 connections) — `server/tests/unit/npc/test_lifecycle_despawn.py`
- **Any** (3 connections)
- **.despawn_npc()** (3 connections) — `server/npc/lifecycle_manager.py`
- **.get_statistics()** (3 connections) — `server/npc/lifecycle_types.py`
- **test_despawn_success_with_persistence_and_room()** (3 connections) — `server/tests/unit/npc/test_lifecycle_despawn.py`
- **test_despawn_publishes_event_without_persistence()** (3 connections) — `server/tests/unit/npc/test_lifecycle_despawn.py`
- **test_despawn_record_only_when_not_active()** (3 connections) — `server/tests/unit/npc/test_lifecycle_despawn.py`
- **test_despawn_exception_sets_error_state()** (3 connections) — `server/tests/unit/npc/test_lifecycle_despawn.py`
- **test_despawn_without_population_controller()** (3 connections) — `server/tests/unit/npc/test_lifecycle_despawn.py`
- **test_despawn_skips_left_event_when_room_unknown()** (3 connections) — `server/tests/unit/npc/test_lifecycle_despawn.py`
- **test_despawn_prefers_current_room_over_room_id()** (3 connections) — `server/tests/unit/npc/test_lifecycle_despawn.py`
- **test_despawn_uses_lifecycle_spawn_room_when_attrs_missing()** (3 connections) — `server/tests/unit/npc/test_lifecycle_despawn.py`
- *... and 31 more nodes in this community*

## Relationships

- [inventory mutation guard](inventory_mutation_guard.md) (24 shared connections)
- [Error Conversion](Error_Conversion.md) (17 shared connections)
- [logging examples fastapi](logging_examples_fastapi.md) (6 shared connections)
- [combat services rationale](combat_services_rationale.md) (5 shared connections)
- [npc lifecycle config](npc_lifecycle_config.md) (4 shared connections)
- [room look commands](room_look_commands.md) (2 shared connections)

## Source Files

- `server/npc/lifecycle_despawn.py`
- `server/npc/lifecycle_manager.py`
- `server/npc/lifecycle_types.py`
- `server/tests/unit/npc/test_lifecycle_despawn.py`
- `server/tests/unit/npc/test_lifecycle_manager.py`

## Audit Trail

- EXTRACTED: 253 (97%)
- INFERRED: 9 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*