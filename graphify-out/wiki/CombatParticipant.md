# CombatParticipant

> 266 nodes

## Key Concepts

- **CombatParticipant** (195 connections) — `server/models/combat.py`
- **CombatTurnProcessor** (61 connections) — `server/services/combat_turn_processor.py`
- **test_combat.py** (60 connections) — `server/tests/unit/models/test_combat.py`
- **test_combat_turn_processor.py** (50 connections) — `server/tests/unit/services/test_combat_turn_processor.py`
- **CombatAction** (29 connections) — `server/models/combat.py`
- **asyncio** (27 connections)
- **combat_turn_processor.py** (19 connections) — `server/services/combat_turn_processor.py`
- **._execute_spell_action()** (12 connections) — `server/services/combat_turn_processor.py`
- **._execute_queued_action()** (10 connections) — `server/services/combat_turn_processor.py`
- **._build_spell_target()** (7 connections) — `server/services/combat_turn_processor.py`
- **._execute_default_action()** (7 connections) — `server/services/combat_turn_processor.py`
- **._execute_participant_action()** (7 connections) — `server/services/combat_turn_processor.py`
- **._execute_round()** (7 connections) — `server/services/combat_turn_processor.py`
- **._get_player_and_room_for_spell()** (7 connections) — `server/services/combat_turn_processor.py`
- **test_process_player_turn_fallback_to_basic_unarmed_damage_when_no_player_from_persistence()** (7 connections) — `server/tests/unit/services/test_combat_turn_processor.py`
- **_get_default_damage()** (6 connections) — `server/models/combat.py`
- **._execute_attack_action()** (6 connections) — `server/services/combat_turn_processor.py`
- **._finalize_spell_execution()** (6 connections) — `server/services/combat_turn_processor.py`
- **._get_spell_for_action()** (6 connections) — `server/services/combat_turn_processor.py`
- **._is_npc_still_in_world()** (6 connections) — `server/services/combat_turn_processor.py`
- **_stale_queued_attack_rows()** (6 connections) — `server/tests/unit/services/test_combat_turn_processor.py`
- **test_execute_participant_action_valid_queued_attack()** (6 connections) — `server/tests/unit/services/test_combat_turn_processor.py`
- **test_execute_queued_attack_action()** (6 connections) — `server/tests/unit/services/test_combat_turn_processor.py`
- **test_execute_queued_spell_without_magic_service()** (6 connections) — `server/tests/unit/services/test_combat_turn_processor.py`
- **test_process_player_turn_fallback_to_basic_unarmed_damage_when_no_app()** (6 connections) — `server/tests/unit/services/test_combat_turn_processor.py`
- *... and 241 more nodes in this community*

## Relationships

- [CombatInstance](CombatInstance.md) (109 shared connections)
- [CombatService](CombatService.md) (30 shared connections)
- [NATSError](NATSError.md) (13 shared connections)
- [test_combat_flee_handler.py](test_combat_flee_handler.py.md) (7 shared connections)
- [CombatEventHandler](CombatEventHandler.md) (5 shared connections)
- [get_logger](get_logger.md) (5 shared connections)
- [test_combat_death_handler.py](test_combat_death_handler.py.md) (3 shared connections)
- [test_combat_flee_helpers.py](test_combat_flee_helpers.py.md) (2 shared connections)
- [CombatCommandHandler](CombatCommandHandler.md) (2 shared connections)
- [test_combat_service.py](test_combat_service.py.md) (2 shared connections)
- [TargetResolutionService](TargetResolutionService.md) (2 shared connections)
- [TargetMatch](TargetMatch.md) (2 shared connections)

## Source Files

- `server/models/combat.py`
- `server/services/combat_service.py`
- `server/services/combat_turn_processor.py`
- `server/tests/unit/models/test_combat.py`
- `server/tests/unit/services/test_combat_service_npc_helpers.py`
- `server/tests/unit/services/test_combat_turn_processor.py`

## Audit Trail

- EXTRACTED: 612 (95%)
- INFERRED: 35 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*