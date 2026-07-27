# Game Status API

> 65 nodes · cohesion 0.05

## Key Concepts

- **test_game.py** (18 connections) — `server/tests/unit/api/test_game.py`
- **TestGetMythosTime** (15 connections) — `server/tests/unit/api/test_game.py`
- **get_mythos_time()** (14 connections) — `server/api/game.py`
- **broadcast_message()** (13 connections) — `server/api/game.py`
- **BroadcastMessageResponse** (10 connections) — `server/api/game.py`
- **GameStatusResponse** (10 connections) — `server/api/game.py`
- **MythosTimeResponse** (10 connections) — `server/api/game.py`
- **TestBroadcastMessage** (9 connections) — `server/tests/unit/api/test_game.py`
- **TestGetMythosTimeEdgeCases** (9 connections) — `server/tests/unit/api/test_game.py`
- **TestGetGameStatus** (8 connections) — `server/tests/unit/api/test_game.py`
- **get_game_status()** (7 connections) — `server/api/game.py`
- **TestBroadcastMessageEdgeCases** (7 connections) — `server/tests/unit/api/test_game.py`
- **TestGetGameStatusLogger** (7 connections) — `server/tests/unit/api/test_game.py`
- **.test_broadcast_message_broadcast_error()** (4 connections) — `server/tests/unit/api/test_game.py`
- **.test_get_mythos_time_holiday_service_error()** (4 connections) — `server/tests/unit/api/test_game.py`
- **.test_get_mythos_time_holiday_service_upcoming_error()** (4 connections) — `server/tests/unit/api/test_game.py`
- **.test_get_mythos_time_with_holidays()** (4 connections) — `server/tests/unit/api/test_game.py`
- **User** (4 connections) — `server/api/game.py`
- **.test_broadcast_message_no_recipients()** (3 connections) — `server/tests/unit/api/test_game.py`
- **.test_broadcast_message_success()** (3 connections) — `server/tests/unit/api/test_game.py`
- **.test_broadcast_message_broadcast_stats_structure()** (3 connections) — `server/tests/unit/api/test_game.py`
- **.test_get_game_status_empty_connections()** (3 connections) — `server/tests/unit/api/test_game.py`
- **.test_get_game_status_success()** (3 connections) — `server/tests/unit/api/test_game.py`
- **.test_get_game_status_logs_debug()** (3 connections) — `server/tests/unit/api/test_game.py`
- **.test_broadcast_message_empty_stats()** (3 connections) — `server/tests/unit/api/test_game.py`
- *... and 40 more nodes in this community*

## Relationships

- [[API Test Fixtures]] (7 shared connections)
- [[Admin NPC Schemas]] (4 shared connections)
- [[NPC Admin API]] (3 shared connections)
- [[Database Manager Tests]] (3 shared connections)
- [[Calendar Holiday Schemas]] (2 shared connections)
- [[Game Tick Processing]] (1 shared connections)
- [[Status Effect Tick Tests]] (1 shared connections)

## Source Files

- `server/api/game.py`
- `server/tests/unit/api/test_game.py`

## Audit Trail

- EXTRACTED: 178 (76%)
- INFERRED: 57 (24%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
