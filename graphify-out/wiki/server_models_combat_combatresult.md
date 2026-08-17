# server models combat combatresult

> 62 nodes

## Key Concepts

- **test_combat_service.py** (38 connections) — `server/tests/unit/services/test_combat_service.py`
- **_make_service()** (28 connections) — `server/tests/unit/services/test_combat_service.py`
- **asyncio** (17 connections)
- **_make_combat_instance()** (15 connections) — `server/tests/unit/services/test_combat_service.py`
- **_make_participant()** (12 connections) — `server/tests/unit/services/test_combat_service.py`
- **CombatResult** (11 connections) — `server/models/combat.py`
- **test_process_attack_happy_path_calls_helpers_and_returns_final_result()** (7 connections) — `server/tests/unit/services/test_combat_service.py`
- **test_process_attack_returns_melee_validation_early_result()** (7 connections) — `server/tests/unit/services/test_combat_service.py`
- **test_apply_damage_and_check_involuntary_flee_no_flee_for_npc()** (6 connections) — `server/tests/unit/services/test_combat_service.py`
- **test_apply_damage_and_check_involuntary_flee_returns_early_result_on_flee()** (6 connections) — `server/tests/unit/services/test_combat_service.py`
- **test_finalize_attack_result_awards_xp_and_completes_combat()** (6 connections) — `server/tests/unit/services/test_combat_service.py`
- **test_register_combat_state_tracks_participants()** (6 connections) — `server/tests/unit/services/test_combat_service.py`
- **test_validate_melee_or_end_combat_ends_combat_on_invalid()** (6 connections) — `server/tests/unit/services/test_combat_service.py`
- **test_validate_melee_or_end_combat_returns_none_on_valid()** (6 connections) — `server/tests/unit/services/test_combat_service.py`
- **.apply_damage_and_check_involuntary_flee()** (5 connections) — `server/services/combat_service.py`
- **test_get_combat_by_participant_returns_active_combat()** (5 connections) — `server/tests/unit/services/test_combat_service.py`
- **test_start_combat_happy_path()** (5 connections) — `server/tests/unit/services/test_combat_service.py`
- **test_sync_npc_participant_dp_after_spell_damage()** (5 connections) — `server/tests/unit/services/test_combat_service.py`
- **test_broadcast_aggro_target_switches_delegates()** (4 connections) — `server/tests/unit/services/test_combat_service.py`
- **test_cleanup_combat_tracking_and_connection_state()** (4 connections) — `server/tests/unit/services/test_combat_service.py`
- **test_end_combat_if_npc_died()** (4 connections) — `server/tests/unit/services/test_combat_service.py`
- **test_end_combat_if_npc_died_not_in_combat()** (4 connections) — `server/tests/unit/services/test_combat_service.py`
- **test_get_combat_returns_active_instance()** (4 connections) — `server/tests/unit/services/test_combat_service.py`
- **test_notify_player_combat_ended()** (4 connections) — `server/tests/unit/services/test_combat_service.py`
- **test_process_game_tick_delegates()** (4 connections) — `server/tests/unit/services/test_combat_service.py`
- *... and 37 more nodes in this community*

## Relationships

- [server app game tick counter](server_app_game_tick_counter.md) (6 shared connections)
- [server container bundles combat combatbundle](server_container_bundles_combat_combatbundle.md) (6 shared connections)
- [server models combat combatinstance](server_models_combat_combatinstance.md) (3 shared connections)
- [server models combat combataction](server_models_combat_combataction.md) (3 shared connections)
- [server commands combat handler combatcommandhandler](server_commands_combat_handler_combatcommandhandler.md) (1 shared connections)
- [characterinfo](characterinfo.md) (1 shared connections)

## Source Files

- `server/models/combat.py`
- `server/services/combat_service.py`
- `server/tests/unit/services/test_combat_service.py`

## Audit Trail

- EXTRACTED: 146 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*