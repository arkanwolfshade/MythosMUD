# test combat attack handler

> 241 nodes

## Key Concepts

- **combat.py** (51 connections) — `server/models/combat.py`
- **npc_combat_integration_service.py** (50 connections) — `server/services/npc_combat_integration_service.py`
- **CombatTurnProcessor** (48 connections) — `server/services/combat_turn_processor.py`
- **test_combat_attack_handler.py** (37 connections) — `server/tests/unit/services/test_combat_attack_handler.py`
- **CombatParticipantType** (36 connections) — `server/models/combat.py`
- **test_combat_turn_processor.py** (36 connections) — `server/tests/unit/services/test_combat_turn_processor.py`
- **NPCCombatDataProvider** (29 connections) — `server/services/npc_combat_data_provider.py`
- **test_damage_grace_period.py** (26 connections) — `server/tests/unit/services/test_damage_grace_period.py`
- **CombatAction** (21 connections) — `server/models/combat.py`
- **combat_turn_processor.py** (19 connections) — `server/services/combat_turn_processor.py`
- **npc_combat_integration_validation_mixin.py** (19 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **npc_combat_data_provider.py** (18 connections) — `server/services/npc_combat_data_provider.py`
- **combat_attack_handler.py** (17 connections) — `server/services/combat_attack_handler.py`
- **CombatAttackHandler** (17 connections) — `server/services/combat_attack_handler.py`
- **npc_combat_integration_combat_mixin.py** (15 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **NPCCombatIntegrationValidationMixin** (15 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **test_npc_combat_data_provider.py** (14 connections) — `server/tests/unit/services/test_npc_combat_data_provider.py`
- **CombatStatus** (11 connections) — `server/models/combat.py`
- **._execute_spell_action()** (11 connections) — `server/services/combat_turn_processor.py`
- **combat_types.py** (11 connections) — `server/services/combat_types.py`
- **NPCCombatIntegrationCombatMixin** (11 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **._execute_queued_action()** (10 connections) — `server/services/combat_turn_processor.py`
- **._get_player_and_room_for_spell()** (8 connections) — `server/services/combat_turn_processor.py`
- **npc_combat_uuid_mapping.py** (8 connections) — `server/services/npc_combat_uuid_mapping.py`
- **._execute_participant_action()** (7 connections) — `server/services/combat_turn_processor.py`
- *... and 216 more nodes in this community*

## Relationships

- [close db()](close_db%28%29.md) (79 shared connections)
- [. initialize handlers()](_initialize_handlers%28%29.md) (29 shared connections)
- [world](world.md) (23 shared connections)
- [. init ()](_init_%28%29.md) (23 shared connections)
- [get health service()](get_health_service%28%29.md) (15 shared connections)
- [test exploration service](test_exploration_service.md) (15 shared connections)
- [Any](Any.md) (14 shared connections)
- [CombatService](CombatService.md) (10 shared connections)
- [combat](combat.md) (9 shared connections)
- [get current tick()](get_current_tick%28%29.md) (7 shared connections)
- [.validate target()](validate_target%28%29.md) (6 shared connections)
- [login grace period](login_grace_period.md) (6 shared connections)

## Source Files

- `server/models/combat.py`
- `server/services/combat_attack_handler.py`
- `server/services/combat_turn_processor.py`
- `server/services/combat_types.py`
- `server/services/npc_combat_data_provider.py`
- `server/services/npc_combat_integration_combat_mixin.py`
- `server/services/npc_combat_integration_service.py`
- `server/services/npc_combat_integration_validation_mixin.py`
- `server/services/npc_combat_uuid_mapping.py`
- `server/tests/unit/services/test_combat_attack_handler.py`
- `server/tests/unit/services/test_combat_turn_processor.py`
- `server/tests/unit/services/test_combat_types.py`
- `server/tests/unit/services/test_damage_grace_period.py`
- `server/tests/unit/services/test_npc_combat_data_provider.py`

## Audit Trail

- EXTRACTED: 970 (97%)
- INFERRED: 27 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*