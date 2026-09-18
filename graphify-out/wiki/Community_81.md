# Community 81

> 104 nodes

## Key Concepts

- **CombatTurnProcessor** (61 connections) — `server/services/combat_turn_processor.py`
- **test_combat_turn_processor.py** (49 connections) — `server/tests/unit/services/test_combat_turn_processor.py`
- **CombatAction** (29 connections) — `server/models/combat.py`
- **asyncio** (27 connections)
- **._execute_default_action()** (7 connections) — `server/services/combat_turn_processor.py`
- **._execute_participant_action()** (7 connections) — `server/services/combat_turn_processor.py`
- **._execute_round()** (7 connections) — `server/services/combat_turn_processor.py`
- **test_process_player_turn_fallback_to_basic_unarmed_damage_when_no_player_from_persistence()** (7 connections) — `server/tests/unit/services/test_combat_turn_processor.py`
- **._is_npc_still_in_world()** (6 connections) — `server/services/combat_turn_processor.py`
- **_stale_queued_attack_rows()** (6 connections) — `server/tests/unit/services/test_combat_turn_processor.py`
- **test_execute_participant_action_valid_queued_attack()** (6 connections) — `server/tests/unit/services/test_combat_turn_processor.py`
- **test_execute_queued_attack_action()** (6 connections) — `server/tests/unit/services/test_combat_turn_processor.py`
- **test_execute_queued_spell_without_magic_service()** (6 connections) — `server/tests/unit/services/test_combat_turn_processor.py`
- **test_process_player_turn_fallback_to_basic_unarmed_damage_when_no_app()** (6 connections) — `server/tests/unit/services/test_combat_turn_processor.py`
- **_unarmed_fallback_player_target_pair()** (6 connections) — `server/tests/unit/services/test_combat_turn_processor.py`
- **.process_game_tick()** (5 connections) — `server/services/combat_turn_processor.py`
- **._process_npc_turn()** (5 connections) — `server/services/combat_turn_processor.py`
- **._process_player_turn()** (5 connections) — `server/services/combat_turn_processor.py`
- **test_execute_queued_flee_skip()** (5 connections) — `server/tests/unit/services/test_combat_turn_processor.py`
- **test_execute_queued_unknown_action_logs()** (5 connections) — `server/tests/unit/services/test_combat_turn_processor.py`
- **test_execute_round_stale_queued_attack_uses_default_action()** (5 connections) — `server/tests/unit/services/test_combat_turn_processor.py`
- **test_execute_round_with_participants()** (5 connections) — `server/tests/unit/services/test_combat_turn_processor.py`
- **test_process_npc_turn_no_target()** (5 connections) — `server/tests/unit/services/test_combat_turn_processor.py`
- **test_process_npc_turn_npc_dead()** (5 connections) — `server/tests/unit/services/test_combat_turn_processor.py`
- **test_process_player_turn_casting_spell()** (5 connections) — `server/tests/unit/services/test_combat_turn_processor.py`
- *... and 79 more nodes in this community*

## Relationships

- [Combat Instance Turn Management](Combat_Instance_Turn_Management.md) (58 shared connections)
- [Community 275](Community_275.md) (7 shared connections)
- [Combat Cleanup & Results](Combat_Cleanup_&_Results.md) (5 shared connections)
- [Community 150](Community_150.md) (2 shared connections)
- [Community 33](Community_33.md) (1 shared connections)
- [Community 46](Community_46.md) (1 shared connections)

## Source Files

- `server/models/combat.py`
- `server/services/combat_turn_processor.py`
- `server/tests/unit/services/test_combat_turn_processor.py`

## Audit Trail

- EXTRACTED: 232 (87%)
- INFERRED: 34 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*