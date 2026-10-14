# CombatInstance

> God node · 271 connections · `server/models/combat.py`

**Community:** [CombatInstance](CombatInstance.md)

## Connections by Relation

### calls
- _combat() `EXTRACTED`
- _make_combat() `EXTRACTED`
- _make_combat_instance() `EXTRACTED`
- _combat() `EXTRACTED`
- _fight() `EXTRACTED`
- _combat_instance() `EXTRACTED`
- _fight() `EXTRACTED`
- _make_combat() `EXTRACTED`
- _fight() `EXTRACTED`
- test_get_combat_target_auto_selects_opponent() `EXTRACTED`
- _start_fight() `EXTRACTED`
- _fight() `EXTRACTED`
- test_flee_no_exits_returns_no_escape() `EXTRACTED`
- test_flee_roll_fails_returns_failure_and_uses_action() `EXTRACTED`
- test_flee_roll_succeeds_returns_success() `EXTRACTED`
- _combat() `EXTRACTED`
- test_run_handle_taunt_success_queues_the_taunt_as_the_rounds_action() `EXTRACTED`
- _fight() `EXTRACTED`
- test_execute_flee_failed_free_hits_one_opponent() `EXTRACTED`
- test_execute_flee_failed_free_hits_stops_on_combat_ended() `EXTRACTED`

### contains
- models/combat.py `EXTRACTED`

### imports
- combat_service.py `EXTRACTED`
- [test_combat_service_modules.py](test_combat_service_modules.py.md) `EXTRACTED`
- test_combat.py `EXTRACTED`
- combat_turn_participant_actions.py `EXTRACTED`
- test_combat_turn_processor.py `EXTRACTED`
- [test_utility_threat.py](test_utility_threat.py.md) `EXTRACTED`
- [test_combat_assist.py](test_combat_assist.py.md) `EXTRACTED`
- test_combat_flee_handler.py `EXTRACTED`
- [aggro_threat.py](aggro_threat.py.md) `EXTRACTED`
- [test_combat_service.py](test_combat_service.py.md) `EXTRACTED`
- [test_n_player_combat.py](test_n_player_combat.py.md) `EXTRACTED`
- test_combat_attack_handler.py `EXTRACTED`
- [combat_assist.py](combat_assist.py.md) `EXTRACTED`
- test_combat_protect.py `EXTRACTED`
- test_combat_protect_action.py `EXTRACTED`
- combat_flee_handler.py `EXTRACTED`
- test_combat_taunt_action.py `EXTRACTED`
- combat_service_start.py `EXTRACTED`
- test_aggro_threat.py `EXTRACTED`
- [test_combat_death_handler.py](test_combat_death_handler.py.md) `EXTRACTED`

### method
- .active_guard() `EXTRACTED`
- .get_alive_participants() `EXTRACTED`
- .set_guard() `EXTRACTED`
- .living_tracked_target() `EXTRACTED`
- .is_guarding() `EXTRACTED`
- .get_participants_by_initiative() `EXTRACTED`
- .get_current_turn_participant() `EXTRACTED`
- .is_combat_over() `EXTRACTED`
- .queue_action() `EXTRACTED`
- .get_queued_actions() `EXTRACTED`
- .clear_queued_actions() `EXTRACTED`
- .advance_turn() `EXTRACTED`
- .update_activity() `EXTRACTED`

### rationale_for
- Represents an active combat instance. `EXTRACTED`

### references
- add_damage_threat() `EXTRACTED`
- _assist() `EXTRACTED`
- update_aggro() `EXTRACTED`
- _protect() `EXTRACTED`
- get_or_create_hate_list() `EXTRACTED`
- resolve_protect_action() `EXTRACTED`
- resolve_taunt_action() `EXTRACTED`
- execute_voluntary_flee() `EXTRACTED`
- .create_combat_instance() `EXTRACTED`
- intercept_for_guard() `EXTRACTED`
- add_utility_threat() `EXTRACTED`
- _resolve_flee_preconditions() `EXTRACTED`
- process_player_turn() `EXTRACTED`
- add_heal_threat() `EXTRACTED`
- apply_taunt() `EXTRACTED`
- _hate() `EXTRACTED`
- join_existing_combat() `EXTRACTED`
- resolve_npc_participant_id_in_combat() `EXTRACTED`
- _validate_flee_combat_and_room() `EXTRACTED`
- _validate_taunt_context() `EXTRACTED`

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*