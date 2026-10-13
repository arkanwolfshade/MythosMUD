# Community 821

> 20 nodes

## Key Concepts

- **test_level_service.py** (11 connections) — `server/tests/unit/game/test_level_service.py`
- **asyncio** (6 connections)
- **level_service()** (4 connections) — `server/tests/unit/game/test_level_service.py`
- **test_grant_xp_level_up_calls_hook()** (4 connections) — `server/tests/unit/game/test_level_service.py`
- **test_grant_xp_no_level_change_does_not_call_hook()** (4 connections) — `server/tests/unit/game/test_level_service.py`
- **test_grant_xp_player_not_found_propagates()** (4 connections) — `server/tests/unit/game/test_level_service.py`
- **mock_persistence()** (3 connections) — `server/tests/unit/game/test_level_service.py`
- **test_grant_xp_negative_raises()** (3 connections) — `server/tests/unit/game/test_level_service.py`
- **test_grant_xp_without_hook_does_not_raise_on_level_up()** (3 connections) — `server/tests/unit/game/test_level_service.py`
- **test_grant_xp_zero_no_op()** (3 connections) — `server/tests/unit/game/test_level_service.py`
- **fixture** (2 connections)
- **Unit tests for LevelService: grant_xp and the level-up hook. Character creation…** (1 connections) — `server/tests/unit/game/test_level_service.py`
- **Mock async persistence with award_player_xp returning (new_xp, old_level,…** (1 connections) — `server/tests/unit/game/test_level_service.py`
- **LevelService with mocked persistence.** (1 connections) — `server/tests/unit/game/test_level_service.py`
- **grant_xp(amount=0) does not call persistence.** (1 connections) — `server/tests/unit/game/test_level_service.py`
- **grant_xp(amount < 0) raises ValueError.** (1 connections) — `server/tests/unit/game/test_level_service.py`
- **grant_xp propagates persistence's ValueError when player not found.** (1 connections) — `server/tests/unit/game/test_level_service.py`
- **When persistence reports old_level == new_level, the level-up hook is not…** (1 connections) — `server/tests/unit/game/test_level_service.py`
- **When persistence reports a level increase, the level-up hook is invoked with…** (1 connections) — `server/tests/unit/game/test_level_service.py`
- **No level_up_hook configured: a level-up still completes without error.** (1 connections) — `server/tests/unit/game/test_level_service.py`

## Relationships

- [API Response Models](API_Response_Models.md) (4 shared connections)
- [Community 226](Community_226.md) (1 shared connections)
- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (1 shared connections)

## Source Files

- `server/tests/unit/game/test_level_service.py`

## Audit Trail

- EXTRACTED: 27 (87%)
- INFERRED: 4 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*