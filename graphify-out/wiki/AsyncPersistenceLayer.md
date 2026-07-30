# AsyncPersistenceLayer

> 119 nodes

## Key Concepts

- **CombatInstance** (167 connections) — `server/models/combat.py`
- **combat_flee_handler.py** (22 connections) — `server/services/combat_flee_handler.py`
- **test_combat_flee_handler.py** (17 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **execute_voluntary_flee()** (15 connections) — `server/services/combat_flee_handler.py`
- **try_voluntary_flee_roll()** (11 connections) — `server/services/combat_flee_handler.py`
- **_make_participant()** (11 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **_check_involuntary_flee_with_session()** (8 connections) — `server/services/combat_flee_handler.py`
- **._execute_round()** (7 connections) — `server/services/combat_turn_processor.py`
- **check_involuntary_flee()** (6 connections) — `server/services/combat_flee_handler.py`
- **.is_dead()** (5 connections) — `server/models/combat.py`
- **.get_alive_participants()** (5 connections) — `server/models/combat.py`
- **_involuntary_flee_on_cooldown()** (5 connections) — `server/services/combat_flee_handler.py`
- **._handle_player_dp_update()** (5 connections) — `server/services/combat_service.py`
- **.apply_attack_damage()** (5 connections) — `server/services/combat_service.py`
- **.process_game_tick()** (5 connections) — `server/services/combat_turn_processor.py`
- **test_try_voluntary_flee_roll_zero_exits_returns_false()** (5 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **test_try_voluntary_flee_roll_roll_above_chance_fails()** (5 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **test_try_voluntary_flee_roll_roll_below_chance_succeeds()** (5 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **test_try_voluntary_flee_roll_opponents_reduce_chance()** (5 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **test_try_voluntary_flee_roll_dead_opponent_not_counted()** (5 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **test_execute_voluntary_flee_no_room_returns_false()** (5 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **test_execute_voluntary_flee_no_exits_returns_false()** (5 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **UUID** (4 connections)
- **.get_participants_by_initiative()** (4 connections) — `server/models/combat.py`
- **UUID** (4 connections)
- *... and 94 more nodes in this community*

## Relationships

- [test combat attack handler](test_combat_attack_handler.md) (60 shared connections)
- [Any](Any.md) (43 shared connections)
- [. initialize handlers()](_initialize_handlers%28%29.md) (20 shared connections)
- [close db()](close_db%28%29.md) (14 shared connections)
- [.model dump()](model_dump%28%29.md) (12 shared connections)
- [combat flee](combat_flee.md) (8 shared connections)
- [test player event handlers room](test_player_event_handlers_room.md) (6 shared connections)
- [test exploration service](test_exploration_service.md) (4 shared connections)
- [test flee command](test_flee_command.md) (4 shared connections)
- [TerminalButtonProps](TerminalButtonProps.md) (4 shared connections)
- [get health service()](get_health_service%28%29.md) (3 shared connections)
- [.end combat()](end_combat%28%29.md) (3 shared connections)

## Source Files

- `server/models/combat.py`
- `server/services/combat_cleanup_handler.py`
- `server/services/combat_flee_handler.py`
- `server/services/combat_service.py`
- `server/services/combat_turn_processor.py`
- `server/services/lucidity_command_disruption.py`
- `server/tests/unit/models/test_combat.py`
- `server/tests/unit/services/test_combat_attack_handler.py`
- `server/tests/unit/services/test_combat_cleanup_handler.py`
- `server/tests/unit/services/test_combat_flee_handler.py`

## Audit Trail

- EXTRACTED: 487 (96%)
- INFERRED: 22 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*