# websocket helpers realtime

> 298 nodes

## Key Concepts

- **AsyncPersistenceLayer** (202 connections) — `server/async_persistence.py`
- **async_persistence.py** (79 connections) — `server/async_persistence.py`
- **test_async_persistence_core.py** (40 connections) — `server/tests/unit/infrastructure/test_async_persistence_core.py`
- **test_async_persistence_delegates.py** (35 connections) — `server/tests/unit/infrastructure/test_async_persistence_delegates.py`
- **RoomCacheLoader** (29 connections) — `server/async_persistence_room_loader.py`
- **ContainerRepository** (26 connections) — `server/persistence/repositories/container_repository.py`
- **Player** (22 connections)
- **UUID** (21 connections)
- **test_container_repository.py** (21 connections) — `server/tests/unit/persistence/repositories/test_container_repository.py`
- **Any** (19 connections)
- **get_async_persistence()** (19 connections) — `server/async_persistence.py`
- **.__init__()** (13 connections) — `server/async_persistence.py`
- **._ensure_room_cache_loaded()** (13 connections) — `server/async_persistence.py`
- **profession_service.py** (13 connections) — `server/game/profession_service.py`
- **Any** (12 connections)
- **_container_data_to_dict()** (12 connections) — `server/persistence/repositories/container_repository.py`
- **CreateItemInstanceInput** (11 connections) — `server/async_persistence_constants.py`
- **_sample_container_data()** (11 connections) — `server/tests/unit/persistence/repositories/test_container_repository.py`
- **.load()** (10 connections) — `server/async_persistence_room_loader.py`
- **profession.py** (10 connections) — `server/models/profession.py`
- **container_create_params.py** (9 connections) — `server/persistence/container_create_params.py`
- **._generate_room_id_from_zone_data()** (7 connections) — `server/async_persistence_room_loader.py`
- **Any** (7 connections)
- **.create_container()** (7 connections) — `server/persistence/repositories/container_repository.py`
- **.get_container()** (7 connections) — `server/persistence/repositories/container_repository.py`
- *... and 273 more nodes in this community*

## Relationships

- [commands party examples](commands_party_examples.md) (23 shared connections)
- [game weapon player](game_weapon_player.md) (22 shared connections)
- [endpoints auth rationale](endpoints_auth_rationale.md) (18 shared connections)
- [combat models rationale](combat_models_rationale.md) (17 shared connections)
- [player event handlers](player_event_handlers.md) (16 shared connections)
- [add used user](add_used_user.md) (15 shared connections)
- [Error Conversion](Error_Conversion.md) (13 shared connections)
- [command combat models](command_combat_models.md) (13 shared connections)
- [logging examples fastapi](logging_examples_fastapi.md) (8 shared connections)
- [commands shutdown process](commands_shutdown_process.md) (8 shared connections)
- [Exception Containers](Exception_Containers.md) (7 shared connections)
- [player room realtime](player_room_realtime.md) (7 shared connections)

## Source Files

- `server/async_persistence.py`
- `server/async_persistence_constants.py`
- `server/async_persistence_room_loader.py`
- `server/game/profession_service.py`
- `server/models/profession.py`
- `server/persistence/container_create_params.py`
- `server/persistence/repositories/container_repository.py`
- `server/tests/unit/infrastructure/conftest.py`
- `server/tests/unit/infrastructure/test_async_persistence_core.py`
- `server/tests/unit/infrastructure/test_async_persistence_delegates.py`
- `server/tests/unit/persistence/repositories/test_container_repository.py`

## Audit Trail

- EXTRACTED: 1165 (92%)
- INFERRED: 97 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*