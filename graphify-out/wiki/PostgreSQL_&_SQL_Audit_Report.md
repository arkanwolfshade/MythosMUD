# PostgreSQL & SQL Audit Report

> 32 nodes · cohesion 0.09

## Key Concepts

- **_NPCCombatIntegrationValidationDeps** (19 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **.store_npc_xp_mapping_for_mixin()** (10 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **.get_uuid_mapping()** (7 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **.get_data_provider()** (6 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **._setup_combat_uuids_and_mappings()** (6 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **._validate_and_get_npc_instance()** (6 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **.get_combat_service()** (5 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **.get_engaged_foe_name()** (5 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **._setup_combat_uuids_npc_attacker()** (5 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **._validate_combat_location()** (5 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **UUID** (5 connections)
- **.get_lucidity_service()** (4 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **._end_combat_if_participant_in_combat()** (4 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **_coerce_xp_mapping_value()** (3 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **.store_npc_xp_mapping_for_mixin()** (3 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **_warn_attacked_dead_npc()** (3 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **Protocol** (1 connections)
- **Validate NPC instance (lookup when missing). Return instance or None.** (1 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **Validate that player and NPC are in the same room.** (1 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **End any active combat that includes this player when room validation fails.** (1 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **Name of the foe this player is already fighting when it is not ``npc_id``…** (1 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **Convert string IDs to UUIDs and set up XP mappings.** (1 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **Set up UUIDs for NPC-as-attacker combat (aggro). Returns (npc_uuid,…** (1 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **Parse xp_value from NPC base_stats JSON; bool maps to 0 (avoid True -> 1).** (1 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **Store NPC XP mapping and apply encounter lucidity effect if first engagement.** (1 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- *... and 7 more nodes in this community*

## Relationships

- [ValidationError](ValidationError.md) (14 shared connections)
- [NPCLifecycleManager](NPCLifecycleManager.md) (2 shared connections)
- [ground_channel.py](ground_channel.py.md) (2 shared connections)
- [log_and_raise_enhanced](log_and_raise_enhanced.md) (2 shared connections)
- [ErrorType](ErrorType.md) (1 shared connections)
- [WearableContainerService](WearableContainerService.md) (1 shared connections)

## Source Files

- `server/services/npc_combat_integration_validation_mixin.py`

## Audit Trail

- EXTRACTED: 61 (91%)
- INFERRED: 6 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*