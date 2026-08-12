# test_level_service.py

> 61 nodes

## Key Concepts

- **test_level_service.py** (16 connections) — `server/tests/unit/game/test_level_service.py`
- **total_xp_for_level()** (15 connections) — `server/game/level_curve.py`
- **test_level_curve.py** (15 connections) — `server/tests/unit/game/test_level_curve.py`
- **level_from_total_xp()** (13 connections) — `server/game/level_curve.py`
- **asyncio** (8 connections)
- **xp_required_for_level()** (6 connections) — `server/game/level_curve.py`
- **level_curve.py** (6 connections) — `server/game/level_curve.py`
- **test_grant_xp_level_up_calls_hook()** (5 connections) — `server/tests/unit/game/test_level_service.py`
- **.check_level_up()** (4 connections) — `server/game/level_service.py`
- **.grant_xp()** (4 connections) — `server/game/level_service.py`
- **test_level_from_total_xp_roundtrip()** (4 connections) — `server/tests/unit/game/test_level_curve.py`
- **test_level_from_total_xp_threshold_level_two()** (4 connections) — `server/tests/unit/game/test_level_curve.py`
- **test_xp_required_for_level_marginal()** (4 connections) — `server/tests/unit/game/test_level_curve.py`
- **level_service()** (4 connections) — `server/tests/unit/game/test_level_service.py`
- **test_check_level_up_increase_persists_and_returns_true()** (4 connections) — `server/tests/unit/game/test_level_service.py`
- **test_check_level_up_no_change_returns_false()** (4 connections) — `server/tests/unit/game/test_level_service.py`
- **test_level_from_total_xp_negative()** (3 connections) — `server/tests/unit/game/test_level_curve.py`
- **test_level_from_total_xp_zero()** (3 connections) — `server/tests/unit/game/test_level_curve.py`
- **test_total_xp_for_level_increases()** (3 connections) — `server/tests/unit/game/test_level_curve.py`
- **test_total_xp_for_level_invalid()** (3 connections) — `server/tests/unit/game/test_level_curve.py`
- **test_total_xp_for_level_one()** (3 connections) — `server/tests/unit/game/test_level_curve.py`
- **test_total_xp_for_level_two_positive()** (3 connections) — `server/tests/unit/game/test_level_curve.py`
- **test_xp_required_for_level_invalid()** (3 connections) — `server/tests/unit/game/test_level_curve.py`
- **mock_persistence()** (3 connections) — `server/tests/unit/game/test_level_service.py`
- **sample_player()** (3 connections) — `server/tests/unit/game/test_level_service.py`
- *... and 36 more nodes in this community*

## Relationships

- [GameBundle](GameBundle.md) (5 shared connections)
- [get_logger](get_logger.md) (4 shared connections)

## Source Files

- `server/game/level_curve.py`
- `server/game/level_service.py`
- `server/tests/unit/game/test_level_curve.py`
- `server/tests/unit/game/test_level_service.py`

## Audit Trail

- EXTRACTED: 193 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*