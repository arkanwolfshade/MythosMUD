# Player Left Room Tests

> 96 nodes

## Key Concepts

- **test_combat_attack_handler.py** (37 connections) — `server/tests/unit/services/test_combat_attack_handler.py`
- **test_damage_grace_period.py** (27 connections) — `server/tests/unit/services/test_damage_grace_period.py`
- **CombatAttackHandler** (19 connections) — `server/services/combat_attack_handler.py`
- **combat_attack_handler.py** (17 connections) — `server/services/combat_attack_handler.py`
- **._apply_damage()** (9 connections) — `server/services/combat_attack_handler.py`
- **.validate_and_get_combat_participants()** (8 connections) — `server/services/combat_attack_handler.py`
- **.apply_attack_damage()** (5 connections) — `server/services/combat_attack_handler.py`
- **._find_combat_target()** (5 connections) — `server/services/combat_attack_handler.py`
- **._validate_attack()** (4 connections) — `server/services/combat_attack_handler.py`
- **._room_has_no_death()** (4 connections) — `server/services/combat_attack_handler.py`
- **test_apply_damage_blocked_during_grace_period()** (4 connections) — `server/tests/unit/services/test_damage_grace_period.py`
- **.__init__()** (3 connections) — `server/services/combat_attack_handler.py`
- **UUID** (3 connections)
- **._validate_target_can_be_attacked()** (3 connections) — `server/services/combat_attack_handler.py`
- **attack_handler()** (3 connections) — `server/tests/unit/services/test_combat_attack_handler.py`
- **mock_combat()** (3 connections) — `server/tests/unit/services/test_combat_attack_handler.py`
- **mock_attacker()** (3 connections) — `server/tests/unit/services/test_combat_attack_handler.py`
- **mock_target_player()** (3 connections) — `server/tests/unit/services/test_combat_attack_handler.py`
- **mock_target_npc()** (3 connections) — `server/tests/unit/services/test_combat_attack_handler.py`
- **test_apply_damage_player_no_death_room_caps_damage()** (3 connections) — `server/tests/unit/services/test_combat_attack_handler.py`
- **test_apply_damage_player_no_death_room_zero_damage_when_at_zero()** (3 connections) — `server/tests/unit/services/test_combat_attack_handler.py`
- **player_participant()** (3 connections) — `server/tests/unit/services/test_damage_grace_period.py`
- **test_apply_damage_allowed_after_grace_period()** (3 connections) — `server/tests/unit/services/test_damage_grace_period.py`
- **test_apply_damage_fails_open_on_error()** (3 connections) — `server/tests/unit/services/test_damage_grace_period.py`
- **mock_combat_service()** (2 connections) — `server/tests/unit/services/test_combat_attack_handler.py`
- *... and 71 more nodes in this community*

## Relationships

- [Rest Command Flow](Rest_Command_Flow.md) (17 shared connections)
- [Container Component Capacity](Container_Component_Capacity.md) (10 shared connections)
- [Player Respawn Events](Player_Respawn_Events.md) (7 shared connections)
- [Combat Domain Events](Combat_Domain_Events.md) (4 shared connections)
- [NPC Service Tests](NPC_Service_Tests.md) (4 shared connections)
- [Commands Look Item](Commands_Look_Item.md) (3 shared connections)
- [Combat Attack Service](Combat_Attack_Service.md) (3 shared connections)
- [WebSocket Initial State](WebSocket_Initial_State.md) (2 shared connections)
- [Archive Frd Random](Archive_Frd_Random.md) (2 shared connections)
- [Game Service Bundle](Game_Service_Bundle.md) (2 shared connections)
- [test_profession_meets_stat_requirements_multiple_not_met](test_profession_meets_stat_requirements_multiple_not_met.md) (2 shared connections)
- [Level and XP Curve](Level_and_XP_Curve.md) (1 shared connections)

## Source Files

- `server/services/combat_attack_handler.py`
- `server/tests/unit/services/test_combat_attack_handler.py`
- `server/tests/unit/services/test_damage_grace_period.py`

## Audit Trail

- EXTRACTED: 269 (98%)
- INFERRED: 6 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*