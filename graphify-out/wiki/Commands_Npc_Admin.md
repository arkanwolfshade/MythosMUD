# Commands Npc Admin

> 12 nodes · cohesion 0.17

## Key Concepts

- **level_from_total_xp()** (13 connections) — `server/game/level_curve.py`
- **test_level_from_total_xp_roundtrip()** (4 connections) — `server/tests/unit/game/test_level_curve.py`
- **test_level_from_total_xp_threshold_level_two()** (4 connections) — `server/tests/unit/game/test_level_curve.py`
- **test_level_from_total_xp_negative()** (3 connections) — `server/tests/unit/game/test_level_curve.py`
- **test_level_from_total_xp_zero()** (3 connections) — `server/tests/unit/game/test_level_curve.py`
- **test_check_level_up_no_change_returns_false()** (3 connections) — `server/tests/unit/game/test_level_service.py`
- **Compute character level from total experience points.      Uses the same curve a** (1 connections) — `server/game/level_curve.py`
- **Zero XP gives level 1.** (1 connections) — `server/tests/unit/game/test_level_curve.py`
- **Negative XP treated as zero gives level 1.** (1 connections) — `server/tests/unit/game/test_level_curve.py`
- **level_from_total_xp(total_xp_for_level(n)) >= n (at least that level).** (1 connections) — `server/tests/unit/game/test_level_curve.py`
- **XP just below total_xp_for_level(2) gives level 1; at or above gives level 2.** (1 connections) — `server/tests/unit/game/test_level_curve.py`
- **check_level_up when level already matches curve returns False.** (1 connections) — `server/tests/unit/game/test_level_service.py`

## Relationships

- [Command Handler Patterns](Command_Handler_Patterns.md) (6 shared connections)
- [Scenario Conversion Guide](Scenario_Conversion_Guide.md) (3 shared connections)
- [Level and XP Curve](Level_and_XP_Curve.md) (2 shared connections)
- [NPC Occupants Verification](NPC_Occupants_Verification.md) (2 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (1 shared connections)

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