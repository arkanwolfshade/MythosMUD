# test_combat_attack_handler.py

> 84 nodes

## Key Concepts

- **test_combat_attack_handler.py** (38 connections) — `server/tests/unit/services/test_combat_attack_handler.py`
- **CombatAttackHandler** (19 connections) — `server/services/combat_attack_handler.py`
- **combat_attack_handler.py** (17 connections) — `server/services/combat_attack_handler.py`
- **CombatStatus** (13 connections) — `server/models/combat.py`
- **._apply_damage()** (9 connections) — `server/services/combat_attack_handler.py`
- **.validate_and_get_combat_participants()** (8 connections) — `server/services/combat_attack_handler.py`
- **asyncio** (7 connections)
- **fixture** (6 connections)
- **.apply_attack_damage()** (5 connections) — `server/services/combat_attack_handler.py`
- **._find_combat_target()** (5 connections) — `server/services/combat_attack_handler.py`
- **._room_has_no_death()** (4 connections) — `server/services/combat_attack_handler.py`
- **._validate_attack()** (4 connections) — `server/services/combat_attack_handler.py`
- **attack_handler()** (4 connections) — `server/tests/unit/services/test_combat_attack_handler.py`
- **mock_target_npc()** (4 connections) — `server/tests/unit/services/test_combat_attack_handler.py`
- **mock_target_player()** (4 connections) — `server/tests/unit/services/test_combat_attack_handler.py`
- **.__init__()** (3 connections) — `server/services/combat_attack_handler.py`
- **._validate_target_can_be_attacked()** (3 connections) — `server/services/combat_attack_handler.py`
- **mock_attacker()** (3 connections) — `server/tests/unit/services/test_combat_attack_handler.py`
- **mock_combat()** (3 connections) — `server/tests/unit/services/test_combat_attack_handler.py`
- **mock_combat_service()** (3 connections) — `server/tests/unit/services/test_combat_attack_handler.py`
- **test_apply_attack_damage()** (3 connections) — `server/tests/unit/services/test_combat_attack_handler.py`
- **test_validate_and_get_combat_participants_attacker_not_found()** (3 connections) — `server/tests/unit/services/test_combat_attack_handler.py`
- **test_validate_and_get_combat_participants_inactive_combat()** (3 connections) — `server/tests/unit/services/test_combat_attack_handler.py`
- **test_validate_and_get_combat_participants_not_in_combat()** (3 connections) — `server/tests/unit/services/test_combat_attack_handler.py`
- **test_validate_and_get_combat_participants_success()** (3 connections) — `server/tests/unit/services/test_combat_attack_handler.py`
- *... and 59 more nodes in this community*

## Relationships

- [CombatService](CombatService.md) (13 shared connections)
- [CombatParticipant](CombatParticipant.md) (12 shared connections)
- [CombatInstance](CombatInstance.md) (7 shared connections)
- [test_spell_effects.py](test_spell_effects.py.md) (5 shared connections)
- [test_combat_service_modules.py](test_combat_service_modules.py.md) (2 shared connections)
- [is_player_in_login_grace_period](is_player_in_login_grace_period.md) (2 shared connections)
- [test_websocket_initial_state.py](test_websocket_initial_state.py.md) (2 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [game_tick_death.py](game_tick_death.py.md) (1 shared connections)
- [game_tick_processing.py](game_tick_processing.py.md) (1 shared connections)
- [test_combat_cleanup_handler.py](test_combat_cleanup_handler.py.md) (1 shared connections)
- [login_grace_period.py](login_grace_period.py.md) (1 shared connections)

## Source Files

- `server/models/combat.py`
- `server/services/combat_attack_handler.py`
- `server/tests/unit/services/test_combat_attack_handler.py`

## Audit Trail

- EXTRACTED: 150 (97%)
- INFERRED: 4 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*