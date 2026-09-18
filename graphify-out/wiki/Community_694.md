# Community 694

> 24 nodes

## Key Concepts

- **total_xp_for_level()** (15 connections) — `server/game/level_curve.py`
- **test_level_curve.py** (15 connections) — `server/tests/unit/game/test_level_curve.py`
- **xp_required_for_level()** (6 connections) — `server/game/level_curve.py`
- **level_curve.py** (6 connections) — `server/game/level_curve.py`
- **test_level_from_total_xp_roundtrip()** (4 connections) — `server/tests/unit/game/test_level_curve.py`
- **test_level_from_total_xp_threshold_level_two()** (4 connections) — `server/tests/unit/game/test_level_curve.py`
- **test_xp_required_for_level_marginal()** (4 connections) — `server/tests/unit/game/test_level_curve.py`
- **test_total_xp_for_level_increases()** (3 connections) — `server/tests/unit/game/test_level_curve.py`
- **test_total_xp_for_level_invalid()** (3 connections) — `server/tests/unit/game/test_level_curve.py`
- **test_total_xp_for_level_one()** (3 connections) — `server/tests/unit/game/test_level_curve.py`
- **test_total_xp_for_level_two_positive()** (3 connections) — `server/tests/unit/game/test_level_curve.py`
- **test_xp_required_for_level_invalid()** (3 connections) — `server/tests/unit/game/test_level_curve.py`
- **Level and XP curve for MythosMUD. Placeholder implementation: XP required for…** (1 connections) — `server/game/level_curve.py`
- **Total XP required to reach a given level (cumulative). Level 1 requires 0 XP.…** (1 connections) — `server/game/level_curve.py`
- **XP required to go from (level - 1) to level. Args: level: Target level (2-based…** (1 connections) — `server/game/level_curve.py`
- **Unit tests for level curve (XP to level, level from total XP). Character…** (1 connections) — `server/tests/unit/game/test_level_curve.py`
- **Level 1 requires 0 cumulative XP.** (1 connections) — `server/tests/unit/game/test_level_curve.py`
- **Level 2 requires positive cumulative XP.** (1 connections) — `server/tests/unit/game/test_level_curve.py`
- **Cumulative XP increases with level.** (1 connections) — `server/tests/unit/game/test_level_curve.py`
- **total_xp_for_level raises for level < 1.** (1 connections) — `server/tests/unit/game/test_level_curve.py`
- **xp_required_for_level(2) equals total_xp_for_level(2) - total_xp_for_level(1).** (1 connections) — `server/tests/unit/game/test_level_curve.py`
- **xp_required_for_level raises for level < 2.** (1 connections) — `server/tests/unit/game/test_level_curve.py`
- **level_from_total_xp(total_xp_for_level(n)) >= n (at least that level).** (1 connections) — `server/tests/unit/game/test_level_curve.py`
- **XP just below total_xp_for_level(2) gives level 1; at or above gives level 2.** (1 connections) — `server/tests/unit/game/test_level_curve.py`

## Relationships

- [Community 1416](Community_1416.md) (7 shared connections)
- [Community 841](Community_841.md) (3 shared connections)
- [Aliases & Webhook/Schema Validation](Aliases_&_Webhook-Schema_Validation.md) (1 shared connections)

## Source Files

- `server/game/level_curve.py`
- `server/tests/unit/game/test_level_curve.py`

## Audit Trail

- EXTRACTED: 46 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*