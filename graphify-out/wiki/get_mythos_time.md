# get_mythos_time

> 16 nodes

## Key Concepts

- **get_mythos_time()** (15 connections) — `server/api/game.py`
- **TestGetMythosTime** (11 connections) — `server/tests/unit/api/test_game.py`
- **.test_get_mythos_time_with_holidays()** (4 connections) — `server/tests/unit/api/test_game.py`
- **.test_get_mythos_time_holiday_service_error()** (3 connections) — `server/tests/unit/api/test_game.py`
- **.test_get_mythos_time_holiday_service_upcoming_error()** (3 connections) — `server/tests/unit/api/test_game.py`
- **.test_get_mythos_time_no_container()** (3 connections) — `server/tests/unit/api/test_game.py`
- **.test_get_mythos_time_no_holiday_service()** (3 connections) — `server/tests/unit/api/test_game.py`
- **.test_get_mythos_time_success()** (3 connections) — `server/tests/unit/api/test_game.py`
- **Return the current Mythos calendar metadata for HUD initialization. In-memory…** (1 connections) — `server/api/game.py`
- **Test get_mythos_time endpoint.** (1 connections) — `server/tests/unit/api/test_game.py`
- **Test get_mythos_time returns time data.** (1 connections) — `server/tests/unit/api/test_game.py`
- **Test get_mythos_time handles missing holiday service.** (1 connections) — `server/tests/unit/api/test_game.py`
- **Test get_mythos_time handles holiday service errors gracefully.** (1 connections) — `server/tests/unit/api/test_game.py`
- **Test get_mythos_time includes holiday data when available.** (1 connections) — `server/tests/unit/api/test_game.py`
- **Test get_mythos_time handles None container.** (1 connections) — `server/tests/unit/api/test_game.py`
- **Test get_mythos_time handles upcoming holidays error gracefully.** (1 connections) — `server/tests/unit/api/test_game.py`

## Relationships

- [broadcast_message](broadcast_message.md) (3 shared connections)
- [TestGetMythosTimeEdgeCases](TestGetMythosTimeEdgeCases.md) (3 shared connections)
- [test_game.py](test_game.py.md) (2 shared connections)
- [lifespan_startup.py](lifespan_startup.py.md) (1 shared connections)
- [get_game_status](get_game_status.md) (1 shared connections)
- [game/game.py](game-game.py.md) (1 shared connections)
- [get_logger](get_logger.md) (1 shared connections)
- [bundles/game.py](bundles-game.py.md) (1 shared connections)

## Source Files

- `server/api/game.py`
- `server/tests/unit/api/test_game.py`

## Audit Trail

- EXTRACTED: 33 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*