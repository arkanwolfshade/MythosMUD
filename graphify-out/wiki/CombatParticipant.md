# CombatParticipant

> 329 nodes

## Key Concepts

- **CombatParticipant** (216 connections) — `server/models/combat.py`
- **CombatTurnProcessor** (61 connections) — `server/services/combat_turn_processor.py`
- **models/combat.py** (60 connections) — `server/models/combat.py`
- **test_combat.py** (60 connections) — `server/tests/unit/models/test_combat.py`
- **test_combat_turn_processor.py** (50 connections) — `server/tests/unit/services/test_combat_turn_processor.py`
- **combat_turn_participant_actions.py** (47 connections) — `server/services/combat_turn_participant_actions.py`
- **CombatParticipantType** (45 connections) — `server/models/combat.py`
- **CombatAction** (29 connections) — `server/models/combat.py`
- **asyncio** (27 connections)
- **combat_attack_handler.py** (22 connections) — `server/services/combat_attack_handler.py`
- **combat_turn_processor.py** (19 connections) — `server/services/combat_turn_processor.py`
- **test_combat_cleanup_handler.py** (19 connections) — `server/tests/unit/services/test_combat_cleanup_handler.py`
- **CombatStatus** (13 connections) — `server/models/combat.py`
- **test_combat_turn_participant_actions.py** (13 connections) — `server/tests/unit/services/test_combat_turn_participant_actions.py`
- **._execute_spell_action()** (12 connections) — `server/services/combat_turn_processor.py`
- **_weapon_damage_from_equipped_player()** (11 connections) — `server/services/combat_turn_participant_actions.py`
- **combat_cleanup_handler.py** (11 connections) — `server/services/combat_cleanup_handler.py`
- **process_npc_turn()** (10 connections) — `server/services/combat_turn_participant_actions.py`
- **process_player_turn()** (10 connections) — `server/services/combat_turn_participant_actions.py`
- **._execute_queued_action()** (10 connections) — `server/services/combat_turn_processor.py`
- **_get_combat_container_services()** (9 connections) — `server/services/combat_turn_participant_actions.py`
- **resolve_player_attack_damage()** (9 connections) — `server/services/combat_turn_participant_actions.py`
- **._apply_damage()** (7 connections) — `server/services/combat_attack_handler.py`
- **_execute_player_attack()** (7 connections) — `server/services/combat_turn_participant_actions.py`
- **_select_npc_target()** (7 connections) — `server/services/combat_turn_participant_actions.py`
- *... and 304 more nodes in this community*

## Relationships

- [CombatInstance](CombatInstance.md) (104 shared connections)
- [CombatService](CombatService.md) (55 shared connections)
- [test_aggro_threat.py](test_aggro_threat.py.md) (27 shared connections)
- [CombatCommandHandler](CombatCommandHandler.md) (15 shared connections)
- [test_combat_event_publisher.py](test_combat_event_publisher.py.md) (15 shared connections)
- [test_combat_death_handler.py](test_combat_death_handler.py.md) (11 shared connections)
- [test_combat_service_modules.py](test_combat_service_modules.py.md) (10 shared connections)
- [get_logger](get_logger.md) (10 shared connections)
- [CombatParticipantData](CombatParticipantData.md) (9 shared connections)
- [get_config](get_config.md) (9 shared connections)
- [SpellEffectType](SpellEffectType.md) (7 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (6 shared connections)

## Source Files

- `server/models/combat.py`
- `server/services/combat_attack_handler.py`
- `server/services/combat_cleanup_handler.py`
- `server/services/combat_turn_participant_actions.py`
- `server/services/combat_turn_processor.py`
- `server/services/player_position_service.py`
- `server/tests/unit/models/test_combat.py`
- `server/tests/unit/services/test_combat_cleanup_handler.py`
- `server/tests/unit/services/test_combat_turn_participant_actions.py`
- `server/tests/unit/services/test_combat_turn_processor.py`

## Audit Trail

- EXTRACTED: 882 (94%)
- INFERRED: 54 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*