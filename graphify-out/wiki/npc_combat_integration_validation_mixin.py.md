# npc_combat_integration_validation_mixin.py

> 32 nodes

## Key Concepts

- **npc_combat_integration_validation_mixin.py** (20 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **_NPCCombatIntegrationValidationDeps** (18 connections) — `server/services/npc_combat_integration_validation_mixin.py`
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
- **Validation and UUID-mapping helpers for NPC combat integration (mixin).** (1 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **Validate that player and NPC are in the same room.** (1 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **End any active combat that includes this player when room validation fails.** (1 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **Convert string IDs to UUIDs and set up XP mappings.** (1 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **Set up UUIDs for NPC-as-attacker combat (aggro). Returns (npc_uuid,…** (1 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **Parse xp_value from NPC base_stats JSON; bool maps to 0 (avoid True -> 1).** (1 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **Store NPC XP mapping and apply encounter lucidity effect if first engagement.** (1 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **Log when a player targets an NPC that exists but is not alive.** (1 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- *... and 7 more nodes in this community*

## Relationships

- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (8 shared connections)
- [CombatService](CombatService.md) (4 shared connections)
- [NPCCombatUUIDMapping](NPCCombatUUIDMapping.md) (4 shared connections)
- [get_logger](get_logger.md) (4 shared connections)
- [NPCCombatDataProvider](NPCCombatDataProvider.md) (3 shared connections)
- [NPCCombatLucidity](NPCCombatLucidity.md) (3 shared connections)
- [RoomDataValidator](RoomDataValidator.md) (2 shared connections)
- [_JSONDict](_JSONDict.md) (1 shared connections)
- [seed_e2e_users.py](seed_e2e_users.py.md) (1 shared connections)
- [CombatParticipantType](CombatParticipantType.md) (1 shared connections)

## Source Files

- `server/services/npc_combat_integration_validation_mixin.py`

## Audit Trail

- EXTRACTED: 72 (94%)
- INFERRED: 5 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*