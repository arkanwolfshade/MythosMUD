# Community 502

> 35 nodes

## Key Concepts

- **_NPCCombatIntegrationValidationDeps** (18 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **NPCCombatIntegrationValidationMixin** (11 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **.store_npc_xp_mapping_for_mixin()** (10 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **.get_uuid_mapping()** (7 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **.get_data_provider()** (6 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **._setup_combat_uuids_and_mappings()** (6 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **._validate_and_get_npc_instance()** (6 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **.get_combat_service()** (5 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **.get_engaged_foe_name()** (5 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **._setup_combat_uuids_npc_attacker()** (5 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **UUID** (5 connections)
- **.get_lucidity_service()** (4 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **._end_combat_if_participant_in_combat()** (4 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **._validate_combat_location()** (4 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **_coerce_xp_mapping_value()** (3 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **.store_npc_xp_mapping_for_mixin()** (3 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **_warn_attacked_dead_npc()** (3 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **NPCCombatUUIDMapping** (1 connections)
- **Protocol** (1 connections)
- **Validate NPC instance (lookup when missing). Return instance or None.** (1 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **Validate that player and NPC are in the same room.** (1 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **End any active combat that includes this player when room validation fails.** (1 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **Name of the foe this player is already fighting when it is not ``npc_id``…** (1 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **Convert string IDs to UUIDs and set up XP mappings.** (1 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **Set up UUIDs for NPC-as-attacker combat (aggro). Returns (npc_uuid,…** (1 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- *... and 10 more nodes in this community*

## Relationships

- [Combat Attack Execution](Combat_Attack_Execution.md) (6 shared connections)
- [Spell Effects & Combat Wiring](Spell_Effects_&_Combat_Wiring.md) (2 shared connections)
- [Community 369](Community_369.md) (2 shared connections)
- [Community 222](Community_222.md) (2 shared connections)
- [NPC Combat Integration](NPC_Combat_Integration.md) (2 shared connections)
- [NPC Definition JSON](NPC_Definition_JSON.md) (1 shared connections)

## Source Files

- `server/services/npc_combat_integration_validation_mixin.py`

## Audit Trail

- EXTRACTED: 64 (93%)
- INFERRED: 5 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*