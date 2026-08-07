# command factories exploration

> 180 nodes

## Key Concepts

- **CombatInstance** (186 connections) — `server/models/combat.py`
- **test_combat.py** (60 connections) — `server/tests/unit/models/test_combat.py`
- **test_combat_flee_handler.py** (33 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **combat_flee_handler.py** (22 connections) — `server/services/combat_flee_handler.py`
- **execute_voluntary_flee()** (20 connections) — `server/services/combat_flee_handler.py`
- **_make_participant()** (20 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **try_voluntary_flee_roll()** (11 connections) — `server/services/combat_flee_handler.py`
- **_check_involuntary_flee_with_session()** (11 connections) — `server/services/combat_flee_handler.py`
- **_involuntary_flee_on_cooldown()** (10 connections) — `server/services/combat_flee_handler.py`
- **check_involuntary_flee()** (9 connections) — `server/services/combat_flee_handler.py`
- **_get_default_damage()** (6 connections) — `server/models/combat.py`
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
- **UUID** (4 connections)
- **UUID** (4 connections)
- *... and 155 more nodes in this community*

## Relationships

- [Item Instances](Item_Instances.md) (76 shared connections)
- [npc database infrastructure](npc_database_infrastructure.md) (25 shared connections)
- [services service phantom](services_service_phantom.md) (14 shared connections)
- [room validator toolkit](room_validator_toolkit.md) (12 shared connections)
- [subject admin controller](subject_admin_controller.md) (11 shared connections)
- [Memory Task Runtime](Memory_Task_Runtime.md) (11 shared connections)
- [combat flee commands](combat_flee_commands.md) (8 shared connections)
- [persistence container extended](persistence_container_extended.md) (8 shared connections)
- [message nats handler](message_nats_handler.md) (8 shared connections)
- [commands position system](commands_position_system.md) (6 shared connections)
- [correct patterns examples](correct_patterns_examples.md) (6 shared connections)
- [cleanup combat handler](cleanup_combat_handler.md) (4 shared connections)

## Source Files

- `server/models/combat.py`
- `server/services/combat_flee_handler.py`
- `server/tests/unit/models/test_combat.py`
- `server/tests/unit/services/test_combat_flee_handler.py`

## Audit Trail

- EXTRACTED: 732 (98%)
- INFERRED: 17 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*