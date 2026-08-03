# combat services rationale

> 77 nodes

## Key Concepts

- **test_npc_utils.py** (30 connections) — `server/tests/unit/npc/test_npc_utils.py`
- **get_zone_key_from_room_id()** (17 connections) — `server/npc/npc_utils.py`
- **extract_npc_metadata()** (12 connections) — `server/npc/npc_utils.py`
- **extract_definition_id_from_npc()** (12 connections) — `server/npc/npc_utils.py`
- **extract_room_id_from_npc()** (11 connections) — `server/npc/npc_utils.py`
- **npc_utils.py** (8 connections) — `server/npc/npc_utils.py`
- **.despawn_npc()** (8 connections) — `server/npc/population_control.py`
- **._get_active_npcs_from_lifecycle_manager()** (6 connections) — `server/npc/population_control.py`
- **._should_remove_inactive_npc()** (5 connections) — `server/npc/population_control.py`
- **.cleanup_inactive_npcs()** (5 connections) — `server/npc/population_control.py`
- **.is_required()** (4 connections) — `server/models/npc.py`
- **._update_population_stats_for_despawn()** (4 connections) — `server/npc/population_control.py`
- **Any** (3 connections)
- **_stable_room_id_for_zone()** (3 connections) — `server/npc/npc_utils.py`
- **.get_zone_population_summary()** (3 connections) — `server/npc/population_control.py`
- **test_extract_room_id_from_npc_current_room()** (3 connections) — `server/tests/unit/npc/test_npc_utils.py`
- **test_extract_room_id_from_npc_current_room_id()** (3 connections) — `server/tests/unit/npc/test_npc_utils.py`
- **test_extract_room_id_from_npc_room_id()** (3 connections) — `server/tests/unit/npc/test_npc_utils.py`
- **test_extract_room_id_from_npc_not_found()** (3 connections) — `server/tests/unit/npc/test_npc_utils.py`
- **test_extract_room_id_from_npc_non_string()** (3 connections) — `server/tests/unit/npc/test_npc_utils.py`
- **test_extract_npc_metadata_valid()** (3 connections) — `server/tests/unit/npc/test_npc_utils.py`
- **test_extract_npc_metadata_defaults()** (3 connections) — `server/tests/unit/npc/test_npc_utils.py`
- **test_extract_npc_metadata_non_string_type()** (3 connections) — `server/tests/unit/npc/test_npc_utils.py`
- **test_extract_npc_metadata_truthy_required()** (3 connections) — `server/tests/unit/npc/test_npc_utils.py`
- **test_extract_npc_metadata_none_required()** (3 connections) — `server/tests/unit/npc/test_npc_utils.py`
- *... and 52 more nodes in this community*

## Relationships

- [Realtime Subscribers](Realtime_Subscribers.md) (12 shared connections)
- [npc spawn validator](npc_spawn_validator.md) (3 shared connections)
- [rate limiter realtime](rate_limiter_realtime.md) (2 shared connections)

## Source Files

- `server/models/npc.py`
- `server/npc/npc_utils.py`
- `server/npc/population_control.py`
- `server/tests/unit/npc/test_npc_utils.py`

## Audit Trail

- EXTRACTED: 237 (98%)
- INFERRED: 4 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*