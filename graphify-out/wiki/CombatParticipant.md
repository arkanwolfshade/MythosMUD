# CombatParticipant

> 145 nodes

## Key Concepts

- **CombatParticipant** (194 connections) — `server/models/combat.py`
- **CombatTurnProcessor** (61 connections) — `server/services/combat_turn_processor.py`
- **test_combat_turn_processor.py** (50 connections) — `server/tests/unit/services/test_combat_turn_processor.py`
- **CombatAction** (29 connections) — `server/models/combat.py`
- **asyncio** (27 connections)
- **._execute_spell_action()** (12 connections) — `server/services/combat_turn_processor.py`
- **._execute_queued_action()** (10 connections) — `server/services/combat_turn_processor.py`
- **_select_npc_target()** (7 connections) — `server/services/combat_turn_participant_actions.py`
- **._build_spell_target()** (7 connections) — `server/services/combat_turn_processor.py`
- **._execute_default_action()** (7 connections) — `server/services/combat_turn_processor.py`
- **._execute_participant_action()** (7 connections) — `server/services/combat_turn_processor.py`
- **._execute_round()** (7 connections) — `server/services/combat_turn_processor.py`
- **._get_player_and_room_for_spell()** (7 connections) — `server/services/combat_turn_processor.py`
- **test_process_player_turn_fallback_to_basic_unarmed_damage_when_no_player_from_persistence()** (7 connections) — `server/tests/unit/services/test_combat_turn_processor.py`
- **._execute_attack_action()** (6 connections) — `server/services/combat_turn_processor.py`
- **._finalize_spell_execution()** (6 connections) — `server/services/combat_turn_processor.py`
- **._get_spell_for_action()** (6 connections) — `server/services/combat_turn_processor.py`
- **._is_npc_still_in_world()** (6 connections) — `server/services/combat_turn_processor.py`
- **_stale_queued_attack_rows()** (6 connections) — `server/tests/unit/services/test_combat_turn_processor.py`
- **test_execute_participant_action_valid_queued_attack()** (6 connections) — `server/tests/unit/services/test_combat_turn_processor.py`
- **test_execute_queued_attack_action()** (6 connections) — `server/tests/unit/services/test_combat_turn_processor.py`
- **test_execute_queued_spell_without_magic_service()** (6 connections) — `server/tests/unit/services/test_combat_turn_processor.py`
- **test_process_player_turn_fallback_to_basic_unarmed_damage_when_no_app()** (6 connections) — `server/tests/unit/services/test_combat_turn_processor.py`
- **_unarmed_fallback_player_target_pair()** (6 connections) — `server/tests/unit/services/test_combat_turn_processor.py`
- **._apply_spell_effects()** (5 connections) — `server/services/combat_turn_processor.py`
- *... and 120 more nodes in this community*

## Relationships

- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (42 shared connections)
- [test_combat.py](test_combat.py.md) (38 shared connections)
- [CombatInstance](CombatInstance.md) (32 shared connections)
- [test_combat_service_modules.py](test_combat_service_modules.py.md) (13 shared connections)
- [test_aggro_threat.py](test_aggro_threat.py.md) (11 shared connections)
- [combat_service_npc.py](combat_service_npc.py.md) (8 shared connections)
- [CombatDeathHandler](CombatDeathHandler.md) (6 shared connections)
- [CombatAttackHandler](CombatAttackHandler.md) (5 shared connections)
- [UUID](UUID.md) (5 shared connections)
- [CombatEventHandler](CombatEventHandler.md) (5 shared connections)
- [test_combat_attack_handler.py](test_combat_attack_handler.py.md) (3 shared connections)
- [test_combat_death_handler.py](test_combat_death_handler.py.md) (3 shared connections)

## Source Files

- `server/models/combat.py`
- `server/services/combat_service.py`
- `server/services/combat_turn_participant_actions.py`
- `server/services/combat_turn_processor.py`
- `server/tests/unit/models/test_combat.py`
- `server/tests/unit/services/test_combat_turn_participant_actions.py`
- `server/tests/unit/services/test_combat_turn_processor.py`

## Audit Trail

- EXTRACTED: 448 (93%)
- INFERRED: 36 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*