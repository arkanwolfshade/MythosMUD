# Test Combat Flee Handler

> 117 nodes

## Key Concepts

- **CombatInstance** (161 connections) — `server/models/combat.py`
- **test_combat_flee_handler.py** (34 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **combat_flee_handler.py** (23 connections) — `server/services/combat_flee_handler.py`
- **execute_voluntary_flee()** (20 connections) — `server/services/combat_flee_handler.py`
- **_make_participant()** (20 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **asyncio** (15 connections)
- **_check_involuntary_flee_with_session()** (11 connections) — `server/services/combat_flee_handler.py`
- **try_voluntary_flee_roll()** (11 connections) — `server/services/combat_flee_handler.py`
- **_involuntary_flee_on_cooldown()** (10 connections) — `server/services/combat_flee_handler.py`
- **check_involuntary_flee()** (9 connections) — `server/services/combat_flee_handler.py`
- **_handle_failed_voluntary_flee()** (6 connections) — `server/services/combat_flee_handler.py`
- **test_execute_voluntary_flee_free_hits_error_logged()** (6 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **test_execute_voluntary_flee_missing_participant_returns_false()** (6 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **test_execute_voluntary_flee_move_fails_returns_false()** (6 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **test_execute_voluntary_flee_no_exits_returns_false()** (6 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **test_execute_voluntary_flee_no_room_returns_false()** (6 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **test_execute_voluntary_flee_roll_fail_consumes_action()** (6 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **test_execute_voluntary_flee_success_moves_player()** (6 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **.apply_attack_damage()** (5 connections) — `server/services/combat_service.py`
- **._handle_player_dp_update()** (5 connections) — `server/services/combat_service.py`
- **test_check_involuntary_flee_session_path()** (5 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **test_check_involuntary_flee_with_session_sets_cooldown()** (5 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **test_check_involuntary_flee_with_session_tier_blocks()** (5 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **test_check_involuntary_flee_zero_max_dp_returns_false()** (5 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **test_try_voluntary_flee_roll_dead_opponent_not_counted()** (5 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- *... and 92 more nodes in this community*

## Relationships

- [Combat Turn Processing](Combat_Turn_Processing.md) (48 shared connections)
- [Combat Service Attack](Combat_Service_Attack.md) (32 shared connections)
- [Test Combat Cleanup Handler](Test_Combat_Cleanup_Handler.md) (14 shared connections)
- [Combat Events](Combat_Events.md) (13 shared connections)
- [Test Aggro Threat](Test_Aggro_Threat.md) (12 shared connections)
- [Combat Turn Participant Actions](Combat_Turn_Participant_Actions.md) (10 shared connections)
- [Combat Flee](Combat_Flee.md) (8 shared connections)
- [Combat Taunt](Combat_Taunt.md) (7 shared connections)
- [Test Flee Command](Test_Flee_Command.md) (4 shared connections)
- [Lucidity Helpers & Catatonia](Lucidity_Helpers_&_Catatonia.md) (4 shared connections)
- [Lucidity Command Disruption](Lucidity_Command_Disruption.md) (3 shared connections)
- [Combat Spell Effects (Flee)](Combat_Spell_Effects_Flee.md) (3 shared connections)

## Source Files

- `server/models/combat.py`
- `server/services/combat_flee_handler.py`
- `server/services/combat_service.py`
- `server/tests/unit/models/test_combat.py`
- `server/tests/unit/services/test_combat_flee_handler.py`

## Audit Trail

- EXTRACTED: 375 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*