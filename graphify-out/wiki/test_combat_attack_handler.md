# test combat attack handler

> 210 nodes

## Key Concepts

- **CombatParticipant** (168 connections) — `server/models/combat.py`
- **test_combat.py** (60 connections) — `server/tests/unit/models/test_combat.py`
- **CombatTurnProcessor** (48 connections) — `server/services/combat_turn_processor.py`
- **test_combat_turn_processor.py** (36 connections) — `server/tests/unit/services/test_combat_turn_processor.py`
- **combat_service_attack.py** (26 connections) — `server/services/combat_service_attack.py`
- **CombatAction** (21 connections) — `server/models/combat.py`
- **finalize_attack_result()** (11 connections) — `server/services/combat_service_attack.py`
- **._execute_spell_action()** (11 connections) — `server/services/combat_turn_processor.py`
- **validate_melee_or_end_combat()** (10 connections) — `server/services/combat_service_attack.py`
- **._execute_queued_action()** (10 connections) — `server/services/combat_turn_processor.py`
- **validate_melee_location()** (9 connections) — `server/services/combat_service_attack.py`
- **process_attack()** (9 connections) — `server/services/combat_service_attack.py`
- **apply_damage_and_check_involuntary_flee()** (8 connections) — `server/services/combat_service_attack.py`
- **._get_player_and_room_for_spell()** (8 connections) — `server/services/combat_turn_processor.py`
- **._execute_participant_action()** (7 connections) — `server/services/combat_turn_processor.py`
- **._build_spell_target()** (7 connections) — `server/services/combat_turn_processor.py`
- **._execute_default_action()** (7 connections) — `server/services/combat_turn_processor.py`
- **_get_default_damage()** (6 connections) — `server/models/combat.py`
- **queue_combat_action()** (6 connections) — `server/services/combat_service_attack.py`
- **UUID** (6 connections)
- **._is_npc_still_in_world()** (6 connections) — `server/services/combat_turn_processor.py`
- **._execute_attack_action()** (6 connections) — `server/services/combat_turn_processor.py`
- **._get_spell_for_action()** (6 connections) — `server/services/combat_turn_processor.py`
- **._finalize_spell_execution()** (6 connections) — `server/services/combat_turn_processor.py`
- **_stale_queued_attack_rows()** (6 connections) — `server/tests/unit/services/test_combat_turn_processor.py`
- *... and 185 more nodes in this community*

## Relationships

- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (60 shared connections)
- [Any](Any.md) (51 shared connections)
- [. initialize handlers()](_initialize_handlers%28%29.md) (19 shared connections)
- [.model dump()](model_dump%28%29.md) (18 shared connections)
- [close db()](close_db%28%29.md) (13 shared connections)
- [get health service()](get_health_service%28%29.md) (8 shared connections)
- [test player event handlers room](test_player_event_handlers_room.md) (6 shared connections)
- [TerminalButtonProps](TerminalButtonProps.md) (3 shared connections)
- [process dead players()](process_dead_players%28%29.md) (2 shared connections)
- [.end combat()](end_combat%28%29.md) (2 shared connections)
- [test exploration service](test_exploration_service.md) (2 shared connections)
- [combat flee](combat_flee.md) (2 shared connections)

## Source Files

- `server/models/combat.py`
- `server/services/combat_service_attack.py`
- `server/services/combat_turn_processor.py`
- `server/tests/unit/models/test_combat.py`
- `server/tests/unit/services/test_combat_turn_processor.py`

## Audit Trail

- EXTRACTED: 883 (99%)
- INFERRED: 6 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*