# test_combat_service.py

> 64 nodes

## Key Concepts

- **test_combat_service.py** (41 connections) — `server/tests/unit/services/test_combat_service.py`
- **_make_service()** (32 connections) — `server/tests/unit/services/test_combat_service.py`
- **asyncio** (21 connections)
- **_make_combat_instance()** (19 connections) — `server/tests/unit/services/test_combat_service.py`
- **_make_participant()** (15 connections) — `server/tests/unit/services/test_combat_service.py`
- **test_process_attack_happy_path_calls_helpers_and_returns_final_result()** (7 connections) — `server/tests/unit/services/test_combat_service.py`
- **test_process_attack_returns_melee_validation_early_result()** (7 connections) — `server/tests/unit/services/test_combat_service.py`
- **test_apply_damage_and_check_involuntary_flee_no_flee_for_npc()** (6 connections) — `server/tests/unit/services/test_combat_service.py`
- **test_apply_damage_and_check_involuntary_flee_returns_early_result_on_flee()** (6 connections) — `server/tests/unit/services/test_combat_service.py`
- **test_finalize_attack_result_awards_xp_and_completes_combat()** (6 connections) — `server/tests/unit/services/test_combat_service.py`
- **test_register_combat_state_files_npc_attacker_by_type()** (6 connections) — `server/tests/unit/services/test_combat_service.py`
- **test_register_combat_state_tracks_participants()** (6 connections) — `server/tests/unit/services/test_combat_service.py`
- **test_register_joined_participant_tracks_only_the_joiner()** (6 connections) — `server/tests/unit/services/test_combat_service.py`
- **test_validate_melee_or_end_combat_ends_combat_on_invalid()** (6 connections) — `server/tests/unit/services/test_combat_service.py`
- **test_validate_melee_or_end_combat_returns_none_on_valid()** (6 connections) — `server/tests/unit/services/test_combat_service.py`
- **test_get_combat_by_participant_returns_active_combat()** (5 connections) — `server/tests/unit/services/test_combat_service.py`
- **test_start_combat_happy_path()** (5 connections) — `server/tests/unit/services/test_combat_service.py`
- **test_sync_npc_participant_dp_after_spell_damage()** (5 connections) — `server/tests/unit/services/test_combat_service.py`
- **test_untrack_participant_clears_tracking_and_player_state()** (5 connections) — `server/tests/unit/services/test_combat_service.py`
- **test_broadcast_aggro_target_switches_delegates()** (4 connections) — `server/tests/unit/services/test_combat_service.py`
- **test_cleanup_combat_tracking_and_connection_state()** (4 connections) — `server/tests/unit/services/test_combat_service.py`
- **test_end_combat_if_npc_died()** (4 connections) — `server/tests/unit/services/test_combat_service.py`
- **test_end_combat_if_npc_died_not_in_combat()** (4 connections) — `server/tests/unit/services/test_combat_service.py`
- **test_get_combat_returns_active_instance()** (4 connections) — `server/tests/unit/services/test_combat_service.py`
- **test_join_and_remove_participant_delegate_to_their_modules()** (4 connections) — `server/tests/unit/services/test_combat_service.py`
- *... and 39 more nodes in this community*

## Relationships

- [CombatService](CombatService.md) (6 shared connections)
- [test_combat_service_modules.py](test_combat_service_modules.py.md) (3 shared connections)
- [CombatInstance](CombatInstance.md) (2 shared connections)
- [CombatParticipant](CombatParticipant.md) (2 shared connections)

## Source Files

- `server/tests/unit/services/test_combat_service.py`

## Audit Trail

- EXTRACTED: 155 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*