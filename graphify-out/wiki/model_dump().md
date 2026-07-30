# .model dump()

> 50 nodes

## Key Concepts

- **combat_turn_participant_actions.py** (46 connections) — `server/services/combat_turn_participant_actions.py`
- **_weapon_damage_from_equipped_player()** (11 connections) — `server/services/combat_turn_participant_actions.py`
- **_resolve_npc_target()** (11 connections) — `server/services/combat_turn_participant_actions.py`
- **process_npc_turn()** (10 connections) — `server/services/combat_turn_participant_actions.py`
- **process_player_turn()** (10 connections) — `server/services/combat_turn_participant_actions.py`
- **resolve_player_attack_damage()** (9 connections) — `server/services/combat_turn_participant_actions.py`
- **_get_combat_container_services()** (8 connections) — `server/services/combat_turn_participant_actions.py`
- **_select_npc_target()** (7 connections) — `server/services/combat_turn_participant_actions.py`
- **_execute_player_attack()** (7 connections) — `server/services/combat_turn_participant_actions.py`
- **_execute_npc_attack()** (6 connections) — `server/services/combat_turn_participant_actions.py`
- **test_process_npc_turn_calls_process_attack_when_target_resolved()** (6 connections) — `server/tests/unit/services/test_combat_turn_participant_actions.py`
- **_get_target_stats_for_damage()** (5 connections) — `server/services/combat_turn_participant_actions.py`
- **_apply_physical_strength_bonus()** (5 connections) — `server/services/combat_turn_participant_actions.py`
- **_should_continue_npc_turn()** (5 connections) — `server/services/combat_turn_participant_actions.py`
- **_should_continue_player_turn()** (5 connections) — `server/services/combat_turn_participant_actions.py`
- **_select_player_target()** (5 connections) — `server/services/combat_turn_participant_actions.py`
- **_should_skip_for_casting()** (5 connections) — `server/services/combat_turn_participant_actions.py`
- **test_select_npc_target_prefers_mortally_wounded_player_over_skipping()** (5 connections) — `server/tests/unit/services/test_combat_turn_participant_actions.py`
- **test_resolve_npc_target_uses_aggro_current_target()** (5 connections) — `server/tests/unit/services/test_combat_turn_participant_actions.py`
- **test_resolve_npc_target_broadcasts_when_aggro_switches()** (5 connections) — `server/tests/unit/services/test_combat_turn_participant_actions.py`
- **_strength_modifier_from_attacker_stats()** (4 connections) — `server/services/combat_turn_participant_actions.py`
- **UUID** (3 connections)
- **_attacker_stats_dict_from_full_player()** (3 connections) — `server/services/combat_turn_participant_actions.py`
- **test_strength_modifier_from_attacker_stats_defaults()** (3 connections) — `server/tests/unit/services/test_combat_turn_participant_actions.py`
- **test_apply_physical_strength_bonus_adds_for_physical_only()** (3 connections) — `server/tests/unit/services/test_combat_turn_participant_actions.py`
- *... and 25 more nodes in this community*

## Relationships

- [test combat attack handler](test_combat_attack_handler.md) (18 shared connections)
- [Any](Any.md) (14 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (12 shared connections)
- [. initialize handlers()](_initialize_handlers%28%29.md) (8 shared connections)
- [emit close container event()](emit_close_container_event%28%29.md) (7 shared connections)
- [chat nats publisher](chat_nats_publisher.md) (6 shared connections)
- [close db()](close_db%28%29.md) (5 shared connections)
- [TerminalButtonProps](TerminalButtonProps.md) (3 shared connections)
- [process dead players()](process_dead_players%28%29.md) (3 shared connections)
- [. init ()](_init_%28%29.md) (3 shared connections)
- [test command parser](test_command_parser.md) (3 shared connections)
- [append unique valid occupant()](append_unique_valid_occupant%28%29.md) (2 shared connections)

## Source Files

- `server/services/combat_turn_participant_actions.py`
- `server/tests/unit/services/test_combat_turn_participant_actions.py`

## Audit Trail

- EXTRACTED: 207 (95%)
- INFERRED: 10 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*