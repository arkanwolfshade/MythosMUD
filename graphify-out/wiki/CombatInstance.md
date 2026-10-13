# CombatInstance

> God node · 271 connections · `server/models/combat.py`

**Community:** [Combat Instance Turns](Combat_Instance_Turns.md)

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
- _fight() `EXTRACTED`
- test_execute_flee_failed_free_hits_one_opponent() `EXTRACTED`
- test_execute_flee_failed_free_hits_stops_on_combat_ended() `EXTRACTED`
- test_execute_flee_failed_free_hits_stops_on_target_died() `EXTRACTED`

### contains
- models/combat.py `EXTRACTED`

### imports
- combat_service.py `EXTRACTED`
- test_combat_service_modules.py `EXTRACTED`
- test_combat.py `EXTRACTED`
- test_combat_turn_processor.py `EXTRACTED`
- combat_turn_participant_actions.py `EXTRACTED`
- test_combat_flee_handler.py `EXTRACTED`
- test_combat_assist.py `EXTRACTED`
- test_combat_service.py `EXTRACTED`
- test_n_player_combat.py `EXTRACTED`
- test_utility_threat.py `EXTRACTED`
- aggro_threat.py `EXTRACTED`
- test_combat_attack_handler.py `EXTRACTED`
- test_combat_protect_action.py `EXTRACTED`
- test_combat_protect.py `EXTRACTED`
- combat_assist.py `EXTRACTED`
- combat_flee_handler.py `EXTRACTED`
- test_aggro_threat.py `EXTRACTED`
- test_combat_death_handler.py `EXTRACTED`
- test_combat_taunt_action.py `EXTRACTED`
- combat_service_npc.py `EXTRACTED`

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
- execute_voluntary_flee() `EXTRACTED`
- resolve_taunt_action() `EXTRACTED`
- .create_combat_instance() `EXTRACTED`
- intercept_for_guard() `EXTRACTED`
- add_utility_threat() `EXTRACTED`
- add_heal_threat() `EXTRACTED`
- apply_taunt() `EXTRACTED`
- process_player_turn() `EXTRACTED`
- _hate() `EXTRACTED`
- join_existing_combat() `EXTRACTED`
- _resolve_flee_preconditions() `EXTRACTED`
- resolve_npc_participant_id_in_combat() `EXTRACTED`
- _validate_flee_combat_and_room() `EXTRACTED`
- finalize_attack_result() `EXTRACTED`

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*