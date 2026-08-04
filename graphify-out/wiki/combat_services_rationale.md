# combat services rationale

> 89 nodes

## Key Concepts

- **test_npc_utils.py** (34 connections) — `server/tests/unit/npc/test_npc_utils.py`
- **get_zone_key_from_room_id()** (17 connections) — `server/npc/npc_utils.py`
- **extract_room_id_from_npc()** (15 connections) — `server/npc/npc_utils.py`
- **extract_npc_metadata()** (12 connections) — `server/npc/npc_utils.py`
- **extract_definition_id_from_npc()** (12 connections) — `server/npc/npc_utils.py`
- **npc_utils.py** (10 connections) — `server/npc/npc_utils.py`
- **.despawn_npc()** (8 connections) — `server/npc/population_control.py`
- **extract_room_id_from_lifecycle_record()** (7 connections) — `server/npc/npc_utils.py`
- **_resolve_despawn_room_id()** (6 connections) — `server/npc/lifecycle_despawn.py`
- **._get_active_npcs_from_lifecycle_manager()** (6 connections) — `server/npc/population_control.py`
- **._get_zone_key_from_room_id()** (5 connections) — `server/npc/population_control.py`
- **._should_remove_inactive_npc()** (5 connections) — `server/npc/population_control.py`
- **.cleanup_inactive_npcs()** (5 connections) — `server/npc/population_control.py`
- **.is_required()** (4 connections) — `server/models/npc.py`
- **Any** (4 connections)
- **._update_population_stats_for_despawn()** (4 connections) — `server/npc/population_control.py`
- **_stable_room_id_for_zone()** (3 connections) — `server/npc/npc_utils.py`
- **.get_zone_population_summary()** (3 connections) — `server/npc/population_control.py`
- **test_extract_room_id_from_npc_current_room()** (3 connections) — `server/tests/unit/npc/test_npc_utils.py`
- **test_extract_room_id_from_npc_current_room_id()** (3 connections) — `server/tests/unit/npc/test_npc_utils.py`
- **test_extract_room_id_from_npc_room_id()** (3 connections) — `server/tests/unit/npc/test_npc_utils.py`
- **test_extract_room_id_from_npc_spawn_room_id()** (3 connections) — `server/tests/unit/npc/test_npc_utils.py`
- **test_extract_room_id_from_npc_skips_unknown_sentinel()** (3 connections) — `server/tests/unit/npc/test_npc_utils.py`
- **test_extract_room_id_from_npc_not_found()** (3 connections) — `server/tests/unit/npc/test_npc_utils.py`
- **test_extract_room_id_from_npc_non_string()** (3 connections) — `server/tests/unit/npc/test_npc_utils.py`
- *... and 64 more nodes in this community*

## Relationships

- [models npc rationale](models_npc_rationale.md) (11 shared connections)
- [Realtime Subscribers](Realtime_Subscribers.md) (7 shared connections)
- [command parser rationale](command_parser_rationale.md) (6 shared connections)

## Source Files

- `server/models/npc.py`
- `server/npc/lifecycle_despawn.py`
- `server/npc/npc_utils.py`
- `server/npc/population_control.py`
- `server/tests/unit/npc/test_npc_utils.py`

## Audit Trail

- EXTRACTED: 280 (99%)
- INFERRED: 4 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*