# test_combat_flee_handler.py

> 27 nodes

## Key Concepts

- **test_combat_flee_handler.py** (17 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **execute_voluntary_flee()** (15 connections) — `server/services/combat_flee_handler.py`
- **try_voluntary_flee_roll()** (11 connections) — `server/services/combat_flee_handler.py`
- **_make_participant()** (11 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **_handle_failed_voluntary_flee()** (6 connections) — `server/services/combat_flee_handler.py`
- **test_execute_voluntary_flee_no_exits_returns_false()** (6 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **test_execute_voluntary_flee_no_room_returns_false()** (6 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **test_try_voluntary_flee_roll_dead_opponent_not_counted()** (5 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **test_try_voluntary_flee_roll_opponents_reduce_chance()** (5 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **test_try_voluntary_flee_roll_roll_above_chance_fails()** (5 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **test_try_voluntary_flee_roll_roll_below_chance_succeeds()** (5 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **test_try_voluntary_flee_roll_zero_exits_returns_false()** (5 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **UUID** (5 connections)
- **Any** (3 connections)
- **asyncio** (2 connections)
- **UUID** (2 connections)
- **Execute voluntary flee for a combat participant (shared by /flee command and…** (1 connections) — `server/services/combat_flee_handler.py`
- **Roll for voluntary flee success (no side effects). Formula: base + (bonus *…** (1 connections) — `server/services/combat_flee_handler.py`
- **Unit tests for combat flee handler (voluntary flee roll and…** (1 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **execute_voluntary_flee returns False when get_room_by_id returns None.** (1 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **execute_voluntary_flee returns False when room has no exits.** (1 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **Create a combat participant that can act.** (1 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **With zero exits, flee always fails.** (1 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **When random() returns above computed chance, flee fails.** (1 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **When random() returns below computed chance, flee succeeds.** (1 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- *... and 2 more nodes in this community*

## Relationships

- [CombatParticipant](CombatParticipant.md) (13 shared connections)
- [get_logger](get_logger.md) (7 shared connections)
- [combat_service.py](combat_service.py.md) (3 shared connections)
- [test_combat_flee_helpers.py](test_combat_flee_helpers.py.md) (2 shared connections)
- [spell_effects_status.py](spell_effects_status.py.md) (2 shared connections)
- [TargetResolutionService](TargetResolutionService.md) (1 shared connections)

## Source Files

- `server/services/combat_flee_handler.py`
- `server/tests/unit/services/test_combat_flee_handler.py`

## Audit Trail

- EXTRACTED: 119 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*