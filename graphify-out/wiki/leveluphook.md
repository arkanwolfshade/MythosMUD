# leveluphook

> 69 nodes

## Key Concepts

- **test_level_service.py** (17 connections) — `server/tests/unit/game/test_level_service.py`
- **test_level_curve.py** (16 connections) — `server/tests/unit/game/test_level_curve.py`
- **total_xp_for_level()** (15 connections) — `server/game/level_curve.py`
- **LevelService** (13 connections) — `server/game/level_service.py`
- **level_from_total_xp()** (13 connections) — `server/game/level_curve.py`
- **level_service.py** (9 connections) — `server/game/level_service.py`
- **asyncio** (8 connections)
- **xp_required_for_level()** (6 connections) — `server/game/level_curve.py`
- **level_curve.py** (6 connections) — `server/game/level_curve.py`
- **test_grant_xp_level_up_calls_hook()** (5 connections) — `server/tests/unit/game/test_level_service.py`
- **.check_level_up()** (4 connections) — `server/game/level_service.py`
- **.grant_xp()** (4 connections) — `server/game/level_service.py`
- **.__init__()** (4 connections) — `server/game/level_service.py`
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
- *... and 44 more nodes in this community*

## Relationships

- [server dependencies](server_dependencies.md) (3 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (2 shared connections)
- [claude rules pytest](claude_rules_pytest.md) (2 shared connections)
- [claude rules sqlalchemy](claude_rules_sqlalchemy.md) (1 shared connections)
- [scripts validate calendar](scripts_validate_calendar.md) (1 shared connections)
- [server container bundles chat](server_container_bundles_chat.md) (1 shared connections)

## Source Files

- `server/game/level_curve.py`
- `server/game/level_service.py`
- `server/tests/unit/game/test_level_curve.py`
- `server/tests/unit/game/test_level_service.py`

## Audit Trail

- EXTRACTED: 115 (97%)
- INFERRED: 3 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*