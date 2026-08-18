# test_npc_utils.py

> 101 nodes

## Key Concepts

- **test_npc_utils.py** (34 connections) — `server/tests/unit/npc/test_npc_utils.py`
- **despawn_npc_impl()** (20 connections) — `server/npc/lifecycle_despawn.py`
- **test_lifecycle_despawn.py** (19 connections) — `server/tests/unit/npc/test_lifecycle_despawn.py`
- **get_zone_key_from_room_id()** (17 connections) — `server/npc/npc_utils.py`
- **lifecycle_despawn.py** (16 connections) — `server/npc/lifecycle_despawn.py`
- **extract_room_id_from_npc()** (15 connections) — `server/npc/npc_utils.py`
- **NPCLifecycleEvent** (13 connections) — `server/npc/lifecycle_types.py`
- **extract_definition_id_from_npc()** (12 connections) — `server/npc/npc_utils.py`
- **extract_npc_metadata()** (12 connections) — `server/npc/npc_utils.py`
- **npc_utils.py** (11 connections) — `server/npc/npc_utils.py`
- **_make_manager()** (10 connections) — `server/tests/unit/npc/test_lifecycle_despawn.py`
- **extract_room_id_from_lifecycle_record()** (8 connections) — `server/npc/npc_utils.py`
- **_resolve_despawn_room_id()** (6 connections) — `server/npc/lifecycle_despawn.py`
- **_remove_npc_from_room_on_despawn()** (5 connections) — `server/npc/lifecycle_despawn.py`
- **._get_zone_key_from_room_id()** (5 connections) — `server/npc/population_control.py`
- **test_despawn_exception_sets_error_state()** (5 connections) — `server/tests/unit/npc/test_lifecycle_despawn.py`
- **test_despawn_success_with_persistence_and_room()** (5 connections) — `server/tests/unit/npc/test_lifecycle_despawn.py`
- **Any** (5 connections)
- **_room_id_from_lifecycle_event()** (4 connections) — `server/npc/npc_utils.py`
- **test_despawn_publishes_event_when_room_missing()** (4 connections) — `server/tests/unit/npc/test_lifecycle_despawn.py`
- **.despawn_npc()** (3 connections) — `server/npc/lifecycle_manager.py`
- **_stable_room_id_for_zone()** (3 connections) — `server/npc/npc_utils.py`
- **test_despawn_prefers_current_room_over_room_id()** (3 connections) — `server/tests/unit/npc/test_lifecycle_despawn.py`
- **test_despawn_publishes_event_without_persistence()** (3 connections) — `server/tests/unit/npc/test_lifecycle_despawn.py`
- **test_despawn_record_only_when_not_active()** (3 connections) — `server/tests/unit/npc/test_lifecycle_despawn.py`
- *... and 76 more nodes in this community*

## Relationships

- [NPCDefinition](NPCDefinition.md) (25 shared connections)
- [test_lifecycle_periodic.py](test_lifecycle_periodic.py.md) (12 shared connections)
- [get_logger](get_logger.md) (2 shared connections)

## Source Files

- `server/npc/lifecycle_despawn.py`
- `server/npc/lifecycle_manager.py`
- `server/npc/lifecycle_types.py`
- `server/npc/npc_utils.py`
- `server/npc/population_control.py`
- `server/tests/unit/npc/test_lifecycle_despawn.py`
- `server/tests/unit/npc/test_npc_utils.py`

## Audit Trail

- EXTRACTED: 199 (95%)
- INFERRED: 10 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*