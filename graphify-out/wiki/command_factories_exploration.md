# command factories exploration

> 132 nodes

## Key Concepts

- **CombatInstance** (186 connections) — `server/models/combat.py`
- **test_combat_flee_handler.py** (33 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **combat_flee_handler.py** (22 connections) — `server/services/combat_flee_handler.py`
- **execute_voluntary_flee()** (20 connections) — `server/services/combat_flee_handler.py`
- **_make_participant()** (20 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **try_voluntary_flee_roll()** (11 connections) — `server/services/combat_flee_handler.py`
- **_check_involuntary_flee_with_session()** (11 connections) — `server/services/combat_flee_handler.py`
- **_involuntary_flee_on_cooldown()** (10 connections) — `server/services/combat_flee_handler.py`
- **check_involuntary_flee()** (9 connections) — `server/services/combat_flee_handler.py`
- **.is_dead()** (5 connections) — `server/models/combat.py`
- **.get_alive_participants()** (5 connections) — `server/models/combat.py`
- **._handle_player_dp_update()** (5 connections) — `server/services/combat_service.py`
- **.apply_attack_damage()** (5 connections) — `server/services/combat_service.py`
- **test_try_voluntary_flee_roll_zero_exits_returns_false()** (5 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **test_try_voluntary_flee_roll_roll_above_chance_fails()** (5 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **test_try_voluntary_flee_roll_roll_below_chance_succeeds()** (5 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **test_try_voluntary_flee_roll_opponents_reduce_chance()** (5 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **test_try_voluntary_flee_roll_dead_opponent_not_counted()** (5 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **test_execute_voluntary_flee_no_room_returns_false()** (5 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **test_execute_voluntary_flee_no_exits_returns_false()** (5 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **test_execute_voluntary_flee_missing_participant_returns_false()** (5 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **test_execute_voluntary_flee_roll_fail_consumes_action()** (5 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **test_execute_voluntary_flee_success_moves_player()** (5 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **test_execute_voluntary_flee_free_hits_error_logged()** (5 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **test_execute_voluntary_flee_move_fails_returns_false()** (5 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- *... and 107 more nodes in this community*

## Relationships

- [Item Instances](Item_Instances.md) (55 shared connections)
- [models npc rationale](models_npc_rationale.md) (26 shared connections)
- [npc database infrastructure](npc_database_infrastructure.md) (25 shared connections)
- [subject admin controller](subject_admin_controller.md) (21 shared connections)
- [EdgeCreationModal map STANDARD](EdgeCreationModal_map_STANDARD.md) (13 shared connections)
- [room validator toolkit](room_validator_toolkit.md) (12 shared connections)
- [tick game processing](tick_game_processing.md) (9 shared connections)
- [combat flee commands](combat_flee_commands.md) (8 shared connections)
- [room renderer functions](room_renderer_functions.md) (6 shared connections)
- [container helpers loot](container_helpers_loot.md) (4 shared connections)
- [player room realtime](player_room_realtime.md) (4 shared connections)
- [player look commands](player_look_commands.md) (3 shared connections)

## Source Files

- `server/models/combat.py`
- `server/services/combat_flee_handler.py`
- `server/services/combat_service.py`
- `server/tests/unit/models/test_combat.py`
- `server/tests/unit/services/test_combat_attack_handler.py`
- `server/tests/unit/services/test_combat_cleanup_handler.py`
- `server/tests/unit/services/test_combat_flee_handler.py`

## Audit Trail

- EXTRACTED: 578 (96%)
- INFERRED: 23 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*