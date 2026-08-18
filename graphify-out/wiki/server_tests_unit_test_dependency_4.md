# server tests unit test dependency

> 11 nodes

## Key Concepts

- **TestGetPlayerService** (5 connections) — `server/tests/unit/test_dependency_injection.py`
- **TestGetPlayerServiceForTesting** (5 connections) — `server/tests/unit/test_dependency_injection.py`
- **.test_get_player_service_not_initialized()** (3 connections) — `server/tests/unit/test_dependency_injection.py`
- **.test_get_player_service_success()** (3 connections) — `server/tests/unit/test_dependency_injection.py`
- **.test_get_player_service_for_testing_with_injection()** (3 connections) — `server/tests/unit/test_dependency_injection.py`
- **.test_get_player_service_for_testing_without_injection()** (3 connections) — `server/tests/unit/test_dependency_injection.py`
- **Test get_player_service() function.** (2 connections) — `server/tests/unit/test_dependency_injection.py`
- **Test get_player_service() returns player service from container.** (1 connections) — `server/tests/unit/test_dependency_injection.py`
- **Test get_player_service() raises error when service not initialized.** (1 connections) — `server/tests/unit/test_dependency_injection.py`
- **Test get_player_service_for_testing() with injected service.** (1 connections) — `server/tests/unit/test_dependency_injection.py`
- **Test get_player_service_for_testing() creates mock when None.** (1 connections) — `server/tests/unit/test_dependency_injection.py`

## Relationships

- [server dependencies](server_dependencies.md) (6 shared connections)
- [server api players](server_api_players.md) (2 shared connections)

## Source Files

- `server/tests/unit/test_dependency_injection.py`

## Audit Trail

- EXTRACTED: 16 (89%)
- INFERRED: 2 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*