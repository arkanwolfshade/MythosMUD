# get_player_service_for_testing

> 14 nodes

## Key Concepts

- **get_player_service_for_testing()** (9 connections) — `server/dependencies.py`
- **TestGetPlayerServiceForTesting** (5 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **TestGetPlayerServiceForTesting** (5 connections) — `server/tests/unit/test_dependency_injection.py`
- **.test_get_player_service_for_testing_creates_mock()** (3 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **.test_get_player_service_for_testing_with_provided_service()** (3 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **.test_get_player_service_for_testing_with_injection()** (3 connections) — `server/tests/unit/test_dependency_injection.py`
- **.test_get_player_service_for_testing_without_injection()** (3 connections) — `server/tests/unit/test_dependency_injection.py`
- **Get a PlayerService instance for testing purposes. This function allows tests…** (1 connections) — `server/dependencies.py`
- **Tests for get_player_service_for_testing helper function.** (1 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **Test get_player_service_for_testing returns provided service.** (1 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **Test get_player_service_for_testing creates PlayerService when None provided.** (1 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **Test get_player_service_for_testing() function.** (1 connections) — `server/tests/unit/test_dependency_injection.py`
- **Test get_player_service_for_testing() with injected service.** (1 connections) — `server/tests/unit/test_dependency_injection.py`
- **Test get_player_service_for_testing() creates mock when None.** (1 connections) — `server/tests/unit/test_dependency_injection.py`

## Relationships

- [server/dependencies.py](server-dependencies.py.md) (3 shared connections)
- [PlayerService](PlayerService.md) (3 shared connections)
- [Stats](Stats.md) (2 shared connections)

## Source Files

- `server/dependencies.py`
- `server/tests/unit/infrastructure/test_dependencies.py`
- `server/tests/unit/test_dependency_injection.py`

## Audit Trail

- EXTRACTED: 21 (91%)
- INFERRED: 2 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*