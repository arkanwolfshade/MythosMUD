# Community 121

> 94 nodes

## Key Concepts

- **CombatAttackHandler** (40 connections) — `server/services/combat_attack_handler.py`
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
- **_player_damage_blocked_by_grace()** (6 connections) — `server/services/combat_attack_handler.py`
- **test_apply_damage_player_no_death_room_caps_damage()** (6 connections) — `server/tests/unit/services/test_combat_attack_handler.py`
- **test_apply_damage_player_no_death_room_zero_damage_when_at_zero()** (6 connections) — `server/tests/unit/services/test_combat_attack_handler.py`
- **test_validate_and_get_combat_participants_inactive_combat()** (6 connections) — `server/tests/unit/services/test_combat_attack_handler.py`
- **fixture** (6 connections)
- **Test validate_and_get_combat_participants returns participants.** (6 connections) — `server/tests/unit/services/test_combat_attack_handler.py`
- **_CombatAttackService** (5 connections) — `server/services/combat_attack_handler.py`
- **.apply_attack_damage()** (5 connections) — `server/services/combat_attack_handler.py`
- **._find_combat_target()** (5 connections) — `server/services/combat_attack_handler.py`
- **test_validate_and_get_combat_participants_not_in_combat()** (5 connections) — `server/tests/unit/services/test_combat_attack_handler.py`
- **._room_has_no_death()** (4 connections) — `server/services/combat_attack_handler.py`
- **._validate_attack()** (4 connections) — `server/services/combat_attack_handler.py`
- **_connection_manager_for_grace_check()** (4 connections) — `server/services/combat_attack_handler.py`
- *... and 69 more nodes in this community*

## Relationships

- [Combat Participants](Combat_Participants.md) (29 shared connections)
- [Combat Instance Turns](Combat_Instance_Turns.md) (20 shared connections)
- [Combat Attack Execution](Combat_Attack_Execution.md) (14 shared connections)
- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (2 shared connections)
- [Community 55](Community_55.md) (1 shared connections)
- [Community 46](Community_46.md) (1 shared connections)

## Source Files

- `server/services/combat_attack_handler.py`
- `server/tests/unit/services/test_combat_attack_handler.py`
- `server/tests/unit/services/test_damage_grace_period.py`

## Audit Trail

- EXTRACTED: 193 (89%)
- INFERRED: 24 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*