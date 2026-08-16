# get_zone_key_from_room_id

> 22 nodes

## Key Concepts

- **get_zone_key_from_room_id()** (17 connections) — `server/npc/npc_utils.py`
- **._update_population_stats_for_despawn()** (4 connections) — `server/npc/population_control.py`
- **_stable_room_id_for_zone()** (3 connections) — `server/npc/npc_utils.py`
- **test_get_zone_key_from_room_id_exactly_four_parts()** (3 connections) — `server/tests/unit/npc/test_npc_utils.py`
- **test_get_zone_key_from_room_id_innsmouth()** (3 connections) — `server/tests/unit/npc/test_npc_utils.py`
- **test_get_zone_key_from_room_id_instanced()** (3 connections) — `server/tests/unit/npc/test_npc_utils.py`
- **test_get_zone_key_from_room_id_many_parts()** (3 connections) — `server/tests/unit/npc/test_npc_utils.py`
- **test_get_zone_key_from_room_id_short()** (3 connections) — `server/tests/unit/npc/test_npc_utils.py`
- **test_get_zone_key_from_room_id_too_short()** (3 connections) — `server/tests/unit/npc/test_npc_utils.py`
- **test_get_zone_key_from_room_id_valid()** (3 connections) — `server/tests/unit/npc/test_npc_utils.py`
- **test_get_zone_key_from_room_id_with_description()** (3 connections) — `server/tests/unit/npc/test_npc_utils.py`
- **Return stable room id for zone parsing; strip instance_<uuid>_ prefix if…** (1 connections) — `server/npc/npc_utils.py`
- **Extract zone key from room ID. Args: room_id: The room identifier (stable id or…** (1 connections) — `server/npc/npc_utils.py`
- **Update population statistics when an NPC is despawned. Args: room_id: Room ID…** (1 connections) — `server/npc/population_control.py`
- **Test get_zone_key_from_room_id() extracts zone key from valid room ID.** (1 connections) — `server/tests/unit/npc/test_npc_utils.py`
- **Test get_zone_key_from_room_id() handles room ID with description.** (1 connections) — `server/tests/unit/npc/test_npc_utils.py`
- **Test get_zone_key_from_room_id() handles Innsmouth room ID.** (1 connections) — `server/tests/unit/npc/test_npc_utils.py`
- **Test get_zone_key_from_room_id() returns 'unknown/unknown' for short room ID.** (1 connections) — `server/tests/unit/npc/test_npc_utils.py`
- **Test get_zone_key_from_room_id() returns 'unknown/unknown' for too short room…** (1 connections) — `server/tests/unit/npc/test_npc_utils.py`
- **Test get_zone_key_from_room_id() handles room ID with exactly 4 parts.** (1 connections) — `server/tests/unit/npc/test_npc_utils.py`
- **Test get_zone_key_from_room_id() handles room ID with many parts.** (1 connections) — `server/tests/unit/npc/test_npc_utils.py`
- **Instanced room IDs (instance_<uuid>_<stable_id>) use stable id for zone key.** (1 connections) — `server/tests/unit/npc/test_npc_utils.py`

## Relationships

- [test_npc_utils.py](test_npc_utils.py.md) (12 shared connections)
- [get_npc_instance_service](get_npc_instance_service.md) (3 shared connections)
- [NPCDefinition](NPCDefinition.md) (1 shared connections)
- [get_logger](get_logger.md) (1 shared connections)

## Source Files

- `server/npc/npc_utils.py`
- `server/npc/population_control.py`
- `server/tests/unit/npc/test_npc_utils.py`

## Audit Trail

- EXTRACTED: 38 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*