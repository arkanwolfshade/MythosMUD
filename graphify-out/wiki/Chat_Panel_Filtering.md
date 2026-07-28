# Chat Panel Filtering

> 76 nodes · cohesion 0.04

## Key Concepts

- **test_game.py** (20 connections) — `server/tests/unit/api/test_game.py`
- **MythosTimeResponse** (15 connections) — `server/schemas/game/game.py`
- **get_mythos_time()** (14 connections) — `server/api/game.py`
- **broadcast_message()** (13 connections) — `server/api/game.py`
- **TestGetMythosTime** (12 connections) — `server/tests/unit/api/test_game.py`
- **BroadcastMessageResponse** (9 connections) — `server/schemas/game/game.py`
- **GameStatusResponse** (9 connections) — `server/schemas/game/game.py`
- **get_game_status()** (7 connections) — `server/api/game.py`
- **game.py** (7 connections) — `server/schemas/game/game.py`
- **__init__.py** (7 connections) — `server/schemas/game/__init__.py`
- **BroadcastStats** (6 connections) — `server/schemas/game/game.py`
- **TestBroadcastMessage** (6 connections) — `server/tests/unit/api/test_game.py`
- **TestGetMythosTimeEdgeCases** (6 connections) — `server/tests/unit/api/test_game.py`
- **TestGetGameStatus** (5 connections) — `server/tests/unit/api/test_game.py`
- **BaseModel** (4 connections)
- **.test_broadcast_message_success()** (4 connections) — `server/tests/unit/api/test_game.py`
- **TestBroadcastMessageEdgeCases** (4 connections) — `server/tests/unit/api/test_game.py`
- **.test_get_game_status_success()** (4 connections) — `server/tests/unit/api/test_game.py`
- **TestGetGameStatusLogger** (4 connections) — `server/tests/unit/api/test_game.py`
- **.test_get_mythos_time_holiday_service_error()** (4 connections) — `server/tests/unit/api/test_game.py`
- **.test_get_mythos_time_holiday_service_upcoming_error()** (4 connections) — `server/tests/unit/api/test_game.py`
- **.test_get_mythos_time_no_container()** (4 connections) — `server/tests/unit/api/test_game.py`
- **.test_get_mythos_time_no_holiday_service()** (4 connections) — `server/tests/unit/api/test_game.py`
- **.test_get_mythos_time_success()** (4 connections) — `server/tests/unit/api/test_game.py`
- **.test_get_mythos_time_with_holidays()** (4 connections) — `server/tests/unit/api/test_game.py`
- *... and 51 more nodes in this community*

## Relationships

- [Argon2 Password Hashing](Argon2_Password_Hashing.md) (10 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (8 shared connections)
- [System Monitoring API](System_Monitoring_API.md) (4 shared connections)
- [Holiday Persistence Models](Holiday_Persistence_Models.md) (3 shared connections)
- [Weapon Resolution Helpers](Weapon_Resolution_Helpers.md) (1 shared connections)

## Source Files

- `server/api/game.py`
- `server/schemas/game/__init__.py`
- `server/schemas/game/game.py`
- `server/tests/unit/api/test_game.py`

## Audit Trail

- EXTRACTED: 233 (90%)
- INFERRED: 25 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*