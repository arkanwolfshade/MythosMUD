# test_game.py

> 80 nodes

## Key Concepts

- **test_game.py** (20 connections) — `server/tests/unit/api/test_game.py`
- **get_mythos_time()** (15 connections) — `server/api/game.py`
- **broadcast_message()** (14 connections) — `server/api/game.py`
- **TestGetMythosTime** (12 connections) — `server/tests/unit/api/test_game.py`
- **BroadcastMessageResponse** (8 connections) — `server/schemas/game/game.py`
- **GameStatusResponse** (8 connections) — `server/schemas/game/game.py`
- **MythosTimeResponse** (8 connections) — `server/schemas/game/game.py`
- **get_game_status()** (8 connections) — `server/api/game.py`
- **game/game.py** (7 connections) — `server/schemas/game/game.py`
- **schemas/game/__init__.py** (7 connections) — `server/schemas/game/__init__.py`
- **asyncio** (7 connections)
- **BroadcastStats** (6 connections) — `server/schemas/game/game.py`
- **TestBroadcastMessage** (6 connections) — `server/tests/unit/api/test_game.py`
- **TestGetMythosTimeEdgeCases** (6 connections) — `server/tests/unit/api/test_game.py`
- **TestGetGameStatus** (5 connections) — `server/tests/unit/api/test_game.py`
- **TestBroadcastMessageEdgeCases** (4 connections) — `server/tests/unit/api/test_game.py`
- **TestGetGameStatusLogger** (4 connections) — `server/tests/unit/api/test_game.py`
- **.test_broadcast_message_broadcast_error()** (4 connections) — `server/tests/unit/api/test_game.py`
- **.test_broadcast_message_no_recipients()** (4 connections) — `server/tests/unit/api/test_game.py`
- **.test_broadcast_message_success()** (4 connections) — `server/tests/unit/api/test_game.py`
- **.test_broadcast_message_broadcast_stats_structure()** (4 connections) — `server/tests/unit/api/test_game.py`
- **.test_broadcast_message_empty_stats()** (4 connections) — `server/tests/unit/api/test_game.py`
- **.test_broadcast_message_logs_info()** (4 connections) — `server/tests/unit/api/test_game.py`
- **.test_broadcast_message_missing_stats_key()** (4 connections) — `server/tests/unit/api/test_game.py`
- **.test_get_mythos_time_with_holidays()** (4 connections) — `server/tests/unit/api/test_game.py`
- *... and 55 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (9 shared connections)
- [User](User.md) (8 shared connections)
- [server/schemas/__init__.py](server-schemas-__init__.py.md) (4 shared connections)
- [HolidayCollection](HolidayCollection.md) (3 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (1 shared connections)

## Source Files

- `server/api/game.py`
- `server/schemas/game/__init__.py`
- `server/schemas/game/game.py`
- `server/tests/unit/api/test_game.py`

## Audit Trail

- EXTRACTED: 139 (96%)
- INFERRED: 6 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*