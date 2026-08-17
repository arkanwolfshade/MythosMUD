# NPCCombatUUIDMapping

> 48 nodes

## Key Concepts

- **NPCCombatUUIDMapping** (38 connections) — `server/services/npc_combat_uuid_mapping.py`
- **TestNPCCombatUUIDMapping** (22 connections) — `server/tests/unit/services/test_npc_combat_uuid_mapping.py`
- **test_npc_combat_uuid_mapping.py** (4 connections) — `server/tests/unit/services/test_npc_combat_uuid_mapping.py`
- **.get_uuid_mapping()** (3 connections) — `server/services/npc_combat_integration_service.py`
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
- **.test_negative_xp_value()** (3 connections) — `server/tests/unit/services/test_npc_combat_uuid_mapping.py`
- **.test_store_string_id_mapping()** (3 connections) — `server/tests/unit/services/test_npc_combat_uuid_mapping.py`
- **.test_store_string_id_mapping_overwrites()** (3 connections) — `server/tests/unit/services/test_npc_combat_uuid_mapping.py`
- **.test_store_xp_mapping()** (3 connections) — `server/tests/unit/services/test_npc_combat_uuid_mapping.py`
- **.test_store_xp_mapping_overwrites()** (3 connections) — `server/tests/unit/services/test_npc_combat_uuid_mapping.py`
- **.test_zero_xp_value()** (3 connections) — `server/tests/unit/services/test_npc_combat_uuid_mapping.py`
- **.__init__()** (2 connections) — `server/services/npc_combat_uuid_mapping.py`
- **Return UUID mapping dependency for integration collaborators.** (1 connections) — `server/services/npc_combat_integration_service.py`
- *... and 23 more nodes in this community*

## Relationships

- [UUID](UUID.md) (7 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (4 shared connections)
- [_NPCCombatIntegrationValidationDeps](_NPCCombatIntegrationValidationDeps.md) (2 shared connections)
- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (2 shared connections)
- [NPCCombatLifecycle](NPCCombatLifecycle.md) (1 shared connections)

## Source Files

- `server/services/npc_combat_integration_service.py`
- `server/services/npc_combat_uuid_mapping.py`
- `server/tests/unit/services/test_npc_combat_uuid_mapping.py`

## Audit Trail

- EXTRACTED: 80 (96%)
- INFERRED: 3 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*