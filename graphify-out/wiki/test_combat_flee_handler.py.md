# test_combat_flee_handler.py

> 61 nodes

## Key Concepts

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
- **test_check_involuntary_flee_session_path()** (5 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **test_check_involuntary_flee_with_session_sets_cooldown()** (5 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **test_check_involuntary_flee_with_session_tier_blocks()** (5 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **test_check_involuntary_flee_zero_max_dp_returns_false()** (5 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **test_try_voluntary_flee_roll_dead_opponent_not_counted()** (5 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **test_try_voluntary_flee_roll_opponents_reduce_chance()** (5 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **test_try_voluntary_flee_roll_roll_above_chance_fails()** (5 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **test_try_voluntary_flee_roll_roll_below_chance_succeeds()** (5 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- *... and 36 more nodes in this community*

## Relationships

- [CombatInstance](CombatInstance.md) (22 shared connections)
- [CombatParticipant](CombatParticipant.md) (7 shared connections)
- [LucidityService](LucidityService.md) (4 shared connections)
- [test_lucidity_command_disruption.py](test_lucidity_command_disruption.py.md) (3 shared connections)
- [run_flee_effect](run_flee_effect.md) (3 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (2 shared connections)
- [test_combat_flee_helpers.py](test_combat_flee_helpers.py.md) (2 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [TargetResolutionService](TargetResolutionService.md) (1 shared connections)
- [database.py](database.py.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/services/combat_flee_handler.py`
- `server/tests/unit/services/test_combat_flee_handler.py`

## Audit Trail

- EXTRACTED: 171 (98%)
- INFERRED: 3 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*