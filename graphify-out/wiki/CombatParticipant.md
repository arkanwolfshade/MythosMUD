# CombatParticipant

> 208 nodes

## Key Concepts

- **CombatParticipant** (219 connections) — `server/models/combat.py`
- **test_combat.py** (60 connections) — `server/tests/unit/models/test_combat.py`
- **CombatAttackHandler** (43 connections) — `server/services/combat_attack_handler.py`
- **test_combat_attack_handler.py** (39 connections) — `server/tests/unit/services/test_combat_attack_handler.py`
- **test_damage_grace_period.py** (27 connections) — `server/tests/unit/services/test_damage_grace_period.py`
- **combat_attack_handler.py** (22 connections) — `server/services/combat_attack_handler.py`
- **.validate_and_get_combat_participants()** (8 connections) — `server/services/combat_attack_handler.py`
- **_bind_get_combat_by_participant()** (8 connections) — `server/tests/unit/services/test_combat_attack_handler.py`
- **._apply_damage()** (7 connections) — `server/services/combat_attack_handler.py`
- **test_apply_attack_damage()** (7 connections) — `server/tests/unit/services/test_combat_attack_handler.py`
- **test_validate_and_get_combat_participants_attacker_not_found()** (7 connections) — `server/tests/unit/services/test_combat_attack_handler.py`
- **test_validate_and_get_combat_participants_success()** (7 connections) — `server/tests/unit/services/test_combat_attack_handler.py`
- **test_validate_and_get_combat_participants_target_dead()** (7 connections) — `server/tests/unit/services/test_combat_attack_handler.py`
- **test_validate_and_get_combat_participants_target_not_found()** (7 connections) — `server/tests/unit/services/test_combat_attack_handler.py`
- **asyncio** (7 connections)
- **_get_default_damage()** (6 connections) — `server/models/combat.py`
- **._cap_damage_for_no_death_room()** (6 connections) — `server/services/combat_attack_handler.py`
- **_player_damage_blocked_by_grace()** (6 connections) — `server/services/combat_attack_handler.py`
- **test_apply_damage_player_no_death_room_caps_damage()** (6 connections) — `server/tests/unit/services/test_combat_attack_handler.py`
- **test_apply_damage_player_no_death_room_zero_damage_when_at_zero()** (6 connections) — `server/tests/unit/services/test_combat_attack_handler.py`
- **test_validate_and_get_combat_participants_inactive_combat()** (6 connections) — `server/tests/unit/services/test_combat_attack_handler.py`
- **fixture** (6 connections)
- **_CombatAttackService** (5 connections) — `server/services/combat_attack_handler.py`
- **.apply_attack_damage()** (5 connections) — `server/services/combat_attack_handler.py`
- **._find_combat_target()** (5 connections) — `server/services/combat_attack_handler.py`
- *... and 183 more nodes in this community*

## Relationships

- [CombatInstance](CombatInstance.md) (51 shared connections)
- [CombatTurnProcessor](CombatTurnProcessor.md) (42 shared connections)
- [CombatService](CombatService.md) (37 shared connections)
- [combat_turn_participant_actions.py](combat_turn_participant_actions.py.md) (20 shared connections)
- [test_aggro_threat.py](test_aggro_threat.py.md) (11 shared connections)
- [test_combat_service_modules.py](test_combat_service_modules.py.md) (11 shared connections)
- [test_combat_event_publisher.py](test_combat_event_publisher.py.md) (9 shared connections)
- [is_player_in_login_grace_period](is_player_in_login_grace_period.md) (8 shared connections)
- [TauntCommandHandler](TauntCommandHandler.md) (6 shared connections)
- [CombatEventHandler](CombatEventHandler.md) (5 shared connections)
- [TargetMatch](TargetMatch.md) (5 shared connections)
- [test_combat_death_handler.py](test_combat_death_handler.py.md) (3 shared connections)

## Source Files

- `server/models/combat.py`
- `server/services/combat_attack_handler.py`
- `server/services/combat_service.py`
- `server/tests/unit/models/test_combat.py`
- `server/tests/unit/services/test_combat_attack_handler.py`
- `server/tests/unit/services/test_damage_grace_period.py`

## Audit Trail

- EXTRACTED: 547 (96%)
- INFERRED: 25 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*