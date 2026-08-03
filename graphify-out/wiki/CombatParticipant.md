# CombatParticipant

> God node · 193 connections · `server/models/combat.py`

**Community:** [Item Instances](Item_Instances.md)

## Connections by Relation

### calls
- _combat_instance() `EXTRACTED`
- test_run_handle_taunt_success() `EXTRACTED`
- test_process_npc_turn_calls_process_attack_when_target_resolved() `EXTRACTED`
- test_get_combat_target_auto_selects_opponent() `EXTRACTED`
- test_combat_instance_queue_action() `EXTRACTED`
- test_resolve_npc_target_broadcasts_when_aggro_switches() `EXTRACTED`
- test_resolve_npc_target_uses_aggro_current_target() `EXTRACTED`
- test_select_npc_target_prefers_mortally_wounded_player_over_skipping() `EXTRACTED`
- test_execute_participant_action_valid_queued_attack() `EXTRACTED`
- test_execute_queued_attack_action() `EXTRACTED`
- test_execute_queued_spell_without_magic_service() `EXTRACTED`
- test_combat_instance_get_alive_participants() `EXTRACTED`
- test_combat_instance_get_alive_participants_empty() `EXTRACTED`
- test_combat_instance_get_current_turn_participant_with_valid_turn() `EXTRACTED`
- test_combat_instance_get_participants_by_initiative() `EXTRACTED`
- test_combat_instance_is_combat_over_when_active() `EXTRACTED`
- test_resolve_npc_participant_id_in_combat_by_uuid() `EXTRACTED`
- test_sync_npc_participant_dp_after_spell_damage() `EXTRACTED`
- test_build_spell_target_npc() `EXTRACTED`
- test_execute_queued_flee_skip() `EXTRACTED`

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
- test_flee_command.py `EXTRACTED`
- test_spell_targeting.py `EXTRACTED`
- combat_service_attack.py `EXTRACTED`
- test_combat_flee_helpers.py `EXTRACTED`
- test_damage_grace_period.py `EXTRACTED`
- spell_targeting.py `EXTRACTED`

### indirect_call
- mock_attacker() `INFERRED`

### method
- .is_dead() `EXTRACTED`
- .is_alive() `EXTRACTED`
- .apply_damage() `EXTRACTED`
- .can_act_in_combat() `EXTRACTED`
- .is_mortally_wounded() `EXTRACTED`

### rationale_for
- Represents a participant in combat. `EXTRACTED`

### references
- update_aggro() `EXTRACTED`
- add_damage_threat() `EXTRACTED`
- _make_participant() `EXTRACTED`
- add_heal_threat() `EXTRACTED`
- _validate_taunt_context() `EXTRACTED`
- _make_participant() `EXTRACTED`
- finalize_attack_result() `EXTRACTED`
- ._execute_spell_action() `EXTRACTED`
- _make_participant() `EXTRACTED`
- _check_involuntary_flee_with_session() `EXTRACTED`
- validate_melee_or_end_combat() `EXTRACTED`
- get_npc_participant_current_room() `EXTRACTED`
- _resolve_npc_target() `EXTRACTED`
- _weapon_damage_from_equipped_player() `EXTRACTED`
- validate_melee_location() `EXTRACTED`
- get_participant_current_room() `EXTRACTED`
- process_npc_turn() `EXTRACTED`
- process_player_turn() `EXTRACTED`
- ._execute_queued_action() `EXTRACTED`
- _participant() `EXTRACTED`

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*