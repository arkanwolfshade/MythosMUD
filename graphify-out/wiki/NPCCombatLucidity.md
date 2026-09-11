# NPCCombatLucidity

> 83 nodes

## Key Concepts

- **NPCCombatLucidity** (33 connections) — `server/services/npc_combat_lucidity.py`
- **_NPCCombatIntegrationValidationDeps** (18 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **TestNPCCombatLucidity** (17 connections) — `server/tests/unit/services/test_npc_combat_lucidity.py`
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
- **.get_combat_service()** (4 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **.get_lucidity_service()** (4 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **._end_combat_if_participant_in_combat()** (4 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **._archetype_from_definition()** (4 connections) — `server/services/npc_combat_lucidity.py`
- **._resolve_lucidity_category()** (4 connections) — `server/services/npc_combat_lucidity.py`
- **.test_apply_encounter_lucidity_effect_success()** (4 connections) — `server/tests/unit/services/test_npc_combat_lucidity.py`
- **.test_apply_encounter_lucidity_effect_with_npc_name()** (4 connections) — `server/tests/unit/services/test_npc_combat_lucidity.py`
- *... and 58 more nodes in this community*

## Relationships

- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (17 shared connections)
- [test_lucidity_recovery_commands.py](test_lucidity_recovery_commands.py.md) (6 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [NPCDefinition](NPCDefinition.md) (3 shared connections)
- [CombatService](CombatService.md) (2 shared connections)
- [NPCCombatDataProvider](NPCCombatDataProvider.md) (2 shared connections)
- [PlayerCombatService](PlayerCombatService.md) (1 shared connections)
- [RoomDataValidator](RoomDataValidator.md) (1 shared connections)
- [get_async_session](get_async_session.md) (1 shared connections)
- [websocket_handler.py](websocket_handler.py.md) (1 shared connections)

## Source Files

- `server/models/npc.py`
- `server/services/npc_combat_integration_validation_mixin.py`
- `server/services/npc_combat_lucidity.py`
- `server/tests/unit/services/test_npc_combat_lucidity.py`

## Audit Trail

- EXTRACTED: 152 (93%)
- INFERRED: 11 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*