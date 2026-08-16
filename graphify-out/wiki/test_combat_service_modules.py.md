# test_combat_service_modules.py

> 73 nodes

## Key Concepts

- **test_combat_service_modules.py** (65 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **asyncio** (37 connections)
- **_dp_sync()** (17 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **_combat_instance()** (13 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **combat_service_end.py** (12 connections) — `server/services/combat_service_end.py`
- **handle_combat_completion()** (10 connections) — `server/services/combat_service_attack.py`
- **_participant()** (10 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **_attack_participant()** (8 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **end_combat()** (7 connections) — `server/services/combat_service_end.py`
- **clear_aggro_for_combat()** (6 connections) — `server/services/aggro_threat.py`
- **test_finalize_attack_result_and_process_attack()** (6 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **test_register_combat_delegates_to_service()** (6 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **test_apply_damage_and_check_involuntary_flee()** (5 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **test_apply_target_rest_cancels_rest()** (5 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **test_apply_target_rest_grace_raises_on_grace_period()** (5 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **test_check_attacker_grace_period_raises()** (5 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **test_check_target_rest_skips_non_player()** (5 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **test_combat_dp_sync_persist_background_persistence_failure_sends_correction()** (5 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **test_end_combat_full_flow()** (5 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **test_handle_combat_completion_end_error_swallowed()** (5 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **test_publish_combat_started_event_handles_errors()** (5 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **test_publish_combat_started_event_success()** (5 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **test_validate_combat_can_start_ok()** (5 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **test_validate_combat_can_start_raises_when_in_combat()** (5 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **test_validate_melee_location_paths()** (5 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- *... and 48 more nodes in this community*

## Relationships

- [CombatInstance](CombatInstance.md) (51 shared connections)
- [get_logger](get_logger.md) (5 shared connections)
- [test_aggro_threat.py](test_aggro_threat.py.md) (3 shared connections)
- [CombatParticipant](CombatParticipant.md) (3 shared connections)
- [DatabaseError](DatabaseError.md) (3 shared connections)
- [get_current_tick](get_current_tick.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)
- [server/exceptions.py](server-exceptions.py.md) (1 shared connections)

## Source Files

- `server/services/aggro_threat.py`
- `server/services/combat_service_attack.py`
- `server/services/combat_service_end.py`
- `server/tests/unit/services/test_combat_service_modules.py`

## Audit Trail

- EXTRACTED: 211 (96%)
- INFERRED: 9 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*