# CombatInstance

> God node · 174 connections · `server/models/combat.py`

**Community:** [CombatInstance](CombatInstance.md)

## Connections by Relation

### calls
- test_get_combat_target_auto_selects_opponent() `EXTRACTED`
- test_flee_no_exits_returns_no_escape() `EXTRACTED`
- test_flee_roll_fails_returns_failure_and_uses_action() `EXTRACTED`
- test_flee_roll_succeeds_returns_success() `EXTRACTED`
- test_run_handle_taunt_success() `EXTRACTED`
- test_validate_flee_combat_and_room_success() `EXTRACTED`
- test_execute_voluntary_flee_free_hits_error_logged() `EXTRACTED`
- test_execute_voluntary_flee_missing_participant_returns_false() `EXTRACTED`
- test_execute_voluntary_flee_move_fails_returns_false() `EXTRACTED`
- test_execute_voluntary_flee_no_exits_returns_false() `EXTRACTED`
- test_execute_voluntary_flee_no_room_returns_false() `EXTRACTED`
- test_execute_voluntary_flee_roll_fail_consumes_action() `EXTRACTED`
- test_execute_voluntary_flee_success_moves_player() `EXTRACTED`
- test_finalize_attack_result_and_process_attack() `EXTRACTED`
- test_validate_flee_combat_and_room_no_movement_service() `EXTRACTED`
- test_combat_instance_queue_action() `EXTRACTED`
- test_try_voluntary_flee_roll_dead_opponent_not_counted() `EXTRACTED`
- test_try_voluntary_flee_roll_opponents_reduce_chance() `EXTRACTED`
- test_try_voluntary_flee_roll_roll_above_chance_fails() `EXTRACTED`
- test_try_voluntary_flee_roll_roll_below_chance_succeeds() `EXTRACTED`

### contains
- models/combat.py `EXTRACTED`

### imports
- combat_service.py `EXTRACTED`
- [test_combat_service_modules.py](test_combat_service_modules.py.md) `EXTRACTED`
- [test_combat.py](test_combat.py.md) `EXTRACTED`
- test_combat_turn_processor.py `EXTRACTED`
- combat_turn_participant_actions.py `EXTRACTED`
- [test_combat_attack_handler.py](test_combat_attack_handler.py.md) `EXTRACTED`
- [test_combat_service.py](test_combat_service.py.md) `EXTRACTED`
- test_combat_flee_handler.py `EXTRACTED`
- combat_taunt.py `EXTRACTED`
- [combat_service_npc.py](combat_service_npc.py.md) `EXTRACTED`
- [test_combat_death_handler.py](test_combat_death_handler.py.md) `EXTRACTED`
- test_combat_service_npc_helpers.py `EXTRACTED`
- [test_flee_command.py](test_flee_command.py.md) `EXTRACTED`
- test_spell_targeting.py `EXTRACTED`
- [test_aggro_threat.py](test_aggro_threat.py.md) `EXTRACTED`
- aggro_threat.py `EXTRACTED`
- combat_service_attack.py `EXTRACTED`
- combat_service_start.py `EXTRACTED`
- [test_combat_flee_helpers.py](test_combat_flee_helpers.py.md) `EXTRACTED`
- game_tick_protocols.py `EXTRACTED`

### method
- .get_alive_participants() `EXTRACTED`
- .get_participants_by_initiative() `EXTRACTED`
- .get_current_turn_participant() `EXTRACTED`
- .queue_action() `EXTRACTED`
- .get_queued_actions() `EXTRACTED`
- .clear_queued_actions() `EXTRACTED`
- .advance_turn() `EXTRACTED`
- .is_combat_over() `EXTRACTED`
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
- _combat_instance() `EXTRACTED`
- _validate_flee_combat_and_room() `EXTRACTED`
- _validate_taunt_context() `EXTRACTED`
- apply_taunt() `EXTRACTED`
- ._execute_spell_action() `EXTRACTED`
- try_voluntary_flee_roll() `EXTRACTED`
- find_participant_uuid_by_string_id() `EXTRACTED`
- resolve_npc_participant_id_in_combat() `EXTRACTED`
- _resolve_npc_target() `EXTRACTED`
- finalize_attack_result() `EXTRACTED`
- handle_combat_completion() `EXTRACTED`

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*