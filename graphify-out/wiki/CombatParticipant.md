# CombatParticipant

> 276 nodes

## Key Concepts

- **CombatParticipant** (194 connections) — `server/models/combat.py`
- **CombatTurnProcessor** (61 connections) — `server/services/combat_turn_processor.py`
- **models/combat.py** (58 connections) — `server/models/combat.py`
- **test_combat_turn_processor.py** (50 connections) — `server/tests/unit/services/test_combat_turn_processor.py`
- **combat_turn_participant_actions.py** (47 connections) — `server/services/combat_turn_participant_actions.py`
- **CombatParticipantType** (44 connections) — `server/models/combat.py`
- **test_combat_attack_handler.py** (38 connections) — `server/tests/unit/services/test_combat_attack_handler.py`
- **CombatAction** (29 connections) — `server/models/combat.py`
- **test_damage_grace_period.py** (28 connections) — `server/tests/unit/services/test_damage_grace_period.py`
- **asyncio** (27 connections)
- **spell_targeting.py** (25 connections) — `server/game/magic/spell_targeting.py`
- **combat_turn_processor.py** (19 connections) — `server/services/combat_turn_processor.py`
- **combat_attack_handler.py** (17 connections) — `server/services/combat_attack_handler.py`
- **CombatStatus** (13 connections) — `server/models/combat.py`
- **test_combat_turn_participant_actions.py** (13 connections) — `server/tests/unit/services/test_combat_turn_participant_actions.py`
- **._execute_spell_action()** (12 connections) — `server/services/combat_turn_processor.py`
- **_weapon_damage_from_equipped_player()** (11 connections) — `server/services/combat_turn_participant_actions.py`
- **process_npc_turn()** (10 connections) — `server/services/combat_turn_participant_actions.py`
- **process_player_turn()** (10 connections) — `server/services/combat_turn_participant_actions.py`
- **._execute_queued_action()** (10 connections) — `server/services/combat_turn_processor.py`
- **_get_combat_container_services()** (9 connections) — `server/services/combat_turn_participant_actions.py`
- **resolve_player_attack_damage()** (9 connections) — `server/services/combat_turn_participant_actions.py`
- **_execute_player_attack()** (7 connections) — `server/services/combat_turn_participant_actions.py`
- **_select_npc_target()** (7 connections) — `server/services/combat_turn_participant_actions.py`
- **._build_spell_target()** (7 connections) — `server/services/combat_turn_processor.py`
- *... and 251 more nodes in this community*

## Relationships

- [CombatService](CombatService.md) (55 shared connections)
- [CombatInstance](CombatInstance.md) (45 shared connections)
- [test_combat.py](test_combat.py.md) (42 shared connections)
- [get_logger](get_logger.md) (28 shared connections)
- [test_aggro_threat.py](test_aggro_threat.py.md) (27 shared connections)
- [TargetType](TargetType.md) (14 shared connections)
- [CombatAttackHandler](CombatAttackHandler.md) (13 shared connections)
- [CombatParticipantData](CombatParticipantData.md) (12 shared connections)
- [test_combat_event_publisher.py](test_combat_event_publisher.py.md) (12 shared connections)
- [combat_service_npc.py](combat_service_npc.py.md) (12 shared connections)
- [test_combat_service_modules.py](test_combat_service_modules.py.md) (10 shared connections)
- [TargetMatch](TargetMatch.md) (10 shared connections)

## Source Files

- `server/game/magic/spell_targeting.py`
- `server/models/combat.py`
- `server/services/combat_attack_handler.py`
- `server/services/combat_turn_participant_actions.py`
- `server/services/combat_turn_processor.py`
- `server/tests/unit/models/test_combat.py`
- `server/tests/unit/services/test_combat_attack_handler.py`
- `server/tests/unit/services/test_combat_turn_participant_actions.py`
- `server/tests/unit/services/test_combat_turn_processor.py`
- `server/tests/unit/services/test_combat_types.py`
- `server/tests/unit/services/test_damage_grace_period.py`

## Audit Trail

- EXTRACTED: 814 (94%)
- INFERRED: 52 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*