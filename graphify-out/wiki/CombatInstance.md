# CombatInstance

> 104 nodes

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
- **test_run_handle_taunt_success()** (8 connections) — `server/tests/unit/commands/test_combat_taunt.py`
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
- **_select_player_target()** (5 connections) — `server/services/combat_turn_participant_actions.py`
- **test_check_involuntary_flee_session_path()** (5 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **test_check_involuntary_flee_with_session_sets_cooldown()** (5 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **test_check_involuntary_flee_with_session_tier_blocks()** (5 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- *... and 79 more nodes in this community*

## Relationships

- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (40 shared connections)
- [CombatParticipant](CombatParticipant.md) (32 shared connections)
- [test_combat.py](test_combat.py.md) (19 shared connections)
- [test_aggro_threat.py](test_aggro_threat.py.md) (15 shared connections)
- [test_combat_service_modules.py](test_combat_service_modules.py.md) (11 shared connections)
- [combat_service_npc.py](combat_service_npc.py.md) (10 shared connections)
- [test_combat_flee_helpers.py](test_combat_flee_helpers.py.md) (8 shared connections)
- [UUID](UUID.md) (7 shared connections)
- [CombatDeathHandler](CombatDeathHandler.md) (7 shared connections)
- [AliasStorage](AliasStorage.md) (6 shared connections)
- [CombatAttackHandler](CombatAttackHandler.md) (5 shared connections)
- [test_flee_command.py](test_flee_command.py.md) (4 shared connections)

## Source Files

- `server/models/combat.py`
- `server/services/combat_cleanup_handler.py`
- `server/services/combat_flee_handler.py`
- `server/services/combat_service.py`
- `server/services/combat_turn_participant_actions.py`
- `server/tests/unit/commands/test_combat_taunt.py`
- `server/tests/unit/services/test_combat_flee_handler.py`

## Audit Trail

- EXTRACTED: 378 (99%)
- INFERRED: 5 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*