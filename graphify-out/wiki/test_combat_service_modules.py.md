# test_combat_service_modules.py

> 85 nodes

## Key Concepts

- **test_combat_service_modules.py** (63 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **asyncio** (37 connections)
- **_dp_sync()** (17 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **CombatDPSync** (13 connections) — `server/services/combat_hp_sync.py`
- **_combat_instance()** (13 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **_participant()** (10 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **handle_combat_completion()** (9 connections) — `server/services/combat_service_attack.py`
- **_attack_participant()** (8 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **._persist_player_dp_sync()** (7 connections) — `server/services/combat_hp_sync.py`
- **end_combat()** (7 connections) — `server/services/combat_service_end.py`
- **test_finalize_attack_result_and_process_attack()** (6 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **test_register_combat_delegates_to_service()** (6 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **._get_persistence()** (5 connections) — `server/services/combat_hp_sync.py`
- **._update_and_save_player_dp()** (5 connections) — `server/services/combat_hp_sync.py`
- **test_apply_damage_and_check_involuntary_flee()** (5 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **test_apply_target_rest_cancels_rest()** (5 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **test_apply_target_rest_grace_raises_on_grace_period()** (5 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **test_check_attacker_grace_period_raises()** (5 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **test_check_target_rest_skips_non_player()** (5 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **test_end_combat_full_flow()** (5 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **test_handle_combat_completion_end_error_swallowed()** (5 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **test_publish_combat_started_event_handles_errors()** (5 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **test_publish_combat_started_event_success()** (5 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **test_validate_combat_can_start_ok()** (5 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **test_validate_combat_can_start_raises_when_in_combat()** (5 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- *... and 60 more nodes in this community*

## Relationships

- [CombatService](CombatService.md) (40 shared connections)
- [EventBus](EventBus.md) (8 shared connections)
- [get_logger](get_logger.md) (5 shared connections)
- [CombatInstance](CombatInstance.md) (5 shared connections)
- [CombatParticipant](CombatParticipant.md) (3 shared connections)
- [test_nats_message_handler.py](test_nats_message_handler.py.md) (2 shared connections)
- [NPCStartupService](NPCStartupService.md) (1 shared connections)
- [get_current_tick](get_current_tick.md) (1 shared connections)
- [test_aggro_threat.py](test_aggro_threat.py.md) (1 shared connections)
- [nats_exceptions.py](nats_exceptions.py.md) (1 shared connections)

## Source Files

- `server/services/combat_hp_sync.py`
- `server/services/combat_service_attack.py`
- `server/services/combat_service_end.py`
- `server/tests/unit/services/test_combat_service_modules.py`

## Audit Trail

- EXTRACTED: 233 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*