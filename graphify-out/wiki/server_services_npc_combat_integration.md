# server services npc combat integration

> 63 nodes

## Key Concepts

- **NPCCombatUUIDMapping** (35 connections) — `server/services/npc_combat_uuid_mapping.py`
- **TestNPCCombatUUIDMapping** (22 connections) — `server/tests/unit/services/test_npc_combat_uuid_mapping.py`
- **UUID** (7 connections)
- **.convert_to_uuid()** (4 connections) — `server/services/npc_combat_uuid_mapping.py`
- **test_npc_combat_uuid_mapping.py** (4 connections) — `server/tests/unit/services/test_npc_combat_uuid_mapping.py`
- **.get_uuid_mapping()** (3 connections) — `server/services/npc_combat_integration_service.py`
- **.get_original_string_id()** (3 connections) — `server/services/npc_combat_uuid_mapping.py`
- **.get_uuid_for_string_id()** (3 connections) — `server/services/npc_combat_uuid_mapping.py`
- **.get_xp_value()** (3 connections) — `server/services/npc_combat_uuid_mapping.py`
- **.is_valid_uuid()** (3 connections) — `server/services/npc_combat_uuid_mapping.py`
- **.store_string_id_mapping()** (3 connections) — `server/services/npc_combat_uuid_mapping.py`
- **.store_xp_mapping()** (3 connections) — `server/services/npc_combat_uuid_mapping.py`
- **.test_convert_to_uuid_from_string_id()** (3 connections) — `server/tests/unit/services/test_npc_combat_uuid_mapping.py`
- **.test_convert_to_uuid_from_uuid_string()** (3 connections) — `server/tests/unit/services/test_npc_combat_uuid_mapping.py`
- **.test_get_original_string_id_found()** (3 connections) — `server/tests/unit/services/test_npc_combat_uuid_mapping.py`
- **.test_get_original_string_id_not_found()** (3 connections) — `server/tests/unit/services/test_npc_combat_uuid_mapping.py`
- **.test_get_uuid_for_string_id_found()** (3 connections) — `server/tests/unit/services/test_npc_combat_uuid_mapping.py`
- **.test_get_uuid_for_string_id_not_found()** (3 connections) — `server/tests/unit/services/test_npc_combat_uuid_mapping.py`
- **.test_get_xp_value_found()** (3 connections) — `server/tests/unit/services/test_npc_combat_uuid_mapping.py`
- **.test_get_xp_value_not_found()** (3 connections) — `server/tests/unit/services/test_npc_combat_uuid_mapping.py`
- **.test_init()** (3 connections) — `server/tests/unit/services/test_npc_combat_uuid_mapping.py`
- **.test_is_valid_uuid_invalid()** (3 connections) — `server/tests/unit/services/test_npc_combat_uuid_mapping.py`
- **.test_is_valid_uuid_valid()** (3 connections) — `server/tests/unit/services/test_npc_combat_uuid_mapping.py`
- **.test_large_xp_value()** (3 connections) — `server/tests/unit/services/test_npc_combat_uuid_mapping.py`
- **.test_multiple_mappings()** (3 connections) — `server/tests/unit/services/test_npc_combat_uuid_mapping.py`
- *... and 38 more nodes in this community*

## Relationships

- [server commands combat handler combatcommandhandler](server_commands_combat_handler_combatcommandhandler.md) (4 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (3 shared connections)

## Source Files

- `server/services/npc_combat_integration_service.py`
- `server/services/npc_combat_uuid_mapping.py`
- `server/tests/unit/services/test_npc_combat_uuid_mapping.py`

## Audit Trail

- EXTRACTED: 93 (98%)
- INFERRED: 2 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*