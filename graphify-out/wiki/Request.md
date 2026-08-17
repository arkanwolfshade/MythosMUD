# Request

> 13 nodes

## Key Concepts

- **Request** (28 connections)
- **get_magic_service()** (7 connections) — `server/dependencies.py`
- **get_level_service()** (5 connections) — `server/dependencies.py`
- **get_quest_service()** (5 connections) — `server/dependencies.py`
- **TestGetMagicService** (4 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **.test_get_magic_service_none_raises_runtime_error()** (3 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **.test_get_magic_service_success()** (3 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **Get a LevelService instance with dependency injection. LevelService provides…** (1 connections) — `server/dependencies.py`
- **Get QuestService from container (quest log, start, progress, abandon).** (1 connections) — `server/dependencies.py`
- **Get a MagicService instance with dependency injection. Args: request: The…** (1 connections) — `server/dependencies.py`
- **Tests for get_magic_service dependency function.** (1 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **Test get_magic_service returns service when present.** (1 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **Test get_magic_service raises RuntimeError when service is None.** (1 connections) — `server/tests/unit/infrastructure/test_dependencies.py`

## Relationships

- [get_container](get_container.md) (4 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (4 shared connections)
- [test_dependencies.py](test_dependencies.py.md) (2 shared connections)
- [api/character_creation.py](api-character_creation.py.md) (2 shared connections)
- [QuestService](QuestService.md) (1 shared connections)
- [get_async_persistence](get_async_persistence.md) (1 shared connections)
- [get_catatonia_registry](get_catatonia_registry.md) (1 shared connections)
- [get_chat_service](get_chat_service.md) (1 shared connections)
- [get_combat_service](get_combat_service.md) (1 shared connections)
- [get_connection_manager](get_connection_manager.md) (1 shared connections)
- [get_exploration_service](get_exploration_service.md) (1 shared connections)
- [get_mp_regeneration_service](get_mp_regeneration_service.md) (1 shared connections)

## Source Files

- `server/dependencies.py`
- `server/tests/unit/infrastructure/test_dependencies.py`

## Audit Trail

- EXTRACTED: 48 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*