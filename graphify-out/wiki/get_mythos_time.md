# get_mythos_time

> 59 nodes

## Key Concepts

- **get_mythos_time()** (15 connections) — `server/api/game.py`
- **broadcast_message()** (14 connections) — `server/api/game.py`
- **TestGetMythosTime** (11 connections) — `server/tests/unit/api/test_game.py`
- **BroadcastMessageResponse** (8 connections) — `server/schemas/game/game.py`
- **GameStatusResponse** (8 connections) — `server/schemas/game/game.py`
- **MythosTimeResponse** (8 connections) — `server/schemas/game/game.py`
- **game/game.py** (8 connections) — `server/schemas/game/game.py`
- **schemas/game/__init__.py** (8 connections) — `server/schemas/game/__init__.py`
- **asyncio** (7 connections)
- **BroadcastStats** (6 connections) — `server/schemas/game/game.py`
- **TestBroadcastMessage** (5 connections) — `server/tests/unit/api/test_game.py`
- **TestGetMythosTimeEdgeCases** (5 connections) — `server/tests/unit/api/test_game.py`
- **.test_broadcast_message_broadcast_error()** (4 connections) — `server/tests/unit/api/test_game.py`
- **.test_broadcast_message_no_recipients()** (4 connections) — `server/tests/unit/api/test_game.py`
- **.test_broadcast_message_success()** (4 connections) — `server/tests/unit/api/test_game.py`
- **.test_broadcast_message_broadcast_stats_structure()** (4 connections) — `server/tests/unit/api/test_game.py`
- **.test_broadcast_message_empty_stats()** (4 connections) — `server/tests/unit/api/test_game.py`
- **.test_broadcast_message_logs_info()** (4 connections) — `server/tests/unit/api/test_game.py`
- **.test_broadcast_message_missing_stats_key()** (4 connections) — `server/tests/unit/api/test_game.py`
- **.test_get_mythos_time_with_holidays()** (4 connections) — `server/tests/unit/api/test_game.py`
- **BaseModel** (4 connections)
- **TestBroadcastMessageEdgeCases** (3 connections) — `server/tests/unit/api/test_game.py`
- **.test_get_mythos_time_holiday_service_error()** (3 connections) — `server/tests/unit/api/test_game.py`
- **.test_get_mythos_time_holiday_service_upcoming_error()** (3 connections) — `server/tests/unit/api/test_game.py`
- **.test_get_mythos_time_no_container()** (3 connections) — `server/tests/unit/api/test_game.py`
- *... and 34 more nodes in this community*

## Relationships

- [test_game.py](test_game.py.md) (9 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (8 shared connections)
- [server/schemas/__init__.py](server-schemas-__init__.py.md) (4 shared connections)
- [get_game_status](get_game_status.md) (2 shared connections)
- [HolidayEntry](HolidayEntry.md) (2 shared connections)
- [get_username_from_user](get_username_from_user.md) (1 shared connections)
- [BaseCommand](BaseCommand.md) (1 shared connections)

## Source Files

- `server/api/game.py`
- `server/schemas/game/__init__.py`
- `server/schemas/game/game.py`
- `server/tests/unit/api/test_game.py`

## Audit Trail

- EXTRACTED: 111 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*