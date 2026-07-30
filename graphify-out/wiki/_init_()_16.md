# . init ()

> 71 nodes

## Key Concepts

- **NPCCombatLucidity** (30 connections) — `server/services/npc_combat_lucidity.py`
- **_NPCCombatIntegrationValidationDeps** (19 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **TestNPCCombatLucidity** (17 connections) — `server/tests/unit/services/test_npc_combat_lucidity.py`
- **.store_npc_xp_mapping_for_mixin()** (10 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **.get_data_provider()** (6 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **.get_uuid_mapping()** (6 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **UUID** (6 connections)
- **._setup_combat_uuids_and_mappings()** (6 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **.apply_encounter_lucidity_effect()** (6 connections) — `server/services/npc_combat_lucidity.py`
- **._validate_and_get_npc_instance()** (5 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **._validate_combat_location()** (5 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **._end_combat_if_participant_in_combat()** (5 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **._setup_combat_uuids_npc_attacker()** (5 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **.get_combat_service()** (4 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **.get_lucidity_service()** (4 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **._resolve_lucidity_category()** (4 connections) — `server/services/npc_combat_lucidity.py`
- **test_npc_combat_lucidity.py** (4 connections) — `server/tests/unit/services/test_npc_combat_lucidity.py`
- **.test_resolve_lucidity_category_get_behavior_config_exception()** (4 connections) — `server/tests/unit/services/test_npc_combat_lucidity.py`
- **.get_lucidity_service()** (3 connections) — `server/services/npc_combat_integration_service.py`
- **_coerce_xp_mapping_value()** (3 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **_warn_attacked_dead_npc()** (3 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **.store_npc_xp_mapping_for_mixin()** (3 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **.test_init()** (3 connections) — `server/tests/unit/services/test_npc_combat_lucidity.py`
- **.test_resolve_lucidity_category_none_npc()** (3 connections) — `server/tests/unit/services/test_npc_combat_lucidity.py`
- **.test_resolve_lucidity_category_from_base_stats()** (3 connections) — `server/tests/unit/services/test_npc_combat_lucidity.py`
- *... and 46 more nodes in this community*

## Relationships

- [test combat attack handler](test_combat_attack_handler.md) (15 shared connections)
- [main()](main%28%29.md) (3 shared connections)
- [combat](combat.md) (2 shared connections)
- [. initialize handlers()](_initialize_handlers%28%29.md) (2 shared connections)
- [Path](Path.md) (2 shared connections)
- [Any](Any.md) (2 shared connections)
- [CommandHandler](CommandHandler.md) (2 shared connections)
- [test skill service](test_skill_service.md) (1 shared connections)
- [Test despawn npc handles NPC](Test_despawn_npc_handles_NPC.md) (1 shared connections)
- [close db()](close_db%28%29.md) (1 shared connections)
- [create access token()](create_access_token%28%29.md) (1 shared connections)

## Source Files

- `server/services/npc_combat_integration_service.py`
- `server/services/npc_combat_integration_validation_mixin.py`
- `server/services/npc_combat_lucidity.py`
- `server/tests/unit/services/test_npc_combat_lucidity.py`

## Audit Trail

- EXTRACTED: 220 (94%)
- INFERRED: 14 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*