# test_game.py

> 80 nodes

## Key Concepts

- **test_game.py** (20 connections) — `server/tests/unit/api/test_game.py`
- **broadcast_message()** (18 connections) — `server/api/game.py`
- **get_mythos_time()** (15 connections) — `server/api/game.py`
- **TestGetMythosTime** (11 connections) — `server/tests/unit/api/test_game.py`
- **BroadcastMessageResponse** (8 connections) — `server/schemas/game/game.py`
- **GameStatusResponse** (8 connections) — `server/schemas/game/game.py`
- **MythosTimeResponse** (8 connections) — `server/schemas/game/game.py`
- **get_game_status()** (8 connections) — `server/api/game.py`
- **schemas/game/__init__.py** (8 connections) — `server/schemas/game/__init__.py`
- **game/game.py** (7 connections) — `server/schemas/game/game.py`
- **asyncio** (7 connections)
- **BroadcastStats** (6 connections) — `server/schemas/game/game.py`
- **TestBroadcastMessage** (5 connections) — `server/tests/unit/api/test_game.py`
- **TestGetMythosTimeEdgeCases** (5 connections) — `server/tests/unit/api/test_game.py`
- **TestGetGameStatus** (4 connections) — `server/tests/unit/api/test_game.py`
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
- *... and 55 more nodes in this community*

## Relationships

- [LoggedHTTPException](LoggedHTTPException.md) (17 shared connections)
- [HolidayEntry](HolidayEntry.md) (3 shared connections)
- [test_message_category_invariants.py](test_message_category_invariants.py.md) (2 shared connections)
- [test_room_system_message_categories.py](test_room_system_message_categories.py.md) (2 shared connections)
- [test_lifespan_shutdown.py](test_lifespan_shutdown.py.md) (1 shared connections)

## Source Files

- `server/api/game.py`
- `server/schemas/game/__init__.py`
- `server/schemas/game/game.py`
- `server/tests/unit/api/test_game.py`

## Audit Trail

- EXTRACTED: 144 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*