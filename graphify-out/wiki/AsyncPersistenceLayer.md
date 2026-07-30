# AsyncPersistenceLayer

> 43 nodes

## Key Concepts

- **combat_flee_handler.py** (22 connections) — `server/services/combat_flee_handler.py`
- **test_combat_flee_handler.py** (17 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **execute_voluntary_flee()** (15 connections) — `server/services/combat_flee_handler.py`
- **try_voluntary_flee_roll()** (11 connections) — `server/services/combat_flee_handler.py`
- **_make_participant()** (11 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **_check_involuntary_flee_with_session()** (8 connections) — `server/services/combat_flee_handler.py`
- **lucidity_command_disruption.py** (8 connections) — `server/services/lucidity_command_disruption.py`
- **check_involuntary_flee()** (6 connections) — `server/services/combat_flee_handler.py`
- **_involuntary_flee_on_cooldown()** (5 connections) — `server/services/combat_flee_handler.py`
- **test_try_voluntary_flee_roll_zero_exits_returns_false()** (5 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **test_try_voluntary_flee_roll_roll_above_chance_fails()** (5 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **test_try_voluntary_flee_roll_roll_below_chance_succeeds()** (5 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **test_try_voluntary_flee_roll_opponents_reduce_chance()** (5 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **test_try_voluntary_flee_roll_dead_opponent_not_counted()** (5 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **test_execute_voluntary_flee_no_room_returns_false()** (5 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **test_execute_voluntary_flee_no_exits_returns_false()** (5 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **UUID** (4 connections)
- **should_involuntary_flee()** (4 connections) — `server/services/lucidity_command_disruption.py`
- **Any** (2 connections)
- **should_misfire_command()** (2 connections) — `server/services/lucidity_command_disruption.py`
- **get_misfire_message()** (2 connections) — `server/services/lucidity_command_disruption.py`
- **can_perform_action()** (2 connections) — `server/services/lucidity_command_disruption.py`
- **UUID** (2 connections)
- **Combat flee handler for involuntary and voluntary flee logic.  Handles checking** (1 connections) — `server/services/combat_flee_handler.py`
- **Roll for voluntary flee success (no side effects).      Formula: base + (bonus *** (1 connections) — `server/services/combat_flee_handler.py`
- *... and 18 more nodes in this community*

## Relationships

- [close db()](close_db%28%29.md) (19 shared connections)
- [test combat attack handler](test_combat_attack_handler.md) (5 shared connections)
- [main()](main%28%29.md) (4 shared connections)
- [world](world.md) (4 shared connections)
- [ASGIApp](ASGIApp.md) (3 shared connections)
- [. initialize handlers()](_initialize_handlers%28%29.md) (2 shared connections)
- [combat flee](combat_flee.md) (2 shared connections)
- [CombatService](CombatService.md) (1 shared connections)

## Source Files

- `server/services/combat_flee_handler.py`
- `server/services/lucidity_command_disruption.py`
- `server/tests/unit/services/test_combat_flee_handler.py`

## Audit Trail

- EXTRACTED: 175 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*