# test_npc_utils.py

> 56 nodes

## Key Concepts

- **test_npc_utils.py** (37 connections) — `server/tests/unit/npc/test_npc_utils.py`
- **extract_room_id_from_npc()** (15 connections) — `server/npc/npc_utils.py`
- **npc_utils.py** (14 connections) — `server/npc/npc_utils.py`
- **extract_definition_id_from_npc()** (12 connections) — `server/npc/npc_utils.py`
- **extract_npc_metadata()** (12 connections) — `server/npc/npc_utils.py`
- **extract_room_id_from_lifecycle_record()** (8 connections) — `server/npc/npc_utils.py`
- **.despawn_npc()** (8 connections) — `server/npc/population_control.py`
- **_resolve_despawn_room_id()** (6 connections) — `server/npc/lifecycle_despawn.py`
- **Any** (6 connections)
- **_room_id_from_lifecycle_event()** (4 connections) — `server/npc/npc_utils.py`
- **test_extract_definition_id_from_npc_from_lifecycle_manager()** (3 connections) — `server/tests/unit/npc/test_npc_utils.py`
- **test_extract_definition_id_from_npc_has_definition_id()** (3 connections) — `server/tests/unit/npc/test_npc_utils.py`
- **test_extract_definition_id_from_npc_lifecycle_manager_no_definition()** (3 connections) — `server/tests/unit/npc/test_npc_utils.py`
- **test_extract_definition_id_from_npc_lifecycle_manager_no_record()** (3 connections) — `server/tests/unit/npc/test_npc_utils.py`
- **test_extract_definition_id_from_npc_no_manager()** (3 connections) — `server/tests/unit/npc/test_npc_utils.py`
- **test_extract_definition_id_from_npc_non_int()** (3 connections) — `server/tests/unit/npc/test_npc_utils.py`
- **test_extract_npc_metadata_defaults()** (3 connections) — `server/tests/unit/npc/test_npc_utils.py`
- **test_extract_npc_metadata_non_string_type()** (3 connections) — `server/tests/unit/npc/test_npc_utils.py`
- **test_extract_npc_metadata_none_required()** (3 connections) — `server/tests/unit/npc/test_npc_utils.py`
- **test_extract_npc_metadata_truthy_required()** (3 connections) — `server/tests/unit/npc/test_npc_utils.py`
- **test_extract_npc_metadata_valid()** (3 connections) — `server/tests/unit/npc/test_npc_utils.py`
- **test_extract_room_id_from_npc_current_room()** (3 connections) — `server/tests/unit/npc/test_npc_utils.py`
- **test_extract_room_id_from_npc_current_room_id()** (3 connections) — `server/tests/unit/npc/test_npc_utils.py`
- **test_extract_room_id_from_npc_non_string()** (3 connections) — `server/tests/unit/npc/test_npc_utils.py`
- **test_extract_room_id_from_npc_not_found()** (3 connections) — `server/tests/unit/npc/test_npc_utils.py`
- *... and 31 more nodes in this community*

## Relationships

- [get_zone_key_from_room_id](get_zone_key_from_room_id.md) (12 shared connections)
- [NPCDefinition](NPCDefinition.md) (8 shared connections)
- [event_types.py](event_types.py.md) (7 shared connections)
- [spawn_npc_via_population_controller](spawn_npc_via_population_controller.md) (5 shared connections)
- [test_lifecycle_respawn.py](test_lifecycle_respawn.py.md) (1 shared connections)

## Source Files

- `server/npc/lifecycle_despawn.py`
- `server/npc/npc_utils.py`
- `server/npc/population_control.py`
- `server/tests/unit/npc/test_npc_utils.py`

## Audit Trail

- EXTRACTED: 118 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*