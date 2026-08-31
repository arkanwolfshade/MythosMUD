# CombatService

> 160 nodes

## Key Concepts

- **CombatService** (173 connections) — `server/services/combat_service.py`
- **combat_service.py** (104 connections) — `server/services/combat_service.py`
- **combat_service_attack.py** (28 connections) — `server/services/combat_service_attack.py`
- **CombatResult** (22 connections) — `server/models/combat.py`
- **UUID** (20 connections)
- **npc_combat_integration_combat_mixin.py** (18 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **get_current_tick()** (16 connections) — `server/app/game_tick_counter.py`
- **_NPCCombatIntegrationDeps** (14 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **finalize_attack_result()** (11 connections) — `server/services/combat_service_attack.py`
- **NPCCombatIntegrationCombatMixin** (9 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **apply_damage_and_check_involuntary_flee()** (9 connections) — `server/services/combat_service_attack.py`
- **validate_melee_location()** (9 connections) — `server/services/combat_service_attack.py`
- **validate_melee_or_end_combat()** (9 connections) — `server/services/combat_service_attack.py`
- **game_tick_counter.py** (9 connections) — `server/app/game_tick_counter.py`
- **test_combat_service_npc_in_combat.py** (9 connections) — `server/tests/unit/services/test_combat_service_npc_in_combat.py`
- **get_combat_service()** (8 connections) — `server/services/combat_service_state.py`
- **._process_combat_attack()** (8 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **.start_new_combat_for_mixin()** (8 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **._create_combat_service_with_nats()** (7 connections) — `server/container/bundles/combat.py`
- **process_attack()** (7 connections) — `server/services/combat_service_attack.py`
- **queue_combat_action()** (7 connections) — `server/services/combat_service_attack.py`
- **._apply_npc_attack_damage_for_npc_initiated_combat()** (7 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **_effective_room_for_melee()** (6 connections) — `server/services/combat_service_attack.py`
- **.finalize_attack_result()** (6 connections) — `server/services/combat_service.py`
- **.validate_melee_or_end_combat()** (6 connections) — `server/services/combat_service.py`
- *... and 135 more nodes in this community*

## Relationships

- [test_combat_service_modules.py](test_combat_service_modules.py.md) (41 shared connections)
- [test_combat_event_publisher.py](test_combat_event_publisher.py.md) (27 shared connections)
- [CombatInstance](CombatInstance.md) (24 shared connections)
- [combat_service_npc.py](combat_service_npc.py.md) (23 shared connections)
- [CombatParticipant](CombatParticipant.md) (22 shared connections)
- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (18 shared connections)
- [spell_effects.py](spell_effects.py.md) (17 shared connections)
- [combat_turn_participant_actions.py](combat_turn_participant_actions.py.md) (12 shared connections)
- [CombatParticipantType](CombatParticipantType.md) (11 shared connections)
- [get_logger](get_logger.md) (8 shared connections)
- [models/combat.py](models-combat.py.md) (7 shared connections)
- [test_player_death_service.py](test_player_death_service.py.md) (7 shared connections)

## Source Files

- `server/app/game_tick_counter.py`
- `server/container/bundles/combat.py`
- `server/models/combat.py`
- `server/services/combat_service.py`
- `server/services/combat_service_attack.py`
- `server/services/combat_service_state.py`
- `server/services/combat_service_types.py`
- `server/services/npc_combat_integration_combat_mixin.py`
- `server/tests/unit/services/test_combat_service_npc_in_combat.py`

## Audit Trail

- EXTRACTED: 468 (84%)
- INFERRED: 91 (16%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*