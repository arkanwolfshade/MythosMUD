# CombatInstance

> 120 nodes

## Key Concepts

- **CombatInstance** (174 connections) — `server/models/combat.py`
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
- *... and 95 more nodes in this community*

## Relationships

- [CombatParticipant](CombatParticipant.md) (48 shared connections)
- [CombatService](CombatService.md) (41 shared connections)
- [test_aggro_threat.py](test_aggro_threat.py.md) (13 shared connections)
- [combat_service_npc.py](combat_service_npc.py.md) (10 shared connections)
- [test_combat_flee_helpers.py](test_combat_flee_helpers.py.md) (8 shared connections)
- [UUID](UUID.md) (8 shared connections)
- [npc_combat_integration_service.py](npc_combat_integration_service.py.md) (6 shared connections)
- [test_combat_service_modules.py](test_combat_service_modules.py.md) (6 shared connections)
- [combat_service_attack.py](combat_service_attack.py.md) (6 shared connections)
- [.connection_manager](connection_manager.md) (6 shared connections)
- [CombatAttackHandler](CombatAttackHandler.md) (5 shared connections)
- [get_logger](get_logger.md) (5 shared connections)

## Source Files

- `server/models/combat.py`
- `server/services/combat_cleanup_handler.py`
- `server/services/combat_flee_handler.py`
- `server/services/combat_service.py`
- `server/tests/unit/models/test_combat.py`
- `server/tests/unit/services/test_combat_flee_handler.py`

## Audit Trail

- EXTRACTED: 389 (99%)
- INFERRED: 3 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*