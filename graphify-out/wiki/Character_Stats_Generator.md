# Character Stats Generator

> 38 nodes · cohesion 0.06

## Key Concepts

- **test_dependency_injection.py** (18 connections) — `server/tests/unit/test_dependency_injection.py`
- **get_stats_generator()** (8 connections) — `server/dependencies.py`
- **TestGetContainer** (8 connections) — `server/tests/unit/test_dependency_injection.py`
- **TestGetPlayerService** (7 connections) — `server/tests/unit/test_dependency_injection.py`
- **TestGetPlayerServiceForTesting** (7 connections) — `server/tests/unit/test_dependency_injection.py`
- **TestGetRoomService** (7 connections) — `server/tests/unit/test_dependency_injection.py`
- **TestGetStatsGenerator** (7 connections) — `server/tests/unit/test_dependency_injection.py`
- **TestGetStatsGenerator** (4 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **.test_get_player_service_success()** (4 connections) — `server/tests/unit/test_dependency_injection.py`
- **.test_get_player_service_for_testing_with_injection()** (4 connections) — `server/tests/unit/test_dependency_injection.py`
- **.test_get_player_service_for_testing_without_injection()** (4 connections) — `server/tests/unit/test_dependency_injection.py`
- **.test_get_stats_generator()** (4 connections) — `server/tests/unit/test_dependency_injection.py`
- **.test_get_stats_generator_stateless()** (4 connections) — `server/tests/unit/test_dependency_injection.py`
- **.test_get_stats_generator_returns_instance()** (3 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **.test_get_container_missing()** (3 connections) — `server/tests/unit/test_dependency_injection.py`
- **.test_get_container_no_app_state()** (3 connections) — `server/tests/unit/test_dependency_injection.py`
- **.test_get_container_success()** (3 connections) — `server/tests/unit/test_dependency_injection.py`
- **.test_get_player_service_not_initialized()** (3 connections) — `server/tests/unit/test_dependency_injection.py`
- **.test_get_room_service_not_initialized()** (3 connections) — `server/tests/unit/test_dependency_injection.py`
- **Get a StatsGenerator instance via dependency injection.      StatsGenerator is s** (1 connections) — `server/dependencies.py`
- **Tests for get_stats_generator dependency function.** (1 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **Test get_stats_generator returns StatsGenerator instance.** (1 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **Unit tests for dependency injection functions.  Tests dependency injection provi** (1 connections) — `server/tests/unit/test_dependency_injection.py`
- **Test get_room_service() function.** (1 connections) — `server/tests/unit/test_dependency_injection.py`
- **Test get_room_service() raises error when service not initialized.** (1 connections) — `server/tests/unit/test_dependency_injection.py`
- *... and 13 more nodes in this community*

## Relationships

- [Dependency Injection Tests](Dependency_Injection_Tests.md) (16 shared connections)
- [Players API Endpoints](Players_API_Endpoints.md) (11 shared connections)
- [Player Effects API](Player_Effects_API.md) (10 shared connections)
- [ASCII Map API](ASCII_Map_API.md) (8 shared connections)

## Source Files

- `server/dependencies.py`
- `server/tests/unit/infrastructure/test_dependencies.py`
- `server/tests/unit/test_dependency_injection.py`

## Audit Trail

- EXTRACTED: 102 (83%)
- INFERRED: 21 (17%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*