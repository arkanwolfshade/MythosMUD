# CombatParticipant

> God node · 183 connections · `server/models/combat.py`

**Community:** [Combat Turn Processing](Combat_Turn_Processing.md)

## Connections by Relation

### calls
- _make_participant() `EXTRACTED`
- _make_participant() `EXTRACTED`
- _participant() `EXTRACTED`
- _make_participant() `EXTRACTED`
- test_get_combat_target_auto_selects_opponent() `EXTRACTED`
- _make_participant() `EXTRACTED`
- test_run_handle_taunt_success() `EXTRACTED`
- test_apply_taunt_and_maybe_broadcast_publishes_target_switch_to_nats() `EXTRACTED`
- _make_participant() `EXTRACTED`
- test_process_npc_turn_calls_process_attack_when_target_resolved() `EXTRACTED`
- _stale_queued_attack_rows() `EXTRACTED`
- test_execute_participant_action_valid_queued_attack() `EXTRACTED`
- test_execute_queued_attack_action() `EXTRACTED`
- test_execute_queued_spell_without_magic_service() `EXTRACTED`
- _unarmed_fallback_player_target_pair() `EXTRACTED`
- _build_participant() `EXTRACTED`
- test_combat_instance_queue_action() `EXTRACTED`
- test_resolve_npc_target_broadcasts_when_aggro_switches() `EXTRACTED`
- test_resolve_npc_target_uses_aggro_current_target() `EXTRACTED`
- test_execute_queued_flee_skip() `EXTRACTED`

### contains
- models/combat.py `EXTRACTED`

### imports
- combat_service.py `EXTRACTED`
- test_combat.py `EXTRACTED`
- test_combat_turn_processor.py `EXTRACTED`
- combat_turn_participant_actions.py `EXTRACTED`
- test_combat_service.py `EXTRACTED`
- combat_taunt.py `EXTRACTED`
- test_combat_flee_handler.py `EXTRACTED`
- combat_service_npc.py `EXTRACTED`
- test_combat_death_handler.py `EXTRACTED`
- test_combat_service_npc_helpers.py `EXTRACTED`
- test_flee_command.py `EXTRACTED`
- test_spell_targeting.py `EXTRACTED`
- test_aggro_threat.py `EXTRACTED`
- aggro_threat.py `EXTRACTED`
- combat_service_attack.py `EXTRACTED`
- test_combat_flee_helpers.py `EXTRACTED`
- test_damage_grace_period.py `EXTRACTED`
- spell_targeting.py `EXTRACTED`
- combat_death_handler.py `EXTRACTED`
- combat_flee_handler.py `EXTRACTED`

### method
- .is_alive() `EXTRACTED`
- .apply_damage() `EXTRACTED`
- .is_dead() `EXTRACTED`
- .is_mortally_wounded() `EXTRACTED`
- .can_act_in_combat() `EXTRACTED`

### rationale_for
- Represents a participant in combat. `EXTRACTED`

### references
- update_aggro() `EXTRACTED`
- add_damage_threat() `EXTRACTED`
- add_heal_threat() `EXTRACTED`
- _validate_taunt_context() `EXTRACTED`
- ._execute_spell_action() `EXTRACTED`
- _apply_taunt_and_maybe_broadcast() `EXTRACTED`
- _check_involuntary_flee_with_session() `EXTRACTED`
- _weapon_damage_from_equipped_player() `EXTRACTED`
- _resolve_npc_target() `EXTRACTED`
- process_npc_turn() `EXTRACTED`
- process_player_turn() `EXTRACTED`
- ._execute_queued_action() `EXTRACTED`
- _resolve_taunt_combat_and_participant() `EXTRACTED`
- ._create_corpse_on_death() `EXTRACTED`
- ._publish_attack_events() `EXTRACTED`
- check_involuntary_flee() `EXTRACTED`
- finalize_attack_result() `EXTRACTED`
- get_participant_current_room() `EXTRACTED`
- resolve_player_attack_damage() `EXTRACTED`
- ._handle_npc_death() `EXTRACTED`

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*