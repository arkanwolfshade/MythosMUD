# test_combat_attack_handler.py

> 101 nodes

## Key Concepts

- **test_combat_attack_handler.py** (37 connections) — `server/tests/unit/services/test_combat_attack_handler.py`
- **test_damage_grace_period.py** (27 connections) — `server/tests/unit/services/test_damage_grace_period.py`
- **CombatAttackHandler** (19 connections) — `server/services/combat_attack_handler.py`
- **combat_attack_handler.py** (17 connections) — `server/services/combat_attack_handler.py`
- **CombatStatus** (13 connections) — `server/models/combat.py`
- **._apply_damage()** (9 connections) — `server/services/combat_attack_handler.py`
- **.validate_and_get_combat_participants()** (8 connections) — `server/services/combat_attack_handler.py`
- **asyncio** (7 connections)
- **fixture** (6 connections)
- **.apply_attack_damage()** (5 connections) — `server/services/combat_attack_handler.py`
- **._find_combat_target()** (5 connections) — `server/services/combat_attack_handler.py`
- **test_apply_damage_blocked_during_grace_period()** (5 connections) — `server/tests/unit/services/test_damage_grace_period.py`
- **._room_has_no_death()** (4 connections) — `server/services/combat_attack_handler.py`
- **._validate_attack()** (4 connections) — `server/services/combat_attack_handler.py`
- **attack_handler()** (4 connections) — `server/tests/unit/services/test_combat_attack_handler.py`
- **mock_target_npc()** (4 connections) — `server/tests/unit/services/test_combat_attack_handler.py`
- **mock_target_player()** (4 connections) — `server/tests/unit/services/test_combat_attack_handler.py`
- **player_participant()** (4 connections) — `server/tests/unit/services/test_damage_grace_period.py`
- **fixture** (4 connections)
- **.__init__()** (3 connections) — `server/services/combat_attack_handler.py`
- **._validate_target_can_be_attacked()** (3 connections) — `server/services/combat_attack_handler.py`
- **mock_attacker()** (3 connections) — `server/tests/unit/services/test_combat_attack_handler.py`
- **mock_combat()** (3 connections) — `server/tests/unit/services/test_combat_attack_handler.py`
- **mock_combat_service()** (3 connections) — `server/tests/unit/services/test_combat_attack_handler.py`
- **test_apply_attack_damage()** (3 connections) — `server/tests/unit/services/test_combat_attack_handler.py`
- *... and 76 more nodes in this community*

## Relationships

- [CombatParticipant](CombatParticipant.md) (14 shared connections)
- [models/combat.py](models-combat.py.md) (8 shared connections)
- [CombatInstance](CombatInstance.md) (7 shared connections)
- [is_player_in_login_grace_period](is_player_in_login_grace_period.md) (7 shared connections)
- [TargetMatch](TargetMatch.md) (6 shared connections)
- [CombatService](CombatService.md) (5 shared connections)
- [get_logger](get_logger.md) (4 shared connections)
- [test_combat_service_modules.py](test_combat_service_modules.py.md) (2 shared connections)
- [get_config](get_config.md) (2 shared connections)
- [Player](Player.md) (2 shared connections)
- [server/models/game.py](server-models-game.py.md) (2 shared connections)
- [test_game_tick_processing.py](test_game_tick_processing.py.md) (1 shared connections)

## Source Files

- `server/models/combat.py`
- `server/services/combat_attack_handler.py`
- `server/tests/unit/services/test_combat_attack_handler.py`
- `server/tests/unit/services/test_damage_grace_period.py`

## Audit Trail

- EXTRACTED: 186 (97%)
- INFERRED: 6 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*