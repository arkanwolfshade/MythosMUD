# game rationale schemas

> 65 nodes

## Key Concepts

- **MythosTimeResponse** (15 connections) — `server/schemas/game/game.py`
- **get_mythos_time()** (14 connections) — `server/api/game.py`
- **broadcast_message()** (13 connections) — `server/api/game.py`
- **TestGetMythosTime** (12 connections) — `server/tests/unit/api/test_game.py`
- **GameStatusResponse** (9 connections) — `server/schemas/game/game.py`
- **BroadcastMessageResponse** (9 connections) — `server/schemas/game/game.py`
- **get_game_status()** (7 connections) — `server/api/game.py`
- **__init__.py** (7 connections) — `server/schemas/game/__init__.py`
- **game.py** (7 connections) — `server/schemas/game/game.py`
- **BroadcastStats** (6 connections) — `server/schemas/game/game.py`
- **TestBroadcastMessage** (6 connections) — `server/tests/unit/api/test_game.py`
- **TestGetMythosTimeEdgeCases** (6 connections) — `server/tests/unit/api/test_game.py`
- **TestGetGameStatus** (5 connections) — `server/tests/unit/api/test_game.py`
- **BaseModel** (4 connections)
- **.test_get_game_status_success()** (4 connections) — `server/tests/unit/api/test_game.py`
- **.test_broadcast_message_success()** (4 connections) — `server/tests/unit/api/test_game.py`
- **.test_get_mythos_time_success()** (4 connections) — `server/tests/unit/api/test_game.py`
- **.test_get_mythos_time_no_holiday_service()** (4 connections) — `server/tests/unit/api/test_game.py`
- **.test_get_mythos_time_holiday_service_error()** (4 connections) — `server/tests/unit/api/test_game.py`
- **.test_get_mythos_time_with_holidays()** (4 connections) — `server/tests/unit/api/test_game.py`
- **.test_get_mythos_time_no_container()** (4 connections) — `server/tests/unit/api/test_game.py`
- **.test_get_mythos_time_holiday_service_upcoming_error()** (4 connections) — `server/tests/unit/api/test_game.py`
- **.test_get_mythos_time_container_no_holiday_service_attribute()** (4 connections) — `server/tests/unit/api/test_game.py`
- **.test_get_mythos_time_logs_debug()** (4 connections) — `server/tests/unit/api/test_game.py`
- **.test_get_game_status_empty_connections()** (3 connections) — `server/tests/unit/api/test_game.py`
- *... and 40 more nodes in this community*

## Relationships

- [player requests schemas](player_requests_schemas.md) (24 shared connections)
- [inventory schemas schema](inventory_schemas_schema.md) (4 shared connections)
- [holiday service services](holiday_service_services.md) (2 shared connections)
- [time service rationale](time_service_rationale.md) (1 shared connections)

## Source Files

- `server/api/game.py`
- `server/schemas/game/__init__.py`
- `server/schemas/game/game.py`
- `server/tests/unit/api/test_game.py`

## Audit Trail

- EXTRACTED: 197 (90%)
- INFERRED: 22 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*