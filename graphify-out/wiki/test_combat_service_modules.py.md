# test_combat_service_modules.py

> 92 nodes

## Key Concepts

- **test_combat_service_modules.py** (64 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **asyncio** (36 connections)
- **_combat_instance()** (14 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **_dp_sync()** (14 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **CombatDPSync** (12 connections) — `server/services/combat_hp_sync.py`
- **combat_service_end.py** (12 connections) — `server/services/combat_service_end.py`
- **handle_combat_completion()** (10 connections) — `server/services/combat_service_attack.py`
- **_attack_participant()** (10 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **_participant()** (10 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **._persist_player_dp_sync()** (7 connections) — `server/services/combat_hp_sync.py`
- **end_combat()** (7 connections) — `server/services/combat_service_end.py`
- **clear_aggro_for_combat()** (6 connections) — `server/services/aggro_threat.py`
- **test_apply_damage_and_check_involuntary_flee_suppresses_non_damaging_phantom()** (6 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **test_finalize_attack_result_and_process_attack()** (6 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **test_finalize_attack_result_phantom_dissipation()** (6 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **test_register_combat_delegates_to_service()** (6 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **._get_persistence()** (5 connections) — `server/services/combat_hp_sync.py`
- **._update_and_save_player_dp()** (5 connections) — `server/services/combat_hp_sync.py`
- **test_apply_damage_and_check_involuntary_flee()** (5 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **test_apply_target_rest_cancels_rest()** (5 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **test_apply_target_rest_grace_raises_on_grace_period()** (5 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **test_check_attacker_grace_period_raises()** (5 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **test_check_target_rest_skips_non_player()** (5 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **test_combat_dp_sync_persist_background_persistence_failure_sends_correction()** (5 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **test_end_combat_full_flow()** (5 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- *... and 67 more nodes in this community*

## Relationships

- [CombatService](CombatService.md) (27 shared connections)
- [CombatParticipant](CombatParticipant.md) (10 shared connections)
- [event_types.py](event_types.py.md) (9 shared connections)
- [CombatInstance](CombatInstance.md) (7 shared connections)
- [test_combat_event_publisher.py](test_combat_event_publisher.py.md) (6 shared connections)
- [get_logger](get_logger.md) (6 shared connections)
- [test_aggro_threat.py](test_aggro_threat.py.md) (3 shared connections)
- [NATSError](NATSError.md) (3 shared connections)
- [CombatParticipantData](CombatParticipantData.md) (3 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (1 shared connections)
- [magic_service.py](magic_service.py.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/services/aggro_threat.py`
- `server/services/combat_hp_sync.py`
- `server/services/combat_service_attack.py`
- `server/services/combat_service_end.py`
- `server/tests/unit/services/test_combat_service_modules.py`

## Audit Trail

- EXTRACTED: 248 (97%)
- INFERRED: 7 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*