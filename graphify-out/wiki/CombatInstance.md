# CombatInstance

> 116 nodes

## Key Concepts

- **CombatInstance** (172 connections) — `server/models/combat.py`
- **test_combat_flee_handler.py** (33 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **combat_flee_handler.py** (23 connections) — `server/services/combat_flee_handler.py`
- **execute_voluntary_flee()** (20 connections) — `server/services/combat_flee_handler.py`
- **_make_participant()** (20 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **asyncio** (15 connections)
- **_check_involuntary_flee_with_session()** (11 connections) — `server/services/combat_flee_handler.py`
- **try_voluntary_flee_roll()** (11 connections) — `server/services/combat_flee_handler.py`
- **_involuntary_flee_on_cooldown()** (10 connections) — `server/services/combat_flee_handler.py`
- **check_involuntary_flee()** (9 connections) — `server/services/combat_flee_handler.py`
- **process_player_turn()** (9 connections) — `server/services/combat_turn_participant_actions.py`
- **_handle_failed_voluntary_flee()** (6 connections) — `server/services/combat_flee_handler.py`
- **test_execute_voluntary_flee_free_hits_error_logged()** (6 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **test_execute_voluntary_flee_missing_participant_returns_false()** (6 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **test_execute_voluntary_flee_move_fails_returns_false()** (6 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **test_execute_voluntary_flee_no_exits_returns_false()** (6 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **test_execute_voluntary_flee_no_room_returns_false()** (6 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **test_execute_voluntary_flee_roll_fail_consumes_action()** (6 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **test_execute_voluntary_flee_success_moves_player()** (6 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **.apply_attack_damage()** (5 connections) — `server/services/combat_service.py`
- **.apply_damage_and_check_involuntary_flee()** (5 connections) — `server/services/combat_service.py`
- **.handle_attack_events_and_xp()** (5 connections) — `server/services/combat_service.py`
- **._handle_player_dp_update()** (5 connections) — `server/services/combat_service.py`
- **.validate_and_get_combat_participants()** (5 connections) — `server/services/combat_service.py`
- **_select_player_target()** (5 connections) — `server/services/combat_turn_participant_actions.py`
- *... and 91 more nodes in this community*

## Relationships

- [CombatService](CombatService.md) (65 shared connections)
- [CombatParticipant](CombatParticipant.md) (38 shared connections)
- [test_combat.py](test_combat.py.md) (19 shared connections)
- [test_aggro_threat.py](test_aggro_threat.py.md) (14 shared connections)
- [test_combat_flee_helpers.py](test_combat_flee_helpers.py.md) (8 shared connections)
- [test_combat_death_handler.py](test_combat_death_handler.py.md) (8 shared connections)
- [combat_turn_participant_actions.py](combat_turn_participant_actions.py.md) (6 shared connections)
- [test_combat_service_modules.py](test_combat_service_modules.py.md) (5 shared connections)
- [CombatAttackHandler](CombatAttackHandler.md) (5 shared connections)
- [test_combat_turn_participant_actions.py](test_combat_turn_participant_actions.py.md) (5 shared connections)
- [get_logger](get_logger.md) (5 shared connections)
- [test_flee_command.py](test_flee_command.py.md) (4 shared connections)

## Source Files

- `server/models/combat.py`
- `server/services/combat_cleanup_handler.py`
- `server/services/combat_flee_handler.py`
- `server/services/combat_service.py`
- `server/services/combat_turn_participant_actions.py`
- `server/tests/unit/services/test_combat_flee_handler.py`
- `server/tests/unit/services/test_combat_service_npc_helpers.py`

## Audit Trail

- EXTRACTED: 404 (100%)
- INFERRED: 1 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*