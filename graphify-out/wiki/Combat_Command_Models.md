# Combat Command Models

> 63 nodes

## Key Concepts

- **NPCCombatUUIDMapping** (39 connections) — `server/services/npc_combat_uuid_mapping.py`
- **TestNPCCombatUUIDMapping** (22 connections) — `server/tests/unit/services/test_npc_combat_uuid_mapping.py`
- **UUID** (8 connections)
- **.is_valid_uuid()** (4 connections) — `server/services/npc_combat_uuid_mapping.py`
- **.convert_to_uuid()** (4 connections) — `server/services/npc_combat_uuid_mapping.py`
- **test_npc_combat_uuid_mapping.py** (4 connections) — `server/tests/unit/services/test_npc_combat_uuid_mapping.py`
- **.get_uuid_mapping()** (3 connections) — `server/services/npc_combat_integration_service.py`
- **.store_string_id_mapping()** (3 connections) — `server/services/npc_combat_uuid_mapping.py`
- **.store_xp_mapping()** (3 connections) — `server/services/npc_combat_uuid_mapping.py`
- **.get_uuid_for_string_id()** (3 connections) — `server/services/npc_combat_uuid_mapping.py`
- **.get_original_string_id()** (3 connections) — `server/services/npc_combat_uuid_mapping.py`
- **.get_xp_value()** (3 connections) — `server/services/npc_combat_uuid_mapping.py`
- **.test_init()** (3 connections) — `server/tests/unit/services/test_npc_combat_uuid_mapping.py`
- **.test_is_valid_uuid_valid()** (3 connections) — `server/tests/unit/services/test_npc_combat_uuid_mapping.py`
- **.test_is_valid_uuid_invalid()** (3 connections) — `server/tests/unit/services/test_npc_combat_uuid_mapping.py`
- **.test_convert_to_uuid_from_uuid_string()** (3 connections) — `server/tests/unit/services/test_npc_combat_uuid_mapping.py`
- **.test_convert_to_uuid_from_string_id()** (3 connections) — `server/tests/unit/services/test_npc_combat_uuid_mapping.py`
- **.test_store_string_id_mapping()** (3 connections) — `server/tests/unit/services/test_npc_combat_uuid_mapping.py`
- **.test_store_string_id_mapping_overwrites()** (3 connections) — `server/tests/unit/services/test_npc_combat_uuid_mapping.py`
- **.test_store_xp_mapping()** (3 connections) — `server/tests/unit/services/test_npc_combat_uuid_mapping.py`
- **.test_store_xp_mapping_overwrites()** (3 connections) — `server/tests/unit/services/test_npc_combat_uuid_mapping.py`
- **.test_get_original_string_id_found()** (3 connections) — `server/tests/unit/services/test_npc_combat_uuid_mapping.py`
- **.test_get_original_string_id_not_found()** (3 connections) — `server/tests/unit/services/test_npc_combat_uuid_mapping.py`
- **.test_get_uuid_for_string_id_found()** (3 connections) — `server/tests/unit/services/test_npc_combat_uuid_mapping.py`
- **.test_get_uuid_for_string_id_not_found()** (3 connections) — `server/tests/unit/services/test_npc_combat_uuid_mapping.py`
- *... and 38 more nodes in this community*

## Relationships

- [Argon2 Password Hashing](Argon2_Password_Hashing.md) (9 shared connections)
- [Command Testing Guide](Command_Testing_Guide.md) (2 shared connections)

## Source Files

- `server/services/npc_combat_integration_service.py`
- `server/services/npc_combat_uuid_mapping.py`
- `server/tests/unit/services/test_npc_combat_uuid_mapping.py`

## Audit Trail

- EXTRACTED: 184 (97%)
- INFERRED: 5 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*