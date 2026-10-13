# Combat Participants

> 236 nodes

## Key Concepts

- **CombatParticipant** (291 connections) — `server/models/combat.py`
- **CombatTurnProcessor** (75 connections) — `server/services/combat_turn_processor.py`
- **test_combat.py** (63 connections) — `server/tests/unit/models/test_combat.py`
- **test_combat_turn_processor.py** (49 connections) — `server/tests/unit/services/test_combat_turn_processor.py`
- **CombatAction** (45 connections) — `server/models/combat.py`
- **asyncio** (27 connections)
- **._execute_queued_action()** (12 connections) — `server/services/combat_turn_processor.py`
- **._execute_spell_action()** (11 connections) — `server/services/combat_turn_processor.py`
- **._execute_default_action()** (7 connections) — `server/services/combat_turn_processor.py`
- **._execute_participant_action()** (7 connections) — `server/services/combat_turn_processor.py`
- **._execute_round()** (7 connections) — `server/services/combat_turn_processor.py`
- **test_process_player_turn_fallback_to_basic_unarmed_damage_when_no_player_from_persistence()** (7 connections) — `server/tests/unit/services/test_combat_turn_processor.py`
- **._build_spell_target()** (6 connections) — `server/services/combat_turn_processor.py`
- **._execute_attack_action()** (6 connections) — `server/services/combat_turn_processor.py`
- **._execute_protect_action()** (6 connections) — `server/services/combat_turn_processor.py`
- **._execute_taunt_action()** (6 connections) — `server/services/combat_turn_processor.py`
- **._finalize_spell_execution()** (6 connections) — `server/services/combat_turn_processor.py`
- **._get_player_and_room_for_spell()** (6 connections) — `server/services/combat_turn_processor.py`
- **._get_spell_for_action()** (6 connections) — `server/services/combat_turn_processor.py`
- **._is_npc_still_in_world()** (6 connections) — `server/services/combat_turn_processor.py`
- **test_process_npc_turn_calls_process_attack_when_target_resolved()** (6 connections) — `server/tests/unit/services/test_combat_turn_participant_actions.py`
- **_stale_queued_attack_rows()** (6 connections) — `server/tests/unit/services/test_combat_turn_processor.py`
- **test_execute_participant_action_valid_queued_attack()** (6 connections) — `server/tests/unit/services/test_combat_turn_processor.py`
- **test_execute_queued_attack_action()** (6 connections) — `server/tests/unit/services/test_combat_turn_processor.py`
- **test_execute_queued_spell_without_magic_service()** (6 connections) — `server/tests/unit/services/test_combat_turn_processor.py`
- *... and 211 more nodes in this community*

## Relationships

- [Combat Instance Turns](Combat_Instance_Turns.md) (60 shared connections)
- [Combat Attack Execution](Combat_Attack_Execution.md) (46 shared connections)
- [Community 121](Community_121.md) (29 shared connections)
- [Community 134](Community_134.md) (24 shared connections)
- [Community 52](Community_52.md) (21 shared connections)
- [Spell Effects & Combat Wiring](Spell_Effects_&_Combat_Wiring.md) (21 shared connections)
- [Community 427](Community_427.md) (15 shared connections)
- [Community 126](Community_126.md) (11 shared connections)
- [Community 118](Community_118.md) (11 shared connections)
- [Community 227](Community_227.md) (9 shared connections)
- [Community 431](Community_431.md) (9 shared connections)
- [Community 758](Community_758.md) (5 shared connections)

## Source Files

- `server/models/combat.py`
- `server/services/combat_turn_processor.py`
- `server/tests/unit/models/test_combat.py`
- `server/tests/unit/services/test_combat_turn_participant_actions.py`
- `server/tests/unit/services/test_combat_turn_processor.py`

## Audit Trail

- EXTRACTED: 690 (95%)
- INFERRED: 39 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*