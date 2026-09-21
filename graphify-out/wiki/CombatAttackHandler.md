# CombatAttackHandler

> 90 nodes

## Key Concepts

- **CombatAttackHandler** (43 connections) — `server/services/combat_attack_handler.py`
- **test_combat_attack_handler.py** (39 connections) — `server/tests/unit/services/test_combat_attack_handler.py`
- **.validate_and_get_combat_participants()** (8 connections) — `server/services/combat_attack_handler.py`
- **_bind_get_combat_by_participant()** (8 connections) — `server/tests/unit/services/test_combat_attack_handler.py`
- **._apply_damage()** (7 connections) — `server/services/combat_attack_handler.py`
- **test_apply_attack_damage()** (7 connections) — `server/tests/unit/services/test_combat_attack_handler.py`
- **test_validate_and_get_combat_participants_attacker_not_found()** (7 connections) — `server/tests/unit/services/test_combat_attack_handler.py`
- **test_validate_and_get_combat_participants_success()** (7 connections) — `server/tests/unit/services/test_combat_attack_handler.py`
- **test_validate_and_get_combat_participants_target_dead()** (7 connections) — `server/tests/unit/services/test_combat_attack_handler.py`
- **test_validate_and_get_combat_participants_target_not_found()** (7 connections) — `server/tests/unit/services/test_combat_attack_handler.py`
- **asyncio** (7 connections)
- **._cap_damage_for_no_death_room()** (6 connections) — `server/services/combat_attack_handler.py`
- **test_apply_damage_player_no_death_room_caps_damage()** (6 connections) — `server/tests/unit/services/test_combat_attack_handler.py`
- **test_apply_damage_player_no_death_room_zero_damage_when_at_zero()** (6 connections) — `server/tests/unit/services/test_combat_attack_handler.py`
- **test_validate_and_get_combat_participants_inactive_combat()** (6 connections) — `server/tests/unit/services/test_combat_attack_handler.py`
- **fixture** (6 connections)
- **_CombatAttackService** (5 connections) — `server/services/combat_attack_handler.py`
- **.apply_attack_damage()** (5 connections) — `server/services/combat_attack_handler.py`
- **._find_combat_target()** (5 connections) — `server/services/combat_attack_handler.py`
- **test_validate_and_get_combat_participants_not_in_combat()** (5 connections) — `server/tests/unit/services/test_combat_attack_handler.py`
- **._room_has_no_death()** (4 connections) — `server/services/combat_attack_handler.py`
- **._validate_attack()** (4 connections) — `server/services/combat_attack_handler.py`
- **attack_handler()** (4 connections) — `server/tests/unit/services/test_combat_attack_handler.py`
- **mock_attacker()** (4 connections) — `server/tests/unit/services/test_combat_attack_handler.py`
- **mock_combat()** (4 connections) — `server/tests/unit/services/test_combat_attack_handler.py`
- *... and 65 more nodes in this community*

## Relationships

- [CombatParticipant](CombatParticipant.md) (28 shared connections)
- [CombatInstance](CombatInstance.md) (20 shared connections)
- [get_logger](get_logger.md) (13 shared connections)
- [test_combat_cleanup_handler.py](test_combat_cleanup_handler.py.md) (1 shared connections)
- [CombatService](CombatService.md) (1 shared connections)
- [is_player_in_login_grace_period](is_player_in_login_grace_period.md) (1 shared connections)
- [websocket_helpers.py](websocket_helpers.py.md) (1 shared connections)

## Source Files

- `server/services/combat_attack_handler.py`
- `server/tests/unit/services/test_combat_attack_handler.py`
- `server/tests/unit/services/test_damage_grace_period.py`

## Audit Trail

- EXTRACTED: 181 (88%)
- INFERRED: 25 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*