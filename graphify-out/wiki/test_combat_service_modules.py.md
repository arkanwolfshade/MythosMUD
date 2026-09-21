# test_combat_service_modules.py

> 98 nodes

## Key Concepts

- **test_combat_service_modules.py** (64 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **asyncio** (37 connections)
- **_combat_instance()** (14 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **_dp_sync()** (14 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **CombatDPSync** (13 connections) — `server/services/combat_hp_sync.py`
- **apply_target_rest_and_grace_checks()** (11 connections) — `server/services/combat_service_start.py`
- **_participant()** (11 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **handle_combat_completion()** (10 connections) — `server/services/combat_service_attack.py`
- **_attack_participant()** (10 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **apply_damage_and_check_involuntary_flee()** (9 connections) — `server/services/combat_service_attack.py`
- **UUID** (9 connections)
- **._persist_player_dp_sync()** (7 connections) — `server/services/combat_hp_sync.py`
- **validate_combat_can_start()** (7 connections) — `server/services/combat_service_start.py`
- **._get_persistence()** (6 connections) — `server/services/combat_hp_sync.py`
- **._publish_correction_to_event_bus()** (6 connections) — `server/services/combat_hp_sync.py`
- **._publish_player_dp_correction_event()** (6 connections) — `server/services/combat_hp_sync.py`
- **test_apply_damage_and_check_involuntary_flee_suppresses_non_damaging_phantom()** (6 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **test_finalize_attack_result_and_process_attack()** (6 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **test_finalize_attack_result_phantom_dissipation()** (6 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **test_register_combat_delegates_to_service()** (6 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **._update_and_save_player_dp()** (5 connections) — `server/services/combat_hp_sync.py`
- **test_apply_damage_and_check_involuntary_flee()** (5 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **test_apply_target_rest_cancels_rest()** (5 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **test_apply_target_rest_grace_allows_disconnect_grace_target()** (5 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **test_apply_target_rest_grace_raises_on_grace_period()** (5 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- *... and 73 more nodes in this community*

## Relationships

- [get_config](get_config.md) (20 shared connections)
- [combat_service.py](combat_service.py.md) (18 shared connections)
- [CombatInstance](CombatInstance.md) (7 shared connections)
- [CombatParticipant](CombatParticipant.md) (4 shared connections)
- [CombatService](CombatService.md) (4 shared connections)
- [NATSError](NATSError.md) (4 shared connections)
- [CombatParticipantData](CombatParticipantData.md) (4 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [DatabaseError](DatabaseError.md) (3 shared connections)
- [EventBus](EventBus.md) (2 shared connections)
- [PlayerDPUpdated](PlayerDPUpdated.md) (2 shared connections)
- [test_rest_command.py](test_rest_command.py.md) (2 shared connections)

## Source Files

- `server/services/combat_hp_sync.py`
- `server/services/combat_service_attack.py`
- `server/services/combat_service_start.py`
- `server/tests/unit/services/test_combat_service_modules.py`

## Audit Trail

- EXTRACTED: 259 (95%)
- INFERRED: 13 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*