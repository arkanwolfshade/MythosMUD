# server tests unit infrastructure test

> 21 nodes

## Key Concepts

- **Tests for get_player_service dependency function.** (5 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **TestGetCombatService** (4 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **TestGetPlayerDeathService** (4 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **TestGetPlayerRespawnService** (4 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **TestGetPlayerService** (4 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **.test_get_combat_service_none_raises_runtime_error()** (3 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **.test_get_combat_service_success()** (3 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **.test_get_player_death_service_none_raises_runtime_error()** (3 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **.test_get_player_death_service_success()** (3 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **.test_get_player_respawn_service_none_raises_runtime_error()** (3 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **.test_get_player_respawn_service_success()** (3 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **.test_get_player_service_none_raises_runtime_error()** (3 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **.test_get_player_service_success()** (3 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **Test get_player_service raises RuntimeError when service is None.** (1 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **Test get_player_respawn_service returns service when present.** (1 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **Test get_player_respawn_service raises RuntimeError when service is None.** (1 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **Test get_player_death_service returns service when present.** (1 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **Test get_player_death_service raises RuntimeError when service is None.** (1 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **Test get_combat_service returns service when present.** (1 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **Test get_combat_service raises RuntimeError when service is None.** (1 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **Test get_player_service returns service when present.** (1 connections) — `server/tests/unit/infrastructure/test_dependencies.py`

## Relationships

- [server dependencies](server_dependencies.md) (13 shared connections)

## Source Files

- `server/tests/unit/infrastructure/test_dependencies.py`

## Audit Trail

- EXTRACTED: 33 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*