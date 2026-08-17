# combat_service_attack.py

> 52 nodes

## Key Concepts

- **combat_service_attack.py** (28 connections) — `server/services/combat_service_attack.py`
- **CombatResult** (20 connections) — `server/models/combat.py`
- **_NPCCombatIntegrationDeps** (14 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **get_current_tick()** (14 connections) — `server/app/game_tick_counter.py`
- **finalize_attack_result()** (10 connections) — `server/services/combat_service_attack.py`
- **NPCCombatIntegrationCombatMixin** (9 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **validate_melee_location()** (9 connections) — `server/services/combat_service_attack.py`
- **validate_melee_or_end_combat()** (9 connections) — `server/services/combat_service_attack.py`
- **apply_damage_and_check_involuntary_flee()** (8 connections) — `server/services/combat_service_attack.py`
- **._process_combat_attack()** (8 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **.start_new_combat_for_mixin()** (8 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **game_tick_counter.py** (8 connections) — `server/app/game_tick_counter.py`
- **process_attack()** (7 connections) — `server/services/combat_service_attack.py`
- **queue_combat_action()** (7 connections) — `server/services/combat_service_attack.py`
- **._apply_npc_attack_damage_for_npc_initiated_combat()** (7 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **_effective_room_for_melee()** (6 connections) — `server/services/combat_service_attack.py`
- **._broadcast_room_after_npc_death()** (6 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **.get_combat_service()** (6 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **UUID** (6 connections)
- **_melee_location_fail_reason()** (5 connections) — `server/services/combat_service_attack.py`
- **.apply_damage_and_check_involuntary_flee()** (5 connections) — `server/services/combat_service.py`
- **.get_data_provider()** (5 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **UUID** (5 connections)
- **.get_messaging_integration()** (4 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **.start_new_combat_for_mixin()** (4 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- *... and 27 more nodes in this community*

## Relationships

- [CombatService](CombatService.md) (27 shared connections)
- [test_combat_service_modules.py](test_combat_service_modules.py.md) (11 shared connections)
- [CombatParticipant](CombatParticipant.md) (10 shared connections)
- [CombatInstance](CombatInstance.md) (6 shared connections)
- [test_game_tick_processing.py](test_game_tick_processing.py.md) (4 shared connections)
- [test_combat_service.py](test_combat_service.py.md) (3 shared connections)
- [UUID](UUID.md) (3 shared connections)
- [PlayerService](PlayerService.md) (3 shared connections)
- [test_aggro_threat.py](test_aggro_threat.py.md) (3 shared connections)
- [npc_combat_integration_service.py](npc_combat_integration_service.py.md) (2 shared connections)
- [NPCCombatDataProvider](NPCCombatDataProvider.md) (2 shared connections)
- [game_tick_processing.py](game_tick_processing.py.md) (2 shared connections)

## Source Files

- `server/app/game_tick_counter.py`
- `server/models/combat.py`
- `server/services/combat_service.py`
- `server/services/combat_service_attack.py`
- `server/services/npc_combat_integration_combat_mixin.py`
- `server/tests/unit/services/test_combat_service_modules.py`

## Audit Trail

- EXTRACTED: 154 (92%)
- INFERRED: 14 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*