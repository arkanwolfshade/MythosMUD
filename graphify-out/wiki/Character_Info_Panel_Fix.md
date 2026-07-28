# Character Info Panel Fix

> 18 nodes · cohesion 0.11

## Key Concepts

- **test_npc_utils.py** (30 connections) — `server/tests/unit/npc/test_npc_utils.py`
- **test_get_zone_key_from_room_id_exactly_four_parts()** (3 connections) — `server/tests/unit/npc/test_npc_utils.py`
- **test_get_zone_key_from_room_id_innsmouth()** (3 connections) — `server/tests/unit/npc/test_npc_utils.py`
- **test_get_zone_key_from_room_id_instanced()** (3 connections) — `server/tests/unit/npc/test_npc_utils.py`
- **test_get_zone_key_from_room_id_many_parts()** (3 connections) — `server/tests/unit/npc/test_npc_utils.py`
- **test_get_zone_key_from_room_id_short()** (3 connections) — `server/tests/unit/npc/test_npc_utils.py`
- **test_get_zone_key_from_room_id_too_short()** (3 connections) — `server/tests/unit/npc/test_npc_utils.py`
- **test_get_zone_key_from_room_id_valid()** (3 connections) — `server/tests/unit/npc/test_npc_utils.py`
- **test_get_zone_key_from_room_id_with_description()** (3 connections) — `server/tests/unit/npc/test_npc_utils.py`
- **Unit tests for NPC utility functions.  Tests the utility functions in npc_utils.** (1 connections) — `server/tests/unit/npc/test_npc_utils.py`
- **Test get_zone_key_from_room_id() extracts zone key from valid room ID.** (1 connections) — `server/tests/unit/npc/test_npc_utils.py`
- **Test get_zone_key_from_room_id() handles room ID with description.** (1 connections) — `server/tests/unit/npc/test_npc_utils.py`
- **Test get_zone_key_from_room_id() handles Innsmouth room ID.** (1 connections) — `server/tests/unit/npc/test_npc_utils.py`
- **Test get_zone_key_from_room_id() returns 'unknown/unknown' for short room ID.** (1 connections) — `server/tests/unit/npc/test_npc_utils.py`
- **Test get_zone_key_from_room_id() returns 'unknown/unknown' for too short room ID** (1 connections) — `server/tests/unit/npc/test_npc_utils.py`
- **Test get_zone_key_from_room_id() handles room ID with exactly 4 parts.** (1 connections) — `server/tests/unit/npc/test_npc_utils.py`
- **Test get_zone_key_from_room_id() handles room ID with many parts.** (1 connections) — `server/tests/unit/npc/test_npc_utils.py`
- **Instanced room IDs (instance_<uuid>_<stable_id>) use stable id for zone key.** (1 connections) — `server/tests/unit/npc/test_npc_utils.py`

## Relationships

- [Distributed Event Bus](Distributed_Event_Bus.md) (9 shared connections)
- [Security Issues And Fixes](Security_Issues_And_Fixes.md) (7 shared connections)
- [NPC Utility Functions](NPC_Utility_Functions.md) (6 shared connections)
- [E 2 E Scenario Whisper](E_2_E_Scenario_Whisper.md) (6 shared connections)
- [E 2 E Scenarios Scenario](E_2_E_Scenarios_Scenario.md) (1 shared connections)

## Source Files

- `server/tests/unit/npc/test_npc_utils.py`

## Audit Trail

- EXTRACTED: 63 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*