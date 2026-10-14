# CombatParticipant

> 249 nodes

## Key Concepts

- **CombatParticipant** (295 connections) — `server/models/combat.py`
- **CombatTurnProcessor** (75 connections) — `server/services/combat_turn_processor.py`
- **test_combat.py** (63 connections) — `server/tests/unit/models/test_combat.py`
- **test_combat_turn_processor.py** (49 connections) — `server/tests/unit/services/test_combat_turn_processor.py`
- **CombatAction** (45 connections) — `server/models/combat.py`
- **asyncio** (27 connections)
- **._execute_queued_action()** (12 connections) — `server/services/combat_turn_processor.py`
- **._execute_spell_action()** (12 connections) — `server/services/combat_turn_processor.py`
- **test_combat_tracked_target.py** (11 connections) — `server/tests/unit/models/test_combat_tracked_target.py`
- **_fight()** (8 connections) — `server/tests/unit/models/test_combat_tracked_target.py`
- **._build_spell_target()** (7 connections) — `server/services/combat_turn_processor.py`
- **._execute_default_action()** (7 connections) — `server/services/combat_turn_processor.py`
- **._execute_participant_action()** (7 connections) — `server/services/combat_turn_processor.py`
- **._execute_round()** (7 connections) — `server/services/combat_turn_processor.py`
- **._get_player_and_room_for_spell()** (7 connections) — `server/services/combat_turn_processor.py`
- **test_process_player_turn_fallback_to_basic_unarmed_damage_when_no_player_from_persistence()** (7 connections) — `server/tests/unit/services/test_combat_turn_processor.py`
- **._execute_attack_action()** (6 connections) — `server/services/combat_turn_processor.py`
- **._execute_protect_action()** (6 connections) — `server/services/combat_turn_processor.py`
- **._execute_taunt_action()** (6 connections) — `server/services/combat_turn_processor.py`
- **._finalize_spell_execution()** (6 connections) — `server/services/combat_turn_processor.py`
- **._get_spell_for_action()** (6 connections) — `server/services/combat_turn_processor.py`
- **._is_npc_still_in_world()** (6 connections) — `server/services/combat_turn_processor.py`
- **test_process_npc_turn_calls_process_attack_when_target_resolved()** (6 connections) — `server/tests/unit/services/test_combat_turn_participant_actions.py`
- **_stale_queued_attack_rows()** (6 connections) — `server/tests/unit/services/test_combat_turn_processor.py`
- **test_execute_participant_action_valid_queued_attack()** (6 connections) — `server/tests/unit/services/test_combat_turn_processor.py`
- *... and 224 more nodes in this community*

## Relationships

- [CombatService](CombatService.md) (66 shared connections)
- [CombatInstance](CombatInstance.md) (61 shared connections)
- [CombatAttackHandler](CombatAttackHandler.md) (28 shared connections)
- [SuccessLevel](SuccessLevel.md) (24 shared connections)
- [aggro_threat.py](aggro_threat.py.md) (19 shared connections)
- [test_utility_threat.py](test_utility_threat.py.md) (15 shared connections)
- [test_combat_service_modules.py](test_combat_service_modules.py.md) (13 shared connections)
- [combat_assist.py](combat_assist.py.md) (11 shared connections)
- [CombatEventHandler](CombatEventHandler.md) (11 shared connections)
- [combat_taunt.py](combat_taunt.py.md) (9 shared connections)
- [test_combat_turn_player_turn.py](test_combat_turn_player_turn.py.md) (6 shared connections)
- [test_combat_event_publisher.py](test_combat_event_publisher.py.md) (5 shared connections)

## Source Files

- `server/models/combat.py`
- `server/services/combat_service.py`
- `server/services/combat_turn_processor.py`
- `server/tests/unit/models/test_combat.py`
- `server/tests/unit/models/test_combat_tracked_target.py`
- `server/tests/unit/services/test_combat_turn_participant_actions.py`
- `server/tests/unit/services/test_combat_turn_processor.py`

## Audit Trail

- EXTRACTED: 715 (95%)
- INFERRED: 40 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*