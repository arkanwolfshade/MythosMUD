# player look commands

> 61 nodes

## Key Concepts

- **test_combat_service.py** (37 connections) — `server/tests/unit/services/test_combat_service.py`
- **_make_service()** (28 connections) — `server/tests/unit/services/test_combat_service.py`
- **CombatResult** (23 connections) — `server/models/combat.py`
- **_make_combat_instance()** (15 connections) — `server/tests/unit/services/test_combat_service.py`
- **_make_participant()** (12 connections) — `server/tests/unit/services/test_combat_service.py`
- **test_validate_melee_or_end_combat_ends_combat_on_invalid()** (6 connections) — `server/tests/unit/services/test_combat_service.py`
- **test_apply_damage_and_check_involuntary_flee_returns_early_result_on_flee()** (6 connections) — `server/tests/unit/services/test_combat_service.py`
- **test_finalize_attack_result_awards_xp_and_completes_combat()** (6 connections) — `server/tests/unit/services/test_combat_service.py`
- **test_process_attack_returns_melee_validation_early_result()** (6 connections) — `server/tests/unit/services/test_combat_service.py`
- **test_process_attack_happy_path_calls_helpers_and_returns_final_result()** (6 connections) — `server/tests/unit/services/test_combat_service.py`
- **.apply_damage_and_check_involuntary_flee()** (5 connections) — `server/services/combat_service.py`
- **test_validate_melee_or_end_combat_returns_none_on_valid()** (5 connections) — `server/tests/unit/services/test_combat_service.py`
- **test_apply_damage_and_check_involuntary_flee_no_flee_for_npc()** (5 connections) — `server/tests/unit/services/test_combat_service.py`
- **test_sync_npc_participant_dp_after_spell_damage()** (5 connections) — `server/tests/unit/services/test_combat_service.py`
- **test_register_combat_state_tracks_participants()** (5 connections) — `server/tests/unit/services/test_combat_service.py`
- **test_get_combat_returns_active_instance()** (4 connections) — `server/tests/unit/services/test_combat_service.py`
- **test_get_combat_by_participant_returns_active_combat()** (4 connections) — `server/tests/unit/services/test_combat_service.py`
- **test_cleanup_combat_tracking_and_connection_state()** (4 connections) — `server/tests/unit/services/test_combat_service.py`
- **test_start_combat_happy_path()** (4 connections) — `server/tests/unit/services/test_combat_service.py`
- **test_combat_service_property_getters_setters()** (3 connections) — `server/tests/unit/services/test_combat_service.py`
- **test_get_combat_id_for_participant()** (3 connections) — `server/tests/unit/services/test_combat_service.py`
- **test_is_npc_in_combat_sync()** (3 connections) — `server/tests/unit/services/test_combat_service.py`
- **test_get_npc_combat_integration_service_round_trip()** (3 connections) — `server/tests/unit/services/test_combat_service.py`
- **test_publish_npc_damage_event_delegates()** (3 connections) — `server/tests/unit/services/test_combat_service.py`
- **test_publish_npc_died_event_delegates()** (3 connections) — `server/tests/unit/services/test_combat_service.py`
- *... and 36 more nodes in this community*

## Relationships

- [npc database infrastructure](npc_database_infrastructure.md) (6 shared connections)
- [Item Instances](Item_Instances.md) (5 shared connections)
- [subject admin controller](subject_admin_controller.md) (5 shared connections)
- [models player rationale](models_player_rationale.md) (5 shared connections)
- [command factories exploration](command_factories_exploration.md) (3 shared connections)
- [Memory Task Runtime](Memory_Task_Runtime.md) (2 shared connections)
- [cleanup combat handler](cleanup_combat_handler.md) (2 shared connections)

## Source Files

- `server/models/combat.py`
- `server/services/combat_service.py`
- `server/tests/unit/services/test_combat_service.py`

## Audit Trail

- EXTRACTED: 248 (98%)
- INFERRED: 6 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*