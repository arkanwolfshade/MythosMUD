# CombatParticipant

> God node · 167 connections · `server/models/combat.py`

**Community:** [CombatParticipant](CombatParticipant.md)

## Connections by Relation

### calls
- test_run_handle_taunt_success() `EXTRACTED`
- test_process_npc_turn_calls_process_attack_when_target_resolved() `EXTRACTED`
- test_combat_instance_queue_action() `EXTRACTED`
- test_resolve_npc_target_broadcasts_when_aggro_switches() `EXTRACTED`
- test_resolve_npc_target_uses_aggro_current_target() `EXTRACTED`
- test_execute_round_with_participants() `EXTRACTED`
- test_process_npc_turn_no_target() `EXTRACTED`
- test_process_npc_turn_npc_dead() `EXTRACTED`
- test_process_player_turn_casting_spell() `EXTRACTED`
- test_process_player_turn_no_target() `EXTRACTED`
- test_process_player_turn_player_unconscious() `EXTRACTED`
- test_combat_instance_get_alive_participants() `EXTRACTED`
- test_combat_instance_get_alive_participants_empty() `EXTRACTED`
- test_combat_instance_get_current_turn_participant_with_valid_turn() `EXTRACTED`
- test_combat_instance_get_participants_by_initiative() `EXTRACTED`
- test_combat_instance_is_combat_over_when_active() `EXTRACTED`
- mock_target_npc() `EXTRACTED`
- mock_target_player() `EXTRACTED`
- test_select_npc_target_prefers_mortally_wounded_player_over_skipping() `EXTRACTED`
- test_is_npc_still_in_world_false_when_npc_removed_from_active_npcs() `EXTRACTED`

### contains
- models/combat.py `EXTRACTED`

### imports
- combat_service.py `EXTRACTED`
- test_combat.py `EXTRACTED`
- [combat_turn_participant_actions.py](combat_turn_participant_actions.py.md) `EXTRACTED`
- [test_combat_attack_handler.py](test_combat_attack_handler.py.md) `EXTRACTED`
- test_combat_turn_processor.py `EXTRACTED`
- [combat_taunt.py](combat_taunt.py.md) `EXTRACTED`
- combat_service_npc.py `EXTRACTED`
- test_aggro_threat.py `EXTRACTED`
- aggro_threat.py `EXTRACTED`
- [test_flee_command.py](test_flee_command.py.md) `EXTRACTED`
- [test_combat_flee_helpers.py](test_combat_flee_helpers.py.md) `EXTRACTED`
- test_damage_grace_period.py `EXTRACTED`
- combat_service_attack.py `EXTRACTED`
- [combat_flee_handler.py](combat_flee_handler.py.md) `EXTRACTED`
- combat_death_handler.py `EXTRACTED`
- test_combat_taunt.py `EXTRACTED`
- combat_turn_processor.py `EXTRACTED`
- [test_combat_service.py](test_combat_service.py.md) `EXTRACTED`
- combat_attack_handler.py `EXTRACTED`
- combat_event_handler.py `EXTRACTED`

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
- _make_participant() `EXTRACTED`
- _validate_taunt_context() `EXTRACTED`
- _weapon_damage_from_equipped_player() `EXTRACTED`
- ._execute_spell_action() `EXTRACTED`
- _resolve_npc_target() `EXTRACTED`
- _make_participant() `EXTRACTED`
- ._execute_queued_action() `EXTRACTED`
- _make_participant() `EXTRACTED`
- _resolve_taunt_combat_and_participant() `EXTRACTED`
- _apply_taunt_and_maybe_broadcast() `EXTRACTED`
- ._apply_damage() `EXTRACTED`
- ._create_corpse_on_death() `EXTRACTED`
- ._publish_attack_events() `EXTRACTED`
- finalize_attack_result() `EXTRACTED`
- process_npc_turn() `EXTRACTED`
- process_player_turn() `EXTRACTED`
- _make_participant() `EXTRACTED`

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*