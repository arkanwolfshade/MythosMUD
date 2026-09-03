# Test Combat Attack Handler

> 100 nodes

## Key Concepts

- **CombatAttackHandler** (43 connections) — `server/services/combat_attack_handler.py`
- **test_combat_attack_handler.py** (36 connections) — `server/tests/unit/services/test_combat_attack_handler.py`
- **CombatParticipant** (21 connections)
- **combat_attack_handler.py** (16 connections) — `server/services/combat_attack_handler.py`
- **CombatInstance** (12 connections)
- **.validate_and_get_combat_participants()** (8 connections) — `server/services/combat_attack_handler.py`
- **_bind_get_combat_by_participant()** (8 connections) — `server/tests/unit/services/test_combat_attack_handler.py`
- **._apply_damage()** (7 connections) — `server/services/combat_attack_handler.py`
- **test_apply_attack_damage()** (7 connections) — `server/tests/unit/services/test_combat_attack_handler.py`
- **test_validate_and_get_combat_participants_attacker_not_found()** (7 connections) — `server/tests/unit/services/test_combat_attack_handler.py`
- **test_validate_and_get_combat_participants_success()** (7 connections) — `server/tests/unit/services/test_combat_attack_handler.py`
- **test_validate_and_get_combat_participants_target_dead()** (7 connections) — `server/tests/unit/services/test_combat_attack_handler.py`
- **test_validate_and_get_combat_participants_target_not_found()** (7 connections) — `server/tests/unit/services/test_combat_attack_handler.py`
- **CombatInstance** (7 connections)
- **CombatParticipant** (7 connections)
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
- *... and 75 more nodes in this community*

## Relationships

- [Combat Spell Effects (Flee)](Combat_Spell_Effects_Flee.md) (5 shared connections)
- [Combat Events](Combat_Events.md) (3 shared connections)
- [Test Websocket Initial State](Test_Websocket_Initial_State.md) (2 shared connections)
- [Game State Provider](Game_State_Provider.md) (2 shared connections)
- [Test Combat Cleanup Handler](Test_Combat_Cleanup_Handler.md) (2 shared connections)
- [Combat Service Attack](Combat_Service_Attack.md) (1 shared connections)
- [Test Login Grace Period](Test_Login_Grace_Period.md) (1 shared connections)
- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (1 shared connections)
- [Container Exception Handling](Container_Exception_Handling.md) (1 shared connections)

## Source Files

- `server/services/combat_attack_handler.py`
- `server/tests/unit/services/test_combat_attack_handler.py`
- `server/tests/unit/services/test_damage_grace_period.py`

## Audit Trail

- EXTRACTED: 199 (89%)
- INFERRED: 25 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*