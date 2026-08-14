# CombatAttackHandler

> 22 nodes

## Key Concepts

- **CombatAttackHandler** (19 connections) — `server/services/combat_attack_handler.py`
- **._apply_damage()** (9 connections) — `server/services/combat_attack_handler.py`
- **.validate_and_get_combat_participants()** (8 connections) — `server/services/combat_attack_handler.py`
- **.apply_attack_damage()** (5 connections) — `server/services/combat_attack_handler.py`
- **._find_combat_target()** (5 connections) — `server/services/combat_attack_handler.py`
- **._room_has_no_death()** (4 connections) — `server/services/combat_attack_handler.py`
- **._validate_attack()** (4 connections) — `server/services/combat_attack_handler.py`
- **.__init__()** (3 connections) — `server/services/combat_attack_handler.py`
- **._validate_target_can_be_attacked()** (3 connections) — `server/services/combat_attack_handler.py`
- **test_apply_damage_allowed_after_grace_period()** (3 connections) — `server/tests/unit/services/test_damage_grace_period.py`
- **test_apply_damage_fails_open_on_error()** (3 connections) — `server/tests/unit/services/test_damage_grace_period.py`
- **UUID** (3 connections)
- **Any** (1 connections)
- **Apply damage to target and update combat state. Args: combat: Combat instance…** (1 connections) — `server/services/combat_attack_handler.py`
- **Validate attack and retrieve combat participants. Args: attacker_id: ID of the…** (1 connections) — `server/services/combat_attack_handler.py`
- **Handles combat attack processing and damage application.** (1 connections) — `server/services/combat_attack_handler.py`
- **Initialize the attack handler. Args: combat_service: Reference to the parent…** (1 connections) — `server/services/combat_attack_handler.py`
- **Validate that attack is allowed.** (1 connections) — `server/services/combat_attack_handler.py`
- **Apply damage to target and check death states. Delegates domain logic to…** (1 connections) — `server/services/combat_attack_handler.py`
- **Check if room has no_death attribute (tutorial/safe zones).** (1 connections) — `server/services/combat_attack_handler.py`
- **Test that damage application fails open if grace period check errors.** (1 connections) — `server/tests/unit/services/test_damage_grace_period.py`
- **Test that damage is applied normally after grace period.** (1 connections) — `server/tests/unit/services/test_damage_grace_period.py`

## Relationships

- [CombatService](CombatService.md) (5 shared connections)
- [CombatInstance](CombatInstance.md) (5 shared connections)
- [CombatParticipant](CombatParticipant.md) (5 shared connections)
- [TargetMatch](TargetMatch.md) (4 shared connections)
- [test_combat_attack_handler.py](test_combat_attack_handler.py.md) (2 shared connections)
- [get_logger](get_logger.md) (1 shared connections)
- [is_player_in_login_grace_period](is_player_in_login_grace_period.md) (1 shared connections)
- [test_combat_death_handler.py](test_combat_death_handler.py.md) (1 shared connections)
- [websocket_initial_state.py](websocket_initial_state.py.md) (1 shared connections)

## Source Files

- `server/services/combat_attack_handler.py`
- `server/tests/unit/services/test_damage_grace_period.py`

## Audit Trail

- EXTRACTED: 50 (96%)
- INFERRED: 2 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*