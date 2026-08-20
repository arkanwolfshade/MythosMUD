# test_combat_service_modules.py

> 95 nodes

## Key Concepts

- **test_combat_service_modules.py** (64 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **asyncio** (36 connections)
- **_combat_instance()** (14 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **_dp_sync()** (14 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **CombatDPSync** (12 connections) — `server/services/combat_hp_sync.py`
- **combat_service_end.py** (12 connections) — `server/services/combat_service_end.py`
- **_attack_participant()** (10 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **_participant()** (10 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **broadcast_aggro_target_switches()** (8 connections) — `server/services/combat_service_events.py`
- **UUID** (8 connections)
- **._persist_player_dp_sync()** (7 connections) — `server/services/combat_hp_sync.py`
- **end_combat()** (7 connections) — `server/services/combat_service_end.py`
- **clear_aggro_for_combat()** (6 connections) — `server/services/aggro_threat.py`
- **test_apply_damage_and_check_involuntary_flee_suppresses_non_damaging_phantom()** (6 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **test_finalize_attack_result_and_process_attack()** (6 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **test_finalize_attack_result_phantom_dissipation()** (6 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **test_register_combat_delegates_to_service()** (6 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **._get_persistence()** (5 connections) — `server/services/combat_hp_sync.py`
- **._publish_player_dp_correction_event()** (5 connections) — `server/services/combat_hp_sync.py`
- **._update_and_save_player_dp()** (5 connections) — `server/services/combat_hp_sync.py`
- **test_apply_damage_and_check_involuntary_flee()** (5 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **test_apply_target_rest_cancels_rest()** (5 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **test_apply_target_rest_grace_raises_on_grace_period()** (5 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **test_check_attacker_grace_period_raises()** (5 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **test_check_target_rest_skips_non_player()** (5 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- *... and 70 more nodes in this community*

## Relationships

- [CombatService](CombatService.md) (37 shared connections)
- [get_logger](get_logger.md) (9 shared connections)
- [NATSError](NATSError.md) (9 shared connections)
- [CombatInstance](CombatInstance.md) (6 shared connections)
- [test_aggro_threat.py](test_aggro_threat.py.md) (3 shared connections)
- [CombatParticipant](CombatParticipant.md) (3 shared connections)
- [test_combat_attack_handler.py](test_combat_attack_handler.py.md) (2 shared connections)
- [.get_instance](get_instance.md) (1 shared connections)
- [EventBus](EventBus.md) (1 shared connections)
- [player_event_handlers.py](player_event_handlers.py.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)
- [nats_exceptions.py](nats_exceptions.py.md) (1 shared connections)

## Source Files

- `server/services/aggro_threat.py`
- `server/services/combat_hp_sync.py`
- `server/services/combat_service_end.py`
- `server/services/combat_service_events.py`
- `server/tests/unit/services/test_combat_service_modules.py`

## Audit Trail

- EXTRACTED: 253 (98%)
- INFERRED: 6 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*