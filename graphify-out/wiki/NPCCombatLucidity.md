# NPCCombatLucidity

> 87 nodes

## Key Concepts

- **NPCCombatLucidity** (33 connections) — `server/services/npc_combat_lucidity.py`
- **_NPCCombatIntegrationValidationDeps** (18 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **TestNPCCombatLucidity** (17 connections) — `server/tests/unit/services/test_npc_combat_lucidity.py`
- **npc_combat_lucidity.py** (13 connections) — `server/services/npc_combat_lucidity.py`
- **.store_npc_xp_mapping_for_mixin()** (10 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **.apply_encounter_lucidity_effect()** (9 connections) — `server/services/npc_combat_lucidity.py`
- **._apply_loss_with_fallback()** (8 connections) — `server/services/npc_combat_lucidity.py`
- **_EncounterCtx** (7 connections) — `server/services/npc_combat_lucidity.py`
- **._apply_disturbing_fallback()** (7 connections) — `server/services/npc_combat_lucidity.py`
- **._commit_loss()** (7 connections) — `server/services/npc_combat_lucidity.py`
- **.get_base_stats()** (6 connections) — `server/models/npc.py`
- **.get_data_provider()** (6 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **.get_uuid_mapping()** (6 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **._setup_combat_uuids_and_mappings()** (6 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **Any** (6 connections)
- **._setup_combat_uuids_npc_attacker()** (5 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **._validate_and_get_npc_instance()** (5 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **._validate_combat_location()** (5 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **UUID** (5 connections)
- **test_npc_combat_lucidity.py** (5 connections) — `server/tests/unit/services/test_npc_combat_lucidity.py`
- **.get_combat_service()** (4 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **.get_lucidity_service()** (4 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **._end_combat_if_participant_in_combat()** (4 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **._archetype_from_definition()** (4 connections) — `server/services/npc_combat_lucidity.py`
- **._resolve_lucidity_category()** (4 connections) — `server/services/npc_combat_lucidity.py`
- *... and 62 more nodes in this community*

## Relationships

- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (11 shared connections)
- [test_lucidity_recovery_commands.py](test_lucidity_recovery_commands.py.md) (9 shared connections)
- [NPCCombatDataProvider](NPCCombatDataProvider.md) (8 shared connections)
- [ValidationError](ValidationError.md) (3 shared connections)
- [CombatService](CombatService.md) (2 shared connections)
- [NPCCombatUUIDMapping](NPCCombatUUIDMapping.md) (2 shared connections)
- [NPCSpawnRule](NPCSpawnRule.md) (2 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [NPCDefinition](NPCDefinition.md) (1 shared connections)
- [PlayerCombatService](PlayerCombatService.md) (1 shared connections)
- [RoomDataValidator](RoomDataValidator.md) (1 shared connections)
- [AttributeError](AttributeError.md) (1 shared connections)

## Source Files

- `server/models/npc.py`
- `server/services/npc_combat_integration_service.py`
- `server/services/npc_combat_integration_validation_mixin.py`
- `server/services/npc_combat_lucidity.py`
- `server/tests/unit/services/test_npc_combat_lucidity.py`

## Audit Trail

- EXTRACTED: 165 (94%)
- INFERRED: 11 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*