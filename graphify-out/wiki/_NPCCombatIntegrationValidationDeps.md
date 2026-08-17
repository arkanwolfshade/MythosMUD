# _NPCCombatIntegrationValidationDeps

> 32 nodes

## Key Concepts

- **_NPCCombatIntegrationValidationDeps** (18 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **NPCCombatIntegrationValidationMixin** (11 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **.store_npc_xp_mapping_for_mixin()** (10 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **.get_data_provider()** (6 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **.get_uuid_mapping()** (6 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **._setup_combat_uuids_and_mappings()** (6 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **._setup_combat_uuids_npc_attacker()** (5 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **._validate_and_get_npc_instance()** (5 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **._validate_combat_location()** (5 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **UUID** (5 connections)
- **.get_combat_service()** (4 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **.get_lucidity_service()** (4 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **._end_combat_if_participant_in_combat()** (4 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **_coerce_xp_mapping_value()** (3 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **.store_npc_xp_mapping_for_mixin()** (3 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **_warn_attacked_dead_npc()** (3 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **Protocol** (1 connections)
- **Validate that player and NPC are in the same room.** (1 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **End any active combat that includes this player when room validation fails.** (1 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **Convert string IDs to UUIDs and set up XP mappings.** (1 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **Set up UUIDs for NPC-as-attacker combat (aggro). Returns (npc_uuid,…** (1 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **Parse xp_value from NPC base_stats JSON; bool maps to 0 (avoid True -> 1).** (1 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **Store NPC XP mapping and apply encounter lucidity effect if first engagement.** (1 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **Log when a player targets an NPC that exists but is not alive.** (1 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **Attributes supplied by NPCCombatIntegrationService (mixin cannot initialize…** (1 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- *... and 7 more nodes in this community*

## Relationships

- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (8 shared connections)
- [NPCCombatDataProvider](NPCCombatDataProvider.md) (2 shared connections)
- [NPCCombatUUIDMapping](NPCCombatUUIDMapping.md) (2 shared connections)
- [NPCCombatLucidity](NPCCombatLucidity.md) (2 shared connections)
- [RoomDataValidator](RoomDataValidator.md) (2 shared connections)
- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (1 shared connections)
- [_JSONDict](_JSONDict.md) (1 shared connections)

## Source Files

- `server/services/npc_combat_integration_validation_mixin.py`

## Audit Trail

- EXTRACTED: 59 (89%)
- INFERRED: 7 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*