# Community 841

> 19 nodes

## Key Concepts

- **test_level_service.py** (16 connections) — `server/tests/unit/game/test_level_service.py`
- **asyncio** (8 connections)
- **test_grant_xp_level_up_calls_hook()** (5 connections) — `server/tests/unit/game/test_level_service.py`
- **test_check_level_up_increase_persists_and_returns_true()** (4 connections) — `server/tests/unit/game/test_level_service.py`
- **test_check_level_up_no_change_returns_false()** (4 connections) — `server/tests/unit/game/test_level_service.py`
- **test_check_level_up_player_not_found_raises()** (3 connections) — `server/tests/unit/game/test_level_service.py`
- **test_grant_xp_increases_xp_and_persists()** (3 connections) — `server/tests/unit/game/test_level_service.py`
- **test_grant_xp_negative_raises()** (3 connections) — `server/tests/unit/game/test_level_service.py`
- **test_grant_xp_player_not_found_raises()** (3 connections) — `server/tests/unit/game/test_level_service.py`
- **test_grant_xp_zero_no_op()** (3 connections) — `server/tests/unit/game/test_level_service.py`
- **Unit tests for LevelService: grant_xp, check_level_up, level-up hook. Character…** (1 connections) — `server/tests/unit/game/test_level_service.py`
- **check_level_up when player not found raises ValueError.** (1 connections) — `server/tests/unit/game/test_level_service.py`
- **check_level_up when curve gives higher level updates player and returns True.** (1 connections) — `server/tests/unit/game/test_level_service.py`
- **grant_xp(amount=0) does not load or save.** (1 connections) — `server/tests/unit/game/test_level_service.py`
- **grant_xp(amount < 0) raises ValueError.** (1 connections) — `server/tests/unit/game/test_level_service.py`
- **grant_xp when player not found raises ValueError.** (1 connections) — `server/tests/unit/game/test_level_service.py`
- **grant_xp adds amount to experience_points and saves (level unchanged).** (1 connections) — `server/tests/unit/game/test_level_service.py`
- **When level increases, save is called and level_up_hook is invoked.** (1 connections) — `server/tests/unit/game/test_level_service.py`
- **check_level_up when level already matches curve returns False.** (1 connections) — `server/tests/unit/game/test_level_service.py`

## Relationships

- [Community 694](Community_694.md) (3 shared connections)
- [Community 1360](Community_1360.md) (3 shared connections)
- [Community 1416](Community_1416.md) (2 shared connections)
- [Community 1127](Community_1127.md) (2 shared connections)
- [Aliases & Webhook/Schema Validation](Aliases_&_Webhook-Schema_Validation.md) (1 shared connections)

## Source Files

- `server/tests/unit/game/test_level_service.py`

## Audit Trail

- EXTRACTED: 35 (97%)
- INFERRED: 1 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*