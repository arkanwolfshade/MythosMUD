# persistence container extended

> 48 nodes

## Key Concepts

- **test_dependency_injection.py** (18 connections) — `server/tests/unit/test_dependency_injection.py`
- **get_player_service_for_testing()** (9 connections) — `server/dependencies.py`
- **get_stats_generator()** (8 connections) — `server/dependencies.py`
- **TestGetContainer** (8 connections) — `server/tests/unit/test_dependency_injection.py`
- **TestGetPlayerService** (7 connections) — `server/tests/unit/test_dependency_injection.py`
- **TestGetPlayerServiceForTesting** (7 connections) — `server/tests/unit/test_dependency_injection.py`
- **TestGetRoomService** (7 connections) — `server/tests/unit/test_dependency_injection.py`
- **TestGetStatsGenerator** (7 connections) — `server/tests/unit/test_dependency_injection.py`
- **TestGetPlayerServiceForTesting** (5 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **.test_get_player_service_for_testing_creates_mock()** (4 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **TestGetStatsGenerator** (4 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **.test_get_player_service_success()** (4 connections) — `server/tests/unit/test_dependency_injection.py`
- **.test_get_player_service_for_testing_with_injection()** (4 connections) — `server/tests/unit/test_dependency_injection.py`
- **.test_get_player_service_for_testing_without_injection()** (4 connections) — `server/tests/unit/test_dependency_injection.py`
- **.test_get_room_service_success()** (4 connections) — `server/tests/unit/test_dependency_injection.py`
- **.test_get_stats_generator()** (4 connections) — `server/tests/unit/test_dependency_injection.py`
- **.test_get_stats_generator_stateless()** (4 connections) — `server/tests/unit/test_dependency_injection.py`
- **.test_get_player_service_for_testing_with_provided_service()** (3 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **.test_get_stats_generator_returns_instance()** (3 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **.test_get_container_success()** (3 connections) — `server/tests/unit/test_dependency_injection.py`
- **.test_get_container_missing()** (3 connections) — `server/tests/unit/test_dependency_injection.py`
- **.test_get_container_no_app_state()** (3 connections) — `server/tests/unit/test_dependency_injection.py`
- **.test_get_player_service_not_initialized()** (3 connections) — `server/tests/unit/test_dependency_injection.py`
- **.test_get_room_service_not_initialized()** (3 connections) — `server/tests/unit/test_dependency_injection.py`
- **Get a PlayerService instance for testing purposes.      This function allows tes** (1 connections) — `server/dependencies.py`
- *... and 23 more nodes in this community*

## Relationships

- [NPC Definitions Admin](NPC_Definitions_Admin.md) (17 shared connections)
- [persistence core infrastructure](persistence_core_infrastructure.md) (13 shared connections)
- [System Metrics](System_Metrics.md) (10 shared connections)
- [maps handle ascii](maps_handle_ascii.md) (7 shared connections)
- [add used user](add_used_user.md) (1 shared connections)
- [database helpers infrastructure](database_helpers_infrastructure.md) (1 shared connections)

## Source Files

- `server/dependencies.py`
- `server/tests/unit/infrastructure/test_dependencies.py`
- `server/tests/unit/test_dependency_injection.py`

## Audit Trail

- EXTRACTED: 129 (84%)
- INFERRED: 24 (16%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*