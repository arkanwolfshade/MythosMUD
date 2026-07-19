# Combat Turn Processor

> 48 nodes · cohesion 0.09

## Key Concepts

- **CombatTurnProcessor** (44 connections) — `server/services/combat_turn_processor.py`
- **CombatParticipant** (16 connections) — `server/services/combat_turn_processor.py`
- **CombatInstance** (13 connections) — `server/services/combat_turn_processor.py`
- **._execute_spell_action()** (11 connections) — `server/services/combat_turn_processor.py`
- **._execute_queued_action()** (10 connections) — `server/services/combat_turn_processor.py`
- **CombatAction** (8 connections) — `server/services/combat_turn_processor.py`
- **._build_spell_target()** (7 connections) — `server/services/combat_turn_processor.py`
- **._execute_default_action()** (7 connections) — `server/services/combat_turn_processor.py`
- **._execute_participant_action()** (7 connections) — `server/services/combat_turn_processor.py`
- **._execute_round()** (7 connections) — `server/services/combat_turn_processor.py`
- **._get_player_and_room_for_spell()** (7 connections) — `server/services/combat_turn_processor.py`
- **Any** (6 connections) — `server/services/combat_turn_processor.py`
- **._execute_attack_action()** (6 connections) — `server/services/combat_turn_processor.py`
- **._finalize_spell_execution()** (6 connections) — `server/services/combat_turn_processor.py`
- **._get_spell_for_action()** (6 connections) — `server/services/combat_turn_processor.py`
- **._is_npc_still_in_world()** (6 connections) — `server/services/combat_turn_processor.py`
- **._apply_spell_effects()** (5 connections) — `server/services/combat_turn_processor.py`
- **._handle_flee_skip_action()** (5 connections) — `server/services/combat_turn_processor.py`
- **.process_game_tick()** (5 connections) — `server/services/combat_turn_processor.py`
- **._process_npc_turn()** (5 connections) — `server/services/combat_turn_processor.py`
- **._process_player_turn()** (5 connections) — `server/services/combat_turn_processor.py`
- **._load_round_actions()** (4 connections) — `server/services/combat_turn_processor.py`
- **._log_unknown_action()** (4 connections) — `server/services/combat_turn_processor.py`
- **._npc_id_in_active_npcs()** (4 connections) — `server/services/combat_turn_processor.py`
- **._resolve_npc_participant_to_string_id()** (4 connections) — `server/services/combat_turn_processor.py`
- *... and 23 more nodes in this community*

## Relationships

- [[Combat Service Bundle]] (20 shared connections)
- [[Combat Taunt Tests]] (8 shared connections)
- [[Combat Command Handler]] (1 shared connections)
- [[NPC Admin API]] (1 shared connections)
- [[NPC Occupant Verification]] (1 shared connections)

## Source Files

- `server/services/combat_turn_processor.py`

## Audit Trail

- EXTRACTED: 212 (90%)
- INFERRED: 23 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
