# Lucidity Recovery Commands

> 78 nodes

## Key Concepts

- **test_npc_utils.py** (30 connections) — `server/tests/unit/npc/test_npc_utils.py`
- **get_zone_key_from_room_id()** (17 connections) — `server/npc/npc_utils.py`
- **extract_npc_metadata()** (12 connections) — `server/npc/npc_utils.py`
- **extract_definition_id_from_npc()** (12 connections) — `server/npc/npc_utils.py`
- **extract_room_id_from_npc()** (11 connections) — `server/npc/npc_utils.py`
- **npc_utils.py** (8 connections) — `server/npc/npc_utils.py`
- **.despawn_npc()** (8 connections) — `server/npc/population_control.py`
- **._get_active_npcs_from_lifecycle_manager()** (6 connections) — `server/npc/population_control.py`
- **._get_zone_key_from_room_id()** (5 connections) — `server/npc/population_control.py`
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
- *... and 53 more nodes in this community*

## Relationships

- [Level and XP Curve](Level_and_XP_Curve.md) (8 shared connections)
- [LRU Cache Manager](LRU_Cache_Manager.md) (7 shared connections)
- [Command Parser Tests](Command_Parser_Tests.md) (3 shared connections)

## Source Files

- `server/models/npc.py`
- `server/npc/npc_utils.py`
- `server/npc/population_control.py`
- `server/tests/unit/npc/test_npc_utils.py`

## Audit Trail

- EXTRACTED: 239 (99%)
- INFERRED: 3 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*