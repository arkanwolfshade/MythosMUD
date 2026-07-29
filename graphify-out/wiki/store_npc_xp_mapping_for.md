# .store npc xp mapping for

> 32 nodes

## Key Concepts

- **_NPCCombatIntegrationValidationDeps** (19 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **.store_npc_xp_mapping_for_mixin()** (10 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **.get_base_stats()** (6 connections) — `server/models/npc.py`
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
- **Get base stats as dictionary.** (1 connections) — `server/models/npc.py`
- **Protocol** (1 connections)
- **Parse xp_value from NPC base_stats JSON; bool maps to 0 (avoid True -> 1).** (1 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **Log when a player targets an NPC that exists but is not alive.** (1 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **Attributes supplied by NPCCombatIntegrationService (mixin cannot initialize them** (1 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **Return combat service dependency.** (1 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **Return data provider dependency.** (1 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **Return UUID mapping dependency.** (1 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **Return lucidity dependency.** (1 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- *... and 7 more nodes in this community*

## Relationships

- [initialize nats and combat services()](initialize_nats_and_combat_services%28%29.md) (14 shared connections)
- [. repr ()](_repr_%28%29.md) (3 shared connections)
- [.get lucidity service()](get_lucidity_service%28%29.md) (2 shared connections)
- [.get uuid mapping()](get_uuid_mapping%28%29.md) (2 shared connections)
- [Any](Any.md) (2 shared connections)
- [.set player combat service()](set_player_combat_service%28%29.md) (1 shared connections)

## Source Files

- `server/models/npc.py`
- `server/services/npc_combat_integration_validation_mixin.py`

## Audit Trail

- EXTRACTED: 104 (93%)
- INFERRED: 8 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*