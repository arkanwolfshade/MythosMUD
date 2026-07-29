# get room service()

> 36 nodes

## Key Concepts

- **get_room_service()** (12 connections) — `server/dependencies.py`
- **Tests for get_player_service dependency function.** (7 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **TestGetPlayerService** (5 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **TestGetRoomService** (5 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **TestGetPlayerRespawnService** (5 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **TestGetPlayerCombatService** (5 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **TestGetPlayerDeathService** (5 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **TestGetCombatService** (5 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **TestGetMagicService** (5 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **TestGetChatService** (5 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **Test get_player_service returns service when present.** (5 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **Test get_player_service raises RuntimeError when service is None.** (4 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **.test_get_player_service_success()** (3 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **.test_get_player_service_none_raises_runtime_error()** (3 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **.test_get_room_service_success()** (3 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **.test_get_room_service_none_raises_runtime_error()** (3 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **.test_get_player_respawn_service_success()** (3 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **.test_get_player_respawn_service_none_raises_runtime_error()** (3 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **.test_get_player_combat_service_none_raises_runtime_error()** (3 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **.test_get_player_death_service_success()** (3 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **.test_get_player_death_service_none_raises_runtime_error()** (3 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **.test_get_combat_service_success()** (3 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **.test_get_combat_service_none_raises_runtime_error()** (3 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **.test_get_magic_service_success()** (3 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **.test_get_magic_service_none_raises_runtime_error()** (3 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- *... and 11 more nodes in this community*

## Relationships

- [. init ()](_init_%28%29.md) (26 shared connections)
- [Connection Manager](Connection_Manager.md) (8 shared connections)
- [AsyncSession](AsyncSession.md) (2 shared connections)
- [character creation](character_creation.md) (2 shared connections)
- [Tests for get exploration service](Tests_for_get_exploration_service.md) (1 shared connections)

## Source Files

- `server/dependencies.py`
- `server/tests/unit/infrastructure/test_dependencies.py`
- `server/tests/unit/test_dependency_injection.py`

## Audit Trail

- EXTRACTED: 116 (93%)
- INFERRED: 9 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*