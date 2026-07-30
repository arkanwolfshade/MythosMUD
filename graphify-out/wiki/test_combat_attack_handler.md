# test combat attack handler

> 96 nodes

## Key Concepts

- **CombatTurnProcessor** (48 connections) — `server/services/combat_turn_processor.py`
- **test_combat_turn_processor.py** (36 connections) — `server/tests/unit/services/test_combat_turn_processor.py`
- **CombatAction** (21 connections) — `server/models/combat.py`
- **._execute_spell_action()** (11 connections) — `server/services/combat_turn_processor.py`
- **._execute_queued_action()** (10 connections) — `server/services/combat_turn_processor.py`
- **._get_player_and_room_for_spell()** (8 connections) — `server/services/combat_turn_processor.py`
- **._execute_round()** (7 connections) — `server/services/combat_turn_processor.py`
- **._build_spell_target()** (7 connections) — `server/services/combat_turn_processor.py`
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
- **test_process_player_turn_fallback_to_basic_unarmed_damage_when_no_app()** (5 connections) — `server/tests/unit/services/test_combat_turn_processor.py`
- **._resolve_npc_participant_to_string_id()** (4 connections) — `server/services/combat_turn_processor.py`
- **._npc_id_in_active_npcs()** (4 connections) — `server/services/combat_turn_processor.py`
- **._load_round_actions()** (4 connections) — `server/services/combat_turn_processor.py`
- **._log_unknown_action()** (4 connections) — `server/services/combat_turn_processor.py`
- **test_process_game_tick_inactive_combat()** (4 connections) — `server/tests/unit/services/test_combat_turn_processor.py`
- *... and 71 more nodes in this community*

## Relationships

- [close db()](close_db%28%29.md) (53 shared connections)
- [.validate target()](validate_target%28%29.md) (4 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (2 shared connections)
- [. initialize handlers()](_initialize_handlers%28%29.md) (1 shared connections)
- [NATSMessageSubscriptionMixin](NATSMessageSubscriptionMixin.md) (1 shared connections)
- [get current tick()](get_current_tick%28%29.md) (1 shared connections)
- [. init ()](_init_%28%29.md) (1 shared connections)
- [CombatService](CombatService.md) (1 shared connections)

## Source Files

- `server/models/combat.py`
- `server/services/combat_turn_processor.py`
- `server/tests/unit/services/test_combat_turn_processor.py`

## Audit Trail

- EXTRACTED: 357 (99%)
- INFERRED: 5 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*