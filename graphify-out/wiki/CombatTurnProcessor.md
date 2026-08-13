# CombatTurnProcessor

> 75 nodes

## Key Concepts

- **CombatTurnProcessor** (48 connections) — `server/services/combat_turn_processor.py`
- **test_combat_turn_processor.py** (36 connections) — `server/tests/unit/services/test_combat_turn_processor.py`
- **asyncio** (17 connections)
- **._execute_round()** (7 connections) — `server/services/combat_turn_processor.py`
- **test_process_player_turn_fallback_to_basic_unarmed_damage_when_no_player_from_persistence()** (7 connections) — `server/tests/unit/services/test_combat_turn_processor.py`
- **._is_npc_still_in_world()** (6 connections) — `server/services/combat_turn_processor.py`
- **_stale_queued_attack_rows()** (6 connections) — `server/tests/unit/services/test_combat_turn_processor.py`
- **test_process_player_turn_fallback_to_basic_unarmed_damage_when_no_app()** (6 connections) — `server/tests/unit/services/test_combat_turn_processor.py`
- **_unarmed_fallback_player_target_pair()** (6 connections) — `server/tests/unit/services/test_combat_turn_processor.py`
- **.process_game_tick()** (5 connections) — `server/services/combat_turn_processor.py`
- **test_execute_round_stale_queued_attack_uses_default_action()** (5 connections) — `server/tests/unit/services/test_combat_turn_processor.py`
- **test_execute_round_with_participants()** (5 connections) — `server/tests/unit/services/test_combat_turn_processor.py`
- **test_process_npc_turn_no_target()** (5 connections) — `server/tests/unit/services/test_combat_turn_processor.py`
- **test_process_npc_turn_npc_dead()** (5 connections) — `server/tests/unit/services/test_combat_turn_processor.py`
- **test_process_player_turn_casting_spell()** (5 connections) — `server/tests/unit/services/test_combat_turn_processor.py`
- **test_process_player_turn_no_target()** (5 connections) — `server/tests/unit/services/test_combat_turn_processor.py`
- **test_process_player_turn_player_unconscious()** (5 connections) — `server/tests/unit/services/test_combat_turn_processor.py`
- **._load_round_actions()** (4 connections) — `server/services/combat_turn_processor.py`
- **._npc_id_in_active_npcs()** (4 connections) — `server/services/combat_turn_processor.py`
- **._resolve_npc_participant_to_string_id()** (4 connections) — `server/services/combat_turn_processor.py`
- **combat_turn_processor()** (4 connections) — `server/tests/unit/services/test_combat_turn_processor.py`
- **test_execute_round_no_participants()** (4 connections) — `server/tests/unit/services/test_combat_turn_processor.py`
- **test_is_npc_still_in_world_false_when_npc_removed_from_active_npcs()** (4 connections) — `server/tests/unit/services/test_combat_turn_processor.py`
- **test_is_npc_still_in_world_true_for_player()** (4 connections) — `server/tests/unit/services/test_combat_turn_processor.py`
- **test_process_game_tick_combat_auto_progression_disabled()** (4 connections) — `server/tests/unit/services/test_combat_turn_processor.py`
- *... and 50 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (43 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (1 shared connections)

## Source Files

- `server/services/combat_turn_processor.py`
- `server/tests/unit/services/test_combat_turn_processor.py`

## Audit Trail

- EXTRACTED: 168 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*