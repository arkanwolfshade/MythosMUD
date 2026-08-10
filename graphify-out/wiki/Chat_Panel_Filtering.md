# Chat Panel Filtering

> 33 nodes

## Key Concepts

- **test_game.py** (20 connections) — `server/tests/unit/api/test_game.py`
- **MythosTimeResponse** (15 connections) — `server/schemas/game/game.py`
- **get_mythos_time()** (14 connections) — `server/api/game.py`
- **TestGetMythosTime** (12 connections) — `server/tests/unit/api/test_game.py`
- **TestGetMythosTimeEdgeCases** (6 connections) — `server/tests/unit/api/test_game.py`
- **.test_get_mythos_time_success()** (4 connections) — `server/tests/unit/api/test_game.py`
- **.test_get_mythos_time_no_holiday_service()** (4 connections) — `server/tests/unit/api/test_game.py`
- **.test_get_mythos_time_holiday_service_error()** (4 connections) — `server/tests/unit/api/test_game.py`
- **.test_get_mythos_time_with_holidays()** (4 connections) — `server/tests/unit/api/test_game.py`
- **.test_get_mythos_time_no_container()** (4 connections) — `server/tests/unit/api/test_game.py`
- **.test_get_mythos_time_holiday_service_upcoming_error()** (4 connections) — `server/tests/unit/api/test_game.py`
- **.test_get_mythos_time_container_no_holiday_service_attribute()** (4 connections) — `server/tests/unit/api/test_game.py`
- **.test_get_mythos_time_logs_debug()** (4 connections) — `server/tests/unit/api/test_game.py`
- **.test_get_mythos_time_different_calendar_components()** (3 connections) — `server/tests/unit/api/test_game.py`
- **mock_connection_manager()** (2 connections) — `server/tests/unit/api/test_game.py`
- **mock_user()** (2 connections) — `server/tests/unit/api/test_game.py`
- **mock_container()** (2 connections) — `server/tests/unit/api/test_game.py`
- **Return the current Mythos calendar metadata for HUD initialization.      In-memo** (1 connections) — `server/api/game.py`
- **Response model for Mythos calendar time endpoint.** (1 connections) — `server/schemas/game/game.py`
- **Unit tests for game API endpoints.  Tests game status, broadcasting, and time en** (1 connections) — `server/tests/unit/api/test_game.py`
- **Create a mock connection manager.** (1 connections) — `server/tests/unit/api/test_game.py`
- **Create a mock application container.** (1 connections) — `server/tests/unit/api/test_game.py`
- **Test get_mythos_time endpoint.** (1 connections) — `server/tests/unit/api/test_game.py`
- **Test get_mythos_time returns time data.** (1 connections) — `server/tests/unit/api/test_game.py`
- **Test get_mythos_time handles missing holiday service.** (1 connections) — `server/tests/unit/api/test_game.py`
- *... and 8 more nodes in this community*

## Relationships

- [Client Lifecycle Metrics](Client_Lifecycle_Metrics.md) (11 shared connections)
- [Game Service Bundle](Game_Service_Bundle.md) (4 shared connections)
- [Combat Command Handler](Combat_Command_Handler.md) (4 shared connections)
- [Archive Planning Code](Archive_Planning_Code.md) (3 shared connections)
- [Player Respawn Service](Player_Respawn_Service.md) (2 shared connections)
- [Test Modernization Plan](Test_Modernization_Plan.md) (1 shared connections)
- [Dead Code Cleanup Plan](Dead_Code_Cleanup_Plan.md) (1 shared connections)

## Source Files

- `server/api/game.py`
- `server/schemas/game/game.py`
- `server/tests/unit/api/test_game.py`

## Audit Trail

- EXTRACTED: 107 (86%)
- INFERRED: 17 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*