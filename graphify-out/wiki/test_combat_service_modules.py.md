# test_combat_service_modules.py

> 91 nodes

## Key Concepts

- **test_combat_service_modules.py** (65 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **asyncio** (37 connections)
- **combat_service_start.py** (28 connections) — `server/services/combat_service_start.py`
- **_dp_sync()** (17 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **_combat_instance()** (13 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **combat_service_end.py** (12 connections) — `server/services/combat_service_end.py`
- **apply_target_rest_and_grace_checks()** (11 connections) — `server/services/combat_service_start.py`
- **handle_combat_completion()** (10 connections) — `server/services/combat_service_attack.py`
- **_participant()** (10 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **check_attacker_grace_period()** (9 connections) — `server/services/combat_service_start.py`
- **publish_combat_started_event()** (9 connections) — `server/services/combat_service_start.py`
- **check_target_rest_and_grace_period()** (8 connections) — `server/services/combat_service_start.py`
- **_attack_participant()** (8 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **end_combat()** (7 connections) — `server/services/combat_service_end.py`
- **get_connection_manager_for_combat_check()** (7 connections) — `server/services/combat_service_start.py`
- **register_combat()** (7 connections) — `server/services/combat_service_start.py`
- **validate_combat_can_start()** (7 connections) — `server/services/combat_service_start.py`
- **clear_aggro_for_combat()** (6 connections) — `server/services/aggro_threat.py`
- **test_finalize_attack_result_and_process_attack()** (6 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **test_register_combat_delegates_to_service()** (6 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **test_apply_damage_and_check_involuntary_flee()** (5 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **test_apply_target_rest_cancels_rest()** (5 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **test_apply_target_rest_grace_raises_on_grace_period()** (5 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **test_check_attacker_grace_period_raises()** (5 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **test_check_target_rest_skips_non_player()** (5 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- *... and 66 more nodes in this community*

## Relationships

- [CombatService](CombatService.md) (29 shared connections)
- [models/combat.py](models-combat.py.md) (17 shared connections)
- [get_logger](get_logger.md) (12 shared connections)
- [CombatInstance](CombatInstance.md) (9 shared connections)
- [NATSError](NATSError.md) (7 shared connections)
- [test_rest_command.py](test_rest_command.py.md) (5 shared connections)
- [DatabaseError](DatabaseError.md) (4 shared connections)
- [combat_taunt.py](combat_taunt.py.md) (3 shared connections)
- [is_player_in_login_grace_period](is_player_in_login_grace_period.md) (3 shared connections)
- [get_config](get_config.md) (3 shared connections)
- [CombatParticipant](CombatParticipant.md) (3 shared connections)
- [.connection_manager](connection_manager.md) (2 shared connections)

## Source Files

- `server/services/aggro_threat.py`
- `server/services/combat_service_attack.py`
- `server/services/combat_service_end.py`
- `server/services/combat_service_start.py`
- `server/tests/unit/services/test_combat_service_modules.py`

## Audit Trail

- EXTRACTED: 264 (91%)
- INFERRED: 25 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*