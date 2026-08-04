# CombatInstance

> God node · 186 connections · `server/models/combat.py`

**Community:** [models npc rationale](models_npc_rationale.md)

## Connections by Relation

### calls
- test_flee_no_exits_returns_no_escape() `EXTRACTED`
- test_flee_roll_fails_returns_failure_and_uses_action() `EXTRACTED`
- test_flee_roll_succeeds_returns_success() `EXTRACTED`
- test_run_handle_taunt_success() `EXTRACTED`
- test_validate_flee_combat_and_room_success() `EXTRACTED`
- test_get_combat_target_auto_selects_opponent() `EXTRACTED`
- test_combat_instance_queue_action() `EXTRACTED`
- test_execute_voluntary_flee_free_hits_error_logged() `EXTRACTED`
- test_execute_voluntary_flee_missing_participant_returns_false() `EXTRACTED`
- test_execute_voluntary_flee_move_fails_returns_false() `EXTRACTED`
- test_execute_voluntary_flee_no_exits_returns_false() `EXTRACTED`
- test_execute_voluntary_flee_no_room_returns_false() `EXTRACTED`
- test_execute_voluntary_flee_roll_fail_consumes_action() `EXTRACTED`
- test_execute_voluntary_flee_success_moves_player() `EXTRACTED`
- test_try_voluntary_flee_roll_dead_opponent_not_counted() `EXTRACTED`
- test_try_voluntary_flee_roll_opponents_reduce_chance() `EXTRACTED`
- test_try_voluntary_flee_roll_roll_above_chance_fails() `EXTRACTED`
- test_try_voluntary_flee_roll_roll_below_chance_succeeds() `EXTRACTED`
- test_try_voluntary_flee_roll_zero_exits_returns_false() `EXTRACTED`
- test_finalize_attack_result_and_process_attack() `EXTRACTED`

### contains
- combat.py `EXTRACTED`

### imports
- combat_service.py `EXTRACTED`
- test_combat_service_modules.py `EXTRACTED`
- test_combat.py `EXTRACTED`
- test_combat_turn_processor.py `EXTRACTED`
- combat_turn_participant_actions.py `EXTRACTED`
- test_combat_attack_handler.py `EXTRACTED`
- test_combat_service.py `EXTRACTED`
- test_combat_flee_handler.py `EXTRACTED`
- combat_taunt.py `EXTRACTED`
- combat_service_npc.py `EXTRACTED`
- test_combat_death_handler.py `EXTRACTED`
- test_combat_service_npc_helpers.py `EXTRACTED`
- test_aggro_threat.py `EXTRACTED`
- aggro_threat.py `EXTRACTED`
- combat_service_start.py `EXTRACTED`
- test_flee_command.py `EXTRACTED`
- test_spell_targeting.py `EXTRACTED`
- combat_service_attack.py `EXTRACTED`
- test_combat_flee_helpers.py `EXTRACTED`
- combat_flee.py `EXTRACTED`

### indirect_call
- test_process_npc_turn_calls_process_attack_when_target_resolved() `INFERRED`
- test_resolve_npc_target_broadcasts_when_aggro_switches() `INFERRED`
- test_resolve_npc_target_uses_aggro_current_target() `INFERRED`
- test_select_npc_target_prefers_mortally_wounded_player_over_skipping() `INFERRED`
- test_process_game_tick_combat_auto_progression_disabled() `INFERRED`
- test_process_game_tick_inactive_combat() `INFERRED`
- test_process_game_tick_tick_not_reached() `INFERRED`
- test_process_game_tick_triggers_execute_round() `INFERRED`
- mock_combat() `INFERRED`
- test_apply_damage_player_no_death_room_caps_damage() `INFERRED`
- test_apply_damage_player_no_death_room_zero_damage_when_at_zero() `INFERRED`
- mock_combat() `INFERRED`
- test_cleanup_stale_combats() `INFERRED`
- test_cleanup_stale_combats_no_end_combat_method() `INFERRED`
- test_cleanup_stale_combats_no_stale_combats() `INFERRED`
- combat() `INFERRED`

### method
- .get_alive_participants() `EXTRACTED`
- .get_participants_by_initiative() `EXTRACTED`
- .clear_queued_actions() `EXTRACTED`
- .get_current_turn_participant() `EXTRACTED`
- .get_queued_actions() `EXTRACTED`
- .is_combat_over() `EXTRACTED`
- .queue_action() `EXTRACTED`
- .advance_turn() `EXTRACTED`
- .update_activity() `EXTRACTED`

### rationale_for
- Represents an active combat instance. `EXTRACTED`

### references
- update_aggro() `EXTRACTED`
- _make_combat() `EXTRACTED`
- add_damage_threat() `EXTRACTED`
- execute_voluntary_flee() `EXTRACTED`
- get_or_create_hate_list() `EXTRACTED`
- .create_combat_instance() `EXTRACTED`
- _resolve_flee_preconditions() `EXTRACTED`
- _make_combat_instance() `EXTRACTED`
- add_heal_threat() `EXTRACTED`
- _validate_taunt_context() `EXTRACTED`
- _combat_instance() `EXTRACTED`
- _validate_flee_combat_and_room() `EXTRACTED`
- apply_taunt() `EXTRACTED`
- finalize_attack_result() `EXTRACTED`
- find_participant_uuid_by_string_id() `EXTRACTED`
- ._execute_spell_action() `EXTRACTED`
- try_voluntary_flee_roll() `EXTRACTED`
- handle_combat_completion() `EXTRACTED`
- validate_melee_or_end_combat() `EXTRACTED`
- resolve_npc_participant_id_in_combat() `EXTRACTED`

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*