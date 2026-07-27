# Level and XP Curve

> 59 nodes · cohesion 0.05

## Key Concepts

- **total_xp_for_level()** (15 connections) — `server/game/level_curve.py`
- **test_level_service.py** (15 connections) — `server/tests/unit/game/test_level_service.py`
- **test_level_curve.py** (14 connections) — `server/tests/unit/game/test_level_curve.py`
- **level_from_total_xp()** (13 connections) — `server/game/level_curve.py`
- **xp_required_for_level()** (6 connections) — `server/game/level_curve.py`
- **level_curve.py** (5 connections) — `server/game/level_curve.py`
- **.check_level_up()** (4 connections) — `server/game/level_service.py`
- **.grant_xp()** (4 connections) — `server/game/level_service.py`
- **test_level_from_total_xp_roundtrip()** (4 connections) — `server/tests/unit/game/test_level_curve.py`
- **test_level_from_total_xp_threshold_level_two()** (4 connections) — `server/tests/unit/game/test_level_curve.py`
- **test_xp_required_for_level_marginal()** (4 connections) — `server/tests/unit/game/test_level_curve.py`
- **test_grant_xp_level_up_calls_hook()** (4 connections) — `server/tests/unit/game/test_level_service.py`
- **test_level_from_total_xp_negative()** (3 connections) — `server/tests/unit/game/test_level_curve.py`
- **test_level_from_total_xp_zero()** (3 connections) — `server/tests/unit/game/test_level_curve.py`
- **test_total_xp_for_level_increases()** (3 connections) — `server/tests/unit/game/test_level_curve.py`
- **test_total_xp_for_level_invalid()** (3 connections) — `server/tests/unit/game/test_level_curve.py`
- **test_total_xp_for_level_one()** (3 connections) — `server/tests/unit/game/test_level_curve.py`
- **test_total_xp_for_level_two_positive()** (3 connections) — `server/tests/unit/game/test_level_curve.py`
- **test_xp_required_for_level_invalid()** (3 connections) — `server/tests/unit/game/test_level_curve.py`
- **level_service()** (3 connections) — `server/tests/unit/game/test_level_service.py`
- **test_check_level_up_increase_persists_and_returns_true()** (3 connections) — `server/tests/unit/game/test_level_service.py`
- **test_check_level_up_no_change_returns_false()** (3 connections) — `server/tests/unit/game/test_level_service.py`
- **UUID** (3 connections) — `server/game/level_service.py`
- **mock_persistence()** (2 connections) — `server/tests/unit/game/test_level_service.py`
- **sample_player()** (2 connections) — `server/tests/unit/game/test_level_service.py`
- *... and 34 more nodes in this community*

## Relationships

- [[Game Service Bundle]] (5 shared connections)
- [[NPC Admin API]] (3 shared connections)

## Source Files

- `server/game/level_curve.py`
- `server/game/level_service.py`
- `server/tests/unit/game/test_level_curve.py`
- `server/tests/unit/game/test_level_service.py`

## Audit Trail

- EXTRACTED: 168 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
