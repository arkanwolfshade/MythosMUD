# command factories exploration

> 160 nodes

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
- **.validate_and_get_combat_participants()** (6 connections) — `server/services/combat_attack_handler.py`
- **test_process_npc_turn_calls_process_attack_when_target_resolved()** (6 connections) — `server/tests/unit/services/test_combat_turn_participant_actions.py`
- **._handle_player_dp_update()** (5 connections) — `server/services/combat_service.py`
- **.validate_and_get_combat_participants()** (5 connections) — `server/services/combat_service.py`
- **.apply_attack_damage()** (5 connections) — `server/services/combat_service.py`
- **.handle_attack_events_and_xp()** (5 connections) — `server/services/combat_service.py`
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
- *... and 135 more nodes in this community*

## Relationships

- [combat commands handler](combat_commands_handler.md) (47 shared connections)
- [Item Instances](Item_Instances.md) (46 shared connections)
- [NPC Combat](NPC_Combat.md) (23 shared connections)
- [room validator toolkit](room_validator_toolkit.md) (13 shared connections)
- [models npc rationale](models_npc_rationale.md) (12 shared connections)
- [services combat sync](services_combat_sync.md) (10 shared connections)
- [npc database infrastructure](npc_database_infrastructure.md) (10 shared connections)
- [combat flee commands](combat_flee_commands.md) (8 shared connections)
- [websocket handler realtime](websocket_handler_realtime.md) (6 shared connections)
- [Memory Task Runtime](Memory_Task_Runtime.md) (5 shared connections)
- [movement monitor game](movement_monitor_game.md) (5 shared connections)
- [scripts worktree ops](scripts_worktree_ops.md) (5 shared connections)

## Source Files

- `server/models/combat.py`
- `server/services/combat_attack_handler.py`
- `server/services/combat_cleanup_handler.py`
- `server/services/combat_flee_handler.py`
- `server/services/combat_service.py`
- `server/tests/unit/models/test_combat.py`
- `server/tests/unit/services/test_combat_attack_handler.py`
- `server/tests/unit/services/test_combat_cleanup_handler.py`
- `server/tests/unit/services/test_combat_flee_handler.py`
- `server/tests/unit/services/test_combat_turn_participant_actions.py`

## Audit Trail

- EXTRACTED: 648 (96%)
- INFERRED: 28 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*