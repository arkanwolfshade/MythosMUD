# NPCCombatDataProvider

> 79 nodes

## Key Concepts

- **NPCCombatDataProvider** (44 connections) — `server/services/npc_combat_data_provider.py`
- **test_npc_combat_data_provider.py** (21 connections) — `server/tests/unit/services/test_npc_combat_data_provider.py`
- **_NPCCombatIntegrationValidationDeps** (19 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **.store_npc_xp_mapping_for_mixin()** (10 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **.get_npc_combat_data()** (9 connections) — `server/services/npc_combat_data_provider.py`
- **asyncio** (8 connections)
- **.get_uuid_mapping()** (7 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **.get_player_combat_data()** (6 connections) — `server/services/npc_combat_data_provider.py`
- **.get_data_provider()** (6 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **._setup_combat_uuids_and_mappings()** (6 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **._validate_and_get_npc_instance()** (6 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **Any** (6 connections)
- **._resolve_npc_behavior_snapshot()** (5 connections) — `server/services/npc_combat_data_provider.py`
- **.get_combat_service()** (5 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **.get_engaged_foe_name()** (5 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **._setup_combat_uuids_npc_attacker()** (5 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **._validate_combat_location()** (5 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **UUID** (5 connections)
- **.get_npc_definition()** (4 connections) — `server/services/npc_combat_data_provider.py`
- **.get_npc_instance()** (4 connections) — `server/services/npc_combat_data_provider.py`
- **._resolve_npc_combat_stats()** (4 connections) — `server/services/npc_combat_data_provider.py`
- **.get_lucidity_service()** (4 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **._end_combat_if_participant_in_combat()** (4 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **test_get_npc_combat_data_reads_aggression_level_from_catalog_or_int()** (4 connections) — `server/tests/unit/services/test_npc_combat_data_provider.py`
- **.__init__()** (3 connections) — `server/services/npc_combat_data_provider.py`
- *... and 54 more nodes in this community*

## Relationships

- [CombatService](CombatService.md) (25 shared connections)
- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (9 shared connections)
- [NpcDisposition](NpcDisposition.md) (2 shared connections)
- [test_combat_service_modules.py](test_combat_service_modules.py.md) (2 shared connections)
- [NPCCombatLucidity](NPCCombatLucidity.md) (2 shared connections)
- [coerce_int](coerce_int.md) (2 shared connections)
- [AliasStorage](AliasStorage.md) (2 shared connections)
- [resolve_npc_attack_damage](resolve_npc_attack_damage.md) (1 shared connections)
- [ValueError](ValueError.md) (1 shared connections)
- [test_aggression.py](test_aggression.py.md) (1 shared connections)
- [NPCSpawnRule](NPCSpawnRule.md) (1 shared connections)
- [RoomDataValidator](RoomDataValidator.md) (1 shared connections)

## Source Files

- `server/services/npc_combat_data_provider.py`
- `server/services/npc_combat_integration_service.py`
- `server/services/npc_combat_integration_validation_mixin.py`
- `server/tests/unit/services/test_npc_combat_data_provider.py`

## Audit Trail

- EXTRACTED: 152 (88%)
- INFERRED: 20 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*