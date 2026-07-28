# Server Models (2)

> 211 nodes

## Key Concepts

- **CombatParticipant** (166 connections) — `server/models/combat.py`
- **test_combat.py** (60 connections) — `server/tests/unit/models/test_combat.py`
- **CombatTurnProcessor** (48 connections) — `server/services/combat_turn_processor.py`
- **test_combat_turn_processor.py** (36 connections) — `server/tests/unit/services/test_combat_turn_processor.py`
- **CombatAction** (21 connections) — `server/models/combat.py`
- **._execute_spell_action()** (11 connections) — `server/services/combat_turn_processor.py`
- **._execute_queued_action()** (10 connections) — `server/services/combat_turn_processor.py`
- **._get_player_and_room_for_spell()** (8 connections) — `server/services/combat_turn_processor.py`
- **._execute_participant_action()** (7 connections) — `server/services/combat_turn_processor.py`
- **._execute_round()** (7 connections) — `server/services/combat_turn_processor.py`
- **._build_spell_target()** (7 connections) — `server/services/combat_turn_processor.py`
- **._execute_default_action()** (7 connections) — `server/services/combat_turn_processor.py`
- **_get_default_damage()** (6 connections) — `server/models/combat.py`
- **._is_npc_still_in_world()** (6 connections) — `server/services/combat_turn_processor.py`
- **._execute_attack_action()** (6 connections) — `server/services/combat_turn_processor.py`
- **._get_spell_for_action()** (6 connections) — `server/services/combat_turn_processor.py`
- **._finalize_spell_execution()** (6 connections) — `server/services/combat_turn_processor.py`
- **_stale_queued_attack_rows()** (6 connections) — `server/tests/unit/services/test_combat_turn_processor.py`
- **_unarmed_fallback_player_target_pair()** (6 connections) — `server/tests/unit/services/test_combat_turn_processor.py`
- **test_process_player_turn_fallback_to_basic_unarmed_damage_when_no_player_from_persistence()** (6 connections) — `server/tests/unit/services/test_combat_turn_processor.py`
- **.process_game_tick()** (5 connections) — `server/services/combat_turn_processor.py`
- **Any** (5 connections)
- **._apply_spell_effects()** (5 connections) — `server/services/combat_turn_processor.py`
- **._handle_flee_skip_action()** (5 connections) — `server/services/combat_turn_processor.py`
- **._process_npc_turn()** (5 connections) — `server/services/combat_turn_processor.py`
- *... and 186 more nodes in this community*

## Relationships

- [Server Services (28)](Server_Services_%2828%29.md) (49 shared connections)
- [Server Services (29)](Server_Services_%2829%29.md) (20 shared connections)
- [Server Services (7)](Server_Services_%287%29.md) (18 shared connections)
- [Server Services (36)](Server_Services_%2836%29.md) (18 shared connections)
- [Server Services (9)](Server_Services_%289%29.md) (12 shared connections)
- [Server Services (13)](Server_Services_%2813%29.md) (10 shared connections)
- [Server Services (26)](Server_Services_%2826%29.md) (8 shared connections)
- [Server Services (5)](Server_Services_%285%29.md) (7 shared connections)
- [Server Commands (24)](Server_Commands_%2824%29.md) (6 shared connections)
- [Server Services (68)](Server_Services_%2868%29.md) (3 shared connections)
- [Server Game (2)](Server_Game_%282%29.md) (3 shared connections)
- [Server Config (2)](Server_Config_%282%29.md) (2 shared connections)

## Source Files

- `server/models/combat.py`
- `server/services/combat_turn_processor.py`
- `server/tests/unit/models/test_combat.py`
- `server/tests/unit/services/test_combat_turn_processor.py`

## Audit Trail

- EXTRACTED: 839 (99%)
- INFERRED: 6 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*