# test_combat_service_modules.py

> 95 nodes

## Key Concepts

- **test_combat_service_modules.py** (65 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **asyncio** (37 connections)
- **combat_service_attack.py** (28 connections) — `server/services/combat_service_attack.py`
- **CombatResult** (20 connections) — `server/models/combat.py`
- **_dp_sync()** (17 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **_combat_instance()** (13 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **finalize_attack_result()** (10 connections) — `server/services/combat_service_attack.py`
- **handle_combat_completion()** (10 connections) — `server/services/combat_service_attack.py`
- **_participant()** (10 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **validate_melee_location()** (9 connections) — `server/services/combat_service_attack.py`
- **validate_melee_or_end_combat()** (9 connections) — `server/services/combat_service_attack.py`
- **apply_damage_and_check_involuntary_flee()** (8 connections) — `server/services/combat_service_attack.py`
- **_attack_participant()** (8 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **process_attack()** (7 connections) — `server/services/combat_service_attack.py`
- **queue_combat_action()** (7 connections) — `server/services/combat_service_attack.py`
- **end_combat()** (7 connections) — `server/services/combat_service_end.py`
- **validate_combat_can_start()** (7 connections) — `server/services/combat_service_start.py`
- **_effective_room_for_melee()** (6 connections) — `server/services/combat_service_attack.py`
- **test_finalize_attack_result_and_process_attack()** (6 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **test_register_combat_delegates_to_service()** (6 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **UUID** (6 connections)
- **_melee_location_fail_reason()** (5 connections) — `server/services/combat_service_attack.py`
- **.apply_damage_and_check_involuntary_flee()** (5 connections) — `server/services/combat_service.py`
- **test_apply_damage_and_check_involuntary_flee()** (5 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **test_apply_target_rest_cancels_rest()** (5 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- *... and 70 more nodes in this community*

## Relationships

- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (60 shared connections)
- [CombatParticipant](CombatParticipant.md) (13 shared connections)
- [CombatInstance](CombatInstance.md) (11 shared connections)
- [ConnectionManager](ConnectionManager.md) (6 shared connections)
- [test_aggro_threat.py](test_aggro_threat.py.md) (4 shared connections)
- [test_combat_service.py](test_combat_service.py.md) (3 shared connections)
- [UUID](UUID.md) (3 shared connections)
- [DatabaseError](DatabaseError.md) (3 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [CombatDPSync](CombatDPSync.md) (2 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/models/combat.py`
- `server/services/combat_service.py`
- `server/services/combat_service_attack.py`
- `server/services/combat_service_end.py`
- `server/services/combat_service_start.py`
- `server/tests/unit/services/test_combat_service_modules.py`

## Audit Trail

- EXTRACTED: 285 (94%)
- INFERRED: 17 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*