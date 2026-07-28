# Server Game (43)

> 12 nodes

## Key Concepts

- **level_from_total_xp()** (13 connections) — `server/game/level_curve.py`
- **test_level_from_total_xp_roundtrip()** (4 connections) — `server/tests/unit/game/test_level_curve.py`
- **test_level_from_total_xp_threshold_level_two()** (4 connections) — `server/tests/unit/game/test_level_curve.py`
- **test_level_from_total_xp_zero()** (3 connections) — `server/tests/unit/game/test_level_curve.py`
- **test_level_from_total_xp_negative()** (3 connections) — `server/tests/unit/game/test_level_curve.py`
- **test_check_level_up_no_change_returns_false()** (3 connections) — `server/tests/unit/game/test_level_service.py`
- **Compute character level from total experience points.      Uses the same curve a** (1 connections) — `server/game/level_curve.py`
- **Zero XP gives level 1.** (1 connections) — `server/tests/unit/game/test_level_curve.py`
- **Negative XP treated as zero gives level 1.** (1 connections) — `server/tests/unit/game/test_level_curve.py`
- **level_from_total_xp(total_xp_for_level(n)) >= n (at least that level).** (1 connections) — `server/tests/unit/game/test_level_curve.py`
- **XP just below total_xp_for_level(2) gives level 1; at or above gives level 2.** (1 connections) — `server/tests/unit/game/test_level_curve.py`
- **check_level_up when level already matches curve returns False.** (1 connections) — `server/tests/unit/game/test_level_service.py`

## Relationships

- [Server Game (47)](Server_Game_%2847%29.md) (6 shared connections)
- [Server Game (38)](Server_Game_%2838%29.md) (3 shared connections)
- [Server Game (51)](Server_Game_%2851%29.md) (2 shared connections)
- [Server Game (33)](Server_Game_%2833%29.md) (2 shared connections)
- [Server Commands](Server_Commands.md) (1 shared connections)

## Source Files

- `server/game/level_curve.py`
- `server/tests/unit/game/test_level_curve.py`
- `server/tests/unit/game/test_level_service.py`

## Audit Trail

- EXTRACTED: 36 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*