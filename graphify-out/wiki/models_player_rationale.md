# models player rationale

> 32 nodes

## Key Concepts

- **_NPCCombatIntegrationValidationDeps** (19 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **NPCCombatIntegrationValidationMixin** (15 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **.store_npc_xp_mapping_for_mixin()** (10 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **.get_data_provider()** (6 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **.get_uuid_mapping()** (6 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **UUID** (6 connections)
- **._setup_combat_uuids_and_mappings()** (6 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **._validate_and_get_npc_instance()** (5 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **._validate_combat_location()** (5 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **._end_combat_if_participant_in_combat()** (5 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **._setup_combat_uuids_npc_attacker()** (5 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **.get_combat_service()** (4 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **.get_lucidity_service()** (4 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **_coerce_xp_mapping_value()** (3 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **_warn_attacked_dead_npc()** (3 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **.store_npc_xp_mapping_for_mixin()** (3 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **Protocol** (1 connections)
- **Parse xp_value from NPC base_stats JSON; bool maps to 0 (avoid True -> 1).** (1 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **Log when a player targets an NPC that exists but is not alive.** (1 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **Attributes supplied by NPCCombatIntegrationService (mixin cannot initialize them** (1 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **Return combat service dependency.** (1 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **Return data provider dependency.** (1 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **Return UUID mapping dependency.** (1 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **Return lucidity dependency.** (1 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **Store XP mapping for NPC combat setup from validation mixin.** (1 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- *... and 7 more nodes in this community*

## Relationships

- [game models player](game_models_player.md) (8 shared connections)
- [npc database infrastructure](npc_database_infrastructure.md) (3 shared connections)
- [rate limiter realtime](rate_limiter_realtime.md) (3 shared connections)
- [combat commands handler](combat_commands_handler.md) (3 shared connections)
- [room validator services](room_validator_services.md) (3 shared connections)
- [player event realtime](player_event_realtime.md) (2 shared connections)
- [countdown rest task](countdown_rest_task.md) (1 shared connections)

## Source Files

- `server/services/npc_combat_integration_validation_mixin.py`

## Audit Trail

- EXTRACTED: 109 (90%)
- INFERRED: 12 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*