# Server Game (38)

> 14 nodes

## Key Concepts

- **total_xp_for_level()** (15 connections) — `server/game/level_curve.py`
- **test_grant_xp_level_up_calls_hook()** (4 connections) — `server/tests/unit/game/test_level_service.py`
- **test_total_xp_for_level_one()** (3 connections) — `server/tests/unit/game/test_level_curve.py`
- **test_total_xp_for_level_two_positive()** (3 connections) — `server/tests/unit/game/test_level_curve.py`
- **test_total_xp_for_level_increases()** (3 connections) — `server/tests/unit/game/test_level_curve.py`
- **test_total_xp_for_level_invalid()** (3 connections) — `server/tests/unit/game/test_level_curve.py`
- **test_check_level_up_increase_persists_and_returns_true()** (3 connections) — `server/tests/unit/game/test_level_service.py`
- **Total XP required to reach a given level (cumulative).      Level 1 requires 0 X** (1 connections) — `server/game/level_curve.py`
- **Level 1 requires 0 cumulative XP.** (1 connections) — `server/tests/unit/game/test_level_curve.py`
- **Level 2 requires positive cumulative XP.** (1 connections) — `server/tests/unit/game/test_level_curve.py`
- **Cumulative XP increases with level.** (1 connections) — `server/tests/unit/game/test_level_curve.py`
- **total_xp_for_level raises for level < 1.** (1 connections) — `server/tests/unit/game/test_level_curve.py`
- **When level increases, save is called and level_up_hook is invoked.** (1 connections) — `server/tests/unit/game/test_level_service.py`
- **check_level_up when curve gives higher level updates player and returns True.** (1 connections) — `server/tests/unit/game/test_level_service.py`

## Relationships

- [Server Game (47)](Server_Game_%2847%29.md) (8 shared connections)
- [Server Game (43)](Server_Game_%2843%29.md) (3 shared connections)
- [Server Game (33)](Server_Game_%2833%29.md) (3 shared connections)
- [Server Infrastructure](Server_Infrastructure.md) (1 shared connections)

## Source Files

- `server/game/level_curve.py`
- `server/tests/unit/game/test_level_curve.py`
- `server/tests/unit/game/test_level_service.py`

## Audit Trail

- EXTRACTED: 41 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*