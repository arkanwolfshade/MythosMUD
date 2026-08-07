# commands rescue rationale

> 65 nodes

## Key Concepts

- **test_level_service.py** (16 connections) — `server/tests/unit/game/test_level_service.py`
- **total_xp_for_level()** (15 connections) — `server/game/level_curve.py`
- **test_level_curve.py** (15 connections) — `server/tests/unit/game/test_level_curve.py`
- **level_from_total_xp()** (13 connections) — `server/game/level_curve.py`
- **LevelService** (13 connections) — `server/game/level_service.py`
- **level_curve.py** (6 connections) — `server/game/level_curve.py`
- **xp_required_for_level()** (6 connections) — `server/game/level_curve.py`
- **.__init__()** (4 connections) — `server/game/level_service.py`
- **.grant_xp()** (4 connections) — `server/game/level_service.py`
- **.check_level_up()** (4 connections) — `server/game/level_service.py`
- **test_xp_required_for_level_marginal()** (4 connections) — `server/tests/unit/game/test_level_curve.py`
- **test_level_from_total_xp_roundtrip()** (4 connections) — `server/tests/unit/game/test_level_curve.py`
- **test_level_from_total_xp_threshold_level_two()** (4 connections) — `server/tests/unit/game/test_level_curve.py`
- **test_grant_xp_level_up_calls_hook()** (4 connections) — `server/tests/unit/game/test_level_service.py`
- **UUID** (3 connections)
- **test_total_xp_for_level_one()** (3 connections) — `server/tests/unit/game/test_level_curve.py`
- **test_total_xp_for_level_two_positive()** (3 connections) — `server/tests/unit/game/test_level_curve.py`
- **test_total_xp_for_level_increases()** (3 connections) — `server/tests/unit/game/test_level_curve.py`
- **test_total_xp_for_level_invalid()** (3 connections) — `server/tests/unit/game/test_level_curve.py`
- **test_xp_required_for_level_invalid()** (3 connections) — `server/tests/unit/game/test_level_curve.py`
- **test_level_from_total_xp_zero()** (3 connections) — `server/tests/unit/game/test_level_curve.py`
- **test_level_from_total_xp_negative()** (3 connections) — `server/tests/unit/game/test_level_curve.py`
- **level_service()** (3 connections) — `server/tests/unit/game/test_level_service.py`
- **test_check_level_up_no_change_returns_false()** (3 connections) — `server/tests/unit/game/test_level_service.py`
- **test_check_level_up_increase_persists_and_returns_true()** (3 connections) — `server/tests/unit/game/test_level_service.py`
- *... and 40 more nodes in this community*

## Relationships

- [logging examples fastapi](logging_examples_fastapi.md) (5 shared connections)
- [combat models rationale](combat_models_rationale.md) (2 shared connections)
- [NPC Definitions Admin](NPC_Definitions_Admin.md) (2 shared connections)
- [nats services service](nats_services_service.md) (1 shared connections)

## Source Files

- `server/game/level_curve.py`
- `server/game/level_service.py`
- `server/tests/unit/game/test_level_curve.py`
- `server/tests/unit/game/test_level_service.py`

## Audit Trail

- EXTRACTED: 191 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*