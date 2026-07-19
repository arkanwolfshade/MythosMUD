# Dependency Injection Dependencies

> 19 nodes · cohesion 0.12

## Key Concepts

- **get_player_service_for_testing()** (10 connections) — `server/dependencies.py`
- **TestGetPlayerService** (7 connections) — `server/tests/unit/test_dependency_injection.py`
- **TestGetPlayerServiceForTesting** (7 connections) — `server/tests/unit/test_dependency_injection.py`
- **TestGetPlayerServiceForTesting** (5 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **.test_get_player_service_for_testing_creates_mock()** (3 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **.test_get_player_service_for_testing_with_provided_service()** (3 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **PlayerService** (3 connections) — `server/dependencies.py`
- **Test get_player_service() function.** (3 connections) — `server/tests/unit/test_dependency_injection.py`
- **.test_get_player_service_not_initialized()** (3 connections) — `server/tests/unit/test_dependency_injection.py`
- **.test_get_player_service_success()** (3 connections) — `server/tests/unit/test_dependency_injection.py`
- **.test_get_player_service_for_testing_with_injection()** (3 connections) — `server/tests/unit/test_dependency_injection.py`
- **.test_get_player_service_for_testing_without_injection()** (3 connections) — `server/tests/unit/test_dependency_injection.py`
- **Tests for get_player_service_for_testing helper function.** (1 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **Test get_player_service_for_testing creates PlayerService when None provided.** (1 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **Get a PlayerService instance for testing purposes.      This function allows tes** (1 connections) — `server/dependencies.py`
- **Test get_player_service() returns player service from container.** (1 connections) — `server/tests/unit/test_dependency_injection.py`
- **Test get_player_service() raises error when service not initialized.** (1 connections) — `server/tests/unit/test_dependency_injection.py`
- **Test get_player_service_for_testing() with injected service.** (1 connections) — `server/tests/unit/test_dependency_injection.py`
- **Test get_player_service_for_testing() creates mock when None.** (1 connections) — `server/tests/unit/test_dependency_injection.py`

## Relationships

- [[Dependency Injection Tests]] (8 shared connections)
- [[Combat Command Handler]] (4 shared connections)
- [[Maps API Endpoints]] (2 shared connections)
- [[Character Stats Generator]] (2 shared connections)
- [[NPC Admin API]] (1 shared connections)
- [[Async Persistence Layer]] (1 shared connections)

## Source Files

- `server/dependencies.py`
- `server/tests/unit/infrastructure/test_dependencies.py`
- `server/tests/unit/test_dependency_injection.py`

## Audit Trail

- EXTRACTED: 52 (87%)
- INFERRED: 8 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
