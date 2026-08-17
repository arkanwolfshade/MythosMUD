# CombatAttackHandler

> 18 nodes

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
- **UUID** (3 connections)
- **Any** (1 connections)
- **Apply damage to target and update combat state. Args: combat: Combat instance…** (1 connections) — `server/services/combat_attack_handler.py`
- **Validate attack and retrieve combat participants. Args: attacker_id: ID of the…** (1 connections) — `server/services/combat_attack_handler.py`
- **Handles combat attack processing and damage application.** (1 connections) — `server/services/combat_attack_handler.py`
- **Initialize the attack handler. Args: combat_service: Reference to the parent…** (1 connections) — `server/services/combat_attack_handler.py`
- **Validate that attack is allowed.** (1 connections) — `server/services/combat_attack_handler.py`
- **Apply damage to target and check death states. Delegates domain logic to…** (1 connections) — `server/services/combat_attack_handler.py`
- **Check if room has no_death attribute (tutorial/safe zones).** (1 connections) — `server/services/combat_attack_handler.py`

## Relationships

- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (6 shared connections)
- [CombatInstance](CombatInstance.md) (5 shared connections)
- [CombatParticipant](CombatParticipant.md) (5 shared connections)
- [TargetMatch](TargetMatch.md) (4 shared connections)
- [test_combat_attack_handler.py](test_combat_attack_handler.py.md) (2 shared connections)
- [is_player_in_login_grace_period](is_player_in_login_grace_period.md) (1 shared connections)
- [.connection_manager](connection_manager.md) (1 shared connections)
- [websocket_helpers.py](websocket_helpers.py.md) (1 shared connections)

## Source Files

- `server/services/combat_attack_handler.py`

## Audit Trail

- EXTRACTED: 42 (88%)
- INFERRED: 6 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*