# CombatInstance

> 206 nodes

## Key Concepts

- **CombatInstance** (190 connections) — `server/models/combat.py`
- **CombatAttackHandler** (43 connections) — `server/services/combat_attack_handler.py`
- **test_combat_attack_handler.py** (40 connections) — `server/tests/unit/services/test_combat_attack_handler.py`
- **test_combat_flee_handler.py** (34 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **combat_flee_handler.py** (23 connections) — `server/services/combat_flee_handler.py`
- **execute_voluntary_flee()** (20 connections) — `server/services/combat_flee_handler.py`
- **_make_participant()** (20 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **asyncio** (15 connections)
- **_check_involuntary_flee_with_session()** (11 connections) — `server/services/combat_flee_handler.py`
- **try_voluntary_flee_roll()** (11 connections) — `server/services/combat_flee_handler.py`
- **_involuntary_flee_on_cooldown()** (10 connections) — `server/services/combat_flee_handler.py`
- **check_involuntary_flee()** (9 connections) — `server/services/combat_flee_handler.py`
- **.validate_and_get_combat_participants()** (8 connections) — `server/services/combat_attack_handler.py`
- **_bind_get_combat_by_participant()** (8 connections) — `server/tests/unit/services/test_combat_attack_handler.py`
- **test_apply_attack_damage()** (7 connections) — `server/tests/unit/services/test_combat_attack_handler.py`
- **test_validate_and_get_combat_participants_attacker_not_found()** (7 connections) — `server/tests/unit/services/test_combat_attack_handler.py`
- **test_validate_and_get_combat_participants_success()** (7 connections) — `server/tests/unit/services/test_combat_attack_handler.py`
- **test_validate_and_get_combat_participants_target_dead()** (7 connections) — `server/tests/unit/services/test_combat_attack_handler.py`
- **test_validate_and_get_combat_participants_target_not_found()** (7 connections) — `server/tests/unit/services/test_combat_attack_handler.py`
- **asyncio** (7 connections)
- **._cap_damage_for_no_death_room()** (6 connections) — `server/services/combat_attack_handler.py`
- **_handle_failed_voluntary_flee()** (6 connections) — `server/services/combat_flee_handler.py`
- **test_apply_damage_player_no_death_room_caps_damage()** (6 connections) — `server/tests/unit/services/test_combat_attack_handler.py`
- **test_apply_damage_player_no_death_room_zero_damage_when_at_zero()** (6 connections) — `server/tests/unit/services/test_combat_attack_handler.py`
- **test_validate_and_get_combat_participants_inactive_combat()** (6 connections) — `server/tests/unit/services/test_combat_attack_handler.py`
- *... and 181 more nodes in this community*

## Relationships

- [CombatParticipant](CombatParticipant.md) (104 shared connections)
- [CombatService](CombatService.md) (41 shared connections)
- [test_aggro_threat.py](test_aggro_threat.py.md) (14 shared connections)
- [test_combat_flee_helpers.py](test_combat_flee_helpers.py.md) (8 shared connections)
- [CombatCommandHandler](CombatCommandHandler.md) (8 shared connections)
- [test_combat_death_handler.py](test_combat_death_handler.py.md) (8 shared connections)
- [test_combat_service_modules.py](test_combat_service_modules.py.md) (7 shared connections)
- [test_combat_event_publisher.py](test_combat_event_publisher.py.md) (5 shared connections)
- [get_logger](get_logger.md) (5 shared connections)
- [CombatParticipantData](CombatParticipantData.md) (4 shared connections)
- [test_flee_command.py](test_flee_command.py.md) (4 shared connections)
- [SpellEffects](SpellEffects.md) (4 shared connections)

## Source Files

- `server/models/combat.py`
- `server/services/combat_attack_handler.py`
- `server/services/combat_cleanup_handler.py`
- `server/services/combat_flee_handler.py`
- `server/services/combat_service.py`
- `server/tests/unit/models/test_combat.py`
- `server/tests/unit/services/test_combat_attack_handler.py`
- `server/tests/unit/services/test_combat_flee_handler.py`
- `server/tests/unit/services/test_damage_grace_period.py`

## Audit Trail

- EXTRACTED: 562 (95%)
- INFERRED: 27 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*