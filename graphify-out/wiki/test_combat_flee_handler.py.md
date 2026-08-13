# test_combat_flee_handler.py

> 22 nodes

## Key Concepts

- **test_combat_flee_handler.py** (17 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **try_voluntary_flee_roll()** (11 connections) — `server/services/combat_flee_handler.py`
- **_make_participant()** (11 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **test_execute_voluntary_flee_no_exits_returns_false()** (6 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **test_execute_voluntary_flee_no_room_returns_false()** (6 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **test_try_voluntary_flee_roll_dead_opponent_not_counted()** (5 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **test_try_voluntary_flee_roll_opponents_reduce_chance()** (5 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **test_try_voluntary_flee_roll_roll_above_chance_fails()** (5 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **test_try_voluntary_flee_roll_roll_below_chance_succeeds()** (5 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **test_try_voluntary_flee_roll_zero_exits_returns_false()** (5 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **asyncio** (2 connections)
- **UUID** (2 connections)
- **Roll for voluntary flee success (no side effects). Formula: base + (bonus *…** (1 connections) — `server/services/combat_flee_handler.py`
- **Unit tests for combat flee handler (voluntary flee roll and…** (1 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **execute_voluntary_flee returns False when get_room_by_id returns None.** (1 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **execute_voluntary_flee returns False when room has no exits.** (1 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **Create a combat participant that can act.** (1 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **With zero exits, flee always fails.** (1 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **When random() returns above computed chance, flee fails.** (1 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **When random() returns below computed chance, flee succeeds.** (1 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **More opponents reduce flee chance.** (1 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **Dead or inactive opponents do not reduce chance.** (1 connections) — `server/tests/unit/services/test_combat_flee_handler.py`

## Relationships

- [get_logger](get_logger.md) (13 shared connections)
- [combat_flee_handler.py](combat_flee_handler.py.md) (7 shared connections)

## Source Files

- `server/services/combat_flee_handler.py`
- `server/tests/unit/services/test_combat_flee_handler.py`

## Audit Trail

- EXTRACTED: 55 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*