# get_mythos_time

> 44 nodes

## Key Concepts

- **get_mythos_time()** (15 connections) — `server/api/game.py`
- **broadcast_message()** (14 connections) — `server/api/game.py`
- **TestGetMythosTime** (12 connections) — `server/tests/unit/api/test_game.py`
- **asyncio** (7 connections)
- **TestBroadcastMessage** (6 connections) — `server/tests/unit/api/test_game.py`
- **TestGetMythosTimeEdgeCases** (6 connections) — `server/tests/unit/api/test_game.py`
- **.test_broadcast_message_broadcast_error()** (4 connections) — `server/tests/unit/api/test_game.py`
- **.test_broadcast_message_no_recipients()** (4 connections) — `server/tests/unit/api/test_game.py`
- **.test_broadcast_message_success()** (4 connections) — `server/tests/unit/api/test_game.py`
- **.test_broadcast_message_broadcast_stats_structure()** (4 connections) — `server/tests/unit/api/test_game.py`
- **.test_broadcast_message_empty_stats()** (4 connections) — `server/tests/unit/api/test_game.py`
- **.test_broadcast_message_logs_info()** (4 connections) — `server/tests/unit/api/test_game.py`
- **.test_broadcast_message_missing_stats_key()** (4 connections) — `server/tests/unit/api/test_game.py`
- **.test_get_mythos_time_with_holidays()** (4 connections) — `server/tests/unit/api/test_game.py`
- **.test_get_mythos_time_holiday_service_error()** (3 connections) — `server/tests/unit/api/test_game.py`
- **.test_get_mythos_time_holiday_service_upcoming_error()** (3 connections) — `server/tests/unit/api/test_game.py`
- **.test_get_mythos_time_no_container()** (3 connections) — `server/tests/unit/api/test_game.py`
- **.test_get_mythos_time_no_holiday_service()** (3 connections) — `server/tests/unit/api/test_game.py`
- **.test_get_mythos_time_success()** (3 connections) — `server/tests/unit/api/test_game.py`
- **.test_get_mythos_time_container_no_holiday_service_attribute()** (3 connections) — `server/tests/unit/api/test_game.py`
- **.test_get_mythos_time_different_calendar_components()** (3 connections) — `server/tests/unit/api/test_game.py`
- **.test_get_mythos_time_logs_debug()** (3 connections) — `server/tests/unit/api/test_game.py`
- **post** (1 connections)
- **Return the current Mythos calendar metadata for HUD initialization. In-memory…** (1 connections) — `server/api/game.py`
- **Broadcast a message to all connected players (admin only). Requires superuser…** (1 connections) — `server/api/game.py`
- *... and 19 more nodes in this community*

## Relationships

- [test_game.py](test_game.py.md) (10 shared connections)
- [User](User.md) (4 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [MythosChronicle](MythosChronicle.md) (1 shared connections)
- [HolidayService](HolidayService.md) (1 shared connections)

## Source Files

- `server/api/game.py`
- `server/tests/unit/api/test_game.py`

## Audit Trail

- EXTRACTED: 75 (96%)
- INFERRED: 3 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*