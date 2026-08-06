# combat services rationale

> 111 nodes

## Key Concepts

- **test_npc_utils.py** (34 connections) — `server/tests/unit/npc/test_npc_utils.py`
- **test_lifecycle_despawn.py** (19 connections) — `server/tests/unit/npc/test_lifecycle_despawn.py`
- **despawn_npc_impl()** (18 connections) — `server/npc/lifecycle_despawn.py`
- **get_zone_key_from_room_id()** (17 connections) — `server/npc/npc_utils.py`
- **extract_room_id_from_npc()** (15 connections) — `server/npc/npc_utils.py`
- **extract_npc_metadata()** (12 connections) — `server/npc/npc_utils.py`
- **extract_definition_id_from_npc()** (12 connections) — `server/npc/npc_utils.py`
- **npc_utils.py** (11 connections) — `server/npc/npc_utils.py`
- **_make_manager()** (10 connections) — `server/tests/unit/npc/test_lifecycle_despawn.py`
- **extract_room_id_from_lifecycle_record()** (8 connections) — `server/npc/npc_utils.py`
- **.despawn_npc()** (8 connections) — `server/npc/population_control.py`
- **_resolve_despawn_room_id()** (6 connections) — `server/npc/lifecycle_despawn.py`
- **._get_active_npcs_from_lifecycle_manager()** (6 connections) — `server/npc/population_control.py`
- **_remove_npc_from_room_on_despawn()** (5 connections) — `server/npc/lifecycle_despawn.py`
- **Any** (5 connections)
- **._get_zone_key_from_room_id()** (5 connections) — `server/npc/population_control.py`
- **._should_remove_inactive_npc()** (5 connections) — `server/npc/population_control.py`
- **.cleanup_inactive_npcs()** (5 connections) — `server/npc/population_control.py`
- **.is_required()** (4 connections) — `server/models/npc.py`
- **_room_id_from_lifecycle_event()** (4 connections) — `server/npc/npc_utils.py`
- **._update_population_stats_for_despawn()** (4 connections) — `server/npc/population_control.py`
- **test_despawn_publishes_event_when_room_missing()** (4 connections) — `server/tests/unit/npc/test_lifecycle_despawn.py`
- **Any** (3 connections)
- **.despawn_npc()** (3 connections) — `server/npc/lifecycle_manager.py`
- **_stable_room_id_for_zone()** (3 connections) — `server/npc/npc_utils.py`
- *... and 86 more nodes in this community*

## Relationships

- [Error Conversion](Error_Conversion.md) (28 shared connections)
- [room look commands](room_look_commands.md) (2 shared connections)
- [container events rationale](container_events_rationale.md) (2 shared connections)
- [lucidity event services](lucidity_event_services.md) (2 shared connections)

## Source Files

- `server/models/npc.py`
- `server/npc/lifecycle_despawn.py`
- `server/npc/lifecycle_manager.py`
- `server/npc/npc_utils.py`
- `server/npc/population_control.py`
- `server/tests/unit/npc/test_lifecycle_despawn.py`
- `server/tests/unit/npc/test_npc_utils.py`

## Audit Trail

- EXTRACTED: 379 (99%)
- INFERRED: 5 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*