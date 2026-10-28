# DatabaseManager

> 323 nodes · cohesion 0.01

## Key Concepts

- **CombatParticipant** (295 connections) — `server/models/combat.py`
- **CombatTurnProcessor** (75 connections) — `server/services/combat_turn_processor.py`
- **test_combat.py** (63 connections) — `server/tests/unit/models/test_combat.py`
- **test_combat_turn_processor.py** (49 connections) — `server/tests/unit/services/test_combat_turn_processor.py`
- **CombatAttackHandler** (43 connections) — `server/services/combat_attack_handler.py`
- **test_combat_attack_handler.py** (39 connections) — `server/tests/unit/services/test_combat_attack_handler.py`
- **asyncio** (27 connections)
- **test_combat_tracked_target.py** (11 connections) — `server/tests/unit/models/test_combat_tracked_target.py`
- **.validate_and_get_combat_participants()** (9 connections) — `server/services/combat_attack_handler.py`
- **_fight()** (8 connections) — `server/tests/unit/models/test_combat_tracked_target.py`
- **_bind_get_combat_by_participant()** (8 connections) — `server/tests/unit/services/test_combat_attack_handler.py`
- **._apply_damage()** (7 connections) — `server/services/combat_attack_handler.py`
- **._execute_default_action()** (7 connections) — `server/services/combat_turn_processor.py`
- **._execute_participant_action()** (7 connections) — `server/services/combat_turn_processor.py`
- **._execute_round()** (7 connections) — `server/services/combat_turn_processor.py`
- **asyncio** (7 connections)
- **test_apply_attack_damage()** (7 connections) — `server/tests/unit/services/test_combat_attack_handler.py`
- **test_validate_and_get_combat_participants_attacker_not_found()** (7 connections) — `server/tests/unit/services/test_combat_attack_handler.py`
- **test_validate_and_get_combat_participants_success()** (7 connections) — `server/tests/unit/services/test_combat_attack_handler.py`
- **test_validate_and_get_combat_participants_target_dead()** (7 connections) — `server/tests/unit/services/test_combat_attack_handler.py`
- **test_validate_and_get_combat_participants_target_not_found()** (7 connections) — `server/tests/unit/services/test_combat_attack_handler.py`
- **test_process_player_turn_fallback_to_basic_unarmed_damage_when_no_player_from_persistence()** (7 connections) — `server/tests/unit/services/test_combat_turn_processor.py`
- **_get_default_damage()** (6 connections) — `server/models/combat.py`
- **._cap_damage_for_no_death_room()** (6 connections) — `server/services/combat_attack_handler.py`
- **._find_combat_target()** (6 connections) — `server/services/combat_attack_handler.py`
- *... and 298 more nodes in this community*

## Relationships

- [test_player_combat_service.py](test_player_combat_service.py.md) (96 shared connections)
- [InventorySchemaValidationError](InventorySchemaValidationError.md) (95 shared connections)
- [NPCLifecycleManager](NPCLifecycleManager.md) (25 shared connections)
- [test_npc_combat_integration_join.py](test_npc_combat_integration_join.py.md) (23 shared connections)
- [Reporter](Reporter.md) (13 shared connections)
- [PlayerRespawnEventHandler](PlayerRespawnEventHandler.md) (10 shared connections)
- [CorruptionRepository](CorruptionRepository.md) (10 shared connections)
- [PlayerPositionService](PlayerPositionService.md) (9 shared connections)
- [useThemeContext.ts](useThemeContext.ts.md) (5 shared connections)
- [stateUpdateUtils.ts](stateUpdateUtils.ts.md) (5 shared connections)
- [TestNPCCombatLifecycle](TestNPCCombatLifecycle.md) (4 shared connections)
- [Prometheus Configuration](Prometheus_Configuration.md) (4 shared connections)

## Source Files

- `server/models/combat.py`
- `server/services/combat_attack_handler.py`
- `server/services/combat_turn_processor.py`
- `server/tests/unit/models/test_combat.py`
- `server/tests/unit/models/test_combat_tracked_target.py`
- `server/tests/unit/services/test_combat_attack_handler.py`
- `server/tests/unit/services/test_combat_turn_participant_actions.py`
- `server/tests/unit/services/test_combat_turn_processor.py`
- `server/tests/unit/services/test_damage_grace_period.py`

## Audit Trail

- EXTRACTED: 823 (92%)
- INFERRED: 68 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*