# CombatInstance

> 113 nodes

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
- **._create_corpse_on_death()** (9 connections) — `server/services/combat_death_handler.py`
- **check_involuntary_flee()** (9 connections) — `server/services/combat_flee_handler.py`
- **._handle_npc_death()** (8 connections) — `server/services/combat_death_handler.py`
- **._handle_player_death_events()** (6 connections) — `server/services/combat_death_handler.py`
- **._log_room_subscribers_before_npc_death()** (6 connections) — `server/services/combat_death_handler.py`
- **._resolve_original_npc_id()** (6 connections) — `server/services/combat_death_handler.py`
- **_handle_failed_voluntary_flee()** (6 connections) — `server/services/combat_flee_handler.py`
- **test_execute_voluntary_flee_free_hits_error_logged()** (6 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **test_execute_voluntary_flee_missing_participant_returns_false()** (6 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **test_execute_voluntary_flee_move_fails_returns_false()** (6 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **test_execute_voluntary_flee_no_exits_returns_false()** (6 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **test_execute_voluntary_flee_no_room_returns_false()** (6 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **test_execute_voluntary_flee_roll_fail_consumes_action()** (6 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **test_execute_voluntary_flee_success_moves_player()** (6 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **.handle_target_state_changes()** (5 connections) — `server/services/combat_death_handler.py`
- **.apply_attack_damage()** (5 connections) — `server/services/combat_service.py`
- *... and 88 more nodes in this community*

## Relationships

- [CombatParticipant](CombatParticipant.md) (54 shared connections)
- [CombatService](CombatService.md) (36 shared connections)
- [combat_taunt.py](combat_taunt.py.md) (18 shared connections)
- [models/combat.py](models-combat.py.md) (10 shared connections)
- [CombatDeathHandler](CombatDeathHandler.md) (10 shared connections)
- [test_combat_service_modules.py](test_combat_service_modules.py.md) (9 shared connections)
- [combat_turn_participant_actions.py](combat_turn_participant_actions.py.md) (9 shared connections)
- [test_combat_flee_helpers.py](test_combat_flee_helpers.py.md) (8 shared connections)
- [test_combat_attack_handler.py](test_combat_attack_handler.py.md) (7 shared connections)
- [get_logger](get_logger.md) (5 shared connections)
- [test_flee_command.py](test_flee_command.py.md) (4 shared connections)
- [LucidityService](LucidityService.md) (4 shared connections)

## Source Files

- `server/models/combat.py`
- `server/services/combat_cleanup_handler.py`
- `server/services/combat_death_handler.py`
- `server/services/combat_flee_handler.py`
- `server/services/combat_service.py`
- `server/tests/unit/services/test_combat_flee_handler.py`

## Audit Trail

- EXTRACTED: 396 (99%)
- INFERRED: 6 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*